"""
مجمّع الأخبار العالمي - خادم Flask
يجلب أخبار من 100+ مصدر إعلامي عالمي ويترجمها للعربية
"""

import feedparser
import threading
import sqlite3
import time
import hashlib
import json
import logging
import os
import socket as _socket
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template, request
from deep_translator import GoogleTranslator

# ضبط السجل
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
log = logging.getLogger(__name__)

app = Flask(__name__)

DB_PATH = 'news.db'
FETCH_INTERVAL = 900        # كل 15 دقيقة
ARTICLES_PER_SOURCE = 5     # عدد المقالات من كل مصدر
TRANSLATION_CACHE_LIMIT = 3000  # حد الكاش
NEWS_RETENTION_HOURS = 24   # احتفظ بالأخبار 24 ساعة فقط

# ========== خريطة القارات والمناطق ==========
CONTINENTS = {
    'الشرق الأوسط': [
        'السعودية','الإمارات','قطر','الكويت','البحرين','عُمان',
        'اليمن','العراق','سوريا','لبنان','الأردن','فلسطين',
        'مصر','ليبيا','تونس','الجزائر','المغرب','السودان',
        'إيران','تركيا','إسرائيل','أفغانستان',
    ],
    'أوروبا': [
        'بريطانيا','فرنسا','ألمانيا','إيطاليا','إسبانيا','البرتغال',
        'هولندا','بلجيكا','سويسرا','النرويج','السويد','الدنمارك',
        'فنلندا','أيرلندا','أوكرانيا','بولندا','التشيك','تشيك',
        'سلوفاكيا','المجر','رومانيا','بلغاريا','صربيا','كرواتيا',
        'إستونيا','ليتوانيا','لاتفيا','اليونان','روسيا','بيلاروسيا',
        'أوروبا',
    ],
    'أمريكا الشمالية': ['أمريكا','كندا','المكسيك'],
    'أمريكا اللاتينية': [
        'البرازيل','الأرجنتين','تشيلي','كولومبيا','بيرو','بوليفيا',
        'الإكوادور','فنزويلا','أوروغواي','الأوروغواي','باراغواي',
        'غواتيمالا','السلفادور','بنما','الدومينيكان',
    ],
    'آسيا': [
        'الهند','باكستان','بنغلاديش','سريلانكا','نيبال','المالديف','بوتان',
        'اليابان','كوريا الجنوبية','الصين','تايوان','هونغ كونغ',
        'سنغافورة','ماليزيا','إندونيسيا','الفلبين','تايلاند',
        'فيتنام','ميانمار','كمبوديا','لاوس','بروناي',
        'قيرغيزستان','كازاخستان','أوزبكستان','طاجيكستان',
        'أذربيجان','جورجيا','أرمينيا','روما',
    ],
    'أفريقيا': [
        'نيجيريا','كينيا','جنوب أفريقيا','إثيوبيا','غانا','تنزانيا',
        'أوغندا','الكاميرون','السنغال','زيمبابوي','زامبيا','بوتسوانا',
        'ناميبيا','ملاوي','مدغشقر','الصومال','ساحل العاج',
        'بوركينا فاسو','أفريقيا',
    ],
    'أوقيانوسيا': [
        'أستراليا','نيوزيلندا','فيجي','ساموا','بابوا نيو غينيا','أوقيانوسيا',
    ],
}


# ========== قاعدة البيانات ==========

