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
FETCH_INTERVAL = 600   # كل 10 دقائق (الجلب المتوازي أسرع)
ARTICLES_PER_SOURCE = 8  # عدد المقالات من كل مصدر


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
    """ترجمة النص إلى العربية مع تخزين مؤقت"""
    if not text or not text.strip():
        return text

    cache_key = hashlib.md5(text.encode('utf-8')).hexdigest()
    if cache_key in _translation_cache:
        return _translation_cache[cache_key]

    # تحقق من قاعدة البيانات
    conn = get_db()
    row = conn.execute(
        'SELECT arabic_title FROM news WHERE original_title = ? AND arabic_title IS NOT NULL LIMIT 1',
        (text,)
    ).fetchone()
    conn.close()
    if row:
        _translation_cache[cache_key] = row['arabic_title']
        return row['arabic_title']

    try:
        translator = GoogleTranslator(source=source_lang, target='ar')
        result = translator.translate(text[:500])  # حد 500 حرف
        if result:
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
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
        resp = _req.get(url, headers=headers, timeout=15)
        if resp.status_code != 200:
            log.debug(f"HTTP {resp.status_code}: {source['name']}")
            return 0
        feed = feedparser.parse(resp.content)

        if not feed.entries:
            log.debug(f"لا توجد مقالات: {source['name']}")
            return 0

        conn = get_db()
        c = conn.cursor()
        new_count = 0

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
            if is_arabic_source(source.get('lang', 'en')):
                arabic_title = title
            else:
                arabic_title = translate_to_arabic(title, source.get('lang', 'auto'))
                time.sleep(0.4)  # تأخير بسيط لتجنب الحظر

            # ملخص قصير
            import re
            summary = ''
            for field in ['summary', 'description']:
                val = entry.get(field, '')
                if isinstance(val, list):
                    val = val[0].get('value','') if val else ''
                if val:
                    summary = re.sub(r'<[^>]+>', '', val)[:500]
                    break

            # ترجمة الملخص
            if summary:
                if is_arabic_source(source.get('lang', 'en')):
                    summary_ar = summary
                else:
                    summary_ar = translate_to_arabic(summary, source.get('lang', 'auto'))
                    time.sleep(0.4)
            else:
                summary_ar = ''

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

        if new_count > 0:
            log.info(f"✓ {source['name']}: {new_count} مقال جديد")
        return new_count

    except Exception as e:
        log.warning(f"✗ خطأ في {source['name']}: {type(e).__name__}: {e}")
        return 0


def fetch_all_feeds():
    """جلب جميع المصادر بشكل متوازٍ - أسرع بـ 15x"""
    from sources import SOURCES
    import concurrent.futures
    log.info(f"--- بدء الجلب المتوازي من {len(SOURCES)} مصدر (15 خيط) ---")
    total = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        futures = {executor.submit(fetch_source, src): src for src in SOURCES}
        for future in concurrent.futures.as_completed(futures):
            try:
                count = future.result(timeout=30)
                total += count
            except Exception as e:
                src = futures[future]
                log.warning(f"✗ خطأ في {src['name']}: {e}")

    log.info(f"--- انتهى الجلب المتوازي: {total} مقال جديد ---")
    return total


def background_worker():
    """خيط خلفي يجلب الأخبار بصورة دورية"""
    log.info("بدء الخيط الخلفي للأخبار...")
    # الجلب الأول فوراً
    fetch_all_feeds()
    while True:
        log.info(f"الانتظار {FETCH_INTERVAL // 60} دقائق قبل الجلب التالي...")
        time.sleep(FETCH_INTERVAL)
        fetch_all_feeds()


# ========== مسارات Flask ==========

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/news')
def get_news():
    limit = min(request.args.get('limit', 100, type=int), 500)
    offset = request.args.get('offset', 0, type=int)
    source_filter = request.args.get('source', '').strip()
    search = request.args.get('q', '').strip()

    conn = get_db()

    params = []
    where_clauses = []

    if source_filter:
        where_clauses.append('source = ?')
        params.append(source_filter)

    if search:
        where_clauses.append('(arabic_title LIKE ? OR original_title LIKE ?)')
        params.extend([f'%{search}%', f'%{search}%'])

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
    sources_active = conn.execute('SELECT COUNT(DISTINCT source) FROM news').fetchone()[0]
    conn.close()

    return jsonify({
        'total_articles': total,
        'last_hour': last_hour,
        'sources_active': sources_active
    })


@app.route('/api/refresh', methods=['POST'])
def manual_refresh():
    """تشغيل جلب يدوي في خيط منفصل"""
    t = threading.Thread(target=fetch_all_feeds, daemon=True)
    t.start()
    return jsonify({'status': 'جاري التحديث...', 'message': 'بدأ التحديث اليدوي'})


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
