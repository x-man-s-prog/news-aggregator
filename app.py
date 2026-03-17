import feedparser, threading, sqlite3, time, hashlib, logging, os, gc, re, socket as _socket
import urllib.request, json
import psutil
from datetime import datetime, timezone
from flask import Flask, jsonify, render_template, request, redirect
from deep_translator import GoogleTranslator

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%H:%M:%S")
log = logging.getLogger(__name__)
app = Flask(__name__)

DB_PATH               = "news.db"
FETCH_INTERVAL        = 900
ARTICLES_PER_SOURCE   = 3
TRANSLATION_CACHE_LIMIT = 500
NEWS_RETENTION_HOURS  = 12
MAX_ROWS              = 8000
MEMORY_LIMIT_PCT      = 75

CONTINENTS = {
    "الشرق الأوسط": ["السعودية","الإمارات","قطر","الكويت","البحرين","عُمان","اليمن","العراق",
        "سوريا","لبنان","الأردن","فلسطين","مصر","ليبيا","تونس","الجزائر","المغرب",
        "السودان","إيران","تركيا","إسرائيل","أفغانستان"],
    "أوروبا": ["بريطانيا","فرنسا","ألمانيا","إيطاليا","إسبانيا","هولندا","بلجيكا",
        "سويسرا","النرويج","السويد","الدنمارك","فنلندا","أيرلندا","أوكرانيا",
        "بولندا","المجر","رومانيا","اليونان","روسيا","أوروبا"],
    "أمريكا الشمالية": ["أمريكا","كندا","المكسيك"],
    "أمريكا اللاتينية": ["البرازيل","الأرجنتين","تشيلي","كولومبيا","بيرو","فنزويلا"],
    "آسيا": ["الهند","باكستان","اليابان","كوريا الجنوبية","الصين","تايوان",
        "سنغافورة","ماليزيا","إندونيسيا","الفلبين","تايلاند","فيتنام"],
    "أفريقيا": ["نيجيريا","كينيا","جنوب أفريقيا","إثيوبيا","غانا","الصومال","أفريقيا"],
    "أوقيانوسيا": ["أستراليا","نيوزيلندا","أوقيانوسيا"],
}


def get_memory_pct():
    return psutil.virtual_memory().percent

def get_db_row_count():
    try:
        conn = sqlite3.connect(DB_PATH, timeout=5)
        n = conn.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        conn.close(); return n
    except: return 0

def memory_cleanup(reason=""):
    log.warning("🧹 تنظيف [%s] ذاكرة=%.1f%%", reason, get_memory_pct())
    try:
        conn = sqlite3.connect(DB_PATH, timeout=30)
        c = conn.cursor()
        before = c.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        c.execute("DELETE FROM news WHERE fetched_at < datetime('now', ?)",
                  (f"-{NEWS_RETENTION_HOURS} hours",))
        after_t = c.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        if after_t > MAX_ROWS:
            c.execute("DELETE FROM news WHERE id IN (SELECT id FROM news ORDER BY fetched_at ASC LIMIT ?)",
                      (after_t - MAX_ROWS,))
        after_all = c.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        conn.commit(); conn.close()
        log.info("🧹 حُذف %d | متبقٍّ: %d", before - after_all, after_all)
        conn2 = sqlite3.connect(DB_PATH, timeout=60)
        conn2.execute("VACUUM"); conn2.close()
    except Exception as e:
        log.warning("خطأ cleanup: %s", e)
    global _translation_cache
    _translation_cache.clear()
    gc.collect()
    log.info("✅ تنظيف انتهى ذاكرة=%.1f%%", get_memory_pct())

def _memory_watchdog():
    log.info("👁️ مراقب الذاكرة (حد=%d%%)", MEMORY_LIMIT_PCT)
    while True:
        time.sleep(300)
        mem = get_memory_pct(); rows = get_db_row_count()
        log.info("📊 ذاكرة=%.1f%% | DB=%d سجل", mem, rows)
        if mem >= MEMORY_LIMIT_PCT:
            memory_cleanup(f"ذاكرة {mem:.0f}%")
        elif rows > MAX_ROWS:
            memory_cleanup(f"DB {rows} سجل")