def init_db():
    conn = sqlite3.connect(DB_PATH, timeout=30)
    c = conn.cursor()
    c.execute('PRAGMA journal_mode=WAL')  # يسمح بقراءة وكتابة متزامنة
    c.execute('PRAGMA synchronous=NORMAL')
    c.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id TEXT PRIMARY KEY,
            source TEXT NOT NULL,
            source_ar TEXT,
            country TEXT,
            source_type TEXT,
            original_title TEXT NOT NULL,
            arabic_title TEXT,
            summary TEXT,
            summary_ar TEXT,
            image_url TEXT DEFAULT "",
            link TEXT,
            published TEXT,
            original_lang TEXT DEFAULT "en",
            fetched_at TEXT NOT NULL
        )
    ''')
    # إضافة الأعمدة للجداول القديمة تلقائياً
    for col_def in [
        'ALTER TABLE news ADD COLUMN image_url TEXT DEFAULT ""',
        'ALTER TABLE news ADD COLUMN summary_ar TEXT',
    ]:
        try:
            c.execute(col_def)
        except Exception:
            pass
    c.execute('CREATE INDEX IF NOT EXISTS idx_fetched ON news(fetched_at DESC)')
    c.execute('CREATE INDEX IF NOT EXISTS idx_source ON news(source)')
    conn.commit()
    conn.close()
    log.info("قاعدة البيانات جاهزة.")


def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=30)
    conn.row_factory = sqlite3.Row
    return conn


# ========== الترجمة ==========

_translation_cache = {}

def translate_to_arabic(text, source_lang='auto'):
    """ترجمة النص إلى العربية مع تخزين مؤقت محدود الحجم"""
    if not text or not text.strip():
        return text

    cache_key = hashlib.md5(text.encode('utf-8')).hexdigest()
    if cache_key in _translation_cache:
        return _translation_cache[cache_key]

    try:
        translator = GoogleTranslator(source=source_lang, target='ar')
        result = translator.translate(text[:400])  # حد 400 حرف
        if result:
            # تنظيف الكاش إذا تجاوز الحد
            if len(_translation_cache) >= TRANSLATION_CACHE_LIMIT:
                # حذف ربع الكاش القديم
                keys_to_delete = list(_translation_cache.keys())[:TRANSLATION_CACHE_LIMIT // 4]
                for k in keys_to_delete:
                    del _translation_cache[k]
            _translation_cache[cache_key] = result
            return result
    except Exception as e:
        log.warning(f"فشل الترجمة: {e}")

    return text  # إرجاع النص الأصلي عند الفشل


def is_arabic_source(lang_code):
    return lang_code == 'ar'


# ========== جلب الأخبار ==========

def get_entry_image(entry):
    """استخراج أول صورة متاحة من المقالة"""
    import re
    # 1. media:thumbnail
    mt = getattr(entry, 'media_thumbnail', None)
    if mt and isinstance(mt, list) and mt[0].get('url'):
        return mt[0]['url']
    # 2. media:content
    mc = getattr(entry, 'media_content', None)
    if mc and isinstance(mc, list):
        for m in mc:
            if m.get('url') and ('image' in m.get('type','') or m.get('url','').endswith(('.jpg','.jpeg','.png','.webp'))):
                return m['url']
    # 3. enclosures
    enc = getattr(entry, 'enclosures', None)
    if enc and isinstance(enc, list):
        for e in enc:
            if 'image' in e.get('type', ''):
                return e.get('href') or e.get('url', '')
    # 4. img tag inside summary
    for field in ['summary', 'description', 'content']:
        val = entry.get(field, '')
        if isinstance(val, list):
            val = val[0].get('value','') if val else ''
        if val:
            m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', val)
            if m:
                url = m.group(1)
                if url.startswith('http'):
                    return url
    return ''


def get_article_id(link, title):
    content = f"{link}{title}"
    return hashlib.md5(content.encode('utf-8')).hexdigest()


def parse_date(entry):
    """استخراج تاريخ النشر من المقالة"""
    for field in ['published', 'updated', 'created']:
        if hasattr(entry, field):
            val = getattr(entry, field)
            if val:
                return str(val)
    return datetime.now(timezone.utc).isoformat()


def fetch_source(source):
    """جلب أخبار مصدر واحد وتخزينها"""
    url = source.get('url')
    if not url:
        return 0

    try:
        import requests as _req
        import re, gc
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; NewsBot/1.0)',
            'Accept': 'application/rss+xml, application/xml, text/xml, */*',
            'Accept-Encoding': 'gzip, deflate',
        }
        resp = _req.get(url, headers=headers, timeout=12, stream=False)
        if resp.status_code != 200:
            log.debug(f"HTTP {resp.status_code}: {source['name']}")
            return 0

        feed = feedparser.parse(resp.content)
        del resp  # تحرير الذاكرة فوراً

        if not feed.entries:
            log.debug(f"لا توجد مقالات: {source['name']}")
            return 0

        conn = get_db()
        c = conn.cursor()
        new_count = 0
        is_ar = is_arabic_source(source.get('lang', 'en'))
        src_lang = source.get('lang', 'auto')

        for entry in feed.entries[:ARTICLES_PER_SOURCE]:
            link = entry.get('link', '').strip()
            title = entry.get('title', '').strip()

            if not link or not title:
                continue

            article_id = get_article_id(link, title)

            # تحقق من التكرار
            if c.execute('SELECT 1 FROM news WHERE id = ?', (article_id,)).fetchone():
                continue

            # الترجمة
            if is_ar:
                arabic_title = title
                summary_ar = ''
            else:
                arabic_title = translate_to_arabic(title, src_lang)
                time.sleep(0.3)

            # ملخص قصير (بدون ترجمة لتوفير الذاكرة والوقت)
            summary = ''
            for field in ['summary', 'description']:
                val = entry.get(field, '')
                if isinstance(val, list):
                    val = val[0].get('value','') if val else ''
                if val:
                    summary = re.sub(r'<[^>]+>', '', val)[:300]
                    break

            if not is_ar:
                summary_ar = ''  # نترجم الملخص لاحقاً لتوفير الذاكرة
            else:
                summary_ar = summary

            # استخراج الصورة
            image_url = get_entry_image(entry)
            published = parse_date(entry)

            c.execute('''
                INSERT OR IGNORE INTO news
                (id, source, source_ar, country, source_type,
                 original_title, arabic_title, summary, summary_ar, image_url, link,
                 published, original_lang, fetched_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                article_id,
                source['name'],
                source.get('name_ar', source['name']),
                source.get('country', ''),
                source.get('type', ''),
                title,
                arabic_title,
                summary,
                summary_ar,
                image_url,
                link,
                published,
                source.get('lang', 'en'),
                datetime.now(timezone.utc).isoformat()
            ))

            new_count += 1

        conn.commit()
        conn.close()
        del feed  # تحرير الذاكرة
        gc.collect()

        if new_count > 0:
            log.info(f"✓ {source['name']}: {new_count} مقال جديد")
        return new_count

    except Exception as e:
        log.warning(f"✗ خطأ في {source['name']}: {type(e).__name__}: {e}")
        return 0


