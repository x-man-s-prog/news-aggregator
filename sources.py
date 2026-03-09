# قائمة مصادر الأخبار مع روابط RSS
# lang: ar = عربي (بدون ترجمة), en/fr/de/... = يُترجم للعربية

SOURCES = [

    # ==========================================
    # وكالات أنباء عالمية
    # ==========================================
    {"id": 1,   "name": "Reuters",            "name_ar": "رويترز",               "country": "بريطانيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.reuters.com/reuters/topNews"},
    {"id": 2,   "name": "AP News",            "name_ar": "أسوشيتد برس",         "country": "أمريكا",          "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.apnews.com/rss/apf-topnews"},
    {"id": 6,   "name": "AFP",                "name_ar": "فرانس برس",            "country": "فرنسا",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.france24.com/en/rss"},
    {"id": 62,  "name": "ANSA",               "name_ar": "أنسا",                 "country": "إيطاليا",         "type": "وكالة أنباء", "lang": "it", "url": "https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml"},
    {"id": 63,  "name": "EFE",                "name_ar": "وكالة إيفي",           "country": "إسبانيا",         "type": "وكالة أنباء", "lang": "es", "url": "https://www.efe.com/efe/espana/1/rss"},
    {"id": 65,  "name": "Kyodo News",         "name_ar": "كيودو نيوز",           "country": "اليابان",         "type": "وكالة أنباء", "lang": "en", "url": "https://english.kyodonews.net/rss/all.xml"},
    {"id": 66,  "name": "Yonhap News",        "name_ar": "يونهاب",               "country": "كوريا الجنوبية", "type": "وكالة أنباء", "lang": "en", "url": "https://en.yna.co.kr/RSS/news.xml"},
    {"id": 83,  "name": "Agência Brasil",     "name_ar": "وكالة البرازيل",       "country": "البرازيل",        "type": "وكالة أنباء", "lang": "pt", "url": "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"},

    # ==========================================
    # بريطانيا
    # ==========================================
    {"id": 3,   "name": "BBC News",           "name_ar": "بي بي سي",             "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://feeds.bbci.co.uk/news/world/rss.xml"},
    {"id": 101, "name": "Sky News",           "name_ar": "سكاي نيوز",            "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://feeds.skynews.com/feeds/rss/world.xml"},
    {"id": 4,   "name": "The Guardian",       "name_ar": "الغارديان",            "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.theguardian.com/world/rss"},
    {"id": 9,   "name": "The Economist",      "name_ar": "الإيكونوميست",         "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.economist.com/the-world-this-week/rss.xml"},
    {"id": 10,  "name": "Financial Times",    "name_ar": "فايننشال تايمز",       "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.ft.com/rss/home"},
    {"id": 51,  "name": "The Independent",    "name_ar": "الإندبندنت",           "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.independent.co.uk/news/world/rss"},
    {"id": 23,  "name": "The Times London",   "name_ar": "ذا تايمز",             "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.thetimes.co.uk/rss/home"},
    {"id": 92,  "name": "Middle East Eye",    "name_ar": "ميدل إيست آي",         "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://www.middleeasteye.net/rss"},
    {"id": 104, "name": "Iran International", "name_ar": "إيران إنترناشيونال",   "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://www.iranintl.com/en/rss"},

    # ==========================================
    # أمريكا
    # ==========================================
    {"id": 5,   "name": "New York Times",     "name_ar": "نيويورك تايمز",        "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://rss.nytimes.com/services/xml/rss/nf/HomePage.xml"},
    {"id": 11,  "name": "Washington Post",    "name_ar": "واشنطن بوست",          "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://feeds.washingtonpost.com/rss/world"},
    {"id": 15,  "name": "NPR News",           "name_ar": "إن بي آر",             "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://feeds.npr.org/1001/rss.xml"},
    {"id": 16,  "name": "Wall Street Journal","name_ar": "وول ستريت جورنال",    "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://feeds.a.dj.com/rss/RSSWorldNews.xml"},
    {"id": 17,  "name": "Politico",           "name_ar": "بوليتيكو",             "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.politico.com/rss/politicopicks.xml"},
    {"id": 28,  "name": "Axios",              "name_ar": "أكسيوس",               "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://api.axios.com/feed/"},
    {"id": 29,  "name": "Bloomberg",          "name_ar": "بلومبرغ",              "country": "أمريكا",          "type": "مالي",        "lang": "en", "url": "https://feeds.bloomberg.com/politics/news.rss"},
    {"id": 27,  "name": "The Atlantic",       "name_ar": "ذا أتلانتيك",          "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.theatlantic.com/feed/all/"},
    {"id": 26,  "name": "ProPublica",         "name_ar": "بروبابليكا",           "country": "أمريكا",          "type": "استقصائي",    "lang": "en", "url": "https://feeds.propublica.org/propublica/main"},
    {"id": 43,  "name": "The Intercept",      "name_ar": "ذا إنترسبت",           "country": "أمريكا",          "type": "استقصائي",    "lang": "en", "url": "https://theintercept.com/feed/?lang=en"},
    {"id": 44,  "name": "Science News",       "name_ar": "ساينس نيوز",           "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.sciencenews.org/feed"},
    {"id": 42,  "name": "Al-Monitor",         "name_ar": "المونيتور",            "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.al-monitor.com/rss.xml"},
    {"id": 200, "name": "Vox",                "name_ar": "فوكس",                 "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.vox.com/rss/index.xml"},
    {"id": 201, "name": "The Hill",           "name_ar": "ذا هيل",               "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://thehill.com/news/feed/"},
    {"id": 202, "name": "Foreign Policy",     "name_ar": "فورين بوليسي",         "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://foreignpolicy.com/feed/"},
    {"id": 203, "name": "Foreign Affairs",    "name_ar": "فورين أفيرز",          "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.foreignaffairs.com/rss.xml"},
    {"id": 204, "name": "MIT Tech Review",    "name_ar": "ميت تكنولوجي ريفيو",  "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.technologyreview.com/feed/"},
    {"id": 205, "name": "Wired",              "name_ar": "وايرد",                "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.wired.com/feed/rss"},
    {"id": 206, "name": "TIME Magazine",      "name_ar": "مجلة تايم",            "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://time.com/feed/"},
    {"id": 207, "name": "Newsweek",           "name_ar": "نيوزويك",              "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.newsweek.com/rss"},

    # ==========================================
    # عربي (لا يحتاج ترجمة)
    # ==========================================
    {"id": 14,  "name": "Al Jazeera English", "name_ar": "الجزيرة الإنجليزية",  "country": "قطر",             "type": "تلفزيون",     "lang": "en", "url": "https://www.aljazeera.com/xml/rss/all.xml"},
    {"id": 300, "name": "Al Jazeera Arabic",  "name_ar": "الجزيرة عربي",        "country": "قطر",             "type": "تلفزيون",     "lang": "ar", "url": "https://www.aljazeera.net/rss"},
    {"id": 90,  "name": "Al Arabiya",         "name_ar": "العربية",              "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.alarabiya.net/ar/rss.xml"},
    {"id": 91,  "name": "Asharq Al-Awsat",    "name_ar": "الشرق الأوسط",        "country": "بريطانيا",        "type": "صحيفة",       "lang": "ar", "url": "https://aawsat.com/rss.xml"},
    {"id": 301, "name": "Sky News Arabia",    "name_ar": "سكاي نيوز عربية",     "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.skynewsarabia.com/web/rss"},
    {"id": 302, "name": "BBC Arabic",         "name_ar": "بي بي سي عربي",       "country": "بريطانيا",        "type": "تلفزيون",     "lang": "ar", "url": "https://feeds.bbci.co.uk/arabic/rss.xml"},
    {"id": 303, "name": "France 24 Arabic",   "name_ar": "فرانس 24 عربي",       "country": "فرنسا",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.france24.com/ar/rss"},
    {"id": 304, "name": "DW Arabic",          "name_ar": "دويتشه فيله عربي",    "country": "ألمانيا",         "type": "تلفزيون",     "lang": "ar", "url": "https://rss.dw.com/rdf/rss-ar-all"},
    {"id": 305, "name": "RT Arabic",          "name_ar": "RT عربي",              "country": "روسيا",           "type": "تلفزيون",     "lang": "ar", "url": "https://arabic.rt.com/rss/"},
    {"id": 306, "name": "Raseef22",           "name_ar": "رصيف22",               "country": "لبنان",           "type": "رقمي",        "lang": "ar", "url": "https://raseef22.net/feed/"},
    {"id": 307, "name": "Daraj Media",        "name_ar": "درج",                  "country": "لبنان",           "type": "رقمي",        "lang": "ar", "url": "https://daraj.media/feed/"},
    {"id": 309, "name": "Mada Masr",          "name_ar": "مدى مصر",              "country": "مصر",             "type": "رقمي",        "lang": "ar", "url": "https://www.madamasr.com/ar/feed/"},
    {"id": 310, "name": "The New Arab",       "name_ar": "العربي الجديد",        "country": "بريطانيا",        "type": "رقمي",        "lang": "ar", "url": "https://www.alaraby.co.uk/rss.xml"},
    {"id": 311, "name": "Al-Araby Al-Jadeed", "name_ar": "القدس العربي",         "country": "بريطانيا",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alquds.co.uk/feed/"},
    {"id": 312, "name": "Anadolu Arabic",     "name_ar": "الأناضول عربي",        "country": "تركيا",           "type": "وكالة أنباء", "lang": "ar", "url": "https://www.aa.com.tr/ar/rss/default?cat=general"},
    {"id": 313, "name": "Asharq News",        "name_ar": "الشرق للأخبار",        "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://asharq.com/feed/"},

    # ==========================================
    # ألمانيا
    # ==========================================
    {"id": 13,  "name": "DW News",            "name_ar": "دويتشه فيله",          "country": "ألمانيا",         "type": "تلفزيون",     "lang": "en", "url": "https://rss.dw.com/rdf/rss-en-all"},
    {"id": 7,   "name": "Der Spiegel",        "name_ar": "دير شبيغل",            "country": "ألمانيا",         "type": "مجلة",        "lang": "de", "url": "https://www.spiegel.de/international/index.rss"},
    {"id": 22,  "name": "Süddeutsche Zeitung","name_ar": "زودويتشه تسايتونغ",   "country": "ألمانيا",         "type": "صحيفة",       "lang": "de", "url": "https://rss.sueddeutsche.de/rss/Topthemen"},
    {"id": 54,  "name": "ARD Tagesschau",     "name_ar": "تاغسشاو",              "country": "ألمانيا",         "type": "تلفزيون",     "lang": "de", "url": "https://www.tagesschau.de/xml/rss2/"},
    {"id": 55,  "name": "ZDF Nachrichten",    "name_ar": "زد دي إف",             "country": "ألمانيا",         "type": "تلفزيون",     "lang": "de", "url": "https://www.zdf.de/rss/zdf/nachrichten-100.xml"},

    # ==========================================
    # فرنسا
    # ==========================================
    {"id": 8,   "name": "Le Monde",           "name_ar": "لوموند",               "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.lemonde.fr/rss/une.xml"},
    {"id": 47,  "name": "Le Figaro",          "name_ar": "لوفيغارو",             "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.lefigaro.fr/rss/figaro_flash-actu.xml"},
    {"id": 18,  "name": "RFI English",        "name_ar": "راديو فرانس إنترناشيونال","country": "فرنسا",       "type": "راديو",       "lang": "en", "url": "https://www.rfi.fr/en/rss"},
    {"id": 56,  "name": "France 24 English",  "name_ar": "فرانس 24",             "country": "فرنسا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.france24.com/en/rss"},
    {"id": 400, "name": "Libération",         "name_ar": "ليبيراسيون",           "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.liberation.fr/arc/outboundfeeds/rss-all/"},

    # ==========================================
    # إسبانيا / أمريكا اللاتينية
    # ==========================================
    {"id": 19,  "name": "El País",            "name_ar": "إل باييس",             "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"},
    {"id": 39,  "name": "El Espectador",      "name_ar": "إل إسبيكتادور",        "country": "كولومبيا",        "type": "صحيفة",       "lang": "es", "url": "https://www.elespectador.com/noticias/feed"},
    {"id": 78,  "name": "La Jornada",         "name_ar": "لا خورنادا",            "country": "المكسيك",         "type": "صحيفة",       "lang": "es", "url": "https://www.jornada.com.mx/rss/politica.xml"},
    {"id": 80,  "name": "Clarín",             "name_ar": "كلارين",               "country": "الأرجنتين",       "type": "صحيفة",       "lang": "es", "url": "https://www.clarin.com/rss/lo-ultimo/"},
    {"id": 82,  "name": "La Nación Argentina","name_ar": "لا ناسيون",            "country": "الأرجنتين",       "type": "صحيفة",       "lang": "es", "url": "https://www.lanacion.com.ar/arc/outboundfeeds/rss/"},
    {"id": 84,  "name": "Infobae",            "name_ar": "إنفوباي",              "country": "الأرجنتين",       "type": "رقمي",        "lang": "es", "url": "https://www.infobae.com/feeds/rss/"},
    {"id": 41,  "name": "Folha de S.Paulo",   "name_ar": "فولها دي ساو باولو",   "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://feeds.folha.uol.com.br/mundo/rss091.xml"},
    {"id": 79,  "name": "O Globo",            "name_ar": "أو غلوبو",             "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://oglobo.globo.com/rss.xml"},

    # ==========================================
    # إيطاليا
    # ==========================================
    {"id": 20,  "name": "Corriere della Sera","name_ar": "كورييري ديلا سيرا",   "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.corriere.it/rss/homepage.xml"},
    {"id": 48,  "name": "La Repubblica",      "name_ar": "لا ريبوبليكا",         "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.repubblica.it/rss/homepage/rss2.0.xml"},

    # ==========================================
    # هولندا / بلجيكا / أوروبا
    # ==========================================
    {"id": 33,  "name": "NOS News",           "name_ar": "نوس نيوز",             "country": "هولندا",          "type": "تلفزيون",     "lang": "nl", "url": "https://feeds.nos.nl/nosnieuwsalgemeen"},
    {"id": 52,  "name": "Euronews",           "name_ar": "يورونيوز",             "country": "أوروبا",          "type": "تلفزيون",     "lang": "en", "url": "https://www.euronews.com/rss?format=mrss&level=theme&name=news"},
    {"id": 57,  "name": "RTBF",               "name_ar": "آر تي بي إف",          "country": "بلجيكا",          "type": "تلفزيون",     "lang": "fr", "url": "https://www.rtbf.be/rss/info/general"},

    # ==========================================
    # إسكندنافيا وأوروبا الشمالية
    # ==========================================
    {"id": 32,  "name": "SVT Nyheter",        "name_ar": "إس في تي",             "country": "السويد",          "type": "تلفزيون",     "lang": "sv", "url": "https://www.svt.se/nyheter/rss.xml"},
    {"id": 61,  "name": "NRK Nyheter",        "name_ar": "إن آر كي",             "country": "النرويج",         "type": "تلفزيون",     "lang": "no", "url": "https://www.nrk.no/nyheter/siste.rss"},
    {"id": 35,  "name": "Yle News",           "name_ar": "يلي نيوز",             "country": "فنلندا",          "type": "تلفزيون",     "lang": "fi", "url": "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss"},
    {"id": 60,  "name": "DR News",            "name_ar": "دي آر",                "country": "الدنمارك",        "type": "تلفزيون",     "lang": "da", "url": "https://www.dr.dk/nyheder/service/feeds/allenyheder"},
    {"id": 45,  "name": "Der Standard",       "name_ar": "دير ستاندارد",         "country": "النمسا",          "type": "صحيفة",       "lang": "de", "url": "https://www.derstandard.at/rss"},
    {"id": 59,  "name": "ORF News",           "name_ar": "أو آر إف",             "country": "النمسا",          "type": "تلفزيون",     "lang": "de", "url": "https://rss.orf.at/news.xml"},
    {"id": 46,  "name": "NZZ",                "name_ar": "نيويه تسورخر",         "country": "سويسرا",          "type": "صحيفة",       "lang": "de", "url": "https://www.nzz.ch/recent.rss"},
    {"id": 53,  "name": "RTS Info",           "name_ar": "آر تي إس",             "country": "سويسرا",          "type": "تلفزيون",     "lang": "fr", "url": "https://www.rts.ch/info/rss/"},
    {"id": 31,  "name": "Irish Times",        "name_ar": "آيريش تايمز",          "country": "أيرلندا",         "type": "صحيفة",       "lang": "en", "url": "https://www.irishtimes.com/arc/outboundfeeds/rss/"},
    {"id": 96,  "name": "Gazeta Wyborcza",    "name_ar": "غازيتا ويبورتشا",      "country": "بولندا",          "type": "صحيفة",       "lang": "pl", "url": "https://wyborcza.pl/rss/wyborcza.xml"},

    # ==========================================
    # روسيا / أوروبا الشرقية
    # ==========================================
    {"id": 93,  "name": "Kommersant",         "name_ar": "كوميرسانت",            "country": "روسيا",           "type": "صحيفة",       "lang": "ru", "url": "https://www.kommersant.ru/RSS/main.xml"},
    {"id": 95,  "name": "Meduza",             "name_ar": "ميدوزا",               "country": "لاتفيا",          "type": "رقمي",        "lang": "ru", "url": "https://meduza.io/rss/all"},
    {"id": 103, "name": "RT News",            "name_ar": "روسيا اليوم",          "country": "روسيا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.rt.com/rss/news/"},

    # ==========================================
    # إسرائيل
    # ==========================================
    {"id": 30,  "name": "Haaretz",            "name_ar": "هآرتس",                "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.haaretz.com/rss"},
    {"id": 700, "name": "The Jerusalem Post", "name_ar": "جيروزاليم بوست",       "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.jpost.com/rss/rssfeedsfrontpage.aspx"},
    {"id": 701, "name": "Ynet News",          "name_ar": "واي نت نيوز",          "country": "إسرائيل",         "type": "رقمي",        "lang": "en", "url": "https://www.ynet.co.il/Integration/StoryRss2.xml"},
    {"id": 702, "name": "Times of Israel",    "name_ar": "تايمز أوف إسرائيل",    "country": "إسرائيل",         "type": "رقمي",        "lang": "en", "url": "https://www.timesofisrael.com/feed/"},
    {"id": 703, "name": "i24 News",           "name_ar": "آي 24 نيوز",           "country": "إسرائيل",         "type": "تلفزيون",     "lang": "en", "url": "https://www.i24news.tv/en/rss"},

    # ==========================================
    # تركيا
    # ==========================================
    {"id": 800, "name": "Anadolu Agency",     "name_ar": "وكالة الأناضول",       "country": "تركيا",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.aa.com.tr/en/rss/default?cat=general"},
    {"id": 801, "name": "Daily Sabah",        "name_ar": "ديلي صباح",            "country": "تركيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.dailysabah.com/rssFeed/home"},
    {"id": 802, "name": "Hürriyet Daily",     "name_ar": "حرييت",                "country": "تركيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.hurriyetdailynews.com/rss"},
    {"id": 803, "name": "TRT World",          "name_ar": "تي آر تي ورلد",        "country": "تركيا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.trtworld.com/rss"},

    # ==========================================
    # اليابان / كوريا / آسيا الشرقية
    # ==========================================
    {"id": 12,  "name": "NHK World",          "name_ar": "إن إتش كي ورلد",       "country": "اليابان",         "type": "تلفزيون",     "lang": "en", "url": "https://www3.nhk.or.jp/nhkworld/en/news/feeds/"},
    {"id": 49,  "name": "Nikkei Asia",        "name_ar": "نيكاي آسيا",           "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://asia.nikkei.com/rss/feed/nar"},
    {"id": 72,  "name": "Mainichi Shimbun",   "name_ar": "مايانيتشي شيمبون",     "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://mainichi.jp/rss/etc/english.rss"},
    {"id": 500, "name": "The Japan Times",    "name_ar": "جاباني تايمز",         "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://www.japantimes.co.jp/feed/topstories/"},
    {"id": 73,  "name": "Chosun Ilbo",        "name_ar": "جوسون إيلبو",          "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://english.chosun.com/rss/"},
    {"id": 501, "name": "Korea Herald",       "name_ar": "كوريا هيرالد",         "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://www.koreaherald.com/rss/020100000000.xml"},
    {"id": 37,  "name": "South China Morning Post","name_ar": "ساوث تشاينا مورنينغ بوست","country": "هونغ كونغ","type": "صحيفة",      "lang": "en", "url": "https://www.scmp.com/rss/91/feed"},
    {"id": 50,  "name": "The Straits Times",  "name_ar": "ستريتس تايمز",         "country": "سنغافورة",        "type": "صحيفة",       "lang": "en", "url": "https://www.straitstimes.com/news/world/rss.xml"},
    {"id": 502, "name": "Channel NewsAsia",   "name_ar": "سي إن إيه",            "country": "سنغافورة",        "type": "تلفزيون",     "lang": "en", "url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml"},
    {"id": 102, "name": "CGTN",               "name_ar": "سي جي تي إن",          "country": "الصين",           "type": "تلفزيون",     "lang": "en", "url": "https://www.cgtn.com/subscribe/rss/section/world.do"},

    # ==========================================
    # الهند / جنوب آسيا
    # ==========================================
    {"id": 36,  "name": "The Hindu",          "name_ar": "ذا هندو",              "country": "الهند",           "type": "صحيفة",       "lang": "en", "url": "https://www.thehindu.com/feeder/default.rss"},
    {"id": 68,  "name": "Times of India",     "name_ar": "تايمز أوف إنديا",      "country": "الهند",           "type": "صحيفة",       "lang": "en", "url": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"},
    {"id": 69,  "name": "The Print",          "name_ar": "ذا برينت",             "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://theprint.in/feed/"},
    {"id": 600, "name": "NDTV",               "name_ar": "إن دي تي في",          "country": "الهند",           "type": "تلفزيون",     "lang": "en", "url": "https://feeds.feedburner.com/ndtvnews-top-stories"},
    {"id": 601, "name": "The Wire India",     "name_ar": "ذا واير",              "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://thewire.in/feed"},
    {"id": 70,  "name": "Dawn",               "name_ar": "داون",                 "country": "باكستان",         "type": "صحيفة",       "lang": "en", "url": "https://www.dawn.com/feeds/home"},
    {"id": 71,  "name": "Daily Star Bangladesh","name_ar": "ديلي ستار",          "country": "بنغلاديش",        "type": "صحيفة",       "lang": "en", "url": "https://www.thedailystar.net/rss.xml"},

    # ==========================================
    # أستراليا / نيوزيلندا / كندا
    # ==========================================
    {"id": 25,  "name": "ABC News Australia", "name_ar": "أي بي سي أستراليا",   "country": "أستراليا",        "type": "تلفزيون",     "lang": "en", "url": "https://www.abc.net.au/news/feed/51120/rss.xml"},
    {"id": 74,  "name": "Sydney Morning Herald","name_ar": "سيدني مورنينغ هيرالد","country": "أستراليا",       "type": "صحيفة",       "lang": "en", "url": "https://www.smh.com.au/rss/feed.xml"},
    {"id": 24,  "name": "CBC News",           "name_ar": "سي بي سي",             "country": "كندا",            "type": "تلفزيون",     "lang": "en", "url": "https://www.cbc.ca/cmlink/rss-topstories"},
    {"id": 77,  "name": "Globe and Mail",     "name_ar": "غلوب آند ميل",         "country": "كندا",            "type": "صحيفة",       "lang": "en", "url": "https://www.theglobeandmail.com/arc/outboundfeeds/rss/category/canada/"},

    # ==========================================
    # أفريقيا
    # ==========================================
    {"id": 40,  "name": "Daily Maverick",     "name_ar": "ديلي مافريك",          "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://www.dailymaverick.co.za/feed/"},
    {"id": 85,  "name": "Nation Africa",      "name_ar": "نيشن أفريقيا",         "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://nation.africa/rss.xml"},
    {"id": 86,  "name": "Mail & Guardian",    "name_ar": "ميل آند غارديان",      "country": "جنوب أفريقيا",   "type": "صحيفة",       "lang": "en", "url": "https://mg.co.za/feed/"},
    {"id": 88,  "name": "Premium Times Nigeria","name_ar": "بريميوم تايمز",      "country": "نيجيريا",         "type": "رقمي",        "lang": "en", "url": "https://www.premiumtimesng.com/feed"},
    {"id": 87,  "name": "The East African",   "name_ar": "إيست أفريكان",         "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.theeastafrican.co.ke/tea/rss.xml"},
    {"id": 900, "name": "AllAfrica",          "name_ar": "كل أفريقيا",           "country": "أفريقيا",         "type": "رقمي",        "lang": "en", "url": "https://allafrica.com/tools/headlines/rdf/latest/headlines.rdf"},

    # ==========================================
    # الفلبين / جنوب شرق آسيا
    # ==========================================
    {"id": 100, "name": "Rappler",            "name_ar": "رابلر",                "country": "الفلبين",         "type": "رقمي",        "lang": "en", "url": "https://www.rappler.com/feed/"},
    {"id": 1000,"name": "Bangkok Post",       "name_ar": "بانكوك بوست",          "country": "تايلاند",         "type": "صحيفة",       "lang": "en", "url": "https://www.bangkokpost.com/rss/data/topstories.xml"},
    {"id": 1001,"name": "Jakarta Post",       "name_ar": "جاكارتا بوست",         "country": "إندونيسيا",       "type": "صحيفة",       "lang": "en", "url": "https://www.thejakartapost.com/feed"},
    {"id": 1002,"name": "Vietnam News",       "name_ar": "فيتنام نيوز",          "country": "فيتنام",          "type": "صحيفة",       "lang": "en", "url": "https://vietnamnews.vn/rss/home.rss"},
]