def init_db():
    conn = sqlite3.connect(DB_PATH, timeout=30)
    c = conn.cursor()
    c.execute("PRAGMA journal_mode=WAL")
    c.execute("PRAGMA synchronous=NORMAL")
    c.execute("PRAGMA cache_size=-8000")
    c.execute("PRAGMA temp_store=MEMORY")
    c.execute("""CREATE TABLE IF NOT EXISTS news (
        id TEXT PRIMARY KEY, source TEXT NOT NULL, source_ar TEXT,
        country TEXT, source_type TEXT, original_title TEXT NOT NULL,
        arabic_title TEXT, summary TEXT, summary_ar TEXT,
        image_url TEXT DEFAULT "", link TEXT, published TEXT,
        original_lang TEXT DEFAULT "en", fetched_at TEXT NOT NULL)""")
    for s in ["ALTER TABLE news ADD COLUMN image_url TEXT DEFAULT \"\"",
              "ALTER TABLE news ADD COLUMN summary_ar TEXT"]:
        try: c.execute(s)
        except: pass
    for idx in [
        "CREATE INDEX IF NOT EXISTS idx_fetched ON news(fetched_at DESC)",
        "CREATE INDEX IF NOT EXISTS idx_source  ON news(source)",
        "CREATE INDEX IF NOT EXISTS idx_country ON news(country)",
        "CREATE INDEX IF NOT EXISTS idx_type    ON news(source_type)",
        "CREATE INDEX IF NOT EXISTS idx_cf      ON news(country, fetched_at DESC)",
    ]:
        c.execute(idx)
    conn.commit(); conn.close()
    log.info("قاعدة البيانات جاهزة.")

def get_db():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=30)
    conn.row_factory = sqlite3.Row
    return conn

_translation_cache = {}