def fetch_all_feeds():
    """جلب جميع المصادر بشكل متوازٍ - 6 خيوط لتوازن بين السرعة والذاكرة"""
    from sources import SOURCES
    import concurrent.futures, gc
    log.info(f"--- بدء الجلب المتوازي من {len(SOURCES)} مصدر (6 خيوط) ---")
    total = 0

    # نجلب على دفعات لتجنب تراكم الذاكرة
    batch_size = 100
    for i in range(0, len(SOURCES), batch_size):
        batch = SOURCES[i:i + batch_size]
        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
            futures = {executor.submit(fetch_source, src): src for src in batch}
            for future in concurrent.futures.as_completed(futures):
                try:
                    count = future.result(timeout=35)
                    total += count
                except Exception as e:
                    src = futures[future]
                    log.warning(f"✗ خطأ في {src['name']}: {e}")
        gc.collect()  # تنظيف الذاكرة بين الدفعات
        log.info(f"  دفعة {i//batch_size + 1}: أُنجزت ({min(i+batch_size, len(SOURCES))}/{len(SOURCES)})")

    log.info(f"--- انتهى الجلب المتوازي: {total} مقال جديد ---")
    return total


def cleanup_old_news():
    """حذف الأخبار الأقدم من 24 ساعة - نافذة متحركة"""
    try:
        conn = get_db()
        c = conn.cursor()
        # احسب عدد المقالات قبل الحذف
        before = c.execute('SELECT COUNT(*) FROM news').fetchone()[0]
        # احذف ما تجاوز 24 ساعة بناءً على وقت الجلب
        c.execute(
            "DELETE FROM news WHERE fetched_at < datetime('now', ? )",
            (f'-{NEWS_RETENTION_HOURS} hours',)
        )
        deleted = before - c.execute('SELECT COUNT(*) FROM news').fetchone()[0]
        conn.commit()
        conn.close()
        if deleted > 0:
            log.info(f"🧹 حُذف {deleted} خبر قديم (أقدم من {NEWS_RETENTION_HOURS} ساعة) | متبقٍّ: {before - deleted}")
        # تنظيف مساحة الديسك الفعلية
        conn2 = get_db()
        conn2.execute('VACUUM')
        conn2.close()
    except Exception as e:
        log.warning(f"خطأ في تنظيف الأخبار: {e}")


def background_worker():
    """خيط خلفي يجلب الأخبار بصورة دورية"""
    log.info("بدء الخيط الخلفي للأخبار...")
    # تنظيف أولي عند البدء (في حالة وُجدت بيانات قديمة)
    cleanup_old_news()
    # الجلب الأول فوراً
    fetch_all_feeds()
    cleanup_old_news()  # تنظيف بعد الجلب الأول
    cycle = 0
    while True:
        log.info(f"الانتظار {FETCH_INTERVAL // 60} دقائق قبل الجلب التالي...")
        time.sleep(FETCH_INTERVAL)
        fetch_all_feeds()
        cycle += 1
        # تنظيف بعد كل دورتين (كل 30 دقيقة)
        if cycle % 2 == 0:
            cleanup_old_news()


# ========== مسارات Flask ==========

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/news')
def get_news():
    limit = min(request.args.get('limit', 100, type=int), 500)
    offset = request.args.get('offset', 0, type=int)
    source_filter  = request.args.get('source', '').strip()
    search         = request.args.get('q', '').strip()
    continent      = request.args.get('continent', '').strip()
    source_type    = request.args.get('type', '').strip()

    conn = get_db()

    params = []
    where_clauses = []

    if source_filter:
        where_clauses.append('source = ?')
        params.append(source_filter)

    if search:
        where_clauses.append('(arabic_title LIKE ? OR original_title LIKE ?)')
        params.extend([f'%{search}%', f'%{search}%'])

    if continent and continent in CONTINENTS:
        countries = CONTINENTS[continent]
        where_clauses.append('country IN (' + ','.join(['?']*len(countries)) + ')')
        params.extend(countries)

    if source_type:
        where_clauses.append('source_type = ?')
        params.append(source_type)

    where_sql = ''
    if where_clauses:
        where_sql = 'WHERE ' + ' AND '.join(where_clauses)

    params.extend([limit, offset])
    rows = conn.execute(
        f'''SELECT id, source, source_ar, country, source_type,
                   original_title, arabic_title, summary, summary_ar, image_url, link, published,
                   original_lang, fetched_at
            FROM news {where_sql}
            ORDER BY fetched_at DESC
            LIMIT ? OFFSET ?''',
        params
    ).fetchall()

    total = conn.execute(
        f'SELECT COUNT(*) FROM news {where_sql}',
        params[:-2]
    ).fetchone()[0]

    conn.close()

    news_list = [dict(row) for row in rows]
    return jsonify({'news': news_list, 'total': total, 'offset': offset})


@app.route('/api/sources')
def get_sources():
    from sources import SOURCES
    conn = get_db()
    source_counts = {}
    for row in conn.execute('SELECT source, COUNT(*) as cnt FROM news GROUP BY source'):
        source_counts[row['source']] = row['cnt']
    conn.close()

    result = []
    for s in SOURCES:
        result.append({
            'name': s['name'],
            'name_ar': s.get('name_ar', s['name']),
            'country': s.get('country', ''),
            'type': s.get('type', ''),
            'count': source_counts.get(s['name'], 0)
        })
    return jsonify(result)


@app.route('/api/stats')
def get_stats():
    conn = get_db()
    total = conn.execute('SELECT COUNT(*) FROM news').fetchone()[0]
    last_hour = conn.execute(
        "SELECT COUNT(*) FROM news WHERE fetched_at > datetime('now', '-1 hour')"
    ).fetchone()[0]
    last_6h = conn.execute(
        "SELECT COUNT(*) FROM news WHERE fetched_at > datetime('now', '-6 hours')"
    ).fetchone()[0]
    sources_active = conn.execute('SELECT COUNT(DISTINCT source) FROM news').fetchone()[0]
    oldest = conn.execute(
        "SELECT MIN(fetched_at) FROM news"
    ).fetchone()[0]
    conn.close()

    return jsonify({
        'total_articles': total,
        'last_hour': last_hour,
        'last_6h': last_6h,
        'sources_active': sources_active,
        'oldest_article': oldest,
        'retention_hours': NEWS_RETENTION_HOURS
    })