def translate_to_arabic(text, source_lang="auto"):
    if not text or not text.strip(): return text
    key = hashlib.md5(text.encode("utf-8")).hexdigest()
    if key in _translation_cache: return _translation_cache[key]
    try:
        result = GoogleTranslator(source=source_lang, target="ar").translate(text[:500])
        if result:
            if len(_translation_cache) >= TRANSLATION_CACHE_LIMIT:
                for k in list(_translation_cache.keys())[:TRANSLATION_CACHE_LIMIT // 4]:
                    del _translation_cache[k]
            _translation_cache[key] = result
            return result
    except Exception as e: log.warning("فشل الترجمة: %s", e)
    return text

def is_arabic_source(lang): return lang == "ar"


def get_entry_image(entry):
    mt = getattr(entry, "media_thumbnail", None)
    if mt and isinstance(mt, list) and mt[0].get("url"): return mt[0]["url"]
    mc = getattr(entry, "media_content", None)
    if mc and isinstance(mc, list):
        for m in mc:
            if m.get("url") and ("image" in m.get("type","") or
                m.get("url","").endswith((".jpg",".jpeg",".png",".webp"))):
                return m["url"]
    for field in ["summary","description","content"]:
        val = entry.get(field,"")
        if isinstance(val, list): val = val[0].get("value","") if val else ""
        if val:
            m = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', val)
            if m and m.group(1).startswith("http"): return m.group(1)
    return ""

def get_article_id(link, title):
    return hashlib.md5(f"{link}{title}".encode("utf-8")).hexdigest()

def parse_date(entry):
    for f in ["published","updated","created"]:
        v = getattr(entry, f, None)
        if v: return str(v)
    return datetime.now(timezone.utc).isoformat()

def fetch_source(source):
    if get_memory_pct() >= MEMORY_LIMIT_PCT:
        log.warning("تخطي %s (ذاكرة ممتلئة)", source.get("name",""))
        return 0
    url = source.get("url")
    if not url: return 0
    try:
        import requests as _req
        resp = _req.get(url, headers={"User-Agent":"Mozilla/5.0 (compatible; NewsBot/1.0)"},
                        timeout=10, stream=False)
        if resp.status_code != 200: return 0
        feed = feedparser.parse(resp.content)
        del resp; gc.collect()
        if not feed.entries: return 0
        conn = get_db(); c = conn.cursor(); new_count = 0
        is_ar = is_arabic_source(source.get("lang","en"))
        src_lang = source.get("lang","auto")
        for entry in feed.entries[:ARTICLES_PER_SOURCE]:
            link  = entry.get("link","").strip()
            title = entry.get("title","").strip()
            if not link or not title: continue
            aid = get_article_id(link, title)
            if c.execute("SELECT 1 FROM news WHERE id=?", (aid,)).fetchone(): continue
            arabic_title = title if is_ar else translate_to_arabic(title, src_lang)
            if not is_ar: time.sleep(0.2)
            summary = ""
            for fld in ["summary","description"]:
                val = entry.get(fld,"")
                if isinstance(val, list): val = val[0].get("value","") if val else ""
                if val: summary = re.sub(r"<[^>]+>","",val)[:400]; break
            summary_ar = summary if is_ar else (translate_to_arabic(summary[:300], src_lang) if summary else "")
            if summary and not is_ar: time.sleep(0.2)
            c.execute("""INSERT OR IGNORE INTO news
                (id,source,source_ar,country,source_type,original_title,arabic_title,
                 summary,summary_ar,image_url,link,published,original_lang,fetched_at)
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (aid, source["name"], source.get("name_ar",source["name"]),
                 source.get("country",""), source.get("type",""),
                 title, arabic_title, summary, summary_ar,
                 get_entry_image(entry), link, parse_date(entry),
                 source.get("lang","en"), datetime.now(timezone.utc).isoformat()))
            new_count += 1
        conn.commit(); conn.close()
        del feed; gc.collect()
        if new_count > 0: log.info("✓ %s: %d مقال", source["name"], new_count)
        return new_count
    except Exception as e:
        log.warning("✗ %s: %s", source.get("name",""), e)
        return 0

def fetch_all_feeds():
    from sources import SOURCES
    import concurrent.futures
    log.info("--- جلب من %d مصدر (4 خيوط) ---", len(SOURCES))
    total = 0
    for i in range(0, len(SOURCES), 50):
        mem = get_memory_pct()
        if mem >= MEMORY_LIMIT_PCT:
            log.warning("إيقاف الجلب ذاكرة=%.1f%%", mem)
            memory_cleanup(f"اثناء الجلب {mem:.0f}%")
            break
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
            fts = {ex.submit(fetch_source, s): s for s in SOURCES[i:i+50]}
            for f in concurrent.futures.as_completed(fts):
                try: total += f.result(timeout=30)
                except Exception as e: log.warning("✗ %s: %s", fts[f].get("name",""), e)
        gc.collect()
        log.info("دفعة %d ذاكرة=%.1f%%", i//50+1, get_memory_pct())
    log.info("--- انتهى الجلب: %d جديد ---", total)
    return total

def cleanup_old_news():
    try:
        conn = get_db(); c = conn.cursor()
        before = c.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        c.execute("DELETE FROM news WHERE fetched_at < datetime('now', ?)",
                  (f"-{NEWS_RETENTION_HOURS} hours",))
        after_t = c.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        if after_t > MAX_ROWS:
            c.execute("DELETE FROM news WHERE id IN (SELECT id FROM news ORDER BY fetched_at ASC LIMIT ?)",
                      (after_t - MAX_ROWS,))
        after_all = c.execute("SELECT COUNT(*) FROM news").fetchone()[0]
        conn.commit(); conn.close()
        if before - after_all > 0:
            log.info("🧹 حذف %d | متبقٍّ=%d | ذاكرة=%.1f%%", before-after_all, after_all, get_memory_pct())
        conn2 = get_db(); conn2.execute("VACUUM"); conn2.close()
    except Exception as e: log.warning("خطأ cleanup: %s", e)

def background_worker():
    log.info("بدء الخيط الخلفي...")
    cleanup_old_news()
    fetch_all_feeds()
    cleanup_old_news(); gc.collect()
    while True:
        log.info("⏳ انتظار %d دقيقة...", FETCH_INTERVAL//60)
        time.sleep(FETCH_INTERVAL)
        fetch_all_feeds()
        cleanup_old_news(); gc.collect()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/news")
def get_news():
    limit  = min(request.args.get("limit", 100, type=int), 500)
    offset = request.args.get("offset", 0, type=int)
    sf = request.args.get("source","").strip()
    q  = request.args.get("q","").strip()
    ct = request.args.get("continent","").strip()
    st = request.args.get("type","").strip()
    conn = get_db(); params = []; wc = []
    if sf: wc.append("source=?"); params.append(sf)
    if q:  wc.append("(arabic_title LIKE ? OR original_title LIKE ?)"); params.extend([f"%{q}%",f"%{q}%"])
    if ct and ct in CONTINENTS:
        cls2 = CONTINENTS[ct]; wc.append("country IN ("+",".join(["?"]*len(cls2))+")"); params.extend(cls2)
    if st: wc.append("source_type=?"); params.append(st)
    ws = ("WHERE "+" AND ".join(wc)) if wc else ""
    params.extend([limit, offset])
    rows  = conn.execute(
        "SELECT id,source,source_ar,country,source_type,original_title,arabic_title,"
        "summary,summary_ar,image_url,link,published,original_lang,fetched_at "
        f"FROM news {ws} ORDER BY fetched_at DESC LIMIT ? OFFSET ?", params).fetchall()
    total = conn.execute(f"SELECT COUNT(*) FROM news {ws}", params[:-2]).fetchone()[0]
    conn.close()
    return jsonify({"news":[dict(r) for r in rows],"total":total,"offset":offset})

@app.route("/api/sources")
def get_sources():
    from sources import SOURCES
    conn = get_db()
    sc = {r["source"]:r["cnt"] for r in conn.execute("SELECT source,COUNT(*) as cnt FROM news GROUP BY source")}
    conn.close()
    return jsonify([{"name":s["name"],"name_ar":s.get("name_ar",s["name"]),"country":s.get("country",""),"type":s.get("type",""),"count":sc.get(s["name"],0)} for s in SOURCES])

@app.route("/api/stats")
def get_stats():
    conn = get_db()
    r = {
        "total_articles": conn.execute("SELECT COUNT(*) FROM news").fetchone()[0],
        "last_hour":      conn.execute("SELECT COUNT(*) FROM news WHERE fetched_at>datetime('now','-1 hour')").fetchone()[0],
        "last_6h":        conn.execute("SELECT COUNT(*) FROM news WHERE fetched_at>datetime('now','-6 hours')").fetchone()[0],
        "sources_active": conn.execute("SELECT COUNT(DISTINCT source) FROM news").fetchone()[0],
        "oldest_article": conn.execute("SELECT MIN(fetched_at) FROM news").fetchone()[0],
        "retention_hours":NEWS_RETENTION_HOURS, "max_rows":MAX_ROWS,
        "memory_pct":round(get_memory_pct(),1),
    }
    conn.close(); return jsonify(r)

@app.route("/api/memory")
def memory_status():
    vm = psutil.virtual_memory()
    return jsonify({
        "memory_total_mb":round(vm.total/1024/1024),
        "memory_used_mb": round(vm.used/1024/1024),
        "memory_free_mb": round(vm.available/1024/1024),
        "memory_pct":     round(vm.percent,1),
        "memory_limit_pct":MEMORY_LIMIT_PCT,
        "db_rows":        get_db_row_count(),
        "db_max_rows":    MAX_ROWS,
        "cache_size":     len(_translation_cache),
        "status": "🔴 خطر" if vm.percent>=MEMORY_LIMIT_PCT else
                  "🟡 تحذير" if vm.percent>=MEMORY_LIMIT_PCT-10 else "🟢 طبيعي",
    })

@app.route("/api/cleanup", methods=["POST"])
def manual_cleanup():
    before = get_memory_pct()
    memory_cleanup("يدوي")
    return jsonify({"status":"تم","memory_before":round(before,1),"memory_after":round(get_memory_pct(),1),"db_rows":get_db_row_count()})

@app.route("/api/refresh", methods=["POST"])
def manual_refresh():
    threading.Thread(target=fetch_all_feeds, daemon=True).start()
    return jsonify({"status":"جاري التحديث..."})

@app.route("/api/continents")
def get_continents():
    conn = get_db()
    cc = {r["country"]:r["cnt"] for r in conn.execute("SELECT country,COUNT(*) as cnt FROM news GROUP BY country")}
    conn.close()
    return jsonify([{"name":n,"count":sum(cc.get(c,0) for c in cl)} for n,cl in CONTINENTS.items()])

@app.route("/api/source-types")
def get_source_types():
    conn = get_db()
    rows = conn.execute("SELECT source_type,COUNT(*) as cnt FROM news WHERE source_type!='' GROUP BY source_type ORDER BY cnt DESC").fetchall()
    conn.close()
    return jsonify([{"type":r["source_type"],"count":r["cnt"]} for r in rows])

@app.route("/api/fetch-status")
def fetch_status():
    from sources import SOURCES
    conn = get_db()
    counts = {r["source"]:r["cnt"] for r in conn.execute("SELECT source,COUNT(*) as cnt FROM news GROUP BY source")}
    conn.close()
    active   = [s for s in SOURCES if counts.get(s["name"],0)>0]
    inactive = [s for s in SOURCES if counts.get(s["name"],0)==0]
    return jsonify({
        "total_sources":len(SOURCES),"active_sources":len(active),"inactive_sources":len(inactive),
        "coverage_pct":round(len(active)/len(SOURCES)*100,1),
        "active":[{"name":s["name"],"name_ar":s.get("name_ar",""),"country":s.get("country",""),"articles":counts[s["name"]]} for s in active],
        "inactive":[{"name":s["name"],"name_ar":s.get("name_ar",""),"country":s.get("country",""),"url":s.get("url","")} for s in inactive],
    })

@app.route("/status")
def status_page():
    return redirect("/api/fetch-status")


# ══════════════════════════════════════════════════════════
# تكامل تيليجرام - @Sa10220bot يستقبل الأوامر في المجموعة
# ══════════════════════════════════════════════════════════
BOT1_TOKEN  = os.getenv("BOT1_TOKEN", "8768938352:AAGZsnJH3mqTIWULkW7DhKeGr_EflnV3Wys")
GROUP_ID    = os.getenv("GROUP_CHAT_ID", "-1003782532470")

def _tg_send(text: str) -> None:
    """إرسال رسالة للمجموعة"""
    if not BOT1_TOKEN or not GROUP_ID:
        return
    try:
        payload = json.dumps({"chat_id": GROUP_ID, "text": text}).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{BOT1_TOKEN}/sendMessage",
            data=payload, headers={"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        log.warning("TG send error: %s", e)


def _tg_poll_commands():
    """
    يستقبل الأوامر من المجموعة:
      /stats  → إحصائيات المصادر والأخبار
      /now    → عدد الأخبار الجديدة
    """
    offset = 0
    time.sleep(10)
    log.info("🎧 Bot1 يستمع للأوامر في المجموعة...")
    while True:
        try:
            url = (f"https://api.telegram.org/bot{BOT1_TOKEN}/getUpdates"
                   f"?timeout=25&offset={offset}&allowed_updates=message")
            with urllib.request.urlopen(url, timeout=35) as r:
                updates = json.loads(r.read()).get("result", [])
            for upd in updates:
                offset = upd["update_id"] + 1
                msg  = upd.get("message", {})
                text = msg.get("text", "").strip().lower()
                if not text:
                    continue

                if text in ("/stats", "/stats@sa10220bot"):
                    conn = get_db()
                    total = conn.execute("SELECT COUNT(*) FROM news").fetchone()[0]
                    last_h = conn.execute(
                        "SELECT COUNT(*) FROM news WHERE fetched_at > datetime('now','-1 hour')"
                    ).fetchone()[0]
                    sources_active = conn.execute(
                        "SELECT COUNT(DISTINCT source) FROM news"
                    ).fetchone()[0]
                    conn.close()
                    _tg_send(
                        f"📊 إحصائيات البوت الأول\n\n"
                        f"🗞 إجمالي الأخبار: {total:,}\n"
                        f"⏱ آخر ساعة: {last_h:,} خبر\n"
                        f"📡 مصادر نشطة: {sources_active} مصدر\n"
                        f"🕐 آخر تحديث: {datetime.now(timezone.utc).strftime('%H:%M UTC')}"
                    )

        except Exception as e:
            log.warning("Bot1 poll error: %s", e)
            time.sleep(5)


init_db()
threading.Thread(target=background_worker,     daemon=True).start()
threading.Thread(target=_memory_watchdog,      daemon=True).start()
threading.Thread(target=_tg_poll_commands,     daemon=True).start()


if __name__ == "__main__":
    hostname = _socket.gethostname()
    try: local_ip = _socket.gethostbyname(hostname)
    except: local_ip = "127.0.0.1"
    print("-"*60)
    print("  مجمّع الأخبار العالمي")
    print(f"  http://localhost:5000  |  http://{local_ip}:5000")
    print("-"*60)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