@app.route('/api/refresh', methods=['POST'])
def manual_refresh():
    """تشغيل جلب يدوي في خيط منفصل"""
    t = threading.Thread(target=fetch_all_feeds, daemon=True)
    t.start()
    return jsonify({'status': 'جاري التحديث...', 'message': 'بدأ التحديث اليدوي'})


@app.route('/api/continents')
def get_continents():
    """عدد الأخبار لكل قارة/منطقة"""
    conn = get_db()
    rows = conn.execute('SELECT country, COUNT(*) as cnt FROM news GROUP BY country').fetchall()
    conn.close()
    country_counts = {r['country']: r['cnt'] for r in rows}

    result = []
    for name, countries in CONTINENTS.items():
        total = sum(country_counts.get(c, 0) for c in countries)
        result.append({'name': name, 'count': total})
    return jsonify(result)


@app.route('/api/source-types')
def get_source_types():
    """أنواع المصادر المتاحة مع عدد أخبار كل نوع"""
    conn = get_db()
    rows = conn.execute(
        'SELECT source_type, COUNT(*) as cnt FROM news WHERE source_type != "" GROUP BY source_type ORDER BY cnt DESC'
    ).fetchall()
    conn.close()
    return jsonify([{'type': r['source_type'], 'count': r['cnt']} for r in rows])


@app.route('/api/fetch-status')
def fetch_status():
    """تفاصيل حالة كل مصدر"""
    from sources import SOURCES
    conn = get_db()
    rows = conn.execute('SELECT source, COUNT(*) as cnt FROM news GROUP BY source').fetchall()
    conn.close()

    counts = {r['source']: r['cnt'] for r in rows}
    active   = [s for s in SOURCES if counts.get(s['name'], 0) > 0]
    inactive = [s for s in SOURCES if counts.get(s['name'], 0) == 0]

    return jsonify({
        'total_sources': len(SOURCES),
        'active_sources': len(active),
        'inactive_sources': len(inactive),
        'coverage_pct': round(len(active) / len(SOURCES) * 100, 1),
        'active': [{'name': s['name'], 'name_ar': s.get('name_ar',''), 'country': s.get('country',''), 'articles': counts[s['name']]} for s in active],
        'inactive': [{'name': s['name'], 'name_ar': s.get('name_ar',''), 'country': s.get('country',''), 'url': s.get('url','')} for s in inactive],
    })


@app.route('/status')
def status_page():
    """صفحة مراقبة المصادر"""
    return '''<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
<meta charset="UTF-8">
<meta http-equiv="refresh" content="15">
<title>حالة المصادر</title>
<style>
  body{font-family:Arial,sans-serif;background:#0f172a;color:#e2e8f0;margin:0;padding:20px}
  h1{color:#38bdf8;text-align:center}
  .stats{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin:20px 0}
  .card{background:#1e293b;border-radius:12px;padding:20px 32px;text-align:center;min-width:140px}
  .card .num{font-size:2.5rem;font-weight:bold;color:#38bdf8}
  .card .lbl{color:#94a3b8;font-size:.9rem;margin-top:4px}
  .progress{background:#1e293b;border-radius:8px;overflow:hidden;height:28px;margin:16px auto;max-width:600px}
  .bar{height:100%;background:linear-gradient(90deg,#0ea5e9,#38bdf8);transition:width .5s;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:bold;font-size:.9rem}
  table{width:100%;border-collapse:collapse;margin-top:16px;font-size:.85rem}
  th{background:#1e293b;padding:10px;color:#94a3b8;font-weight:normal}
  td{padding:8px 10px;border-bottom:1px solid #1e293b}
  .active{color:#4ade80} .inactive{color:#f87171}
  .tabs{display:flex;gap:8px;margin:20px 0;justify-content:center}
  .tab{padding:8px 24px;border-radius:8px;cursor:pointer;border:1px solid #334155;background:#1e293b;color:#94a3b8}
  .tab.on{background:#0ea5e9;color:#fff;border-color:#0ea5e9}
  #activeT,#inactiveT{display:none}
  .refresh{font-size:.8rem;color:#475569;text-align:center;margin-top:8px}
</style>
</head>
<body>
<h1>📡 حالة المصادر</h1>
<div class="stats" id="stats">جاري التحميل...</div>
<div class="progress"><div class="bar" id="bar" style="width:0%">0%</div></div>
<div class="tabs">
  <div class="tab on" onclick="show('active')">✅ نشطة</div>
  <div class="tab" onclick="show('inactive')">❌ غير نشطة</div>
</div>
<div id="activeT"><table><thead><tr><th>#</th><th>المصدر</th><th>الدولة</th><th>المقالات</th></tr></thead><tbody id="activeTb"></tbody></table></div>
<div id="inactiveT"><table><thead><tr><th>#</th><th>المصدر</th><th>الدولة</th><th>الرابط</th></tr></thead><tbody id="inactiveTb"></tbody></table></div>
<div class="refresh">🔄 يتجدد تلقائياً كل 15 ثانية</div>
<script>
let cur='active';
function show(t){
  cur=t;
  document.querySelectorAll('.tab').forEach((el,i)=>el.classList.toggle('on',['active','inactive'][i]===t));
  document.getElementById('activeT').style.display=t==='active'?'block':'none';
  document.getElementById('inactiveT').style.display=t==='inactive'?'block':'none';
}
async function load(){
  const d=await fetch('/api/fetch-status').then(r=>r.json());
  document.getElementById('stats').innerHTML=`
    <div class="card"><div class="num">${d.total_sources}</div><div class="lbl">إجمالي المصادر</div></div>
    <div class="card"><div class="num" style="color:#4ade80">${d.active_sources}</div><div class="lbl">نشطة ✅</div></div>
    <div class="card"><div class="num" style="color:#f87171">${d.inactive_sources}</div><div class="lbl">غير نشطة ❌</div></div>
    <div class="card"><div class="num" style="color:#fbbf24">${d.coverage_pct}%</div><div class="lbl">نسبة التغطية</div></div>`;
  document.getElementById('bar').style.width=d.coverage_pct+'%';
  document.getElementById('bar').textContent=d.coverage_pct+'%';
  document.getElementById('activeTb').innerHTML=d.active.map((s,i)=>
    `<tr><td>${i+1}</td><td><b>${s.name_ar}</b><br><small style="color:#64748b">${s.name}</small></td><td>${s.country}</td><td class="active">${s.articles}</td></tr>`).join('');
  document.getElementById('inactiveTb').innerHTML=d.inactive.map((s,i)=>
    `<tr><td>${i+1}</td><td><b>${s.name_ar}</b><br><small style="color:#64748b">${s.name}</small></td><td>${s.country}</td><td><small style="color:#475569;word-break:break-all">${s.url}</small></td></tr>`).join('');
  show(cur);
}
load();
</script>
</body>
</html>'''


# ========== تشغيل تلقائي عند الاستيراد (للخوادم) ==========

init_db()
_worker = threading.Thread(target=background_worker, daemon=True)
_worker.start()


# ========== التشغيل الرئيسي ==========

if __name__ == '__main__':

    hostname = _socket.gethostname()
    try:
        local_ip = _socket.gethostbyname(hostname)
    except Exception:
        local_ip = '127.0.0.1'

    print("\n" + "=" * 60)
    print("  مجمّع الأخبار العالمي - يعمل الآن!")
    print("=" * 60)
    print(f"  الوصول من هذا الحاسوب : http://localhost:5000")
    print(f"  الوصول من الـ iPhone   : http://{local_ip}:5000")
    print("  (تأكد أن الجهازين على نفس الـ WiFi)")
    print("=" * 60 + "\n")

    port = int(os.environ.get('PORT', 5000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        use_reloader=False
    )
