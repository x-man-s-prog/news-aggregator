# قائمة مصادر الأخبار مع روابط RSS — 1392 مصدر
# lang: ar = عربي (بدون ترجمة), en/fr/de/... = يُترجم للعربية

SOURCES = [

    # ══════════════════════════════════════════
    # القسم الأول: المصادر الأصلية (1-129)
    # ══════════════════════════════════════════

    # وكالات أنباء عالمية
    {"id": 1,   "name": "Reuters",              "name_ar": "رويترز",                  "country": "بريطانيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.reuters.com/reuters/topNews"},
    {"id": 2,   "name": "AP News",              "name_ar": "أسوشيتد برس",            "country": "أمريكا",          "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.apnews.com/rss/apf-topnews"},
    {"id": 6,   "name": "AFP",                  "name_ar": "فرانس برس",               "country": "فرنسا",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.france24.com/en/rss"},
    {"id": 62,  "name": "ANSA",                 "name_ar": "أنسا",                    "country": "إيطاليا",         "type": "وكالة أنباء", "lang": "it", "url": "https://www.ansa.it/sito/notizie/topnews/topnews_rss.xml"},
    {"id": 63,  "name": "EFE",                  "name_ar": "وكالة إيفي",              "country": "إسبانيا",         "type": "وكالة أنباء", "lang": "es", "url": "https://www.efe.com/efe/espana/1/rss"},
    {"id": 65,  "name": "Kyodo News",           "name_ar": "كيودو نيوز",              "country": "اليابان",         "type": "وكالة أنباء", "lang": "en", "url": "https://english.kyodonews.net/rss/all.xml"},
    {"id": 66,  "name": "Yonhap News",          "name_ar": "يونهاب",                  "country": "كوريا الجنوبية", "type": "وكالة أنباء", "lang": "en", "url": "https://en.yna.co.kr/RSS/news.xml"},
    {"id": 83,  "name": "Agência Brasil",       "name_ar": "وكالة البرازيل",          "country": "البرازيل",        "type": "وكالة أنباء", "lang": "pt", "url": "https://agenciabrasil.ebc.com.br/rss/ultimasnoticias/feed.xml"},

    # بريطانيا
    {"id": 3,   "name": "BBC News",             "name_ar": "بي بي سي",                "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://feeds.bbci.co.uk/news/world/rss.xml"},
    {"id": 101, "name": "Sky News",             "name_ar": "سكاي نيوز",               "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://feeds.skynews.com/feeds/rss/world.xml"},
    {"id": 4,   "name": "The Guardian",         "name_ar": "الغارديان",               "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.theguardian.com/world/rss"},
    {"id": 9,   "name": "The Economist",        "name_ar": "الإيكونوميست",            "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.economist.com/the-world-this-week/rss.xml"},
    {"id": 10,  "name": "Financial Times",      "name_ar": "فايننشال تايمز",          "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.ft.com/rss/home"},
    {"id": 51,  "name": "The Independent",      "name_ar": "الإندبندنت",              "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.independent.co.uk/news/world/rss"},
    {"id": 23,  "name": "The Times London",     "name_ar": "ذا تايمز",                "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.thetimes.co.uk/rss/home"},
    {"id": 92,  "name": "Middle East Eye",      "name_ar": "ميدل إيست آي",            "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://www.middleeasteye.net/rss"},
    {"id": 104, "name": "Iran International",   "name_ar": "إيران إنترناشيونال",      "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://www.iranintl.com/en/rss"},

    # أمريكا
    {"id": 5,   "name": "New York Times",       "name_ar": "نيويورك تايمز",           "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://rss.nytimes.com/services/xml/rss/nf/HomePage.xml"},
    {"id": 11,  "name": "Washington Post",      "name_ar": "واشنطن بوست",             "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://feeds.washingtonpost.com/rss/world"},
    {"id": 15,  "name": "NPR News",             "name_ar": "إن بي آر",                "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://feeds.npr.org/1001/rss.xml"},
    {"id": 16,  "name": "Wall Street Journal",  "name_ar": "وول ستريت جورنال",        "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://feeds.a.dj.com/rss/RSSWorldNews.xml"},
    {"id": 17,  "name": "Politico",             "name_ar": "بوليتيكو",                "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.politico.com/rss/politicopicks.xml"},
    {"id": 28,  "name": "Axios",                "name_ar": "أكسيوس",                  "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://api.axios.com/feed/"},
    {"id": 29,  "name": "Bloomberg",            "name_ar": "بلومبرغ",                 "country": "أمريكا",          "type": "مالي",        "lang": "en", "url": "https://feeds.bloomberg.com/politics/news.rss"},
    {"id": 27,  "name": "The Atlantic",         "name_ar": "ذا أتلانتيك",             "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.theatlantic.com/feed/all/"},
    {"id": 26,  "name": "ProPublica",           "name_ar": "بروبابليكا",              "country": "أمريكا",          "type": "استقصائي",    "lang": "en", "url": "https://feeds.propublica.org/propublica/main"},
    {"id": 43,  "name": "The Intercept",        "name_ar": "ذا إنترسبت",              "country": "أمريكا",          "type": "استقصائي",    "lang": "en", "url": "https://theintercept.com/feed/?lang=en"},
    {"id": 44,  "name": "Science News",         "name_ar": "ساينس نيوز",              "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.sciencenews.org/feed"},
    {"id": 42,  "name": "Al-Monitor",           "name_ar": "المونيتور",               "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.al-monitor.com/rss.xml"},
    {"id": 200, "name": "Vox",                  "name_ar": "فوكس",                    "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.vox.com/rss/index.xml"},
    {"id": 201, "name": "The Hill",             "name_ar": "ذا هيل",                  "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://thehill.com/news/feed/"},
    {"id": 202, "name": "Foreign Policy",       "name_ar": "فورين بوليسي",            "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://foreignpolicy.com/feed/"},
    {"id": 203, "name": "Foreign Affairs",      "name_ar": "فورين أفيرز",             "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.foreignaffairs.com/rss.xml"},
    {"id": 204, "name": "MIT Tech Review",      "name_ar": "ميت تكنولوجي ريفيو",     "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.technologyreview.com/feed/"},
    {"id": 205, "name": "Wired",                "name_ar": "وايرد",                   "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.wired.com/feed/rss"},
    {"id": 206, "name": "TIME Magazine",        "name_ar": "مجلة تايم",               "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://time.com/feed/"},
    {"id": 207, "name": "Newsweek",             "name_ar": "نيوزويك",                 "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.newsweek.com/rss"},

    # عربي
    {"id": 14,  "name": "Al Jazeera English",   "name_ar": "الجزيرة الإنجليزية",     "country": "قطر",             "type": "تلفزيون",     "lang": "en", "url": "https://www.aljazeera.com/xml/rss/all.xml"},
    {"id": 300, "name": "Al Jazeera Arabic",    "name_ar": "الجزيرة عربي",           "country": "قطر",             "type": "تلفزيون",     "lang": "ar", "url": "https://www.aljazeera.net/rss"},
    {"id": 90,  "name": "Al Arabiya",           "name_ar": "العربية",                 "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.alarabiya.net/ar/rss.xml"},
    {"id": 91,  "name": "Asharq Al-Awsat",      "name_ar": "الشرق الأوسط",           "country": "بريطانيا",        "type": "صحيفة",       "lang": "ar", "url": "https://aawsat.com/rss.xml"},
    {"id": 301, "name": "Sky News Arabia",      "name_ar": "سكاي نيوز عربية",        "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.skynewsarabia.com/web/rss"},
    {"id": 302, "name": "BBC Arabic",           "name_ar": "بي بي سي عربي",          "country": "بريطانيا",        "type": "تلفزيون",     "lang": "ar", "url": "https://feeds.bbci.co.uk/arabic/rss.xml"},
    {"id": 303, "name": "France 24 Arabic",     "name_ar": "فرانس 24 عربي",          "country": "فرنسا",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.france24.com/ar/rss"},
    {"id": 304, "name": "DW Arabic",            "name_ar": "دويتشه فيله عربي",       "country": "ألمانيا",         "type": "تلفزيون",     "lang": "ar", "url": "https://rss.dw.com/rdf/rss-ar-all"},
    {"id": 305, "name": "RT Arabic",            "name_ar": "RT عربي",                 "country": "روسيا",           "type": "تلفزيون",     "lang": "ar", "url": "https://arabic.rt.com/rss/"},
    {"id": 306, "name": "Raseef22",             "name_ar": "رصيف22",                  "country": "لبنان",           "type": "رقمي",        "lang": "ar", "url": "https://raseef22.net/feed/"},
    {"id": 307, "name": "Daraj Media",          "name_ar": "درج",                     "country": "لبنان",           "type": "رقمي",        "lang": "ar", "url": "https://daraj.media/feed/"},
    {"id": 309, "name": "Mada Masr",            "name_ar": "مدى مصر",                 "country": "مصر",             "type": "رقمي",        "lang": "ar", "url": "https://www.madamasr.com/ar/feed/"},
    {"id": 310, "name": "The New Arab",         "name_ar": "العربي الجديد",           "country": "بريطانيا",        "type": "رقمي",        "lang": "ar", "url": "https://www.alaraby.co.uk/rss.xml"},
    {"id": 311, "name": "Al-Araby Al-Jadeed",   "name_ar": "القدس العربي",            "country": "بريطانيا",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alquds.co.uk/feed/"},
    {"id": 312, "name": "Anadolu Arabic",       "name_ar": "الأناضول عربي",           "country": "تركيا",           "type": "وكالة أنباء", "lang": "ar", "url": "https://www.aa.com.tr/ar/rss/default?cat=general"},
    {"id": 313, "name": "Asharq News",          "name_ar": "الشرق للأخبار",           "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://asharq.com/feed/"},

    # ألمانيا
    {"id": 13,  "name": "DW News",              "name_ar": "دويتشه فيله",             "country": "ألمانيا",         "type": "تلفزيون",     "lang": "en", "url": "https://rss.dw.com/rdf/rss-en-all"},
    {"id": 7,   "name": "Der Spiegel",          "name_ar": "دير شبيغل",               "country": "ألمانيا",         "type": "مجلة",        "lang": "de", "url": "https://www.spiegel.de/international/index.rss"},
    {"id": 22,  "name": "Süddeutsche Zeitung",  "name_ar": "زودويتشه تسايتونغ",      "country": "ألمانيا",         "type": "صحيفة",       "lang": "de", "url": "https://rss.sueddeutsche.de/rss/Topthemen"},
    {"id": 54,  "name": "ARD Tagesschau",       "name_ar": "تاغسشاو",                 "country": "ألمانيا",         "type": "تلفزيون",     "lang": "de", "url": "https://www.tagesschau.de/xml/rss2/"},
    {"id": 55,  "name": "ZDF Nachrichten",      "name_ar": "زد دي إف",                "country": "ألمانيا",         "type": "تلفزيون",     "lang": "de", "url": "https://www.zdf.de/rss/zdf/nachrichten-100.xml"},

    # فرنسا
    {"id": 8,   "name": "Le Monde",             "name_ar": "لوموند",                  "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.lemonde.fr/rss/une.xml"},
    {"id": 47,  "name": "Le Figaro",            "name_ar": "لوفيغارو",                "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.lefigaro.fr/rss/figaro_flash-actu.xml"},
    {"id": 18,  "name": "RFI English",          "name_ar": "راديو فرانس الدولي",      "country": "فرنسا",           "type": "راديو",       "lang": "en", "url": "https://www.rfi.fr/en/rss"},
    {"id": 56,  "name": "France 24 English",    "name_ar": "فرانس 24",                "country": "فرنسا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.france24.com/en/rss"},
    {"id": 400, "name": "Libération",           "name_ar": "ليبيراسيون",              "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.liberation.fr/arc/outboundfeeds/rss-all/"},

    # إسبانيا / أمريكا اللاتينية
    {"id": 19,  "name": "El País",              "name_ar": "إل باييس",                "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"},
    {"id": 39,  "name": "El Espectador",        "name_ar": "إل إسبيكتادور",           "country": "كولومبيا",        "type": "صحيفة",       "lang": "es", "url": "https://www.elespectador.com/noticias/feed"},
    {"id": 78,  "name": "La Jornada",           "name_ar": "لا خورنادا",              "country": "المكسيك",         "type": "صحيفة",       "lang": "es", "url": "https://www.jornada.com.mx/rss/politica.xml"},
    {"id": 80,  "name": "Clarín",               "name_ar": "كلارين",                  "country": "الأرجنتين",       "type": "صحيفة",       "lang": "es", "url": "https://www.clarin.com/rss/lo-ultimo/"},
    {"id": 82,  "name": "La Nación Argentina",  "name_ar": "لا ناسيون",               "country": "الأرجنتين",       "type": "صحيفة",       "lang": "es", "url": "https://www.lanacion.com.ar/arc/outboundfeeds/rss/"},
    {"id": 84,  "name": "Infobae",              "name_ar": "إنفوباي",                 "country": "الأرجنتين",       "type": "رقمي",        "lang": "es", "url": "https://www.infobae.com/feeds/rss/"},
    {"id": 41,  "name": "Folha de S.Paulo",     "name_ar": "فولها دي ساو باولو",      "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://feeds.folha.uol.com.br/mundo/rss091.xml"},
    {"id": 79,  "name": "O Globo",              "name_ar": "أو غلوبو",                "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://oglobo.globo.com/rss.xml"},

    # إيطاليا
    {"id": 20,  "name": "Corriere della Sera",  "name_ar": "كورييري ديلا سيرا",      "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.corriere.it/rss/homepage.xml"},
    {"id": 48,  "name": "La Repubblica",        "name_ar": "لا ريبوبليكا",            "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.repubblica.it/rss/homepage/rss2.0.xml"},

    # هولندا / بلجيكا / أوروبا
    {"id": 33,  "name": "NOS News",             "name_ar": "نوس نيوز",                "country": "هولندا",          "type": "تلفزيون",     "lang": "nl", "url": "https://feeds.nos.nl/nosnieuwsalgemeen"},
    {"id": 52,  "name": "Euronews",             "name_ar": "يورونيوز",                "country": "أوروبا",          "type": "تلفزيون",     "lang": "en", "url": "https://www.euronews.com/rss?format=mrss&level=theme&name=news"},
    {"id": 57,  "name": "RTBF",                 "name_ar": "آر تي بي إف",             "country": "بلجيكا",          "type": "تلفزيون",     "lang": "fr", "url": "https://www.rtbf.be/rss/info/general"},

    # إسكندنافيا وأوروبا الشمالية
    {"id": 32,  "name": "SVT Nyheter",          "name_ar": "إس في تي",                "country": "السويد",          "type": "تلفزيون",     "lang": "sv", "url": "https://www.svt.se/nyheter/rss.xml"},
    {"id": 61,  "name": "NRK Nyheter",          "name_ar": "إن آر كي",                "country": "النرويج",         "type": "تلفزيون",     "lang": "no", "url": "https://www.nrk.no/nyheter/siste.rss"},
    {"id": 35,  "name": "Yle News",             "name_ar": "يلي نيوز",                "country": "فنلندا",          "type": "تلفزيون",     "lang": "fi", "url": "https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss"},
    {"id": 60,  "name": "DR News",              "name_ar": "دي آر",                   "country": "الدنمارك",        "type": "تلفزيون",     "lang": "da", "url": "https://www.dr.dk/nyheder/service/feeds/allenyheder"},
    {"id": 45,  "name": "Der Standard",         "name_ar": "دير ستاندارد",            "country": "النمسا",          "type": "صحيفة",       "lang": "de", "url": "https://www.derstandard.at/rss"},
    {"id": 59,  "name": "ORF News",             "name_ar": "أو آر إف",                "country": "النمسا",          "type": "تلفزيون",     "lang": "de", "url": "https://rss.orf.at/news.xml"},
    {"id": 46,  "name": "NZZ",                  "name_ar": "نيويه تسورخر",            "country": "سويسرا",          "type": "صحيفة",       "lang": "de", "url": "https://www.nzz.ch/recent.rss"},
    {"id": 53,  "name": "RTS Info",             "name_ar": "آر تي إس",                "country": "سويسرا",          "type": "تلفزيون",     "lang": "fr", "url": "https://www.rts.ch/info/rss/"},
    {"id": 31,  "name": "Irish Times",          "name_ar": "آيريش تايمز",             "country": "أيرلندا",         "type": "صحيفة",       "lang": "en", "url": "https://www.irishtimes.com/arc/outboundfeeds/rss/"},
    {"id": 96,  "name": "Gazeta Wyborcza",      "name_ar": "غازيتا ويبورتشا",         "country": "بولندا",          "type": "صحيفة",       "lang": "pl", "url": "https://wyborcza.pl/rss/wyborcza.xml"},

    # روسيا / أوروبا الشرقية
    {"id": 93,  "name": "Kommersant",           "name_ar": "كوميرسانت",               "country": "روسيا",           "type": "صحيفة",       "lang": "ru", "url": "https://www.kommersant.ru/RSS/main.xml"},
    {"id": 95,  "name": "Meduza",               "name_ar": "ميدوزا",                  "country": "لاتفيا",          "type": "رقمي",        "lang": "ru", "url": "https://meduza.io/rss/all"},
    {"id": 103, "name": "RT News",              "name_ar": "روسيا اليوم",             "country": "روسيا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.rt.com/rss/news/"},

    # إسرائيل
    {"id": 30,  "name": "Haaretz",              "name_ar": "هآرتس",                   "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.haaretz.com/rss"},
    {"id": 700, "name": "The Jerusalem Post",   "name_ar": "جيروزاليم بوست",          "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.jpost.com/rss/rssfeedsfrontpage.aspx"},
    {"id": 701, "name": "Ynet News",            "name_ar": "واي نت نيوز",             "country": "إسرائيل",         "type": "رقمي",        "lang": "en", "url": "https://www.ynet.co.il/Integration/StoryRss2.xml"},
    {"id": 702, "name": "Times of Israel",      "name_ar": "تايمز أوف إسرائيل",      "country": "إسرائيل",         "type": "رقمي",        "lang": "en", "url": "https://www.timesofisrael.com/feed/"},
    {"id": 703, "name": "i24 News",             "name_ar": "آي 24 نيوز",              "country": "إسرائيل",         "type": "تلفزيون",     "lang": "en", "url": "https://www.i24news.tv/en/rss"},

    # تركيا
    {"id": 800, "name": "Anadolu Agency",       "name_ar": "وكالة الأناضول",          "country": "تركيا",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.aa.com.tr/en/rss/default?cat=general"},
    {"id": 801, "name": "Daily Sabah",          "name_ar": "ديلي صباح",               "country": "تركيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.dailysabah.com/rssFeed/home"},
    {"id": 802, "name": "Hürriyet Daily",       "name_ar": "حرييت",                   "country": "تركيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.hurriyetdailynews.com/rss"},
    {"id": 803, "name": "TRT World",            "name_ar": "تي آر تي ورلد",           "country": "تركيا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.trtworld.com/rss"},

    # اليابان / كوريا / آسيا الشرقية
    {"id": 12,  "name": "NHK World",            "name_ar": "إن إتش كي ورلد",          "country": "اليابان",         "type": "تلفزيون",     "lang": "en", "url": "https://www3.nhk.or.jp/nhkworld/en/news/feeds/"},
    {"id": 49,  "name": "Nikkei Asia",          "name_ar": "نيكاي آسيا",              "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://asia.nikkei.com/rss/feed/nar"},
    {"id": 72,  "name": "Mainichi Shimbun",     "name_ar": "مايانيتشي شيمبون",        "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://mainichi.jp/rss/etc/english.rss"},
    {"id": 500, "name": "The Japan Times",      "name_ar": "جاباني تايمز",            "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://www.japantimes.co.jp/feed/topstories/"},
    {"id": 73,  "name": "Chosun Ilbo",          "name_ar": "جوسون إيلبو",             "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://english.chosun.com/rss/"},
    {"id": 501, "name": "Korea Herald",         "name_ar": "كوريا هيرالد",            "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://www.koreaherald.com/rss/020100000000.xml"},
    {"id": 37,  "name": "South China Morning Post", "name_ar": "ساوث تشاينا مورنينغ بوست", "country": "هونغ كونغ", "type": "صحيفة",      "lang": "en", "url": "https://www.scmp.com/rss/91/feed"},
    {"id": 50,  "name": "The Straits Times",    "name_ar": "ستريتس تايمز",            "country": "سنغافورة",        "type": "صحيفة",       "lang": "en", "url": "https://www.straitstimes.com/news/world/rss.xml"},
    {"id": 502, "name": "Channel NewsAsia",     "name_ar": "سي إن إيه",               "country": "سنغافورة",        "type": "تلفزيون",     "lang": "en", "url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml"},
    {"id": 102, "name": "CGTN",                 "name_ar": "سي جي تي إن",             "country": "الصين",           "type": "تلفزيون",     "lang": "en", "url": "https://www.cgtn.com/subscribe/rss/section/world.do"},

    # الهند / جنوب آسيا
    {"id": 36,  "name": "The Hindu",            "name_ar": "ذا هندو",                 "country": "الهند",           "type": "صحيفة",       "lang": "en", "url": "https://www.thehindu.com/feeder/default.rss"},
    {"id": 68,  "name": "Times of India",       "name_ar": "تايمز أوف إنديا",         "country": "الهند",           "type": "صحيفة",       "lang": "en", "url": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms"},
    {"id": 69,  "name": "The Print",            "name_ar": "ذا برينت",                "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://theprint.in/feed/"},
    {"id": 600, "name": "NDTV",                 "name_ar": "إن دي تي في",             "country": "الهند",           "type": "تلفزيون",     "lang": "en", "url": "https://feeds.feedburner.com/ndtvnews-top-stories"},
    {"id": 601, "name": "The Wire India",       "name_ar": "ذا واير",                 "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://thewire.in/feed"},
    {"id": 70,  "name": "Dawn",                 "name_ar": "داون",                    "country": "باكستان",         "type": "صحيفة",       "lang": "en", "url": "https://www.dawn.com/feeds/home"},
    {"id": 71,  "name": "Daily Star Bangladesh","name_ar": "ديلي ستار بنغلاديش",      "country": "بنغلاديش",        "type": "صحيفة",       "lang": "en", "url": "https://www.thedailystar.net/rss.xml"},

    # أستراليا / كندا
    {"id": 25,  "name": "ABC News Australia",   "name_ar": "أي بي سي أستراليا",      "country": "أستراليا",        "type": "تلفزيون",     "lang": "en", "url": "https://www.abc.net.au/news/feed/51120/rss.xml"},
    {"id": 74,  "name": "Sydney Morning Herald","name_ar": "سيدني مورنينغ هيرالد",    "country": "أستراليا",        "type": "صحيفة",       "lang": "en", "url": "https://www.smh.com.au/rss/feed.xml"},
    {"id": 24,  "name": "CBC News",             "name_ar": "سي بي سي",                "country": "كندا",            "type": "تلفزيون",     "lang": "en", "url": "https://www.cbc.ca/cmlink/rss-topstories"},
    {"id": 77,  "name": "Globe and Mail",       "name_ar": "غلوب آند ميل",            "country": "كندا",            "type": "صحيفة",       "lang": "en", "url": "https://www.theglobeandmail.com/arc/outboundfeeds/rss/category/canada/"},

    # أفريقيا
    {"id": 40,  "name": "Daily Maverick",       "name_ar": "ديلي مافريك",             "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://www.dailymaverick.co.za/feed/"},
    {"id": 85,  "name": "Nation Africa",        "name_ar": "نيشن أفريقيا",            "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://nation.africa/rss.xml"},
    {"id": 86,  "name": "Mail & Guardian",      "name_ar": "ميل آند غارديان",         "country": "جنوب أفريقيا",   "type": "صحيفة",       "lang": "en", "url": "https://mg.co.za/feed/"},
    {"id": 88,  "name": "Premium Times Nigeria","name_ar": "بريميوم تايمز",           "country": "نيجيريا",         "type": "رقمي",        "lang": "en", "url": "https://www.premiumtimesng.com/feed"},
    {"id": 87,  "name": "The East African",     "name_ar": "إيست أفريكان",            "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.theeastafrican.co.ke/tea/rss.xml"},
    {"id": 900, "name": "AllAfrica",            "name_ar": "كل أفريقيا",              "country": "أفريقيا",         "type": "رقمي",        "lang": "en", "url": "https://allafrica.com/tools/headlines/rdf/latest/headlines.rdf"},

    # جنوب شرق آسيا
    {"id": 100, "name": "Rappler",              "name_ar": "رابلر",                   "country": "الفلبين",         "type": "رقمي",        "lang": "en", "url": "https://www.rappler.com/feed/"},
    {"id": 1000,"name": "Bangkok Post",         "name_ar": "بانكوك بوست",             "country": "تايلاند",         "type": "صحيفة",       "lang": "en", "url": "https://www.bangkokpost.com/rss/data/topstories.xml"},
    {"id": 1001,"name": "Jakarta Post",         "name_ar": "جاكارتا بوست",            "country": "إندونيسيا",       "type": "صحيفة",       "lang": "en", "url": "https://www.thejakartapost.com/feed"},
    {"id": 1002,"name": "Vietnam News",         "name_ar": "فيتنام نيوز",             "country": "فيتنام",          "type": "صحيفة",       "lang": "en", "url": "https://vietnamnews.vn/rss/home.rss"},

    # ══════════════════════════════════════════
    # القسم الثاني: 50 مصدراً عالمياً إضافياً (130-179)
    # ══════════════════════════════════════════

    # وكالات أنباء إضافية
    {"id": 2001,"name": "Xinhua English",       "name_ar": "شينخوا",                  "country": "الصين",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.xinhuanet.com/english/rss/worldservice.xml"},
    {"id": 2002,"name": "TASS",                 "name_ar": "تاس",                     "country": "روسيا",           "type": "وكالة أنباء", "lang": "en", "url": "https://tass.com/rss/v2.xml"},
    {"id": 2003,"name": "PTI India",            "name_ar": "وكالة برس تراست",         "country": "الهند",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.ptinews.com/feed/"},
    {"id": 2004,"name": "DPA Germany",          "name_ar": "الوكالة الألمانية",       "country": "ألمانيا",         "type": "وكالة أنباء", "lang": "de", "url": "https://www.dpa.com/de/rss"},
    {"id": 2005,"name": "Bernama",              "name_ar": "برناما",                  "country": "ماليزيا",         "type": "وكالة أنباء", "lang": "en", "url": "https://www.bernama.com/rss/latest.xml"},
    {"id": 2006,"name": "PAP Poland",           "name_ar": "وكالة باب البولندية",     "country": "بولندا",          "type": "وكالة أنباء", "lang": "pl", "url": "https://www.pap.pl/rss.xml"},
    {"id": 2007,"name": "ANA Athens",           "name_ar": "وكالة أثينا",             "country": "اليونان",         "type": "وكالة أنباء", "lang": "el", "url": "https://www.amna.gr/rss"},
    {"id": 2008,"name": "CTK Czech",            "name_ar": "الوكالة التشيكية",        "country": "التشيك",          "type": "وكالة أنباء", "lang": "cs", "url": "https://ct24.ceskatelevize.cz/rss/hlavni-zpravy"},
    {"id": 2009,"name": "MTI Hungary",          "name_ar": "الوكالة المجرية",         "country": "المجر",           "type": "وكالة أنباء", "lang": "hu", "url": "https://www.mti.hu/rss"},
    {"id": 2010,"name": "Belga News",           "name_ar": "بيلغا نيوز",              "country": "بلجيكا",          "type": "وكالة أنباء", "lang": "fr", "url": "https://www.belganewsagency.eu/feed"},

    # صحف ومنصات عالمية كبرى
    {"id": 2011,"name": "USA Today",            "name_ar": "يو إس إيه توداي",         "country": "أمريكا",          "type": "صحيفة",       "lang": "en", "url": "https://rssfeeds.usatoday.com/usatoday-NewsTopStories"},
    {"id": 2012,"name": "The New Yorker",       "name_ar": "ذا نيويوركر",             "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.newyorker.com/feed/everything"},
    {"id": 2013,"name": "CBS News",             "name_ar": "سي بي إس نيوز",           "country": "أمريكا",          "type": "تلفزيون",     "lang": "en", "url": "https://www.cbsnews.com/latest/rss/main"},
    {"id": 2014,"name": "CNN",                  "name_ar": "سي إن إن",                "country": "أمريكا",          "type": "تلفزيون",     "lang": "en", "url": "http://rss.cnn.com/rss/edition_world.rss"},
    {"id": 2015,"name": "Fox News",             "name_ar": "فوكس نيوز",               "country": "أمريكا",          "type": "تلفزيون",     "lang": "en", "url": "https://moxie.foxnews.com/google-publisher/world.xml"},
    {"id": 2016,"name": "ABC News USA",         "name_ar": "إيه بي سي نيوز",          "country": "أمريكا",          "type": "تلفزيون",     "lang": "en", "url": "https://feeds.abcnews.com/abcnews/topstories"},
    {"id": 2017,"name": "The Daily Telegraph",  "name_ar": "ديلي تلغراف",             "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.telegraph.co.uk/rss.xml"},
    {"id": 2018,"name": "Daily Mail",           "name_ar": "ديلي ميل",                "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.dailymail.co.uk/articles.rss"},
    {"id": 2019,"name": "The Observer",         "name_ar": "ذا أوبزيرفر",             "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.theguardian.com/observer/rss"},
    {"id": 2020,"name": "The Scotsman",         "name_ar": "ذا سكوتسمان",             "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.scotsman.com/news.rss"},
    {"id": 2021,"name": "Le Monde Diplomatique","name_ar": "لوموند ديبلوماتيك",       "country": "فرنسا",           "type": "مجلة",        "lang": "fr", "url": "https://www.monde-diplomatique.fr/rss.xml"},
    {"id": 2022,"name": "Die Welt",             "name_ar": "دي فيلت",                 "country": "ألمانيا",         "type": "صحيفة",       "lang": "de", "url": "https://www.welt.de/feeds/latest.rss"},
    {"id": 2023,"name": "Die Zeit",             "name_ar": "دي تسايت",                "country": "ألمانيا",         "type": "مجلة",        "lang": "de", "url": "https://newsfeed.zeit.de/index"},
    {"id": 2024,"name": "Frankfurter Allgemeine","name_ar": "فرانكفورتر ألغماينه",   "country": "ألمانيا",         "type": "صحيفة",       "lang": "de", "url": "https://www.faz.net/rss/aktuell/"},
    {"id": 2025,"name": "La Stampa",            "name_ar": "لا ستامبا",               "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.lastampa.it/rss.xml"},
    {"id": 2026,"name": "Il Sole 24 Ore",       "name_ar": "إل سوله 24 أوره",         "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.ilsole24ore.com/rss/mondo.xml"},
    {"id": 2027,"name": "El Mundo",             "name_ar": "إل موندو",                "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://e00-elmundo.uecdn.es/elmundo/rss/portada.xml"},
    {"id": 2028,"name": "ABC España",           "name_ar": "أي بي سي إسبانيا",       "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://www.abc.es/rss/feeds/abc_ultima_hora.xml"},
    {"id": 2029,"name": "Público Portugal",     "name_ar": "بوبليكو",                 "country": "البرتغال",        "type": "صحيفة",       "lang": "pt", "url": "https://www.publico.pt/rss"},
    {"id": 2030,"name": "Expresso",             "name_ar": "إكسبريسو",                "country": "البرتغال",        "type": "صحيفة",       "lang": "pt", "url": "https://expresso.pt/rss"},
    {"id": 2031,"name": "Kathimerini",          "name_ar": "كاثيميريني",              "country": "اليونان",         "type": "صحيفة",       "lang": "en", "url": "https://www.ekathimerini.com/rss/"},
    {"id": 2032,"name": "Helsingin Sanomat",    "name_ar": "هلسنغين سانومات",         "country": "فنلندا",          "type": "صحيفة",       "lang": "fi", "url": "https://www.hs.fi/rss/tuoreimmat.xml"},
    {"id": 2033,"name": "Aftenposten",          "name_ar": "أفتنبوستن",               "country": "النرويج",         "type": "صحيفة",       "lang": "no", "url": "https://www.aftenposten.no/rss/frontpage.rss"},
    {"id": 2034,"name": "Dagens Nyheter",       "name_ar": "داغنس نيهيتر",            "country": "السويد",          "type": "صحيفة",       "lang": "sv", "url": "https://www.dn.se/rss/"},
    {"id": 2035,"name": "Politiken",            "name_ar": "بوليتيكن",                "country": "الدنمارك",        "type": "صحيفة",       "lang": "da", "url": "https://politiken.dk/rss/"},
    {"id": 2036,"name": "De Volkskrant",        "name_ar": "دي فولكسكرانت",           "country": "هولندا",          "type": "صحيفة",       "lang": "nl", "url": "https://www.volkskrant.nl/nieuws-en-achtergrond/rss.xml"},
    {"id": 2037,"name": "NRC Handelsblad",      "name_ar": "إن آر سي هانديلسبلاد",   "country": "هولندا",          "type": "صحيفة",       "lang": "nl", "url": "https://www.nrc.nl/rss/"},
    {"id": 2038,"name": "Le Temps",             "name_ar": "لو تون",                  "country": "سويسرا",          "type": "صحيفة",       "lang": "fr", "url": "https://www.letemps.ch/rss"},
    {"id": 2039,"name": "Tages-Anzeiger",       "name_ar": "تاغيس أنتسايغر",          "country": "سويسرا",          "type": "صحيفة",       "lang": "de", "url": "https://www.tagesanzeiger.ch/rss.html"},
    {"id": 2040,"name": "Toronto Star",         "name_ar": "تورونتو ستار",            "country": "كندا",            "type": "صحيفة",       "lang": "en", "url": "https://www.thestar.com/search/?f=rss&t=article&c=news&l=50&s=start_time&sd=desc"},
    {"id": 2041,"name": "The Australian",       "name_ar": "ذا أوستراليان",           "country": "أستراليا",        "type": "صحيفة",       "lang": "en", "url": "https://www.theaustralian.com.au/feed"},
    {"id": 2042,"name": "New Zealand Herald",   "name_ar": "نيوزيلاند هيرالد",        "country": "نيوزيلندا",       "type": "صحيفة",       "lang": "en", "url": "https://www.nzherald.co.nz/arc/outboundfeeds/rss/section/all"},
    {"id": 2043,"name": "Japan Forward",        "name_ar": "جاباني فورورد",           "country": "اليابان",         "type": "رقمي",        "lang": "en", "url": "https://japan-forward.com/feed/"},
    {"id": 2044,"name": "Asia Times",           "name_ar": "آسيا تايمز",              "country": "هونغ كونغ",       "type": "رقمي",        "lang": "en", "url": "https://asiatimes.com/feed/"},

    # ══════════════════════════════════════════
    # القسم الثالث: 50 مصدراً عربياً إضافياً (180-229)
    # ══════════════════════════════════════════

    # الخليج العربي
    {"id": 3001,"name": "Al Ittihad UAE",       "name_ar": "الاتحاد",                 "country": "الإمارات",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alittihad.ae/rss.xml"},
    {"id": 3002,"name": "Al Bayan UAE",         "name_ar": "البيان",                  "country": "الإمارات",        "type": "صحيفة",       "lang": "ar", "url": "https://www.albayan.ae/rss"},
    {"id": 3003,"name": "Al Khaleej UAE",       "name_ar": "الخليج",                  "country": "الإمارات",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alkhaleej.ae/rss"},
    {"id": 3004,"name": "Al Roeya UAE",         "name_ar": "الرؤية",                  "country": "الإمارات",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alroeya.com/rss"},
    {"id": 3005,"name": "The National UAE",     "name_ar": "ذا ناشيونال",             "country": "الإمارات",        "type": "صحيفة",       "lang": "en", "url": "https://www.thenationalnews.com/rss.xml"},
    {"id": 3006,"name": "Al Sharq Qatar",       "name_ar": "الشرق",                   "country": "قطر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.al-sharq.com/rss"},
    {"id": 3007,"name": "Al Raya Qatar",        "name_ar": "الراية",                  "country": "قطر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.raya.com/rss"},
    {"id": 3008,"name": "Al Watan Qatar",       "name_ar": "الوطن القطرية",           "country": "قطر",             "type": "صحيفة",       "lang": "ar", "url": "https://alwatan.com.qa/rss"},
    {"id": 3009,"name": "Al Qabas Kuwait",      "name_ar": "القبس",                   "country": "الكويت",          "type": "صحيفة",       "lang": "ar", "url": "https://www.alqabas.com/rss.xml"},
    {"id": 3010,"name": "Al Rai Kuwait",        "name_ar": "الراي",                   "country": "الكويت",          "type": "صحيفة",       "lang": "ar", "url": "https://www.alraimedia.com/rss"},
    {"id": 3011,"name": "Al Anbaa Kuwait",      "name_ar": "الأنباء",                 "country": "الكويت",          "type": "صحيفة",       "lang": "ar", "url": "https://www.alanba.com.kw/rss"},
    {"id": 3012,"name": "Akhbar Al Khaleej BH", "name_ar": "أخبار الخليج",            "country": "البحرين",         "type": "صحيفة",       "lang": "ar", "url": "https://www.akhbar-alkhaleej.com/rss"},
    {"id": 3013,"name": "Al Watan Bahrain",     "name_ar": "الوطن البحرينية",         "country": "البحرين",         "type": "صحيفة",       "lang": "ar", "url": "https://alwatanbh.net/feed/"},
    {"id": 3014,"name": "Al Shabiba Oman",      "name_ar": "الشبيبة",                 "country": "عُمان",           "type": "صحيفة",       "lang": "ar", "url": "https://www.shabiba.com/rss"},
    {"id": 3015,"name": "Oman Observer",        "name_ar": "عُمان أوبزيرفر",          "country": "عُمان",           "type": "صحيفة",       "lang": "en", "url": "https://www.omanoobserver.om/rss.xml"},
    {"id": 3016,"name": "Okaz Saudi",           "name_ar": "عكاظ",                    "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.okaz.com.sa/rss"},
    {"id": 3017,"name": "Al Riyadh",            "name_ar": "الرياض",                  "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alriyadh.com/rss"},
    {"id": 3018,"name": "Al Watan Saudi",       "name_ar": "الوطن السعودية",          "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alwatan.com.sa/rss"},
    {"id": 3019,"name": "Arab News",            "name_ar": "عرب نيوز",                "country": "السعودية",        "type": "صحيفة",       "lang": "en", "url": "https://www.arabnews.com/rss.xml"},
    {"id": 3020,"name": "Al Eqtisadiah",        "name_ar": "الاقتصادية",              "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.aleqt.com/rss"},

    # مصر
    {"id": 3021,"name": "Al Ahram",             "name_ar": "الأهرام",                 "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.ahram.org.eg/rss"},
    {"id": 3022,"name": "Al Masry Al Youm",     "name_ar": "المصري اليوم",            "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.almasryalyoum.com/rss.xml"},
    {"id": 3023,"name": "Al Shorouk Egypt",     "name_ar": "الشروق",                  "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.shorouknews.com/rss"},
    {"id": 3024,"name": "Al Wafd Egypt",        "name_ar": "الوفد",                   "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://alwafd.news/rss"},
    {"id": 3025,"name": "Masrawy",              "name_ar": "مصراوي",                  "country": "مصر",             "type": "رقمي",        "lang": "ar", "url": "https://www.masrawy.com/rss"},

    # المغرب العربي
    {"id": 3026,"name": "Hespress",             "name_ar": "هسبريس",                  "country": "المغرب",          "type": "رقمي",        "lang": "ar", "url": "https://www.hespress.com/feed"},
    {"id": 3027,"name": "Le360 Maroc",          "name_ar": "لو 360",                  "country": "المغرب",          "type": "رقمي",        "lang": "fr", "url": "https://fr.le360.ma/rss"},
    {"id": 3028,"name": "TelQuel Maroc",        "name_ar": "تيل كيل",                 "country": "المغرب",          "type": "مجلة",        "lang": "fr", "url": "https://telquel.ma/feed/"},
    {"id": 3029,"name": "Echorouk Algeria",     "name_ar": "الشروق الجزائرية",        "country": "الجزائر",         "type": "صحيفة",       "lang": "ar", "url": "https://www.echoroukonline.com/feed"},
    {"id": 3030,"name": "El Khabar Algeria",    "name_ar": "الخبر",                   "country": "الجزائر",         "type": "صحيفة",       "lang": "ar", "url": "https://www.elkhabar.com/press/rss"},
    {"id": 3031,"name": "TSA Algérie",          "name_ar": "تي إس إيه الجزائر",      "country": "الجزائر",         "type": "رقمي",        "lang": "fr", "url": "https://www.tsa-algerie.com/feed/"},
    {"id": 3032,"name": "Assabah Tunisia",      "name_ar": "الصباح التونسية",         "country": "تونس",            "type": "صحيفة",       "lang": "ar", "url": "https://www.assabahnews.tn/feed"},
    {"id": 3033,"name": "Nawaat Tunisia",       "name_ar": "نواة",                    "country": "تونس",            "type": "رقمي",        "lang": "ar", "url": "https://nawaat.org/feed/"},
    {"id": 3034,"name": "Libya Al Mostakbal",   "name_ar": "ليبيا المستقبل",          "country": "ليبيا",           "type": "رقمي",        "lang": "ar", "url": "https://libyaalm.com/feed"},

    # الشام والعراق
    {"id": 3035,"name": "An-Nahar Lebanon",     "name_ar": "النهار",                  "country": "لبنان",           "type": "صحيفة",       "lang": "ar", "url": "https://www.annahar.com/rss"},
    {"id": 3036,"name": "Al Liwa Lebanon",      "name_ar": "اللواء",                  "country": "لبنان",           "type": "صحيفة",       "lang": "ar", "url": "https://www.alliwaa.com/rss"},
    {"id": 3037,"name": "Al Modon Lebanon",     "name_ar": "المدن",                   "country": "لبنان",           "type": "رقمي",        "lang": "ar", "url": "https://www.almodon.com/rss"},
    {"id": 3038,"name": "Enab Baladi Syria",    "name_ar": "عنب بلدي",                "country": "سوريا",           "type": "رقمي",        "lang": "ar", "url": "https://english.enabbaladi.net/feed"},
    {"id": 3039,"name": "Al Mamlaka Jordan",    "name_ar": "المملكة",                 "country": "الأردن",          "type": "تلفزيون",     "lang": "ar", "url": "https://www.mamlaka.tv/rss"},
    {"id": 3040,"name": "Al Ghad Jordan",       "name_ar": "الغد",                    "country": "الأردن",          "type": "صحيفة",       "lang": "ar", "url": "https://alghad.com/feed/"},
    {"id": 3041,"name": "Al Rai Jordan",        "name_ar": "الرأي",                   "country": "الأردن",          "type": "صحيفة",       "lang": "ar", "url": "https://alrai.com/rss"},
    {"id": 3042,"name": "Al Mada Iraq",         "name_ar": "المدى",                   "country": "العراق",          "type": "صحيفة",       "lang": "ar", "url": "https://almadapaper.net/rss"},
    {"id": 3043,"name": "Al Sabah Jadeed Iraq", "name_ar": "الصباح الجديد",           "country": "العراق",          "type": "صحيفة",       "lang": "ar", "url": "https://newsabah.com/feed"},
    {"id": 3044,"name": "NRT Arabic Iraq",      "name_ar": "NRT عربي",                "country": "العراق",          "type": "تلفزيون",     "lang": "ar", "url": "https://www.nrttv.com/rss"},

    # اليمن والسودان وفلسطين
    {"id": 3045,"name": "Al Masdar Yemen",      "name_ar": "المصدر اليمني",           "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://almasdaronline.com/rss"},
    {"id": 3046,"name": "Yemen Shabab",         "name_ar": "يمن شباب",                "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://www.yemenshabab.net/rss"},
    {"id": 3047,"name": "Sudan Tribune",        "name_ar": "سودان تريبيون",           "country": "فرنسا",           "type": "رقمي",        "lang": "en", "url": "https://www.sudantribune.com/spip.php?page=backend"},
    {"id": 3048,"name": "Al Taghyeer Sudan",    "name_ar": "التغيير",                 "country": "السودان",         "type": "رقمي",        "lang": "ar", "url": "https://www.altaghyeer.info/feed"},
    {"id": 3049,"name": "WAFA Palestine",       "name_ar": "وفا",                     "country": "فلسطين",          "type": "وكالة أنباء", "lang": "en", "url": "https://english.wafa.ps/rss"},

    # ══════════════════════════════════════════
    # القسم الرابع: 121 مصدراً جغرافياً (230-350)
    # ══════════════════════════════════════════

    # إيران
    {"id": 4001,"name": "Tehran Times",         "name_ar": "طهران تايمز",             "country": "إيران",           "type": "صحيفة",       "lang": "en", "url": "https://www.tehrantimes.com/rss"},
    {"id": 4002,"name": "IRNA",                 "name_ar": "إرنا",                    "country": "إيران",           "type": "وكالة أنباء", "lang": "en", "url": "https://en.irna.ir/rss"},
    {"id": 4003,"name": "Fars News Agency",     "name_ar": "وكالة فارس",              "country": "إيران",           "type": "وكالة أنباء", "lang": "en", "url": "https://english.farsnews.ir/rss.xml"},
    {"id": 4004,"name": "Tasnim News",          "name_ar": "وكالة تسنيم",             "country": "إيران",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.tasnimnews.com/en/rss"},
    {"id": 4005,"name": "Press TV",             "name_ar": "برس تي في",               "country": "إيران",           "type": "تلفزيون",     "lang": "en", "url": "https://www.presstv.ir/RSS"},
    {"id": 4006,"name": "Iran Front Page",      "name_ar": "إيران فرونت بيج",         "country": "إيران",           "type": "رقمي",        "lang": "en", "url": "https://ifpnews.com/feed/"},
    {"id": 4007,"name": "Shargh Daily",         "name_ar": "شرق ديلي",                "country": "إيران",           "type": "صحيفة",       "lang": "fa", "url": "https://www.sharghdaily.com/rss"},
    {"id": 4008,"name": "Hamshahri",            "name_ar": "همشهري",                  "country": "إيران",           "type": "صحيفة",       "lang": "fa", "url": "https://hamshahrionline.ir/rss"},

    # إسرائيل إضافي
    {"id": 4009,"name": "Maariv",               "name_ar": "معاريف",                  "country": "إسرائيل",         "type": "صحيفة",       "lang": "he", "url": "https://www.maariv.co.il/rss"},
    {"id": 4010,"name": "Israel Hayom",         "name_ar": "إسرائيل هايوم",           "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.israelhayom.com/feed/"},
    {"id": 4011,"name": "Kan News Israel",      "name_ar": "كان نيوز",                "country": "إسرائيل",         "type": "تلفزيون",     "lang": "he", "url": "https://www.kan.org.il/rss"},

    # تركيا إضافي
    {"id": 4012,"name": "Cumhuriyet",           "name_ar": "جمهورييت",                "country": "تركيا",           "type": "صحيفة",       "lang": "tr", "url": "https://www.cumhuriyet.com.tr/rss/son_dakika.xml"},
    {"id": 4013,"name": "BirGün Turkey",        "name_ar": "بيرغون",                  "country": "تركيا",           "type": "صحيفة",       "lang": "tr", "url": "https://www.birgun.net/rss"},
    {"id": 4014,"name": "Sözcü",                "name_ar": "سوزجو",                   "country": "تركيا",           "type": "صحيفة",       "lang": "tr", "url": "https://www.sozcu.com.tr/rss.xml"},
    {"id": 4015,"name": "Bianet",               "name_ar": "بيانيت",                  "country": "تركيا",           "type": "رقمي",        "lang": "en", "url": "https://m.bianet.org/rss"},

    # آسيا الوسطى والقوقاز
    {"id": 4016,"name": "Akipress Kyrgyzstan",  "name_ar": "أكيبريس قيرغيزستان",     "country": "قيرغيزستان",      "type": "وكالة أنباء", "lang": "en", "url": "https://akipress.com/rss.xml"},
    {"id": 4017,"name": "The Astana Times",     "name_ar": "أستانا تايمز",            "country": "كازاخستان",       "type": "صحيفة",       "lang": "en", "url": "https://astanatimes.com/feed/"},
    {"id": 4018,"name": "Kun.uz Uzbekistan",    "name_ar": "كون أوزبكستان",           "country": "أوزبكستان",       "type": "رقمي",        "lang": "en", "url": "https://kun.uz/en/rss"},
    {"id": 4019,"name": "Asia-Plus Tajikistan", "name_ar": "آسيا بلاس طاجيكستان",    "country": "طاجيكستان",       "type": "رقمي",        "lang": "en", "url": "https://asiaplustj.info/en/rss"},
    {"id": 4020,"name": "JAMnews Georgia",      "name_ar": "جام نيوز جورجيا",         "country": "جورجيا",          "type": "رقمي",        "lang": "en", "url": "https://jam-news.net/feed/"},
    {"id": 4021,"name": "AzerNews",             "name_ar": "أذربيجان نيوز",           "country": "أذربيجان",        "type": "صحيفة",       "lang": "en", "url": "https://www.azernews.az/rss/"},
    {"id": 4022,"name": "Hetq Armenia",         "name_ar": "هيتك أرمينيا",            "country": "أرمينيا",         "type": "رقمي",        "lang": "en", "url": "https://hetq.am/en/rss"},
    {"id": 4023,"name": "Caucasus Watch",       "name_ar": "قوقاز ووتش",              "country": "ألمانيا",         "type": "رقمي",        "lang": "en", "url": "https://caucasuswatch.de/feed/"},

    # جنوب آسيا إضافي
    {"id": 4024,"name": "Scroll.in India",      "name_ar": "سكرول إن",                "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://scroll.in/rss"},
    {"id": 4025,"name": "The Quint India",      "name_ar": "ذا كوينت",                "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://www.thequint.com/rss"},
    {"id": 4026,"name": "Firstpost India",      "name_ar": "فيرستبوست",               "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://www.firstpost.com/rss"},
    {"id": 4027,"name": "The News International","name_ar": "ذا نيوز",                "country": "باكستان",         "type": "صحيفة",       "lang": "en", "url": "https://www.thenews.com.pk/rss/1/1"},
    {"id": 4028,"name": "Geo News Pakistan",    "name_ar": "جيو نيوز",                "country": "باكستان",         "type": "تلفزيون",     "lang": "en", "url": "https://www.geo.tv/rss/feeds"},
    {"id": 4029,"name": "Daily Mirror Sri Lanka","name_ar": "ديلي ميرور سريلانكا",    "country": "سريلانكا",        "type": "صحيفة",       "lang": "en", "url": "https://www.dailymirror.lk/rss"},
    {"id": 4030,"name": "Kathmandu Post",       "name_ar": "كاتمانضو بوست",           "country": "نيبال",           "type": "صحيفة",       "lang": "en", "url": "https://kathmandupost.com/rss"},
    {"id": 4031,"name": "Dhaka Tribune",        "name_ar": "دكا تريبيون",             "country": "بنغلاديش",        "type": "صحيفة",       "lang": "en", "url": "https://www.dhakatribune.com/rss"},

    # شرق آسيا إضافي
    {"id": 4032,"name": "Asahi Shimbun",        "name_ar": "آساهي شيمبون",            "country": "اليابان",         "type": "صحيفة",       "lang": "en", "url": "https://www.asahi.com/ajw/rss.xml"},
    {"id": 4033,"name": "Korea JoongAng Daily", "name_ar": "كوريا جونغانغ ديلي",      "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://koreajoongangdaily.joins.com/rss/feeds"},
    {"id": 4034,"name": "Hankyoreh Korea",      "name_ar": "هانكيورة",                "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://english.hani.co.kr/rss"},
    {"id": 4035,"name": "Taipei Times",         "name_ar": "تايبيه تايمز",            "country": "تايوان",          "type": "صحيفة",       "lang": "en", "url": "https://www.taipeitimes.com/News/rss"},
    {"id": 4036,"name": "Caixin Global China",  "name_ar": "كايكسن غلوبال",           "country": "الصين",           "type": "صحيفة",       "lang": "en", "url": "https://www.caixinglobal.com/rss"},
    {"id": 4037,"name": "Global Times China",   "name_ar": "غلوبال تايمز",            "country": "الصين",           "type": "صحيفة",       "lang": "en", "url": "https://www.globaltimes.cn/rss/outbrain.xml"},

    # جنوب شرق آسيا إضافي
    {"id": 4038,"name": "Philippine Star",      "name_ar": "فيليبين ستار",            "country": "الفلبين",         "type": "صحيفة",       "lang": "en", "url": "https://www.philstar.com/rss/headlines"},
    {"id": 4039,"name": "Kompas Indonesia",     "name_ar": "كومباس",                  "country": "إندونيسيا",       "type": "صحيفة",       "lang": "id", "url": "https://rss.kompas.com/index.xml"},
    {"id": 4040,"name": "Tempo Indonesia",      "name_ar": "تيمبو",                   "country": "إندونيسيا",       "type": "مجلة",        "lang": "id", "url": "https://www.tempo.co/rss/dunia"},
    {"id": 4041,"name": "Thanh Nien Vietnam",   "name_ar": "ثان نين",                 "country": "فيتنام",          "type": "صحيفة",       "lang": "vi", "url": "https://thanhnien.vn/rss/home.rss"},
    {"id": 4042,"name": "The Nation Thailand",  "name_ar": "ذا نيشن تايلاند",         "country": "تايلاند",         "type": "صحيفة",       "lang": "en", "url": "https://www.nationthailand.com/rss"},
    {"id": 4043,"name": "Malay Mail",           "name_ar": "ملاي ميل",                "country": "ماليزيا",         "type": "صحيفة",       "lang": "en", "url": "https://www.malaymail.com/rss"},
    {"id": 4044,"name": "Mizzima Myanmar",      "name_ar": "ميزيما ميانمار",          "country": "ميانمار",         "type": "رقمي",        "lang": "en", "url": "https://mizzima.com/feed"},

    # أفريقيا إضافي
    {"id": 4045,"name": "Punch Nigeria",        "name_ar": "بنش نيجيريا",             "country": "نيجيريا",         "type": "صحيفة",       "lang": "en", "url": "https://punchng.com/feed/"},
    {"id": 4046,"name": "Vanguard Nigeria",     "name_ar": "فانغارد نيجيريا",         "country": "نيجيريا",         "type": "صحيفة",       "lang": "en", "url": "https://www.vanguardngr.com/feed/"},
    {"id": 4047,"name": "The Citizen Tanzania", "name_ar": "ذا سيتيزن تنزانيا",      "country": "تنزانيا",         "type": "صحيفة",       "lang": "en", "url": "https://www.thecitizen.co.tz/feed"},
    {"id": 4048,"name": "New Vision Uganda",    "name_ar": "نيو فيجن أوغندا",         "country": "أوغندا",          "type": "صحيفة",       "lang": "en", "url": "https://www.newvision.co.ug/rss"},
    {"id": 4049,"name": "Addis Standard",       "name_ar": "أديس ستاندرد",            "country": "إثيوبيا",         "type": "رقمي",        "lang": "en", "url": "https://addisstandard.com/feed/"},
    {"id": 4050,"name": "Garowe Online Somalia","name_ar": "غارووي أونلاين",          "country": "الصومال",         "type": "رقمي",        "lang": "en", "url": "https://www.garoweonline.com/en/rss"},
    {"id": 4051,"name": "Jeune Afrique",        "name_ar": "جون أفريك",               "country": "أفريقيا",         "type": "مجلة",        "lang": "fr", "url": "https://www.jeuneafrique.com/feed/"},
    {"id": 4052,"name": "The Africa Report",    "name_ar": "ذا أفريكا ريبورت",        "country": "أفريقيا",         "type": "مجلة",        "lang": "en", "url": "https://www.theafricareport.com/feed/"},
    {"id": 4053,"name": "News24 South Africa",  "name_ar": "نيوز 24 جنوب أفريقيا",   "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://feeds.news24.com/articles/news24/TopStories/rss"},
    {"id": 4054,"name": "IOL South Africa",     "name_ar": "آي أو إل",                "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://www.iol.co.za/rss"},
    {"id": 4055,"name": "Ghana Web",            "name_ar": "غانا ويب",                "country": "غانا",            "type": "رقمي",        "lang": "en", "url": "https://www.ghanaweb.com/rss"},
    {"id": 4056,"name": "Cameroon Tribune",     "name_ar": "كاميرون تريبيون",         "country": "الكاميرون",       "type": "صحيفة",       "lang": "fr", "url": "https://www.cameroon-tribune.cm/rss"},
    {"id": 4057,"name": "Le Soleil Senegal",    "name_ar": "لو سوليل السنغال",        "country": "السنغال",         "type": "صحيفة",       "lang": "fr", "url": "https://www.lesoleil.sn/feed/"},
    {"id": 4058,"name": "Madagascar Tribune",   "name_ar": "مدغشقر تريبيون",          "country": "مدغشقر",          "type": "صحيفة",       "lang": "fr", "url": "https://www.madagascar-tribune.com/feed/"},

    # أمريكا اللاتينية إضافي
    {"id": 4059,"name": "El Universal México",  "name_ar": "إل أونيفرسال مكسيكو",    "country": "المكسيك",         "type": "صحيفة",       "lang": "es", "url": "https://www.eluniversal.com.mx/rss"},
    {"id": 4060,"name": "El Comercio Perú",     "name_ar": "إل كوميرسيو",             "country": "بيرو",            "type": "صحيفة",       "lang": "es", "url": "https://elcomercio.pe/rss"},
    {"id": 4061,"name": "La Tercera Chile",     "name_ar": "لا تيرسيرا",              "country": "تشيلي",           "type": "صحيفة",       "lang": "es", "url": "https://www.latercera.com/rss"},
    {"id": 4062,"name": "El Mercurio Chile",    "name_ar": "إل ميركوريو",             "country": "تشيلي",           "type": "صحيفة",       "lang": "es", "url": "https://www.emol.com/rss/"},
    {"id": 4063,"name": "El Tiempo Colombia",   "name_ar": "إل تيمبو كولومبيا",      "country": "كولومبيا",        "type": "صحيفة",       "lang": "es", "url": "https://www.eltiempo.com/rss"},
    {"id": 4064,"name": "El Nacional Venezuela","name_ar": "إل ناسيونال",             "country": "فنزويلا",         "type": "صحيفة",       "lang": "es", "url": "https://www.el-nacional.com/feed/"},
    {"id": 4065,"name": "La Diaria Uruguay",    "name_ar": "لا دياريا",               "country": "أوروغواي",        "type": "صحيفة",       "lang": "es", "url": "https://ladiaria.com.uy/feed/"},
    {"id": 4066,"name": "ABC Color Paraguay",   "name_ar": "أي بي سي كولور",          "country": "باراغواي",        "type": "صحيفة",       "lang": "es", "url": "https://www.abc.com.py/rss/ultimas-noticias.xml"},
    {"id": 4067,"name": "El Deber Bolivia",     "name_ar": "إل ديبير بوليفيا",        "country": "بوليفيا",         "type": "صحيفة",       "lang": "es", "url": "https://eldeber.com.bo/feed"},
    {"id": 4068,"name": "El Universo Ecuador",  "name_ar": "إل أونيفيرسو",            "country": "الإكوادور",       "type": "صحيفة",       "lang": "es", "url": "https://www.eluniverso.com/rss"},
    {"id": 4069,"name": "Listín Diario",        "name_ar": "ليستين دياريو",           "country": "الدومينيكان",     "type": "صحيفة",       "lang": "es", "url": "https://listindiario.com/rss.xml"},

    # أوروبا الشرقية والبلقان
    {"id": 4070,"name": "Ukrainska Pravda",     "name_ar": "أوكرانسكا برافدا",        "country": "أوكرانيا",        "type": "رقمي",        "lang": "en", "url": "https://www.pravda.com.ua/eng/rss/"},
    {"id": 4071,"name": "Kyiv Independent",     "name_ar": "كييف إندبندنت",           "country": "أوكرانيا",        "type": "رقمي",        "lang": "en", "url": "https://kyivindependent.com/feed"},
    {"id": 4072,"name": "NEXTA Belarus",        "name_ar": "نيكستا بيلاروسيا",        "country": "بيلاروسيا",       "type": "رقمي",        "lang": "en", "url": "https://nexta.tv/rss"},
    {"id": 4073,"name": "Digi24 Romania",       "name_ar": "ديجي 24 رومانيا",         "country": "رومانيا",         "type": "تلفزيون",     "lang": "ro", "url": "https://www.digi24.ro/rss"},
    {"id": 4074,"name": "Novinite Bulgaria",    "name_ar": "نوفينيتي بلغاريا",        "country": "بلغاريا",         "type": "رقمي",        "lang": "en", "url": "https://www.novinite.com/rss"},
    {"id": 4075,"name": "N1 Info Balkans",      "name_ar": "إن 1 إنفو",               "country": "صربيا",           "type": "تلفزيون",     "lang": "en", "url": "https://n1info.com/feed/"},
    {"id": 4076,"name": "Jutarnji List Croatia","name_ar": "يوتارني ليست",             "country": "كرواتيا",         "type": "صحيفة",       "lang": "hr", "url": "https://www.jutarnji.hr/rss"},
    {"id": 4077,"name": "HVG Hungary",          "name_ar": "إتش في جي المجر",         "country": "المجر",           "type": "مجلة",        "lang": "hu", "url": "https://hvg.hu/rss"},
    {"id": 4078,"name": "Postimees Estonia",    "name_ar": "بوستيميس إستونيا",        "country": "إستونيا",         "type": "صحيفة",       "lang": "et", "url": "https://www.postimees.ee/rss"},
    {"id": 4079,"name": "Delfi Lithuania",      "name_ar": "دلفي ليتوانيا",           "country": "ليتوانيا",        "type": "رقمي",        "lang": "lt", "url": "https://www.delfi.lt/rss/feeds.xml"},
    {"id": 4080,"name": "Berlingske Denmark",   "name_ar": "بيرلينغسكي الدنمارك",     "country": "الدنمارك",        "type": "صحيفة",       "lang": "da", "url": "https://www.berlingske.dk/rss/nyheder"},
    {"id": 4081,"name": "Expressen Sweden",     "name_ar": "إكسبريسن السويد",          "country": "السويد",          "type": "صحيفة",       "lang": "sv", "url": "https://feeds.expressen.se/nyheter/"},
    {"id": 4082,"name": "VG Norway",            "name_ar": "في جي النرويج",            "country": "النرويج",         "type": "صحيفة",       "lang": "no", "url": "https://www.vg.no/rss/feed/?categories=1"},
    {"id": 4083,"name": "RTÉ News Ireland",     "name_ar": "آر تي إي أيرلندا",        "country": "أيرلندا",         "type": "تلفزيون",     "lang": "en", "url": "https://www.rte.ie/rss/news.xml"},
    {"id": 4084,"name": "ERR News Estonia",     "name_ar": "إي آر آر إستونيا",        "country": "إستونيا",         "type": "تلفزيون",     "lang": "en", "url": "https://err.ee/rss"},

    # أستراليا / نيوزيلندا إضافي
    {"id": 4085,"name": "The Age Australia",    "name_ar": "ذا إيج أستراليا",         "country": "أستراليا",        "type": "صحيفة",       "lang": "en", "url": "https://www.theage.com.au/rss/feed.xml"},
    {"id": 4086,"name": "SBS News Australia",   "name_ar": "إس بي إس نيوز",           "country": "أستراليا",        "type": "تلفزيون",     "lang": "en", "url": "https://www.sbs.com.au/news/topic/latest/feed"},
    {"id": 4087,"name": "Stuff New Zealand",    "name_ar": "ستاف نيوزيلندا",          "country": "نيوزيلندا",       "type": "رقمي",        "lang": "en", "url": "https://www.stuff.co.nz/rss"},
    {"id": 4088,"name": "RNZ New Zealand",      "name_ar": "راديو نيوزيلندا",         "country": "نيوزيلندا",       "type": "راديو",       "lang": "en", "url": "https://www.rnz.co.nz/rss/world.xml"},

    # كاريبي وأمريكا الوسطى
    {"id": 4089,"name": "Jamaica Gleaner",      "name_ar": "جامايكا غليانر",          "country": "جامايكا",         "type": "صحيفة",       "lang": "en", "url": "https://jamaica-gleaner.com/feed"},
    {"id": 4090,"name": "Trinidad Express",     "name_ar": "ترينيداد إكسبريس",        "country": "ترينيداد",        "type": "صحيفة",       "lang": "en", "url": "https://trinidadexpress.com/feed"},
    {"id": 4091,"name": "La Prensa Panamá",     "name_ar": "لا برينسا بنما",           "country": "بنما",            "type": "صحيفة",       "lang": "es", "url": "https://www.prensa.com/feed/"},
    {"id": 4092,"name": "El Faro El Salvador",  "name_ar": "إل فارو السلفادور",        "country": "السلفادور",       "type": "رقمي",        "lang": "es", "url": "https://elfaro.net/rss"},

    # مصادر متخصصة عالمية
    {"id": 4093,"name": "Voice of America",     "name_ar": "صوت أمريكا",              "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://www.voanews.com/rss/latest-news.rss"},
    {"id": 4094,"name": "Radio Free Europe",    "name_ar": "راديو أوروبا الحرة",      "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://www.rferl.org/z/632.xml"},
    {"id": 4095,"name": "DW Español",           "name_ar": "دويتشه فيله إسباني",      "country": "ألمانيا",         "type": "تلفزيون",     "lang": "es", "url": "https://rss.dw.com/rdf/rss-es-all"},
    {"id": 4096,"name": "NHK World Arabic",     "name_ar": "إن إتش كي ورلد عربي",    "country": "اليابان",         "type": "تلفزيون",     "lang": "ar", "url": "https://www3.nhk.or.jp/nhkworld/arabic/news/feeds/"},
    {"id": 4097,"name": "BBC Hausa",            "name_ar": "بي بي سي هوسا",           "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://feeds.bbci.co.uk/hausa/rss.xml"},
    {"id": 4098,"name": "BBC Mundo",            "name_ar": "بي بي سي موندو",          "country": "بريطانيا",        "type": "تلفزيون",     "lang": "es", "url": "https://feeds.bbci.co.uk/mundo/rss.xml"},
    {"id": 4099,"name": "France 24 Español",    "name_ar": "فرانس 24 إسباني",         "country": "فرنسا",           "type": "تلفزيون",     "lang": "es", "url": "https://www.france24.com/es/rss"},
    {"id": 4100,"name": "Sputnik International","name_ar": "سبوتنيك الدولية",          "country": "روسيا",           "type": "وكالة أنباء", "lang": "en", "url": "https://sputnikglobe.com/export/rss2/archive/index.xml"},

    # ══════════════════════════════════════════
    # القسم الخامس: مصادر عربية إضافية (351-430)
    # ══════════════════════════════════════════

    # السعودية إضافي
    {"id": 5001,"name": "Al Madina Saudi",      "name_ar": "المدينة",                 "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.al-madina.com/rss"},
    {"id": 5002,"name": "Al Bilad Saudi",       "name_ar": "البلاد",                  "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.al-bilad.com/feed"},
    {"id": 5003,"name": "Sabq Saudi",           "name_ar": "سبق",                     "country": "السعودية",        "type": "رقمي",        "lang": "ar", "url": "https://sabq.org/feed"},
    {"id": 5004,"name": "Akhbaar24 Saudi",      "name_ar": "أخبار 24",                "country": "السعودية",        "type": "رقمي",        "lang": "ar", "url": "https://www.akhbaar24.com/rss"},
    {"id": 5005,"name": "Makkah Newspaper",     "name_ar": "مكة",                     "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://makkahnewspaper.com/feed"},
    {"id": 5006,"name": "Saudi Gazette",        "name_ar": "سعودي غازيت",            "country": "السعودية",        "type": "صحيفة",       "lang": "en", "url": "https://saudigazette.com.sa/feed"},
    {"id": 5007,"name": "Al Yaum Saudi",        "name_ar": "اليوم",                   "country": "السعودية",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alyaum.com/feed"},

    # الإمارات إضافي
    {"id": 5008,"name": "Emarat Al Youm",       "name_ar": "إمارات اليوم",            "country": "الإمارات",        "type": "صحيفة",       "lang": "ar", "url": "https://www.emaratalyoum.com/rss"},
    {"id": 5009,"name": "Gulf News",            "name_ar": "غلف نيوز",                "country": "الإمارات",        "type": "صحيفة",       "lang": "en", "url": "https://gulfnews.com/rss"},
    {"id": 5010,"name": "Khaleej Times",        "name_ar": "خليج تايمز",              "country": "الإمارات",        "type": "صحيفة",       "lang": "en", "url": "https://www.khaleejtimes.com/rssfeed"},
    {"id": 5011,"name": "Al Ain News UAE",      "name_ar": "العين الإخبارية",         "country": "الإمارات",        "type": "رقمي",        "lang": "ar", "url": "https://al-ain.com/rss"},

    # مصر إضافي
    {"id": 5012,"name": "Al Dustour Egypt",     "name_ar": "الدستور",                 "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.dostor.org/rss"},
    {"id": 5013,"name": "Al Yawm Al Sabe",      "name_ar": "اليوم السابع",            "country": "مصر",             "type": "رقمي",        "lang": "ar", "url": "https://www.youm7.com/rss"},
    {"id": 5014,"name": "Veto Gate Egypt",      "name_ar": "فيتو",                    "country": "مصر",             "type": "رقمي",        "lang": "ar", "url": "https://www.vetogate.com/rss"},
    {"id": 5015,"name": "Cairo 24",             "name_ar": "القاهرة 24",              "country": "مصر",             "type": "رقمي",        "lang": "ar", "url": "https://www.cairo24.com/feed"},
    {"id": 5016,"name": "Al Gomhuria Egypt",    "name_ar": "الجمهورية",               "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.algomhuria.net.eg/rss"},
    {"id": 5017,"name": "Al Fagr Egypt",        "name_ar": "الفجر",                   "country": "مصر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.elfagr.com/rss"},
    {"id": 5018,"name": "Sada Al Balad Egypt",  "name_ar": "صدى البلد",               "country": "مصر",             "type": "تلفزيون",     "lang": "ar", "url": "https://www.el-balad.com/rss"},

    # لبنان إضافي
    {"id": 5019,"name": "LBCI Lebanon",         "name_ar": "إل بي سي آي",             "country": "لبنان",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.lbci.com/rss"},
    {"id": 5020,"name": "MTV Lebanon",          "name_ar": "إم تي في لبنان",          "country": "لبنان",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.mtv.com.lb/rss"},
    {"id": 5021,"name": "Al Akhbar Lebanon",    "name_ar": "الأخبار اللبنانية",       "country": "لبنان",           "type": "صحيفة",       "lang": "ar", "url": "https://al-akhbar.com/rss"},
    {"id": 5022,"name": "L'Orient Today",       "name_ar": "لوريان توداي",            "country": "لبنان",           "type": "رقمي",        "lang": "en", "url": "https://today.lorientlejour.com/feed"},

    # الأردن والعراق إضافي
    {"id": 5023,"name": "Jordan Times",         "name_ar": "جوردان تايمز",            "country": "الأردن",          "type": "صحيفة",       "lang": "en", "url": "https://jordantimes.com/feed"},
    {"id": 5024,"name": "Petra Jordan",         "name_ar": "وكالة بترا الأردنية",     "country": "الأردن",          "type": "وكالة أنباء", "lang": "ar", "url": "https://petra.gov.jo/rss"},
    {"id": 5025,"name": "Al Sumaria Iraq",      "name_ar": "السومرية",                "country": "العراق",          "type": "تلفزيون",     "lang": "ar", "url": "https://www.alsumaria.tv/rss"},
    {"id": 5026,"name": "Baghdad Post",         "name_ar": "بغداد بوست",              "country": "العراق",          "type": "رقمي",        "lang": "ar", "url": "https://www.thebaghdadpost.com/rss"},
    {"id": 5027,"name": "Rudaw Kurdistan",      "name_ar": "رووداو",                  "country": "العراق",          "type": "تلفزيون",     "lang": "ar", "url": "https://www.rudaw.net/arabic/rss"},
    {"id": 5028,"name": "Kurdistan 24",         "name_ar": "كردستان 24",              "country": "العراق",          "type": "تلفزيون",     "lang": "ar", "url": "https://www.kurdistan24.net/ar/rss.xml"},

    # سوريا إضافي
    {"id": 5029,"name": "Syria TV",             "name_ar": "سوريا تي في",             "country": "سوريا",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.syria.tv/rss"},
    {"id": 5030,"name": "Syria Direct",         "name_ar": "سوريا ديريكت",            "country": "سوريا",           "type": "رقمي",        "lang": "en", "url": "https://syriadirect.org/feed/"},
    {"id": 5031,"name": "Zaman Al Wasl Syria",  "name_ar": "زمان الوصل",              "country": "سوريا",           "type": "رقمي",        "lang": "ar", "url": "https://www.zamanalwsl.net/rss"},

    # فلسطين إضافي
    {"id": 5032,"name": "Ma'an News Palestine", "name_ar": "معاً الفلسطينية",         "country": "فلسطين",          "type": "وكالة أنباء", "lang": "ar", "url": "https://www.maannews.com/RSS/"},
    {"id": 5033,"name": "Quds Net Palestine",   "name_ar": "القدس نت",                "country": "فلسطين",          "type": "رقمي",        "lang": "ar", "url": "https://qudsnet.com/feed"},
    {"id": 5034,"name": "Watan Voice Palestine","name_ar": "صوت الوطن",               "country": "فلسطين",          "type": "رقمي",        "lang": "ar", "url": "https://www.wattan.net/rss"},

    # المغرب العربي إضافي
    {"id": 5035,"name": "Yabiladi Maroc",       "name_ar": "يبيلادي المغرب",          "country": "المغرب",          "type": "رقمي",        "lang": "fr", "url": "https://www.yabiladi.com/articles/rss.xml"},
    {"id": 5036,"name": "Al Massae Maroc",      "name_ar": "المساء المغربية",         "country": "المغرب",          "type": "صحيفة",       "lang": "ar", "url": "https://www.almassae.press.ma/rss"},
    {"id": 5037,"name": "Ennahar Algeria",      "name_ar": "النهار الجزائرية",        "country": "الجزائر",         "type": "صحيفة",       "lang": "ar", "url": "https://www.ennaharonline.com/feed"},
    {"id": 5038,"name": "Al Khabar Algeria",    "name_ar": "الخبر الجزائرية",         "country": "الجزائر",         "type": "صحيفة",       "lang": "ar", "url": "https://www.elkhabar.com/press/rss"},
    {"id": 5039,"name": "Mosaique FM Tunisia",  "name_ar": "موزاييك إف إم",           "country": "تونس",            "type": "راديو",       "lang": "ar", "url": "https://www.mosaiquefm.net/rss"},
    {"id": 5040,"name": "Business News Tunisia","name_ar": "بيزنس نيوز تونس",         "country": "تونس",            "type": "رقمي",        "lang": "fr", "url": "https://www.businessnews.com.tn/rss.xml"},
    {"id": 5041,"name": "Ain Libya",            "name_ar": "عين ليبيا",               "country": "ليبيا",           "type": "رقمي",        "lang": "ar", "url": "https://www.ain.ly/feed"},
    {"id": 5042,"name": "Al Marsd Sudan",       "name_ar": "المرصد السوداني",         "country": "السودان",         "type": "رقمي",        "lang": "ar", "url": "https://almarsd.com/feed"},

    # اليمن إضافي
    {"id": 5043,"name": "Yemen Monitor",        "name_ar": "يمن مونيتور",             "country": "اليمن",           "type": "رقمي",        "lang": "en", "url": "https://www.yemenmonitor.com/rss"},
    {"id": 5044,"name": "Al Ayyam Yemen",       "name_ar": "الأيام اليمنية",          "country": "اليمن",           "type": "صحيفة",       "lang": "ar", "url": "https://www.alayyam.info/feed"},

    # الكويت والبحرين والسعودية
    {"id": 5045,"name": "Al Jarida Kuwait",     "name_ar": "الجريدة الكويتية",        "country": "الكويت",          "type": "صحيفة",       "lang": "ar", "url": "https://www.aljarida.com/rss"},
    {"id": 5046,"name": "Kuwait Times",         "name_ar": "كويت تايمز",              "country": "الكويت",          "type": "صحيفة",       "lang": "en", "url": "https://www.kuwaittimes.com/feed/"},
    {"id": 5047,"name": "GDN Bahrain",          "name_ar": "جي دي إن البحرين",        "country": "البحرين",         "type": "صحيفة",       "lang": "en", "url": "https://www.gdnonline.com/rss"},
    {"id": 5048,"name": "Times of Oman",        "name_ar": "تايمز أوف عُمان",         "country": "عُمان",           "type": "صحيفة",       "lang": "en", "url": "https://www.timesofoman.com/rss"},
    {"id": 5049,"name": "Al Arab Qatar",        "name_ar": "العرب القطرية",           "country": "قطر",             "type": "صحيفة",       "lang": "ar", "url": "https://www.alarab.qa/rss"},
    {"id": 5050,"name": "Doha News",            "name_ar": "الدوحة نيوز",             "country": "قطر",             "type": "رقمي",        "lang": "en", "url": "https://dohanews.co/feed/"},

    # ══════════════════════════════════════════
    # القسم السادس: مصادر إنجليزية وعالمية (431-510)
    # ══════════════════════════════════════════

    # أمريكا إضافي
    {"id": 6001,"name": "MSNBC",                "name_ar": "إم إس إن بي سي",         "country": "أمريكا",          "type": "تلفزيون",     "lang": "en", "url": "https://feeds.nbcnews.com/nbcnews/public/news"},
    {"id": 6002,"name": "NBC News",             "name_ar": "إن بي سي نيوز",           "country": "أمريكا",          "type": "تلفزيون",     "lang": "en", "url": "https://feeds.nbcnews.com/nbcnews/public/topstories"},
    {"id": 6003,"name": "Newsweek",             "name_ar": "نيوزويك",                 "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.newsweek.com/rss"},
    {"id": 6004,"name": "The Nation USA",       "name_ar": "ذا نيشن أمريكا",         "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.thenation.com/feed/?post_type=article"},
    {"id": 6005,"name": "Slate",                "name_ar": "سليت",                    "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://feeds.slate.com/slate/all"},
    {"id": 6006,"name": "Jacobin",              "name_ar": "جاكوبن",                  "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://jacobin.com/feed/"},
    {"id": 6007,"name": "Common Dreams",        "name_ar": "كومون دريمز",             "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.commondreams.org/feeds/feed.rss"},
    {"id": 6008,"name": "Truthout",             "name_ar": "تروثاوت",                 "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://truthout.org/feed/"},
    {"id": 6009,"name": "Mother Jones",         "name_ar": "ماذر جونز",               "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.motherjones.com/feed/"},
    {"id": 6010,"name": "Buzzfeed News",        "name_ar": "بازفيد نيوز",             "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.buzzfeednews.com/sitemap/news.rss"},

    # بريطانيا إضافي
    {"id": 6011,"name": "The Spectator",        "name_ar": "ذا سبيكتاتور",           "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.spectator.co.uk/feed/"},
    {"id": 6012,"name": "New Statesman",        "name_ar": "نيو ستيتسمان",           "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.newstatesman.com/feed/"},
    {"id": 6013,"name": "The Mirror UK",        "name_ar": "ذا ميرور",               "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.mirror.co.uk/news/rss.xml"},
    {"id": 6014,"name": "The Sun UK",           "name_ar": "ذا صن",                  "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.thesun.co.uk/news/worldnews/feed/"},
    {"id": 6015,"name": "Evening Standard",     "name_ar": "إيفنينغ ستاندرد",        "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.standard.co.uk/news/world/rss"},
    {"id": 6016,"name": "Belfast Telegraph",    "name_ar": "بلفاست تلغراف",          "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://www.belfasttelegraph.co.uk/news/rss"},

    # فرنسا إضافي
    {"id": 6017,"name": "Le Figaro",            "name_ar": "لو فيغارو",               "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.lefigaro.fr/rss/figaro_monde.xml"},
    {"id": 6018,"name": "Liberation",          "name_ar": "ليبيراسيون",              "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.liberation.fr/arc/outboundfeeds/rss/"},
    {"id": 6019,"name": "L'Express",            "name_ar": "ليكسبريس",                "country": "فرنسا",           "type": "مجلة",        "lang": "fr", "url": "https://www.lexpress.fr/rss/alaune.xml"},
    {"id": 6020,"name": "RFI Français",         "name_ar": "راديو فرنسا الدولي",     "country": "فرنسا",           "type": "راديو",       "lang": "fr", "url": "https://www.rfi.fr/fr/rss"},

    # ألمانيا إضافي
    {"id": 6021,"name": "Stern",                "name_ar": "شتيرن",                   "country": "ألمانيا",         "type": "مجلة",        "lang": "de", "url": "https://www.stern.de/feed/standard/alle-nachrichten/"},
    {"id": 6022,"name": "Focus Online",         "name_ar": "فوكوس",                   "country": "ألمانيا",         "type": "رقمي",        "lang": "de", "url": "https://rss.focus.de/fol/XML/rss_folnews.xml"},
    {"id": 6023,"name": "Handelsblatt",         "name_ar": "هانديلسبلات",             "country": "ألمانيا",         "type": "صحيفة",       "lang": "de", "url": "https://www.handelsblatt.com/contentexport/feed/schlagzeilen"},
    {"id": 6024,"name": "Deutsche Welle Arabic","name_ar": "دويتشه فيله عربي",       "country": "ألمانيا",         "type": "تلفزيون",     "lang": "ar", "url": "https://rss.dw.com/rdf/rss-ar-all"},

    # إيطاليا / إسبانيا إضافي
    {"id": 6025,"name": "Corriere della Sera",  "name_ar": "كوريري ديلا سيرا",       "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.corriere.it/rss/homepage.xml"},
    {"id": 6026,"name": "El País",              "name_ar": "إل باييس",                "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/english.elpais.com/portada"},
    {"id": 6027,"name": "La Vanguardia",        "name_ar": "لا فانغوارديا",           "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://www.lavanguardia.com/rss/home.xml"},
    {"id": 6028,"name": "El Confidencial",      "name_ar": "إل كونفيدينسيال",         "country": "إسبانيا",         "type": "رقمي",        "lang": "es", "url": "https://rss.elconfidencial.com/mundo/"},

    # روسيا إضافي
    {"id": 6029,"name": "RT International",     "name_ar": "آر تي الدولية",           "country": "روسيا",           "type": "تلفزيون",     "lang": "en", "url": "https://www.rt.com/rss/"},
    {"id": 6030,"name": "Moscow Times",         "name_ar": "موسكو تايمز",             "country": "روسيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.themoscowtimes.com/rss/news"},
    {"id": 6031,"name": "Meduza",               "name_ar": "ميدوزا",                  "country": "روسيا",           "type": "رقمي",        "lang": "en", "url": "https://meduza.io/rss/all"},
    {"id": 6032,"name": "Novaya Gazeta",        "name_ar": "نوفايا غازيتا",          "country": "روسيا",           "type": "صحيفة",       "lang": "en", "url": "https://novayagazeta.ru/rss/all.xml"},

    # آسيا إضافي
    {"id": 6033,"name": "The Irrawaddy",        "name_ar": "الإراوادي",               "country": "ميانمار",         "type": "رقمي",        "lang": "en", "url": "https://www.irrawaddy.com/feed"},
    {"id": 6034,"name": "Radio Free Asia",      "name_ar": "راديو آسيا الحرة",        "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://www.rfa.org/english/rss2.xml"},
    {"id": 6035,"name": "The Diplomat",         "name_ar": "ذا ديبلومات",             "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://thediplomat.com/feed/"},
    {"id": 6036,"name": "Nikkei",               "name_ar": "نيكاي",                   "country": "اليابان",         "type": "مالي",        "lang": "en", "url": "https://www.nikkei.com/rss/world.xml"},

    # أفريقيا / أمريكا لاتينية إضافي
    {"id": 6037,"name": "The Guardian Nigeria", "name_ar": "غارديان نيجيريا",         "country": "نيجيريا",         "type": "صحيفة",       "lang": "en", "url": "https://guardian.ng/feed"},
    {"id": 6038,"name": "This Day Nigeria",     "name_ar": "ذيس داي نيجيريا",        "country": "نيجيريا",         "type": "صحيفة",       "lang": "en", "url": "https://www.thisdaylive.com/feed/"},
    {"id": 6039,"name": "The Independent Kenya","name_ar": "إندبندنت كينيا",          "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.theindependentkenya.co.ke/feed/"},
    {"id": 6040,"name": "O Globo Brazil",       "name_ar": "أو غلوبو",               "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://oglobo.globo.com/rss.xml"},
    {"id": 6041,"name": "Folha de S.Paulo",     "name_ar": "فولها دي ساو باولو",      "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml"},
    {"id": 6042,"name": "La Nación Argentina",  "name_ar": "لا ناسيون الأرجنتين",    "country": "الأرجنتين",       "type": "صحيفة",       "lang": "es", "url": "https://www.lanacion.com.ar/arc/outboundfeeds/rss/"},
    {"id": 6043,"name": "Clarín Argentina",     "name_ar": "كلارين الأرجنتين",        "country": "الأرجنتين",       "type": "صحيفة",       "lang": "es", "url": "https://www.clarin.com/rss/latest/"},

    # تقنية / علوم
    {"id": 6044,"name": "TechCrunch",           "name_ar": "تيك كرانش",               "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://techcrunch.com/feed/"},
    {"id": 6045,"name": "The Verge",            "name_ar": "ذا فيرج",                 "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.theverge.com/rss/index.xml"},
    {"id": 6046,"name": "Ars Technica",         "name_ar": "أرس تكنيكا",              "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://feeds.arstechnica.com/arstechnica/index"},
    {"id": 6047,"name": "Nature News",          "name_ar": "مجلة نيتشر",              "country": "بريطانيا",        "type": "علمي",        "lang": "en", "url": "https://www.nature.com/nature.rss"},
    {"id": 6048,"name": "New Scientist",        "name_ar": "نيو ساينتيست",            "country": "بريطانيا",        "type": "علمي",        "lang": "en", "url": "https://www.newscientist.com/feed/home/?cmpid=RSS"},
    {"id": 6049,"name": "Scientific American",  "name_ar": "ساينتيفيك أمريكان",       "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.scientificamerican.com/feed/"},
    {"id": 6050,"name": "Space.com",            "name_ar": "سبيس دوت كوم",            "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.space.com/feeds/all"},

    # ══════════════════════════════════════════
    # القسم السابع: مصادر منطقة الشرق الأوسط وآسيا الوسطى (511-590)
    # ══════════════════════════════════════════

    # قنوات عربية فضائية
    {"id": 7001,"name": "Al Jazeera Arabic",    "name_ar": "الجزيرة",                 "country": "قطر",             "type": "تلفزيون",     "lang": "ar", "url": "https://www.aljazeera.net/aljazeerarss/a2/1/1/1"},
    {"id": 7002,"name": "Al Arabiya",           "name_ar": "العربية",                 "country": "السعودية",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.alarabiya.net/rss.xml"},
    {"id": 7003,"name": "Sky News Arabia",      "name_ar": "سكاي نيوز عربية",         "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.skynewsarabia.com/rss.xml"},
    {"id": 7004,"name": "BBC Arabic",           "name_ar": "بي بي سي عربي",           "country": "بريطانيا",        "type": "تلفزيون",     "lang": "ar", "url": "https://feeds.bbci.co.uk/arabic/rss.xml"},
    {"id": 7005,"name": "France 24 Arabic",     "name_ar": "فرانس 24 عربي",           "country": "فرنسا",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.france24.com/ar/rss"},
    {"id": 7006,"name": "Al Hurra",             "name_ar": "الحرة",                   "country": "أمريكا",          "type": "تلفزيون",     "lang": "ar", "url": "https://www.alhurra.com/api/zgqkrvqnlp/rss.xml"},
    {"id": 7007,"name": "Monte Carlo Doualiya", "name_ar": "مونت كارلو الدولية",      "country": "فرنسا",           "type": "راديو",       "lang": "ar", "url": "https://www.mc-doualiya.com/rss"},
    {"id": 7008,"name": "Orient News Syria",    "name_ar": "أورينت نيوز",             "country": "سوريا",           "type": "تلفزيون",     "lang": "ar", "url": "https://orient-news.net/rss"},
    {"id": 7009,"name": "Al Hadath",            "name_ar": "الحدث",                   "country": "السعودية",        "type": "تلفزيون",     "lang": "ar", "url": "https://www.alhadath.net/rss.xml"},
    {"id": 7010,"name": "Al Ghad TV",           "name_ar": "الغد",                    "country": "الإمارات",        "type": "تلفزيون",     "lang": "ar", "url": "https://alghad.tv/feed"},

    # وكالات أنباء عربية
    {"id": 7011,"name": "WAM UAE",              "name_ar": "وام الإمارات",            "country": "الإمارات",        "type": "وكالة أنباء", "lang": "ar", "url": "https://wam.ae/ar/rss"},
    {"id": 7012,"name": "Qatar News Agency",    "name_ar": "وكالة قنا",               "country": "قطر",             "type": "وكالة أنباء", "lang": "ar", "url": "https://www.qna.org.qa/rss"},
    {"id": 7013,"name": "KUNA Kuwait",          "name_ar": "وكالة كونا",              "country": "الكويت",          "type": "وكالة أنباء", "lang": "ar", "url": "https://www.kuna.net.kw/rss"},
    {"id": 7014,"name": "BNA Bahrain",          "name_ar": "وكالة أنباء البحرين",     "country": "البحرين",         "type": "وكالة أنباء", "lang": "ar", "url": "https://www.bna.bh/rss"},
    {"id": 7015,"name": "ONA Oman",             "name_ar": "وكالة الأنباء العُمانية", "country": "عُمان",           "type": "وكالة أنباء", "lang": "ar", "url": "https://omannews.gov.om/rss"},
    {"id": 7016,"name": "SPA Saudi",            "name_ar": "الوكالة السعودية",        "country": "السعودية",        "type": "وكالة أنباء", "lang": "ar", "url": "https://www.spa.gov.sa/rss"},
    {"id": 7017,"name": "Sana Syria",           "name_ar": "سانا السورية",            "country": "سوريا",           "type": "وكالة أنباء", "lang": "ar", "url": "https://sana.sy/ar/rss"},
    {"id": 7018,"name": "INA Iraq",             "name_ar": "وكالة الأنباء العراقية",  "country": "العراق",          "type": "وكالة أنباء", "lang": "ar", "url": "https://ina.iq/rss"},
    {"id": 7019,"name": "MENA Egypt",           "name_ar": "وكالة أنباء الشرق الأوسط","country": "مصر",            "type": "وكالة أنباء", "lang": "ar", "url": "https://www.mena.org.eg/rss"},
    {"id": 7020,"name": "MAP Maroc",            "name_ar": "وكالة المغرب العربي",     "country": "المغرب",          "type": "وكالة أنباء", "lang": "ar", "url": "https://www.mapnews.ma/rss"},

    # إيران وأفغانستان
    {"id": 7021,"name": "Mehr News Agency",     "name_ar": "وكالة مهر",               "country": "إيران",           "type": "وكالة أنباء", "lang": "en", "url": "https://en.mehrnews.com/rss"},
    {"id": 7022,"name": "ISNA Iran",            "name_ar": "إسنا",                    "country": "إيران",           "type": "وكالة أنباء", "lang": "fa", "url": "https://www.isna.ir/rss"},
    {"id": 7023,"name": "Tolo News Afghanistan","name_ar": "طلوع نيوز",               "country": "أفغانستان",       "type": "تلفزيون",     "lang": "en", "url": "https://tolonews.com/rss.xml"},
    {"id": 7024,"name": "Khaama Press Afghan",  "name_ar": "خامه برس",                "country": "أفغانستان",       "type": "رقمي",        "lang": "en", "url": "https://www.khaama.com/feed/"},

    # آسيا الوسطى إضافي
    {"id": 7025,"name": "Kabar Kyrgyzstan",     "name_ar": "كابار قيرغيزستان",        "country": "قيرغيزستان",      "type": "وكالة أنباء", "lang": "en", "url": "https://www.kabar.kg/rss"},
    {"id": 7026,"name": "Trend Azerbaijan",     "name_ar": "ترند أذربيجان",           "country": "أذربيجان",        "type": "وكالة أنباء", "lang": "en", "url": "https://en.trend.az/rss.xml"},
    {"id": 7027,"name": "Hurriyet Turkey",      "name_ar": "حرييت التركية",           "country": "تركيا",           "type": "صحيفة",       "lang": "tr", "url": "https://www.hurriyet.com.tr/rss/anasayfa"},
    {"id": 7028,"name": "Sabah Turkey",         "name_ar": "صباح التركية",            "country": "تركيا",           "type": "صحيفة",       "lang": "tr", "url": "https://www.sabah.com.tr/rss"},

    # إسرائيل إضافي
    {"id": 7029,"name": "Haaretz English",      "name_ar": "هآرتس",                   "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.haaretz.com/cmlink/1.628765"},
    {"id": 7030,"name": "The Times of Israel",  "name_ar": "تايمز أوف إسرائيل",      "country": "إسرائيل",         "type": "رقمي",        "lang": "en", "url": "https://www.timesofisrael.com/feed/"},
    {"id": 7031,"name": "Yedioth Ahronoth",     "name_ar": "يديعوت أحرونوت",          "country": "إسرائيل",         "type": "صحيفة",       "lang": "en", "url": "https://www.ynetnews.com/category/3082"},

    # جنوب شرق آسيا إضافي
    {"id": 7032,"name": "Nhan Dan Vietnam",     "name_ar": "نهان دان فيتنام",         "country": "فيتنام",          "type": "صحيفة",       "lang": "en", "url": "https://en.nhandan.vn/rss"},
    {"id": 7033,"name": "Viet Nam News",        "name_ar": "فيتنام نيوز",             "country": "فيتنام",          "type": "صحيفة",       "lang": "en", "url": "https://vietnamnews.vn/rss/home.rss"},
    {"id": 7034,"name": "Khmer Times Cambodia", "name_ar": "خمير تايمز كمبوديا",      "country": "كمبوديا",         "type": "صحيفة",       "lang": "en", "url": "https://www.khmertimeskh.com/feed/"},
    {"id": 7035,"name": "Vientiane Times Laos", "name_ar": "فيينتيان تايمز",          "country": "لاوس",            "type": "صحيفة",       "lang": "en", "url": "https://www.vientianetimes.org.la/feed/"},
    {"id": 7036,"name": "Brunei Times",         "name_ar": "بروناي تايمز",            "country": "بروناي",          "type": "صحيفة",       "lang": "en", "url": "https://brunei.fm/feed/"},

    # أمريكا الشمالية إضافي
    {"id": 7037,"name": "Montreal Gazette",     "name_ar": "مونتريال غازيت",          "country": "كندا",            "type": "صحيفة",       "lang": "en", "url": "https://montrealgazette.com/feed"},
    {"id": 7038,"name": "National Post Canada", "name_ar": "ناشيونال بوست",           "country": "كندا",            "type": "صحيفة",       "lang": "en", "url": "https://nationalpost.com/feed/"},
    {"id": 7039,"name": "Macleans Canada",      "name_ar": "ماكلينز كندا",            "country": "كندا",            "type": "مجلة",        "lang": "en", "url": "https://macleans.ca/feed/"},

    # أوروبا إضافي
    {"id": 7040,"name": "Euronews English",     "name_ar": "يورونيوز إنجليزي",        "country": "أوروبا",          "type": "تلفزيون",     "lang": "en", "url": "https://www.euronews.com/rss?format=mrss&level=theme&name=news"},
    {"id": 7041,"name": "Euronews Arabic",      "name_ar": "يورونيوز عربي",           "country": "أوروبا",          "type": "تلفزيون",     "lang": "ar", "url": "https://arabic.euronews.com/rss?format=mrss&level=theme&name=news"},
    {"id": 7042,"name": "EUobserver",           "name_ar": "إيو أوبزيرفر",            "country": "بلجيكا",          "type": "رقمي",        "lang": "en", "url": "https://euobserver.com/rss.xml"},
    {"id": 7043,"name": "Politico Europe",      "name_ar": "بوليتيكو أوروبا",         "country": "أوروبا",          "type": "رقمي",        "lang": "en", "url": "https://www.politico.eu/feed/"},
    {"id": 7044,"name": "Le Monde",             "name_ar": "لو موند",                 "country": "فرنسا",           "type": "صحيفة",       "lang": "fr", "url": "https://www.lemonde.fr/rss/une.xml"},
    {"id": 7045,"name": "Der Spiegel",          "name_ar": "دير شبيغل",               "country": "ألمانيا",         "type": "مجلة",        "lang": "de", "url": "https://www.spiegel.de/index.rss"},
    {"id": 7046,"name": "Repubblica Italy",     "name_ar": "لا ريبابليكا",            "country": "إيطاليا",         "type": "صحيفة",       "lang": "it", "url": "https://www.repubblica.it/rss/homepage/rss2.0.xml"},
    {"id": 7047,"name": "El Confidencial",      "name_ar": "إل كونفيدينسيال ع",       "country": "إسبانيا",         "type": "رقمي",        "lang": "es", "url": "https://rss.elconfidencial.com/espana/"},
    {"id": 7048,"name": "SRF Switzerland",      "name_ar": "إس آر إف سويسرا",         "country": "سويسرا",          "type": "تلفزيون",     "lang": "de", "url": "https://www.srf.ch/news/bnf/rss/1646"},
    {"id": 7049,"name": "NOS Netherlands",      "name_ar": "إن أو إس هولندا",         "country": "هولندا",          "type": "تلفزيون",     "lang": "nl", "url": "https://feeds.nos.nl/nosnieuwsalgemeen"},
    {"id": 7050,"name": "VRT News Belgium",     "name_ar": "في آر تي بلجيكا",         "country": "بلجيكا",          "type": "تلفزيون",     "lang": "nl", "url": "https://www.vrt.be/vrtnws/nl.rss.articles.xml"},

    # ══════════════════════════════════════════
    # القسم الثامن: مصادر متخصصة (591-690)
    # ══════════════════════════════════════════

    # اقتصاد وأعمال
    {"id": 8001,"name": "Reuters Business",     "name_ar": "رويترز الأعمال",          "country": "بريطانيا",        "type": "مالي",        "lang": "en", "url": "https://feeds.reuters.com/reuters/businessNews"},
    {"id": 8002,"name": "CNBC World",           "name_ar": "سي إن بي سي",             "country": "أمريكا",          "type": "مالي",        "lang": "en", "url": "https://www.cnbc.com/id/100727362/device/rss/rss.html"},
    {"id": 8003,"name": "MarketWatch",          "name_ar": "ماركت ووتش",              "country": "أمريكا",          "type": "مالي",        "lang": "en", "url": "https://feeds.marketwatch.com/marketwatch/topstories"},
    {"id": 8004,"name": "Investopedia",         "name_ar": "إنفيستوبيديا",            "country": "أمريكا",          "type": "مالي",        "lang": "en", "url": "https://www.investopedia.com/feeds/news.aspx"},
    {"id": 8005,"name": "Business Insider",     "name_ar": "بيزنس إنسايدر",           "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://feeds.businessinsider.com/custom/all"},
    {"id": 8006,"name": "Forbes",               "name_ar": "فوربس",                   "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.forbes.com/real-time/feed2/"},
    {"id": 8007,"name": "Fortune",              "name_ar": "فورتشون",                 "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://fortune.com/feed/"},
    {"id": 8008,"name": "Harvard Business Rev", "name_ar": "هارفارد بيزنس ريفيو",     "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://feeds.hbr.org/harvardbusiness"},
    {"id": 8009,"name": "Quartz",               "name_ar": "كوارتز",                  "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://qz.com/feed/"},
    {"id": 8010,"name": "The Economist Finance","name_ar": "الإيكونوميست مالية",       "country": "بريطانيا",        "type": "مالي",        "lang": "en", "url": "https://www.economist.com/finance-and-economics/rss.xml"},

    # علوم وتقنية
    {"id": 8011,"name": "IEEE Spectrum",        "name_ar": "آي إي إي إي سبيكتروم",   "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://spectrum.ieee.org/feeds/feed.rss"},
    {"id": 8012,"name": "Phys.org",             "name_ar": "فيز دوت أورغ",            "country": "بريطانيا",        "type": "علمي",        "lang": "en", "url": "https://phys.org/rss-feed/"},
    {"id": 8013,"name": "Live Science",         "name_ar": "لايف ساينس",              "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.livescience.com/feeds/all"},
    {"id": 8014,"name": "ZDNet",                "name_ar": "زد دي نت",                "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.zdnet.com/news/rss.xml"},
    {"id": 8015,"name": "Engadget",             "name_ar": "إنغادجيت",                "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.engadget.com/rss.xml"},
    {"id": 8016,"name": "Gizmodo",              "name_ar": "جيزمودو",                 "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://gizmodo.com/rss"},
    {"id": 8017,"name": "CNET",                 "name_ar": "سي نت",                   "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.cnet.com/rss/news/"},
    {"id": 8018,"name": "VentureBeat",          "name_ar": "فنتشر بيت",               "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://venturebeat.com/feed/"},
    {"id": 8019,"name": "Next Web",             "name_ar": "ذا نيكست ويب",            "country": "هولندا",          "type": "تقنية",       "lang": "en", "url": "https://thenextweb.com/feed/"},
    {"id": 8020,"name": "Mashable Tech",        "name_ar": "ماشابل",                  "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://mashable.com/feeds/rss/all"},

    # بيئة وصحة
    {"id": 8021,"name": "The Guardian Climate", "name_ar": "الغارديان المناخ",        "country": "بريطانيا",        "type": "بيئي",        "lang": "en", "url": "https://www.theguardian.com/environment/climate-change/rss"},
    {"id": 8022,"name": "Reuters Health",       "name_ar": "رويترز الصحة",            "country": "بريطانيا",        "type": "صحي",         "lang": "en", "url": "https://feeds.reuters.com/reuters/healthNews"},
    {"id": 8023,"name": "WHO News",             "name_ar": "منظمة الصحة العالمية",    "country": "سويسرا",          "type": "صحي",         "lang": "en", "url": "https://www.who.int/rss-feeds/news-english.xml"},
    {"id": 8024,"name": "Medical News Today",   "name_ar": "ميديكال نيوز توداي",      "country": "بريطانيا",        "type": "صحي",         "lang": "en", "url": "https://www.medicalnewstoday.com/rss"},
    {"id": 8025,"name": "Healthline",           "name_ar": "هيلث لاين",               "country": "أمريكا",          "type": "صحي",         "lang": "en", "url": "https://www.healthline.com/rss/news"},

    # رياضة
    {"id": 8026,"name": "ESPN",                 "name_ar": "إي إس بي إن",             "country": "أمريكا",          "type": "رياضة",       "lang": "en", "url": "https://www.espn.com/espn/rss/news"},
    {"id": 8027,"name": "BBC Sport",            "name_ar": "بي بي سي رياضة",          "country": "بريطانيا",        "type": "رياضة",       "lang": "en", "url": "https://feeds.bbci.co.uk/sport/rss.xml"},
    {"id": 8028,"name": "Sky Sports",           "name_ar": "سكاي سبورتس",             "country": "بريطانيا",        "type": "رياضة",       "lang": "en", "url": "https://www.skysports.com/rss/12040"},
    {"id": 8029,"name": "France Football",      "name_ar": "فرانس فوتبول",            "country": "فرنسا",           "type": "رياضة",       "lang": "fr", "url": "https://www.francefootball.fr/feed"},
    {"id": 8030,"name": "Goal.com",             "name_ar": "غول دوت كوم",             "country": "بريطانيا",        "type": "رياضة",       "lang": "en", "url": "https://www.goal.com/feeds/en/news"},

    # سياسة وعلاقات دولية
    {"id": 8031,"name": "Council on For Rel",   "name_ar": "مجلس العلاقات الخارجية",  "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://www.cfr.org/rss.xml"},
    {"id": 8032,"name": "Brookings Institute",  "name_ar": "معهد بروكينغز",           "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://www.brookings.edu/feed/"},
    {"id": 8033,"name": "Carnegie Endowment",   "name_ar": "مؤسسة كارنيغي",           "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://carnegieendowment.org/rss/solr/posts?q=*:*"},
    {"id": 8034,"name": "RAND Corporation",     "name_ar": "مؤسسة راند",              "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://www.rand.org/feed"},
    {"id": 8035,"name": "Chatham House",        "name_ar": "تشاتام هاوس",             "country": "بريطانيا",        "type": "سياسي",       "lang": "en", "url": "https://www.chathamhouse.org/rss.xml"},
    {"id": 8036,"name": "IISS",                 "name_ar": "المعهد الدولي للدراسات",  "country": "بريطانيا",        "type": "سياسي",       "lang": "en", "url": "https://www.iiss.org/rss"},
    {"id": 8037,"name": "Crisis Group",         "name_ar": "مجموعة الأزمات الدولية",  "country": "بلجيكا",          "type": "سياسي",       "lang": "en", "url": "https://www.crisisgroup.org/rss"},
    {"id": 8038,"name": "ECFR",                 "name_ar": "المجلس الأوروبي للعلاقات","country": "أوروبا",          "type": "سياسي",       "lang": "en", "url": "https://ecfr.eu/feed/"},
    {"id": 8039,"name": "SIPRI",                "name_ar": "معهد ستوكهولم للسلام",    "country": "السويد",          "type": "أمني",        "lang": "en", "url": "https://www.sipri.org/rss.xml"},
    {"id": 8040,"name": "Belfer Center",        "name_ar": "مركز بيلفر",              "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://www.belfercenter.org/feeds/content/rss"},

    # حقوق الإنسان والاستقصاء
    {"id": 8041,"name": "Human Rights Watch",   "name_ar": "هيومن رايتس ووتش",        "country": "أمريكا",          "type": "حقوقي",       "lang": "en", "url": "https://www.hrw.org/rss.xml"},
    {"id": 8042,"name": "Amnesty International","name_ar": "منظمة العفو الدولية",      "country": "بريطانيا",        "type": "حقوقي",       "lang": "en", "url": "https://www.amnesty.org/en/feed.xml"},
    {"id": 8043,"name": "RSF",                  "name_ar": "منظمة مراسلون بلا حدود",  "country": "فرنسا",           "type": "حقوقي",       "lang": "en", "url": "https://rsf.org/en/rss"},
    {"id": 8044,"name": "OCCRP",                "name_ar": "مشروع تقارير الجريمة",    "country": "هولندا",          "type": "استقصائي",    "lang": "en", "url": "https://www.occrp.org/en/rss"},
    {"id": 8045,"name": "Global Witness",       "name_ar": "غلوبال ويتنس",            "country": "بريطانيا",        "type": "استقصائي",    "lang": "en", "url": "https://www.globalwitness.org/en/feed/"},
    {"id": 8046,"name": "Bellingcat",           "name_ar": "بيلينغكات",               "country": "بريطانيا",        "type": "استقصائي",    "lang": "en", "url": "https://www.bellingcat.com/feed/"},
    {"id": 8047,"name": "The Bureau of Invest", "name_ar": "مكتب الصحافة الاستقصائية","country": "بريطانيا",        "type": "استقصائي",    "lang": "en", "url": "https://www.thebureauinvestigates.com/feed"},
    {"id": 8048,"name": "ICIJ",                 "name_ar": "الصحفيون الاستقصائيون",   "country": "أمريكا",          "type": "استقصائي",    "lang": "en", "url": "https://www.icij.org/feed/"},
    {"id": 8049,"name": "Open Democracy",       "name_ar": "الديمقراطية المفتوحة",    "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://www.opendemocracy.net/en/rss.xml"},
    {"id": 8050,"name": "Media Part France",    "name_ar": "ميديا بارت",              "country": "فرنسا",           "type": "استقصائي",    "lang": "fr", "url": "https://www.mediapart.fr/articles/feed"},

    # ══════════════════════════════════════════
    # القسم التاسع: مصادر إقليمية ومتخصصة (691-800)
    # ══════════════════════════════════════════

    # الشرق الأوسط - متخصص
    {"id": 9001,"name": "Al Sharq Al Awsat",    "name_ar": "الشرق الأوسط",            "country": "بريطانيا",        "type": "صحيفة",       "lang": "ar", "url": "https://aawsat.com/rss"},
    {"id": 9002,"name": "Arabi21",              "name_ar": "عربي 21",                 "country": "بريطانيا",        "type": "رقمي",        "lang": "ar", "url": "https://arabi21.com/rss"},
    {"id": 9003,"name": "Middle East Monitor",  "name_ar": "مجلة الشرق الأوسط",      "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://www.middleeastmonitor.com/feed/"},
    {"id": 9004,"name": "Arabia Inform",        "name_ar": "عربيا إنفورم",            "country": "أوروبا",          "type": "رقمي",        "lang": "ar", "url": "https://arabiainform.com/feed"},
    {"id": 9005,"name": "Al Quds Al Arabi",     "name_ar": "القدس العربي",            "country": "بريطانيا",        "type": "صحيفة",       "lang": "ar", "url": "https://www.alquds.co.uk/feed/"},
    {"id": 9006,"name": "Raialyoum",            "name_ar": "رأي اليوم",               "country": "بريطانيا",        "type": "رقمي",        "lang": "ar", "url": "https://www.raialyoum.com/feed/"},
    {"id": 9007,"name": "Anadolu Agency Arabic","name_ar": "الأناضول عربي",           "country": "تركيا",           "type": "وكالة أنباء", "lang": "ar", "url": "https://www.aa.com.tr/ar/rss"},
    {"id": 9008,"name": "Alaraby TV",           "name_ar": "العربي الجديد",           "country": "بريطانيا",        "type": "تلفزيون",     "lang": "ar", "url": "https://alaraby.co.uk/feed"},
    {"id": 9009,"name": "Megaphone Lebanon",    "name_ar": "ميغافون لبنان",           "country": "لبنان",           "type": "رقمي",        "lang": "ar", "url": "https://megaphone.com.lb/feed"},
    {"id": 9010,"name": "Daraja Press Sudan",   "name_ar": "درجة برس السودان",        "country": "السودان",         "type": "رقمي",        "lang": "ar", "url": "https://darajpress.com/feed"},

    # دول الخليج - متخصص
    {"id": 9011,"name": "Al Qabas Online",      "name_ar": "القبس الكويتية",          "country": "الكويت",          "type": "صحيفة",       "lang": "ar", "url": "https://alqabas.com/rss"},
    {"id": 9012,"name": "Al Watan Kuwait",      "name_ar": "الوطن الكويتية",          "country": "الكويت",          "type": "صحيفة",       "lang": "ar", "url": "https://alwatan.com.kw/rss"},
    {"id": 9013,"name": "Argaam Saudi",         "name_ar": "أرقام المالية",           "country": "السعودية",        "type": "مالي",        "lang": "ar", "url": "https://www.argaam.com/ar/rss"},
    {"id": 9014,"name": "Mubasher Finance",     "name_ar": "مباشر المالية",           "country": "الإمارات",        "type": "مالي",        "lang": "ar", "url": "https://www.mubasher.info/rss"},
    {"id": 9015,"name": "Al Borsah UAE",        "name_ar": "البورصة الإماراتية",       "country": "الإمارات",        "type": "مالي",        "lang": "ar", "url": "https://www.alborsah.ae/rss"},

    # أفريقيا - متخصص
    {"id": 9016,"name": "The Continent Africa", "name_ar": "ذا كونتيننت أفريقيا",    "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://thecontinent.org/feed/"},
    {"id": 9017,"name": "Quartz Africa",        "name_ar": "كوارتز أفريقيا",          "country": "أفريقيا",         "type": "رقمي",        "lang": "en", "url": "https://qz.com/africa/feed/"},
    {"id": 9018,"name": "Africa Confidential",  "name_ar": "أفريقيا كونفيدينشيال",   "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://www.africa-confidential.com/rss"},
    {"id": 9019,"name": "RFI Afrique",          "name_ar": "راديو فرنسا الدولي أفريقيا","country": "فرنسا",         "type": "راديو",       "lang": "fr", "url": "https://www.rfi.fr/afrique/rss"},
    {"id": 9020,"name": "BBC Africa",           "name_ar": "بي بي سي أفريقيا",       "country": "بريطانيا",        "type": "تلفزيون",     "lang": "en", "url": "https://feeds.bbci.co.uk/africa/rss.xml"},
    {"id": 9021,"name": "VOA Africa",           "name_ar": "صوت أمريكا أفريقيا",     "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://www.voanews.com/api/zkmqpteioq/rss.xml"},
    {"id": 9022,"name": "South Africa Dispatch","name_ar": "ذيسباتش جنوب أفريقيا",   "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://www.dailydispatch.co.za/feed/"},
    {"id": 9023,"name": "The Citizen SA",       "name_ar": "ذا سيتيزن SA",            "country": "جنوب أفريقيا",   "type": "رقمي",        "lang": "en", "url": "https://www.citizen.co.za/feed/"},
    {"id": 9024,"name": "Ethiopian Reporter",   "name_ar": "الريبورتر الإثيوبي",      "country": "إثيوبيا",         "type": "صحيفة",       "lang": "en", "url": "https://www.ethiopianreporter.com/feed"},
    {"id": 9025,"name": "Daily Monitor Uganda", "name_ar": "ديلي مونيتور أوغندا",    "country": "أوغندا",          "type": "صحيفة",       "lang": "en", "url": "https://www.monitor.co.ug/rss"},

    # آسيا - متخصص
    {"id": 9026,"name": "South Asian Monitor",  "name_ar": "ساوث آسيان مونيتور",      "country": "الهند",           "type": "رقمي",        "lang": "en", "url": "https://southasianmonitor.com/feed/"},
    {"id": 9027,"name": "ANI India",            "name_ar": "وكالة أخبار آسيا",        "country": "الهند",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.aninews.in/rss/world.rss"},
    {"id": 9028,"name": "Tribune Pakistan",     "name_ar": "تريبيون باكستان",         "country": "باكستان",         "type": "صحيفة",       "lang": "en", "url": "https://tribune.com.pk/feed"},
    {"id": 9029,"name": "Express Tribune PK",   "name_ar": "إكسبريس تريبيون",         "country": "باكستان",         "type": "صحيفة",       "lang": "en", "url": "https://tribune.com.pk/feed"},
    {"id": 9030,"name": "Ceylon Today SL",      "name_ar": "سيلون توداي",             "country": "سريلانكا",        "type": "صحيفة",       "lang": "en", "url": "https://ceylontoday.lk/feed/"},
    {"id": 9031,"name": "My Republica Nepal",   "name_ar": "ماي ريبابليكا نيبال",     "country": "نيبال",           "type": "صحيفة",       "lang": "en", "url": "https://myrepublica.nagariknetwork.com/feed"},
    {"id": 9032,"name": "The Daily Star BD",    "name_ar": "ديلي ستار بنغلاديش",      "country": "بنغلاديش",        "type": "صحيفة",       "lang": "en", "url": "https://www.thedailystar.net/rss"},
    {"id": 9033,"name": "Maldives Ind",         "name_ar": "المالديف إندبندنت",        "country": "المالديف",        "type": "رقمي",        "lang": "en", "url": "https://maldivesindependent.com/feed/"},
    {"id": 9034,"name": "Bhutan Broadcasting", "name_ar": "بهوتان برودكاستينغ",       "country": "بوتان",           "type": "تلفزيون",     "lang": "en", "url": "https://www.bbs.bt/news/?feed=rss2"},
    {"id": 9035,"name": "KBS Korea World",      "name_ar": "كي بي إس العالمي",        "country": "كوريا الجنوبية", "type": "راديو",       "lang": "en", "url": "https://world.kbs.co.kr/service/news_meta_view.htm?lang=e&type=rss&id=ne"},

    # أمريكا اللاتينية - متخصص
    {"id": 9036,"name": "Mercopress",           "name_ar": "ميركوبريس",              "country": "الأوروغواي",      "type": "رقمي",        "lang": "en", "url": "https://en.mercopress.com/rss"},
    {"id": 9037,"name": "InSight Crime",        "name_ar": "إنسايت كرايم",            "country": "كولومبيا",        "type": "استقصائي",    "lang": "en", "url": "https://insightcrime.org/feed/"},
    {"id": 9038,"name": "Americas Quarterly",   "name_ar": "أمريكاز كوارترلي",        "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://americasquarterly.org/feed"},
    {"id": 9039,"name": "El Espectador CO",     "name_ar": "إل إسبيكتادور",           "country": "كولومبيا",        "type": "صحيفة",       "lang": "es", "url": "https://www.elespectador.com/rss"},
    {"id": 9040,"name": "Peru Reports",         "name_ar": "بيرو ريبورتس",            "country": "بيرو",            "type": "رقمي",        "lang": "en", "url": "https://perureports.com/feed/"},
    {"id": 9041,"name": "Ecuador Immediato",    "name_ar": "إكوادور إيمدياتو",        "country": "الإكوادور",       "type": "رقمي",        "lang": "es", "url": "https://www.ecuadorinmediato.com/index.php?module=Noticias&func=news_list&format=rss"},
    {"id": 9042,"name": "El Mercurio Chile",    "name_ar": "إل ميركوريو تشيلي",       "country": "تشيلي",           "type": "صحيفة",       "lang": "es", "url": "https://digital.elmercurio.com/RSS"},
    {"id": 9043,"name": "El Deber Bolivia",     "name_ar": "إل ديبر بوليفيا",         "country": "بوليفيا",         "type": "صحيفة",       "lang": "es", "url": "https://eldeber.com.bo/feed/"},

    # أوروبا الشرقية - متخصص
    {"id": 9044,"name": "Euractiv",             "name_ar": "يوراكتيف",                "country": "بلجيكا",          "type": "رقمي",        "lang": "en", "url": "https://www.euractiv.com/feed/"},
    {"id": 9045,"name": "Warsaw Voice Poland",  "name_ar": "صوت وارسو",               "country": "بولندا",          "type": "صحيفة",       "lang": "en", "url": "https://www.warsawvoice.pl/WVPage/WVPAge.php/rss/"},
    {"id": 9046,"name": "Prague Morning CZ",    "name_ar": "براغ مورنينغ",             "country": "التشيك",          "type": "رقمي",        "lang": "en", "url": "https://www.praguemorning.cz/feed/"},
    {"id": 9047,"name": "Budapest Times HU",    "name_ar": "بودابست تايمز",           "country": "المجر",           "type": "صحيفة",       "lang": "en", "url": "https://www.budapesttimes.hu/feed/"},
    {"id": 9048,"name": "Tass Russia",          "name_ar": "تاس الروسية",             "country": "روسيا",           "type": "وكالة أنباء", "lang": "en", "url": "https://tass.com/rss/v2.xml"},
    {"id": 9049,"name": "Baltic Times",         "name_ar": "بالتيك تايمز",            "country": "لاتفيا",          "type": "صحيفة",       "lang": "en", "url": "https://www.baltictimes.com/rss/news/"},
    {"id": 9050,"name": "Emerging Europe",      "name_ar": "أوروبا الناشئة",          "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://emerging-europe.com/feed/"},

    # أوقيانوسيا
    {"id": 9051,"name": "Pacific Beat",         "name_ar": "باسيفيك بيت",             "country": "أستراليا",        "type": "راديو",       "lang": "en", "url": "https://www.abc.net.au/pacific-beat/rss"},
    {"id": 9052,"name": "Radio New Zealand",    "name_ar": "راديو نيوزيلندا الدولي",  "country": "نيوزيلندا",       "type": "راديو",       "lang": "en", "url": "https://www.rnz.co.nz/rss/pacific.xml"},
    {"id": 9053,"name": "PNG Post Courier",     "name_ar": "بوست كورييه PNG",          "country": "بابوا نيو غينيا","type": "صحيفة",       "lang": "en", "url": "https://postcourier.com.pg/feed/"},
    {"id": 9054,"name": "Fiji Times",           "name_ar": "فيجي تايمز",              "country": "فيجي",            "type": "صحيفة",       "lang": "en", "url": "https://www.fijitimes.com/feed/"},

    # متخصص - ذكاء اصطناعي وطاقة ومناخ
    {"id": 9055,"name": "AI News",              "name_ar": "أخبار الذكاء الاصطناعي",  "country": "بريطانيا",        "type": "تقنية",       "lang": "en", "url": "https://www.artificialintelligence-news.com/feed/"},
    {"id": 9056,"name": "MIT AI News",          "name_ar": "أخبار الذكاء MIT",         "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://news.mit.edu/rss/research"},
    {"id": 9057,"name": "Energy Monitor",       "name_ar": "إنرجي مونيتور",            "country": "بريطانيا",        "type": "بيئي",        "lang": "en", "url": "https://www.energymonitor.ai/feed/"},
    {"id": 9058,"name": "Climate Home News",    "name_ar": "كلايمت هوم نيوز",         "country": "بريطانيا",        "type": "بيئي",        "lang": "en", "url": "https://www.climatechangenews.com/feed/"},
    {"id": 9059,"name": "Carbon Brief",         "name_ar": "كاربون بريف",             "country": "بريطانيا",        "type": "بيئي",        "lang": "en", "url": "https://www.carbonbrief.org/feed/"},
    {"id": 9060,"name": "Wired Science",        "name_ar": "وايرد العلوم",             "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.wired.com/feed/category/science/latest/rss"},

    # إعلام المهجر العربي
    {"id": 9061,"name": "Elaph",                "name_ar": "إيلاف",                   "country": "بريطانيا",        "type": "رقمي",        "lang": "ar", "url": "https://elaph.com/rss.xml"},
    {"id": 9062,"name": "Al Moheet",            "name_ar": "المحيط",                  "country": "الإمارات",        "type": "رقمي",        "lang": "ar", "url": "https://almohit.com/rss"},
    {"id": 9063,"name": "Akhbar Al Arab",       "name_ar": "أخبار العرب",             "country": "الإمارات",        "type": "رقمي",        "lang": "ar", "url": "https://akhbararab.ae/feed"},
    {"id": 9064,"name": "Kull Al Arab",         "name_ar": "كل العرب",                "country": "الإمارات",        "type": "رقمي",        "lang": "ar", "url": "https://all4arab.net/feed/"},
    {"id": 9065,"name": "Noon Post",            "name_ar": "نون بوست",                "country": "قطر",             "type": "رقمي",        "lang": "ar", "url": "https://www.noonpost.com/feed/"},

    # مصادر متنوعة إضافية
    {"id": 9066,"name": "DW English",           "name_ar": "دويتشه فيله الإنجليزية",  "country": "ألمانيا",         "type": "تلفزيون",     "lang": "en", "url": "https://rss.dw.com/rdf/rss-en-world"},
    {"id": 9067,"name": "NHK World English",    "name_ar": "إن إتش كي الإنجليزية",    "country": "اليابان",         "type": "تلفزيون",     "lang": "en", "url": "https://www3.nhk.or.jp/nhkworld/en/news/feeds/"},
    {"id": 9068,"name": "Anadolu Agency EN",    "name_ar": "وكالة الأناضول الإنجليزية","country": "تركيا",          "type": "وكالة أنباء", "lang": "en", "url": "https://www.aa.com.tr/en/rss"},
    {"id": 9069,"name": "KUNA English",         "name_ar": "وكالة كونا الإنجليزية",   "country": "الكويت",          "type": "وكالة أنباء", "lang": "en", "url": "https://www.kuna.net.kw/rssFeeds.aspx?type=xml&category=1"},
    {"id": 9070,"name": "IPS News",             "name_ar": "وكالة إنتر برس سيرفيس",  "country": "روما",            "type": "وكالة أنباء", "lang": "en", "url": "https://www.ipsnews.net/feed/"},
    {"id": 9071,"name": "IRIN News",            "name_ar": "إيرين نيوز",              "country": "سويسرا",          "type": "إنساني",      "lang": "en", "url": "https://www.irinnews.org/feed"},
    {"id": 9072,"name": "ReliefWeb",            "name_ar": "ريليف ويب",               "country": "سويسرا",          "type": "إنساني",      "lang": "en", "url": "https://reliefweb.int/updates/rss.xml"},
    {"id": 9073,"name": "Al Araby English",     "name_ar": "العربي الجديد إنجليزي",   "country": "بريطانيا",        "type": "رقمي",        "lang": "en", "url": "https://english.alaraby.co.uk/feed"},
    {"id": 9074,"name": "Now Lebanon",          "name_ar": "ناو لبنان",               "country": "لبنان",           "type": "رقمي",        "lang": "en", "url": "https://www.nowlebanon.com/feed/"},
    {"id": 9075,"name": "Arab Weekly",          "name_ar": "العرب ويكلي",             "country": "بريطانيا",        "type": "صحيفة",       "lang": "en", "url": "https://thearabweekly.com/feed"},

    # صحافة مستقلة متنوعة
    {"id": 9076,"name": "The Conversation",     "name_ar": "ذا كونفرسيشن",            "country": "أستراليا",        "type": "أكاديمي",     "lang": "en", "url": "https://theconversation.com/articles.atom"},
    {"id": 9077,"name": "The Wire Science",     "name_ar": "ذا واير العلوم",          "country": "الهند",           "type": "علمي",        "lang": "en", "url": "https://science.thewire.in/feed/"},
    {"id": 9078,"name": "Nikkei Asia Pacific",  "name_ar": "نيكاي آسيا باسيفيك",     "country": "اليابان",         "type": "مالي",        "lang": "en", "url": "https://asia.nikkei.com/rss/feed/nar"},
    {"id": 9079,"name": "Reuters Africa",       "name_ar": "رويترز أفريقيا",          "country": "بريطانيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.reuters.com/reuters/AFRICANews"},
    {"id": 9080,"name": "Reuters Americas",     "name_ar": "رويترز الأمريكتان",       "country": "بريطانيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.reuters.com/reuters/AMERICASNews"},
    {"id": 9081,"name": "Reuters Asia",         "name_ar": "رويترز آسيا",             "country": "بريطانيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.reuters.com/reuters/ScienceNews"},
    {"id": 9082,"name": "The Review of Religions","name_ar": "مراجعة الأديان",        "country": "بريطانيا",        "type": "ديني",        "lang": "en", "url": "https://www.reviewofreligions.org/feed/"},
    {"id": 9083,"name": "Pew Research",         "name_ar": "مركز بيو للأبحاث",        "country": "أمريكا",          "type": "أبحاث",       "lang": "en", "url": "https://www.pewresearch.org/feed/"},
    {"id": 9084,"name": "Gallup News",          "name_ar": "مركز غالوب",              "country": "أمريكا",          "type": "أبحاث",       "lang": "en", "url": "https://news.gallup.com/rss.aspx"},
    {"id": 9085,"name": "UN News",              "name_ar": "أخبار الأمم المتحدة",     "country": "سويسرا",          "type": "رسمي",        "lang": "en", "url": "https://news.un.org/feed/subscribe/en/news/all/rss.xml"},

    # المزيد من المصادر العالمية
    {"id": 9086,"name": "Alwaght Iran",         "name_ar": "الوقت الإيرانية",         "country": "إيران",           "type": "رقمي",        "lang": "ar", "url": "https://alwaght.com/ar/rss"},
    {"id": 9087,"name": "Sputnik Arabic",       "name_ar": "سبوتنيك عربي",           "country": "روسيا",           "type": "وكالة أنباء", "lang": "ar", "url": "https://arabic.sputniknews.com/export/rss2/archive/index.xml"},
    {"id": 9088,"name": "China Daily English",  "name_ar": "الصين ديلي",              "country": "الصين",           "type": "صحيفة",       "lang": "en", "url": "https://www.chinadaily.com.cn/rss/china_rss.xml"},
    {"id": 9089,"name": "People's Daily China", "name_ar": "بيبلز ديلي",              "country": "الصين",           "type": "صحيفة",       "lang": "en", "url": "https://en.people.cn/rss/90001.xml"},
    {"id": 9090,"name": "The Moscow Times",     "name_ar": "موسكو تايمز",             "country": "روسيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.themoscowtimes.com/rss/news"},

    # صحافة بيانات ومتابعة
    {"id": 9091,"name": "FiveThirtyEight",      "name_ar": "فايف ثيرتي إيت",          "country": "أمريكا",          "type": "بيانات",      "lang": "en", "url": "https://fivethirtyeight.com/features/feed"},
    {"id": 9092,"name": "Our World in Data",    "name_ar": "عالمنا بالأرقام",         "country": "بريطانيا",        "type": "بيانات",      "lang": "en", "url": "https://ourworldindata.org/atom.xml"},
    {"id": 9093,"name": "Statista News",        "name_ar": "ستاتيستا نيوز",           "country": "ألمانيا",         "type": "بيانات",      "lang": "en", "url": "https://www.statista.com/page/rss"},
    {"id": 9094,"name": "DW Arabic",            "name_ar": "دويتشه فيله عربي",        "country": "ألمانيا",         "type": "تلفزيون",     "lang": "ar", "url": "https://rss.dw.com/rdf/rss-ar-top"},
    {"id": 9095,"name": "RT Arabic",            "name_ar": "آر تي عربي",              "country": "روسيا",           "type": "تلفزيون",     "lang": "ar", "url": "https://arabic.rt.com/rss/"},
    {"id": 9096,"name": "China Radio Int Arabic","name_ar": "راديو الصين الدولي",      "country": "الصين",           "type": "راديو",       "lang": "ar", "url": "https://arabic.cri.cn/rss_ara_newschina.xml"},
    {"id": 9097,"name": "Sputnik Türkçe",       "name_ar": "سبوتنيك التركية",         "country": "روسيا",           "type": "وكالة أنباء", "lang": "tr", "url": "https://tr.sputniknews.com/export/rss2/archive/index.xml"},
    {"id": 9098,"name": "TRT Arabî",            "name_ar": "تي آر تي عربي",           "country": "تركيا",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.trtarabi.com/rss"},
    {"id": 9099,"name": "CGTN Arabic",          "name_ar": "سي جي تي إن عربي",        "country": "الصين",           "type": "تلفزيون",     "lang": "ar", "url": "https://arabic.cgtn.com/rss"},
    {"id": 9100,"name": "NHK World Arabic",     "name_ar": "NHK عربي",                "country": "اليابان",         "type": "تلفزيون",     "lang": "ar", "url": "https://www3.nhk.or.jp/nhkworld/arabic/news/feeds/"},

    # ══════════════════════════════════════════
    # القسم العاشر: مصادر تكميلية (801-980)
    # ══════════════════════════════════════════

    # أمريكا - إضافي
    {"id": 10001,"name": "NPR Politics",        "name_ar": "إن بي آر سياسة",          "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://feeds.npr.org/1014/rss.xml"},
    {"id": 10002,"name": "NPR World",           "name_ar": "إن بي آر عالم",           "country": "أمريكا",          "type": "راديو",       "lang": "en", "url": "https://feeds.npr.org/1004/rss.xml"},
    {"id": 10003,"name": "AP Sports",           "name_ar": "أسوشيتد برس رياضة",       "country": "أمريكا",          "type": "رياضة",       "lang": "en", "url": "https://feeds.apnews.com/rss/apf-sports"},
    {"id": 10004,"name": "AP Entertainment",    "name_ar": "أسوشيتد برس ترفيه",       "country": "أمريكا",          "type": "ترفيه",       "lang": "en", "url": "https://feeds.apnews.com/rss/apf-entertainment"},
    {"id": 10005,"name": "AP Politics",         "name_ar": "أسوشيتد برس سياسة",       "country": "أمريكا",          "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.apnews.com/rss/apf-politics"},
    {"id": 10006,"name": "Politico Defense",    "name_ar": "بوليتيكو دفاع",           "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://www.politico.com/rss/defense.xml"},
    {"id": 10007,"name": "Defense One",         "name_ar": "ديفنس ون",                "country": "أمريكا",          "type": "أمني",        "lang": "en", "url": "https://www.defenseone.com/rss/all/"},
    {"id": 10008,"name": "Breaking Defense",    "name_ar": "بريكينغ ديفنس",           "country": "أمريكا",          "type": "أمني",        "lang": "en", "url": "https://breakingdefense.com/feed/"},
    {"id": 10009,"name": "Stratfor",            "name_ar": "ستراتفور",                "country": "أمريكا",          "type": "سياسي",       "lang": "en", "url": "https://worldview.stratfor.com/article/recent.xml"},
    {"id": 10010,"name": "Just Security",       "name_ar": "جاست سيكيوريتي",          "country": "أمريكا",          "type": "أمني",        "lang": "en", "url": "https://www.justsecurity.org/feed/"},

    # بريطانيا - إضافي
    {"id": 10011,"name": "The Week UK",         "name_ar": "ذا ويك UK",               "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.theweek.co.uk/rss"},
    {"id": 10012,"name": "Prospect Magazine",   "name_ar": "بروسبيكت ماغازين",        "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.prospectmagazine.co.uk/feed"},
    {"id": 10013,"name": "London Review Books", "name_ar": "لندن ريفيو أوف بوكس",     "country": "بريطانيا",        "type": "مجلة",        "lang": "en", "url": "https://www.lrb.co.uk/feeds/articles"},
    {"id": 10014,"name": "Reuters UK",          "name_ar": "رويترز بريطانيا",         "country": "بريطانيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.reuters.com/reuters/UKdomesticNews"},
    {"id": 10015,"name": "BBC Tech",            "name_ar": "بي بي سي تقنية",          "country": "بريطانيا",        "type": "تقنية",       "lang": "en", "url": "https://feeds.bbci.co.uk/news/technology/rss.xml"},
    {"id": 10016,"name": "BBC Science",         "name_ar": "بي بي سي علوم",           "country": "بريطانيا",        "type": "علمي",        "lang": "en", "url": "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml"},
    {"id": 10017,"name": "BBC Politics UK",     "name_ar": "بي بي سي سياسة",          "country": "بريطانيا",        "type": "سياسي",       "lang": "en", "url": "https://feeds.bbci.co.uk/news/politics/rss.xml"},
    {"id": 10018,"name": "BBC Business",        "name_ar": "بي بي سي أعمال",          "country": "بريطانيا",        "type": "مالي",        "lang": "en", "url": "https://feeds.bbci.co.uk/news/business/rss.xml"},

    # أوروبا - إضافي
    {"id": 10019,"name": "ANSA English Italy",  "name_ar": "أنسا الإنجليزية",         "country": "إيطاليا",         "type": "وكالة أنباء", "lang": "en", "url": "https://www.ansa.it/sito/notizie/mondo/mondo_rss.xml"},
    {"id": 10020,"name": "Euronews Tech",       "name_ar": "يورونيوز تقنية",          "country": "أوروبا",          "type": "تقنية",       "lang": "en", "url": "https://www.euronews.com/rss?format=mrss&level=theme&name=news"},
    {"id": 10021,"name": "EFE English",         "name_ar": "وكالة إيفي إنجليزية",     "country": "إسبانيا",         "type": "وكالة أنباء", "lang": "en", "url": "https://www.efe.com/efe/english/1/rss"},
    {"id": 10022,"name": "AFP English",         "name_ar": "فرانس برس إنجليزي",       "country": "فرنسا",           "type": "وكالة أنباء", "lang": "en", "url": "https://www.afp.com/en/agencies/world/rss"},
    {"id": 10023,"name": "Swissinfo",           "name_ar": "سويس إنفو",               "country": "سويسرا",          "type": "رقمي",        "lang": "en", "url": "https://www.swissinfo.ch/eng/rss.xml"},
    {"id": 10024,"name": "Balkan Insight",      "name_ar": "بالكان إنسايت",           "country": "صربيا",           "type": "رقمي",        "lang": "en", "url": "https://balkaninsight.com/feed/"},
    {"id": 10025,"name": "Osservatorio Balcani","name_ar": "مرصد البلقان",             "country": "إيطاليا",         "type": "رقمي",        "lang": "en", "url": "https://www.balcanicaucaso.org/rss"},

    # دول عربية - قنوات وإذاعات
    {"id": 10026,"name": "Al Manar Lebanon",    "name_ar": "المنار",                  "country": "لبنان",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.almanar.com.lb/rss.xml"},
    {"id": 10027,"name": "OTV Lebanon",         "name_ar": "أو تي في لبنان",          "country": "لبنان",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.otv.com.lb/rss"},
    {"id": 10028,"name": "Al Mayadeen",         "name_ar": "الميادين",                "country": "لبنان",           "type": "تلفزيون",     "lang": "ar", "url": "https://www.almayadeen.net/rss"},
    {"id": 10029,"name": "Al Masdar News",      "name_ar": "المصدر نيوز",             "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.almasdarnews.com/feed/"},
    {"id": 10030,"name": "Egyptian Streets",    "name_ar": "الشوارع المصرية",         "country": "مصر",             "type": "رقمي",        "lang": "en", "url": "https://egyptianstreets.com/feed/"},
    {"id": 10031,"name": "Egypt Independent",   "name_ar": "مصر المستقل",             "country": "مصر",             "type": "رقمي",        "lang": "en", "url": "https://egyptindependent.com/feed/"},
    {"id": 10032,"name": "Libya Herald",        "name_ar": "ليبيا هيرالد",            "country": "ليبيا",           "type": "رقمي",        "lang": "en", "url": "https://www.libyaherald.com/feed/"},
    {"id": 10033,"name": "Tunisia Live",        "name_ar": "تونس لايف",               "country": "تونس",            "type": "رقمي",        "lang": "en", "url": "https://www.tunisia-live.net/feed/"},
    {"id": 10034,"name": "Morocco World News",  "name_ar": "مغرب وورلد نيوز",         "country": "المغرب",          "type": "رقمي",        "lang": "en", "url": "https://www.moroccoworldnews.com/feed/"},
    {"id": 10035,"name": "Algeria Press Service","name_ar": "وكالة الأنباء الجزائرية","country": "الجزائر",         "type": "وكالة أنباء", "lang": "en", "url": "https://www.aps.dz/en/rss"},

    # رياضة - متخصص
    {"id": 10036,"name": "Reuters Sport",       "name_ar": "رويترز رياضة",            "country": "بريطانيا",        "type": "رياضة",       "lang": "en", "url": "https://feeds.reuters.com/reuters/sportsNews"},
    {"id": 10037,"name": "AP Sports Feed",      "name_ar": "أسوشيتد برس رياضة",       "country": "أمريكا",          "type": "رياضة",       "lang": "en", "url": "https://feeds.apnews.com/rss/apf-sports"},
    {"id": 10038,"name": "Sport24",             "name_ar": "سبورت 24",                "country": "فرنسا",           "type": "رياضة",       "lang": "fr", "url": "https://www.sport24.lefigaro.fr/rss/sport24.xml"},
    {"id": 10039,"name": "Marca Spain",         "name_ar": "ماركا",                   "country": "إسبانيا",         "type": "رياضة",       "lang": "es", "url": "https://www.marca.com/rss/portada.xml"},
    {"id": 10040,"name": "AS Spain",            "name_ar": "أي إس",                   "country": "إسبانيا",         "type": "رياضة",       "lang": "es", "url": "https://as.com/rss/tags/ultimas_noticias.xml"},
    {"id": 10041,"name": "Kooora",              "name_ar": "كووورة",                  "country": "السعودية",        "type": "رياضة",       "lang": "ar", "url": "https://www.kooora.com/?rss"},
    {"id": 10042,"name": "FilGoal",             "name_ar": "فيل جول",                 "country": "مصر",             "type": "رياضة",       "lang": "ar", "url": "https://www.filgoal.com/rss"},
    {"id": 10043,"name": "Yalla Shoot",         "name_ar": "يلا شوت",                 "country": "مصر",             "type": "رياضة",       "lang": "ar", "url": "https://www.yallashoot.net/rss"},

    # آسيا الشرقية - إضافي
    {"id": 10044,"name": "Xinhua Arabic",       "name_ar": "شينخوا عربي",             "country": "الصين",           "type": "وكالة أنباء", "lang": "ar", "url": "https://arabic.news.cn/rss/world.xml"},
    {"id": 10045,"name": "CGTN Documentary",    "name_ar": "سي جي تي إن وثائقي",      "country": "الصين",           "type": "تلفزيون",     "lang": "en", "url": "https://www.cgtn.com/subscribe/rss/section/world.do"},
    {"id": 10046,"name": "Straits Times Tech",  "name_ar": "ستريتس تايمز تقنية",      "country": "سنغافورة",        "type": "تقنية",       "lang": "en", "url": "https://www.straitstimes.com/news/tech/rss.xml"},
    {"id": 10047,"name": "Nikkei Business",     "name_ar": "نيكاي أعمال",             "country": "اليابان",         "type": "مالي",        "lang": "en", "url": "https://www.nikkei.com/rss/business.xml"},
    {"id": 10048,"name": "Korea Pro",           "name_ar": "كوريا برو",               "country": "كوريا الجنوبية", "type": "صحيفة",       "lang": "en", "url": "https://koreaproreport.com/feed/"},
    {"id": 10049,"name": "Taiwan News",         "name_ar": "تايوان نيوز",             "country": "تايوان",          "type": "صحيفة",       "lang": "en", "url": "https://www.taiwannews.com.tw/rss"},
    {"id": 10050,"name": "Hong Kong Free Press","name_ar": "الصحافة الحرة هونغ كونغ", "country": "هونغ كونغ",       "type": "رقمي",        "lang": "en", "url": "https://hongkongfp.com/feed/"},

    # جنوب آسيا - إضافي
    {"id": 10051,"name": "Indian Express",      "name_ar": "الإندين إكسبريس",         "country": "الهند",           "type": "صحيفة",       "lang": "en", "url": "https://indianexpress.com/section/world/feed/"},
    {"id": 10052,"name": "Hindustan Times",     "name_ar": "هندوستان تايمز",          "country": "الهند",           "type": "صحيفة",       "lang": "en", "url": "https://www.hindustantimes.com/feeds/rss/world/rssfeed.xml"},
    {"id": 10053,"name": "WION India",          "name_ar": "وايون الهند",              "country": "الهند",           "type": "تلفزيون",     "lang": "en", "url": "https://www.wionews.com/feeds/all-news.xml"},
    {"id": 10054,"name": "Business Standard IN","name_ar": "بيزنس ستاندرد الهند",     "country": "الهند",           "type": "مالي",        "lang": "en", "url": "https://www.business-standard.com/rss/latest.rss"},
    {"id": 10055,"name": "Economic Times India","name_ar": "الإيكونوميك تايمز الهند", "country": "الهند",           "type": "مالي",        "lang": "en", "url": "https://economictimes.indiatimes.com/rssfeedsdefault.cms"},
    {"id": 10056,"name": "The Nation Pakistan", "name_ar": "ذا نيشن باكستان",         "country": "باكستان",         "type": "صحيفة",       "lang": "en", "url": "https://nation.com.pk/rss/home"},
    {"id": 10057,"name": "Daily Jang Urdu",     "name_ar": "جنگ الأردو",               "country": "باكستان",         "type": "صحيفة",       "lang": "ur", "url": "https://jang.com.pk/rss"},
    {"id": 10058,"name": "ARY News Pakistan",   "name_ar": "إيه آر واي باكستان",      "country": "باكستان",         "type": "تلفزيون",     "lang": "en", "url": "https://arynews.tv/en/feed/"},

    # أفريقيا - إضافي
    {"id": 10059,"name": "Standard Media Kenya","name_ar": "ستاندرد ميديا كينيا",     "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.standardmedia.co.ke/rss"},
    {"id": 10060,"name": "Tuko Kenya",          "name_ar": "توكو كينيا",              "country": "كينيا",           "type": "رقمي",        "lang": "en", "url": "https://www.tuko.co.ke/rss"},
    {"id": 10061,"name": "The Star Kenya",      "name_ar": "ذا ستار كينيا",           "country": "كينيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.the-star.co.ke/rss"},
    {"id": 10062,"name": "Business Day Nigeria","name_ar": "بيزنس داي نيجيريا",       "country": "نيجيريا",         "type": "مالي",        "lang": "en", "url": "https://businessday.ng/feed/"},
    {"id": 10063,"name": "The Punch Nigeria",   "name_ar": "بنش نيجيريا",             "country": "نيجيريا",         "type": "صحيفة",       "lang": "en", "url": "https://punchng.com/feed/"},
    {"id": 10064,"name": "Zimbabwe Herald",     "name_ar": "زيمبابوي هيرالد",         "country": "زيمبابوي",        "type": "صحيفة",       "lang": "en", "url": "https://www.herald.co.zw/feed/"},
    {"id": 10065,"name": "Zambia Daily Mail",   "name_ar": "ديلي ميل زامبيا",         "country": "زامبيا",          "type": "صحيفة",       "lang": "en", "url": "https://www.daily-mail.co.zm/feed/"},
    {"id": 10066,"name": "Botswana Guardian",   "name_ar": "بوتسوانا غارديان",        "country": "بوتسوانا",        "type": "صحيفة",       "lang": "en", "url": "https://www.botswanaguardian.co.bw/feed/"},
    {"id": 10067,"name": "Namibian Newspaper",  "name_ar": "ذا ناميبيان",             "country": "ناميبيا",         "type": "صحيفة",       "lang": "en", "url": "https://www.namibian.com.na/feed/"},
    {"id": 10068,"name": "Times of Zambia",     "name_ar": "تايمز أوف زامبيا",        "country": "زامبيا",          "type": "صحيفة",       "lang": "en", "url": "https://www.times.co.zm/feed/"},
    {"id": 10069,"name": "Mail Online Malawi",  "name_ar": "ميل أونلاين ملاوي",       "country": "ملاوي",           "type": "صحيفة",       "lang": "en", "url": "https://www.malawianews.com/feed/"},
    {"id": 10070,"name": "Africa News",         "name_ar": "أفريقيا نيوز",            "country": "أفريقيا",         "type": "رقمي",        "lang": "en", "url": "https://www.africanews.com/feed/rss"},

    # أمريكا اللاتينية - إضافي
    {"id": 10071,"name": "Telesur English",     "name_ar": "تيليسور الإنجليزية",      "country": "فنزويلا",         "type": "تلفزيون",     "lang": "en", "url": "https://telesurenglish.net/rss"},
    {"id": 10072,"name": "Latin America Report","name_ar": "تقرير أمريكا اللاتينية",  "country": "أمريكا",          "type": "رقمي",        "lang": "en", "url": "https://www.latinnews.com/rss/"},
    {"id": 10073,"name": "Buenos Aires Times",  "name_ar": "بيونس آيريس تايمز",       "country": "الأرجنتين",       "type": "صحيفة",       "lang": "en", "url": "https://www.batimes.com.ar/feed"},
    {"id": 10074,"name": "Brazil247",           "name_ar": "برازيل 247",              "country": "البرازيل",        "type": "رقمي",        "lang": "pt", "url": "https://www.brasil247.com/rss"},
    {"id": 10075,"name": "Nexo Jornal Brazil",  "name_ar": "نيكسو البرازيل",          "country": "البرازيل",        "type": "رقمي",        "lang": "pt", "url": "https://nexojornal.com.br/feed/"},
    {"id": 10076,"name": "El Mostrador Chile",  "name_ar": "إل موستردور تشيلي",       "country": "تشيلي",           "type": "رقمي",        "lang": "es", "url": "https://www.elmostrador.cl/feed/"},
    {"id": 10077,"name": "Caretas Peru",        "name_ar": "كاريتاس بيرو",            "country": "بيرو",            "type": "مجلة",        "lang": "es", "url": "https://caretas.pe/feed/"},
    {"id": 10078,"name": "La Prensa Bolivia",   "name_ar": "لا برينسا بوليفيا",       "country": "بوليفيا",         "type": "صحيفة",       "lang": "es", "url": "https://www.laprensa.com.bo/feed"},
    {"id": 10079,"name": "Prensa Libre Guatemala","name_ar": "برينسا ليبري غواتيمالا","country": "غواتيمالا",        "type": "صحيفة",       "lang": "es", "url": "https://www.prensalibre.com/feed/"},
    {"id": 10080,"name": "El Universal México2","name_ar": "إل أونيفرسال مكسيكو",     "country": "المكسيك",         "type": "صحيفة",       "lang": "es", "url": "https://www.eluniversal.com.mx/rss.xml"},

    # أوروبا الشرقية - إضافي
    {"id": 10081,"name": "TVN24 Poland",        "name_ar": "تي في إن 24 بولندا",      "country": "بولندا",          "type": "تلفزيون",     "lang": "pl", "url": "https://tvn24.pl/najnowsze.xml"},
    {"id": 10082,"name": "Gazeta PL",           "name_ar": "غازيتا بولندا",           "country": "بولندا",          "type": "صحيفة",       "lang": "pl", "url": "https://wyborcza.pl/rss/polityka.xml"},
    {"id": 10083,"name": "Czech Radio",         "name_ar": "راديو التشيك",            "country": "التشيك",          "type": "راديو",       "lang": "en", "url": "https://english.radio.cz/export/rss/all"},
    {"id": 10084,"name": "TASR Slovakia",       "name_ar": "وكالة تاسر سلوفاكيا",    "country": "سلوفاكيا",        "type": "وكالة أنباء", "lang": "en", "url": "https://www.tasr.sk/rss/english"},
    {"id": 10085,"name": "Hina Croatia",        "name_ar": "وكالة هينا كرواتيا",      "country": "كرواتيا",         "type": "وكالة أنباء", "lang": "en", "url": "https://www.hina.hr/en/rss"},
    {"id": 10086,"name": "SEA Monitor",         "name_ar": "مرصد جنوب شرق أوروبا",   "country": "إيطاليا",         "type": "رقمي",        "lang": "en", "url": "https://www.seaesmonitor.eu/feed/"},
    {"id": 10087,"name": "Moscow Times Russia", "name_ar": "موسكو تايمز روسيا",       "country": "روسيا",           "type": "صحيفة",       "lang": "en", "url": "https://www.themoscowtimes.com/rss/news"},
    {"id": 10088,"name": "Kyiv Post Ukraine",   "name_ar": "كييف بوست أوكرانيا",      "country": "أوكرانيا",        "type": "صحيفة",       "lang": "en", "url": "https://kyivpost.com/rss"},

    # علوم وتقنية - إضافي
    {"id": 10089,"name": "ScienceDaily",        "name_ar": "ساينس ديلي",              "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.sciencedaily.com/rss/all.xml"},
    {"id": 10090,"name": "Popular Science",     "name_ar": "بوبيولار ساينس",          "country": "أمريكا",          "type": "علمي",        "lang": "en", "url": "https://www.popsci.com/feed/"},
    {"id": 10091,"name": "Popular Mechanics",   "name_ar": "بوبيولار ميكانيكس",       "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.popularmechanics.com/feed/all"},
    {"id": 10092,"name": "Digital Trends",      "name_ar": "ديجيتال ترندز",           "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.digitaltrends.com/feed/"},
    {"id": 10093,"name": "9to5Mac",             "name_ar": "9 تو 5 ماك",              "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://9to5mac.com/feed/"},
    {"id": 10094,"name": "9to5Google",          "name_ar": "9 تو 5 غوغل",             "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://9to5google.com/feed/"},
    {"id": 10095,"name": "Android Authority",   "name_ar": "أندرويد أوثوريتي",        "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.androidauthority.com/feed/"},
    {"id": 10096,"name": "Tom's Hardware",      "name_ar": "توم هاردوير",             "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.tomshardware.com/feeds/all"},
    {"id": 10097,"name": "Techradar",           "name_ar": "تيك رادار",               "country": "بريطانيا",        "type": "تقنية",       "lang": "en", "url": "https://www.techradar.com/rss"},
    {"id": 10098,"name": "Protocol Tech",       "name_ar": "بروتوكول تك",             "country": "أمريكا",          "type": "تقنية",       "lang": "en", "url": "https://www.protocol.com/feeds/feed.rss"},

    # اقتصاد عربي
    {"id": 10099,"name": "Al Arabiya Business", "name_ar": "العربية الأعمال",         "country": "السعودية",        "type": "مالي",        "lang": "ar", "url": "https://www.alarabiya.net/business/rss.xml"},
    {"id": 10100,"name": "Al Jazeera Economy",  "name_ar": "الجزيرة الاقتصادية",     "country": "قطر",             "type": "مالي",        "lang": "ar", "url": "https://www.aljazeera.net/aljazeerarss/a2/4/1/1"},
    {"id": 10101,"name": "Asharq Business",     "name_ar": "الشرق للأعمال",          "country": "السعودية",        "type": "مالي",        "lang": "ar", "url": "https://www.bloomberg.com/feeds/arabic/business.rss"},
    {"id": 10102,"name": "Al Borsa Egypt",      "name_ar": "البورصة المصرية",         "country": "مصر",             "type": "مالي",        "lang": "ar", "url": "https://www.alborsanews.com/feed"},
    {"id": 10103,"name": "Amwal Al Ghad",       "name_ar": "أموال الغد",              "country": "مصر",             "type": "مالي",        "lang": "ar", "url": "https://amwalalghad.com/feed"},
    {"id": 10104,"name": "Mshaar Saudi",        "name_ar": "مشار السعودية",           "country": "السعودية",        "type": "مالي",        "lang": "ar", "url": "https://www.msharr.com/feed"},
    {"id": 10105,"name": "Aswaaq UAE",          "name_ar": "أسواق الإمارات",          "country": "الإمارات",        "type": "مالي",        "lang": "ar", "url": "https://www.aswaaq.com/feed"},

    # مصادر إخبارية عالمية متنوعة
    {"id": 10106,"name": "VOA Russian",         "name_ar": "صوت أمريكا الروسية",      "country": "أمريكا",          "type": "راديو",       "lang": "ru", "url": "https://www.golosameriki.com/api/zqmqmtqmqm/rss.xml"},
    {"id": 10107,"name": "RFE/RL Russian",      "name_ar": "راديو أوروبا الحرة روسي", "country": "أمريكا",          "type": "راديو",       "lang": "ru", "url": "https://www.rferl.org/z/631.xml"},
    {"id": 10108,"name": "VOA Persian",         "name_ar": "صوت أمريكا الفارسية",     "country": "أمريكا",          "type": "راديو",       "lang": "fa", "url": "https://ir.voanews.com/api/zymqpteioq/rss.xml"},
    {"id": 10109,"name": "VOA Turkish",         "name_ar": "صوت أمريكا التركية",      "country": "أمريكا",          "type": "راديو",       "lang": "tr", "url": "https://www.amerikaninsesi.com/api/zoqmpteioq/rss.xml"},
    {"id": 10110,"name": "RFI Arabic",          "name_ar": "راديو فرنسا الدولي عربي", "country": "فرنسا",           "type": "راديو",       "lang": "ar", "url": "https://www.rfi.fr/ar/rss"},
    {"id": 10111,"name": "DW Persian",          "name_ar": "دويتشه فيله الفارسية",    "country": "ألمانيا",         "type": "تلفزيون",     "lang": "fa", "url": "https://rss.dw.com/rdf/rss-per-all"},
    {"id": 10112,"name": "BBC Persian",         "name_ar": "بي بي سي الفارسية",       "country": "بريطانيا",        "type": "تلفزيون",     "lang": "fa", "url": "https://feeds.bbci.co.uk/persian/rss.xml"},
    {"id": 10113,"name": "BBC Turkish",         "name_ar": "بي بي سي التركية",        "country": "بريطانيا",        "type": "تلفزيون",     "lang": "tr", "url": "https://feeds.bbci.co.uk/turkish/rss.xml"},
    {"id": 10114,"name": "BBC Russian",         "name_ar": "بي بي سي الروسية",        "country": "بريطانيا",        "type": "تلفزيون",     "lang": "ru", "url": "https://feeds.bbci.co.uk/russian/rss.xml"},
    {"id": 10115,"name": "BBC Hindi",           "name_ar": "بي بي سي الهندية",        "country": "بريطانيا",        "type": "تلفزيون",     "lang": "hi", "url": "https://feeds.bbci.co.uk/hindi/rss.xml"},
    {"id": 10116,"name": "BBC Urdu",            "name_ar": "بي بي سي الأردو",         "country": "بريطانيا",        "type": "تلفزيون",     "lang": "ur", "url": "https://feeds.bbci.co.uk/urdu/rss.xml"},
    {"id": 10117,"name": "BBC Swahili",         "name_ar": "بي بي سي السواحيلية",     "country": "بريطانيا",        "type": "تلفزيون",     "lang": "sw", "url": "https://feeds.bbci.co.uk/swahili/rss.xml"},
    {"id": 10118,"name": "BBC Indonesian",      "name_ar": "بي بي سي الإندونيسية",    "country": "بريطانيا",        "type": "تلفزيون",     "lang": "id", "url": "https://feeds.bbci.co.uk/indonesian/rss.xml"},
    {"id": 10119,"name": "BBC Vietnamese",      "name_ar": "بي بي سي الفيتنامية",     "country": "بريطانيا",        "type": "تلفزيون",     "lang": "vi", "url": "https://feeds.bbci.co.uk/vietnamese/rss.xml"},
    {"id": 10120,"name": "BBC Somali",          "name_ar": "بي بي سي الصومالية",      "country": "بريطانيا",        "type": "تلفزيون",     "lang": "so", "url": "https://feeds.bbci.co.uk/somali/rss.xml"},

    # مصادر أكاديمية وفكرية
    {"id": 10121,"name": "Project Syndicate",   "name_ar": "مشروع سينديكيت",          "country": "تشيك",            "type": "أكاديمي",     "lang": "en", "url": "https://www.project-syndicate.org/rss"},
    {"id": 10122,"name": "The Nation USA",      "name_ar": "ذا نيشن USA",             "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.thenation.com/feed/?post_type=article"},
    {"id": 10123,"name": "Boston Review",       "name_ar": "بوسطن ريفيو",             "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.bostonreview.net/feed/"},
    {"id": 10124,"name": "Dissent Magazine",    "name_ar": "ديسنت ماغازين",           "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.dissentmagazine.org/feed"},
    {"id": 10125,"name": "Current Affairs",     "name_ar": "الشؤون الراهنة",          "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.currentaffairs.org/feed"},
    {"id": 10126,"name": "American Prospect",   "name_ar": "الآفاق الأمريكية",        "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://prospect.org/feed"},
    {"id": 10127,"name": "National Review",     "name_ar": "ناشيونال ريفيو",          "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.nationalreview.com/feed/"},
    {"id": 10128,"name": "The Weekly Standard", "name_ar": "ذا ويكلي ستاندرد",        "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.weeklystandard.com/feed"},
    {"id": 10129,"name": "Reason Magazine",     "name_ar": "ريزن ماغازين",            "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://reason.com/feed/"},
    {"id": 10130,"name": "The American Conservative","name_ar": "المحافظ الأمريكي",   "country": "أمريكا",          "type": "مجلة",        "lang": "en", "url": "https://www.theamericanconservative.com/feed/"},

    # مصادر الشرق الأوسط - إضافي
    {"id": 10131,"name": "Syria Reports",       "name_ar": "تقارير سوريا",            "country": "سوريا",           "type": "رقمي",        "lang": "en", "url": "https://www.syriareport.com/feed/"},
    {"id": 10132,"name": "Iraq Oil Report",     "name_ar": "تقرير نفط العراق",        "country": "العراق",          "type": "مالي",        "lang": "en", "url": "https://www.iraqoilreport.com/feed/"},
    {"id": 10133,"name": "Rudaw English",       "name_ar": "رووداو الإنجليزية",        "country": "العراق",          "type": "تلفزيون",     "lang": "en", "url": "https://www.rudaw.net/english/rss"},
    {"id": 10134,"name": "Kurdistan 24 English","name_ar": "كردستان 24 الإنجليزية",   "country": "العراق",          "type": "تلفزيون",     "lang": "en", "url": "https://www.kurdistan24.net/en/rss.xml"},
    {"id": 10135,"name": "The Libya Observer",  "name_ar": "ليبيا أوبزيرفر",          "country": "ليبيا",           "type": "رقمي",        "lang": "en", "url": "https://www.libyaobserver.ly/feed"},
    {"id": 10136,"name": "Yemeni Portal",       "name_ar": "البوابة اليمنية",         "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://yemen-portal.net/feed"},
    {"id": 10137,"name": "Al Mawqef Yemen",     "name_ar": "الموقف اليمني",           "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://almaweqf.net/feed"},
    {"id": 10138,"name": "Yemen Press",         "name_ar": "يمن برس",                 "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://yemenpress.net/feed"},
    {"id": 10139,"name": "Mareb Press",         "name_ar": "مأرب برس",                "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://marebpress.net/feed"},
    {"id": 10140,"name": "Aden Al Ghad",        "name_ar": "عدن الغد",                "country": "اليمن",           "type": "رقمي",        "lang": "ar", "url": "https://adengad.net/feed/"},

    # باقي المصادر العالمية
    {"id": 10141,"name": "El Confidencial Int", "name_ar": "إل كونفيدينسيال دولي",    "country": "إسبانيا",         "type": "رقمي",        "lang": "es", "url": "https://rss.elconfidencial.com/mundo/"},
    {"id": 10142,"name": "El Pais America",     "name_ar": "إل باييس أمريكا",         "country": "إسبانيا",         "type": "صحيفة",       "lang": "es", "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/english.elpais.com/portada"},
    {"id": 10143,"name": "Cinco Dias Spain",    "name_ar": "سينكو دياز إسبانيا",      "country": "إسبانيا",         "type": "مالي",        "lang": "es", "url": "https://cincodias.elpais.com/rss/"},
    {"id": 10144,"name": "Correio Braziliense", "name_ar": "كوريو برازيلينسي",        "country": "البرازيل",        "type": "صحيفة",       "lang": "pt", "url": "https://www.correiobraziliense.com.br/rss_feed.html"},
    {"id": 10145,"name": "Valor Economico BR",  "name_ar": "فالور إيكونوميكو",        "country": "البرازيل",        "type": "مالي",        "lang": "pt", "url": "https://valor.globo.com/rss.xml"},
    {"id": 10146,"name": "El Colombiano",       "name_ar": "إل كولومبيانو",           "country": "كولومبيا",        "type": "صحيفة",       "lang": "es", "url": "https://www.elcolombiano.com/feed"},
    {"id": 10147,"name": "Semana Colombia",     "name_ar": "سيمانا كولومبيا",         "country": "كولومبيا",        "type": "مجلة",        "lang": "es", "url": "https://www.semana.com/rss.xml"},
    {"id": 10148,"name": "La Republica Peru",   "name_ar": "لا ريبابليكا بيرو",       "country": "بيرو",            "type": "صحيفة",       "lang": "es", "url": "https://larepublica.pe/rss"},
    {"id": 10149,"name": "RPP Peru",            "name_ar": "آر بي بي بيرو",           "country": "بيرو",            "type": "راديو",       "lang": "es", "url": "https://rpp.pe/rss"},
    {"id": 10150,"name": "Agencia EFE",         "name_ar": "وكالة إيفي الإسبانية",    "country": "إسبانيا",         "type": "وكالة أنباء", "lang": "es", "url": "https://www.efe.com/efe/espana/1/rss"},
    {"id": 10151,"name": "Sputnik Español",     "name_ar": "سبوتنيك الإسبانية",       "country": "روسيا",           "type": "وكالة أنباء", "lang": "es", "url": "https://mundo.sputniknews.com/export/rss2/archive/index.xml"},
    {"id": 10152,"name": "RT Español",          "name_ar": "آر تي الإسبانية",         "country": "روسيا",           "type": "تلفزيون",     "lang": "es", "url": "https://actualidad.rt.com/rss"},

    # حوض المحيط الهادئ وشرق آسيا
    {"id": 10153,"name": "ABC News Pacific",    "name_ar": "أي بي سي باسيفيك",        "country": "أستراليا",        "type": "تلفزيون",     "lang": "en", "url": "https://www.abc.net.au/pacific/rss"},
    {"id": 10154,"name": "RNZ Pacific",         "name_ar": "راديو نيوزيلندا باسيفيك", "country": "نيوزيلندا",       "type": "راديو",       "lang": "en", "url": "https://www.rnz.co.nz/rss/pacific.xml"},
    {"id": 10155,"name": "Guardian Australia",  "name_ar": "الغارديان أستراليا",       "country": "أستراليا",        "type": "صحيفة",       "lang": "en", "url": "https://www.theguardian.com/australia-news/rss"},
    {"id": 10156,"name": "Crikey Australia",    "name_ar": "كرايكي أستراليا",          "country": "أستراليا",        "type": "رقمي",        "lang": "en", "url": "https://www.crikey.com.au/feed/"},
    {"id": 10157,"name": "New Zealand Listener","name_ar": "نيوزيلند ليسنر",          "country": "نيوزيلندا",       "type": "مجلة",        "lang": "en", "url": "https://www.nzherald.co.nz/arc/outboundfeeds/rss/section/nz"},
    {"id": 10158,"name": "Samoa Observer",      "name_ar": "ساموا أوبزيرفر",           "country": "ساموا",           "type": "صحيفة",       "lang": "en", "url": "https://www.samoaobserver.ws/feed"},
    {"id": 10159,"name": "Islands Business",    "name_ar": "أيلاندز بيزنس",           "country": "فيجي",            "type": "مجلة",        "lang": "en", "url": "https://www.islandsbusiness.com/feed/"},
    {"id": 10160,"name": "Asia Sentinel",       "name_ar": "آسيا سينتينل",            "country": "هونغ كونغ",       "type": "رقمي",        "lang": "en", "url": "https://www.asiasentinel.com/feed/"},
    {"id": 10161,"name": "Asia Pacific Report", "name_ar": "تقرير آسيا باسيفيك",      "country": "نيوزيلندا",       "type": "رقمي",        "lang": "en", "url": "https://asiapacificreport.nz/feed/"},
    {"id": 10162,"name": "Myanmar Times",       "name_ar": "ميانمار تايمز",           "country": "ميانمار",         "type": "صحيفة",       "lang": "en", "url": "https://www.mmtimes.com/feed"},

    # أفريقيا الفرانكوفونية
    {"id": 10163,"name": "Abidjan.net CI",      "name_ar": "أبيدجان نت كوت ديفوار",   "country": "ساحل العاج",      "type": "رقمي",        "lang": "fr", "url": "https://news.abidjan.net/rss"},
    {"id": 10164,"name": "Connectionivoirienne","name_ar": "كونكسيون إيفوارين",        "country": "ساحل العاج",      "type": "رقمي",        "lang": "fr", "url": "https://www.connectionivoirienne.net/feed/"},
    {"id": 10165,"name": "L'Obs Burkina",       "name_ar": "لوبس بوركينا فاسو",       "country": "بوركينا فاسو",    "type": "صحيفة",       "lang": "fr", "url": "https://www.lobservateur.bf/feed/"},
    {"id": 10166,"name": "Ben Benbouzid DZ",    "name_ar": "الخبر الجزائرية",         "country": "الجزائر",         "type": "صحيفة",       "lang": "ar", "url": "https://www.elkhabar.com/press/rss"},
    {"id": 10167,"name": "24h Maroc",           "name_ar": "24 ساعة المغرب",          "country": "المغرب",          "type": "رقمي",        "lang": "ar", "url": "https://www.24h.ma/feed/"},
    {"id": 10168,"name": "Gafsa.tn Tunisia",    "name_ar": "قفصة تيونيزيا",           "country": "تونس",            "type": "رقمي",        "lang": "ar", "url": "https://gafsa.tn/feed/"},
    {"id": 10169,"name": "Observateur Maroc",   "name_ar": "المراقب المغربي",         "country": "المغرب",          "type": "رقمي",        "lang": "fr", "url": "https://observateur.ma/feed/"},
    {"id": 10170,"name": "Liberte Algerie",     "name_ar": "ليبرتيه الجزائر",         "country": "الجزائر",         "type": "صحيفة",       "lang": "fr", "url": "https://www.liberte-algerie.com/feed"},

    # متخصصات إضافية
    {"id": 10171,"name": "Water Policy",        "name_ar": "سياسة المياه",            "country": "هولندا",          "type": "متخصص",       "lang": "en", "url": "https://iwaponline.com/wp/rss/"},
    {"id": 10172,"name": "Food Policy",         "name_ar": "سياسة الغذاء",            "country": "أمريكا",          "type": "متخصص",       "lang": "en", "url": "https://www.foodpolitics.com/feed/"},
    {"id": 10173,"name": "Energy News",         "name_ar": "أخبار الطاقة",            "country": "أمريكا",          "type": "بيئي",        "lang": "en", "url": "https://energynews.us/feed/"},
    {"id": 10174,"name": "Renewables Now",      "name_ar": "الطاقة المتجددة الآن",    "country": "بلغاريا",         "type": "بيئي",        "lang": "en", "url": "https://renewablesnow.com/feed/"},
    {"id": 10175,"name": "Oilprice.com",        "name_ar": "أسعار النفط",             "country": "بريطانيا",        "type": "مالي",        "lang": "en", "url": "https://oilprice.com/rss/main"},
    {"id": 10176,"name": "Mining.com",          "name_ar": "مايننغ دوت كوم",          "country": "كندا",            "type": "متخصص",       "lang": "en", "url": "https://www.mining.com/feed/"},
    {"id": 10177,"name": "Offshore Energy",     "name_ar": "طاقة المياه",             "country": "هولندا",          "type": "متخصص",       "lang": "en", "url": "https://www.offshore-energy.biz/feed/"},
    {"id": 10178,"name": "Al Ain UAE Sports",   "name_ar": "العين الرياضية",          "country": "الإمارات",        "type": "رياضة",       "lang": "ar", "url": "https://al-ain.com/sport/rss"},
    {"id": 10179,"name": "Kooora Extra",        "name_ar": "كووورة إكسترا",           "country": "السعودية",        "type": "رياضة",       "lang": "ar", "url": "https://www.kooora.com/?rss"},
    {"id": 10180,"name": "Goals Arabia",        "name_ar": "أهداف عربية",             "country": "الإمارات",        "type": "رياضة",       "lang": "ar", "url": "https://www.goalzz.com/rss"},


    # ══════════════════════════════════════════
    # المصادر المضافة من snap_bot
    # ══════════════════════════════════════════

    # آيسلندا
    {"id": 10181 ,"name": "RÚV Iceland                        ", "name_ar": "RÚV Iceland                        ", "country": "آيسلندا             ", "type": "صحيفة", "lang": "is", "url": "https://www.ruv.is/rss/frettir"},
    {"id": 10182 ,"name": "Fréttablaðið Iceland               ", "name_ar": "Fréttablaðið Iceland               ", "country": "آيسلندا             ", "type": "صحيفة", "lang": "is", "url": "https://www.frettabladid.is/rss.xml"},
    {"id": 10183 ,"name": "Stundin Iceland                    ", "name_ar": "Stundin Iceland                    ", "country": "آيسلندا             ", "type": "صحيفة", "lang": "en", "url": "https://stundin.is/rss"},

    # أفريقيا
    {"id": 10184 ,"name": "BusinessLive SA                    ", "name_ar": "BusinessLive SA                    ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.fin24.com/rss"},
    {"id": 10185 ,"name": "EWN South Africa                   ", "name_ar": "EWN South Africa                   ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://businesstech.co.za/news/feed"},
    {"id": 10186 ,"name": "The Namibian                       ", "name_ar": "The Namibian                       ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.namibian.com.na/rss"},
    {"id": 10187 ,"name": "Lusaka Times                       ", "name_ar": "Lusaka Times                       ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.lusakatimes.com/feed"},
    {"id": 10188 ,"name": "The EastAfrican                    ", "name_ar": "The EastAfrican                    ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.dailynation.co.ke/rss"},
    {"id": 10189 ,"name": "Standard Kenya                     ", "name_ar": "Standard Kenya                     ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.standardmedia.co.ke/rss/headlines.php"},
    {"id": 10190 ,"name": "Citizen TV Kenya                   ", "name_ar": "Citizen TV Kenya                   ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://citizentv.co.ke/rss"},
    {"id": 10191 ,"name": "Daily News Tanzania                ", "name_ar": "Daily News Tanzania                ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.dailynews.co.tz/feed"},
    {"id": 10192 ,"name": "KT Press Rwanda                    ", "name_ar": "KT Press Rwanda                    ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.ktpress.rw/rss"},
    {"id": 10193 ,"name": "Addis Standard Ethiopia            ", "name_ar": "Addis Standard Ethiopia            ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.ethiopianmonitor.com/feed"},
    {"id": 10194 ,"name": "The Reporter Ethiopia              ", "name_ar": "The Reporter Ethiopia              ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.thereporterethiopia.com/feed"},
    {"id": 10195 ,"name": "Channels TV Nigeria                ", "name_ar": "Channels TV Nigeria                ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.channelstv.com/feed"},
    {"id": 10196 ,"name": "The Cable Nigeria                  ", "name_ar": "The Cable Nigeria                  ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.thecable.ng/feed"},
    {"id": 10197 ,"name": "Sahara Reporters                   ", "name_ar": "Sahara Reporters                   ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://saharareporters.com/rss.xml"},
    {"id": 10198 ,"name": "Daily Trust Nigeria                ", "name_ar": "Daily Trust Nigeria                ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://dailytrust.com/feed"},
    {"id": 10199 ,"name": "Graphic Online Ghana               ", "name_ar": "Graphic Online Ghana               ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.myjoyonline.com/rss"},
    {"id": 10200 ,"name": "Joy Online Ghana                   ", "name_ar": "Joy Online Ghana                   ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.myjoyonline.com/feed"},
    {"id": 10201 ,"name": "Africanews                         ", "name_ar": "Africanews                         ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.africanews.com/feed"},
    {"id": 10202 ,"name": "Africa Check                       ", "name_ar": "Africa Check                       ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.dubawa.org/feed"},
    {"id": 10203 ,"name": "Abidjan.net                        ", "name_ar": "Abidjan.net                        ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.fratmat.info/rss"},
    {"id": 10204 ,"name": "Journal du Cameroun                ", "name_ar": "Journal du Cameroun                ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.journalducameroun.com/feed"},
    {"id": 10205 ,"name": "Radio Okapi RDC                    ", "name_ar": "Radio Okapi RDC                    ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.radiookapi.net/feed"},
    {"id": 10206 ,"name": "Actualite.cd Congo                 ", "name_ar": "Actualite.cd Congo                 ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://actualite.cd/feed"},
    {"id": 10207 ,"name": "Libyan Express                     ", "name_ar": "Libyan Express                     ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.libyanexpress.com/feed"},
    {"id": 10208 ,"name": "Libya Review                       ", "name_ar": "Libya Review                       ", "country": "أفريقيا             ", "type": "صحيفة", "lang": "en", "url": "https://libyareview.com/feed"},

    # ألمانيا
    {"id": 10209 ,"name": "Die Presse Austria                 ", "name_ar": "Die Presse Austria                 ", "country": "ألمانيا             ", "type": "صحيفة", "lang": "de", "url": "https://www.diepresse.com/rss"},
    {"id": 10210 ,"name": "Neue Zürcher Zeitung               ", "name_ar": "Neue Zürcher Zeitung               ", "country": "ألمانيا             ", "type": "صحيفة", "lang": "de", "url": "https://www.nzz.ch/international.rss"},
    {"id": 10211 ,"name": "The Local Austria                  ", "name_ar": "The Local Austria                  ", "country": "ألمانيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.thelocal.at/feeds/rss.php"},

    # أمريكا
    {"id": 10212 ,"name": "SinEmbargo México                  ", "name_ar": "SinEmbargo México                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.proceso.com.mx/rss"},
    {"id": 10213 ,"name": "ACN Venezuela                      ", "name_ar": "ACN Venezuela                      ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.acn.com.ve/feed"},
    {"id": 10214 ,"name": "Telam Argentina                    ", "name_ar": "Telam Argentina                    ", "country": "أمريكا              ", "type": "صحيفة", "lang": "ar", "url": "https://www.telam.com.ar/rss"},
    {"id": 10215 ,"name": "EFE Brasil                         ", "name_ar": "EFE Brasil                         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://g1.globo.com/dynamo/brasil/rss2.xml"},
    {"id": 10216 ,"name": "Mondoweiss Palestine               ", "name_ar": "Mondoweiss Palestine               ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://mondoweiss.net/feed"},
    {"id": 10217 ,"name": "Iraq News Agency                   ", "name_ar": "Iraq News Agency                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://shafaq.com/en/rss"},
    {"id": 10218 ,"name": "India PIB                          ", "name_ar": "India PIB                          ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.pib.gov.in/RssMain.aspx?ModId=6&Lang=1&Regid=3"},
    {"id": 10219 ,"name": "Sri Lanka Newsfirst                ", "name_ar": "Sri Lanka Newsfirst                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.ft.lk/rss"},
    {"id": 10220 ,"name": "Nepal Monitor                      ", "name_ar": "Nepal Monitor                      ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.nepalmonitor.com/feed"},
    {"id": 10221 ,"name": "Caribbean News Wire                ", "name_ar": "Caribbean News Wire                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://caribbeannewsglobal.com/feed"},
    {"id": 10222 ,"name": "Samoa Global News                  ", "name_ar": "Samoa Global News                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://pina.com.fj/feed"},
    {"id": 10223 ,"name": "NBC News World                     ", "name_ar": "NBC News World                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://feeds.nbcnews.com/nbcnews/public/world"},
    {"id": 10224 ,"name": "The Daily Beast                    ", "name_ar": "The Daily Beast                    ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.salon.com/feed"},
    {"id": 10225 ,"name": "PBS NewsHour                       ", "name_ar": "PBS NewsHour                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.pbs.org/newshour/feeds/rss/headlines"},
    {"id": 10226 ,"name": "Christian Science Monitor          ", "name_ar": "Christian Science Monitor          ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.csmonitor.com/rss"},
    {"id": 10227 ,"name": "CBC Canada                         ", "name_ar": "CBC Canada                         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.cbc.ca/cmlink/rss-canada"},
    {"id": 10228 ,"name": "Perfil Argentina                   ", "name_ar": "Perfil Argentina                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.perfil.com/feed"},
    {"id": 10229 ,"name": "Página 12 Argentina                ", "name_ar": "Página 12 Argentina                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "ar", "url": "https://www.pagina12.com.ar/rss"},
    {"id": 10230 ,"name": "O Globo Brasil                     ", "name_ar": "O Globo Brasil                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://g1.globo.com/rss/g1"},
    {"id": 10231 ,"name": "G1 Brasil                          ", "name_ar": "G1 Brasil                          ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://g1.globo.com/dynamo/mundo/rss2.xml"},
    {"id": 10232 ,"name": "UOL Notícias                       ", "name_ar": "UOL Notícias                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://rss.uol.com.br/feed/noticias.xml"},
    {"id": 10233 ,"name": "La Silla Vacía                     ", "name_ar": "La Silla Vacía                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://lasillavacia.com/feed"},
    {"id": 10234 ,"name": "Reforma México                     ", "name_ar": "Reforma México                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.elfinanciero.com.mx/rss"},
    {"id": 10235 ,"name": "Milenio México                     ", "name_ar": "Milenio México                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.jornada.com.mx/rss"},
    {"id": 10236 ,"name": "Proceso México                     ", "name_ar": "Proceso México                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.proceso.com.mx/?feed=rss2"},
    {"id": 10237 ,"name": "Aristegui Noticias                 ", "name_ar": "Aristegui Noticias                 ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://aristeguinoticias.com/feed"},
    {"id": 10238 ,"name": "RPP Noticias Perú                  ", "name_ar": "RPP Noticias Perú                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://rpp.pe/feed"},
    {"id": 10239 ,"name": "Gestión Perú                       ", "name_ar": "Gestión Perú                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://gestion.pe/rss"},
    {"id": 10240 ,"name": "La Nación Costa Rica               ", "name_ar": "La Nación Costa Rica               ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.nacion.com/rss"},
    {"id": 10241 ,"name": "La Tribuna Honduras                ", "name_ar": "La Tribuna Honduras                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://criterio.hn/feed"},
    {"id": 10242 ,"name": "Proceso Digital HN                 ", "name_ar": "Proceso Digital HN                 ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://proceso.hn/rss"},
    {"id": 10243 ,"name": "Cuba Debate                        ", "name_ar": "Cuba Debate                        ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.prensa-latina.cu/en/feed"},
    {"id": 10244 ,"name": "Jamaica Observer                   ", "name_ar": "Jamaica Observer                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.jamaicaobserver.com/rss"},
    {"id": 10245 ,"name": "Barbados Today                     ", "name_ar": "Barbados Today                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://barbadostoday.bb/feed"},
    {"id": 10246 ,"name": "Stabroek News Guyana               ", "name_ar": "Stabroek News Guyana               ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.stabroeknews.com/feed"},
    {"id": 10247 ,"name": "Los Tiempos Bolivia                ", "name_ar": "Los Tiempos Bolivia                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.lostiempos.com/rss.xml"},
    {"id": 10248 ,"name": "El Comercio Ecuador                ", "name_ar": "El Comercio Ecuador                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.elcomercio.com/feed"},
    {"id": 10249 ,"name": "RFE Central Asia                   ", "name_ar": "RFE Central Asia                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.rferl.org/api/eptopstories"},
    {"id": 10250 ,"name": "The Diplomat CA                    ", "name_ar": "The Diplomat CA                    ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://thediplomat.com/regions/central-asia/feed"},
    {"id": 10251 ,"name": "Cabar.asia                         ", "name_ar": "Cabar.asia                         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.akipress.com/rss"},
    {"id": 10252 ,"name": "Fergana News                       ", "name_ar": "Fergana News                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.kun.uz/rss"},
    {"id": 10253 ,"name": "24.kg Kyrgyzstan                   ", "name_ar": "24.kg Kyrgyzstan                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.akipress.com/rss/all"},
    {"id": 10254 ,"name": "KazInform                          ", "name_ar": "KazInform                          ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://kapital.kz/rss"},
    {"id": 10255 ,"name": "Times of Central Asia              ", "name_ar": "Times of Central Asia              ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.timesca.com/feed"},
    {"id": 10256 ,"name": "Intellinews CA                     ", "name_ar": "Intellinews CA                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.intellinews.com/feed"},
    {"id": 10257 ,"name": "Tengrinews Kazakhstan              ", "name_ar": "Tengrinews Kazakhstan              ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://tengrinews.kz/feed"},
    {"id": 10258 ,"name": "InformBuro Kazakhstan              ", "name_ar": "InformBuro Kazakhstan              ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.inform.kz/rss"},
    {"id": 10259 ,"name": "Vlast.kz Kazakhstan                ", "name_ar": "Vlast.kz Kazakhstan                ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://vlast.kz/feed"},
    {"id": 10260 ,"name": "Nur.kz Kazakhstan                  ", "name_ar": "Nur.kz Kazakhstan                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.nur.kz/feed"},
    {"id": 10261 ,"name": "Gazeta.uz                          ", "name_ar": "Gazeta.uz                          ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.gazeta.uz/en/rss"},
    {"id": 10262 ,"name": "Daryo.uz                           ", "name_ar": "Daryo.uz                           ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://daryo.uz/en/feed"},
    {"id": 10263 ,"name": "Spot.uz Uzbekistan                 ", "name_ar": "Spot.uz Uzbekistan                 ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.spot.uz/en/rss"},
    {"id": 10264 ,"name": "Kloop.kg                           ", "name_ar": "Kloop.kg                           ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://kloop.kg/feed"},
    {"id": 10265 ,"name": "Radio Azattyk RFE                  ", "name_ar": "Radio Azattyk RFE                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.azattyk.org/api/zvoqotmqvy"},
    {"id": 10266 ,"name": "Avesta Tajikistan                  ", "name_ar": "Avesta Tajikistan                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://avesta.tj/feed"},
    {"id": 10267 ,"name": "Chronicle of Turkmenistan          ", "name_ar": "Chronicle of Turkmenistan          ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://en.hronikatm.com/feed"},
    {"id": 10268 ,"name": "Turkmen News                       ", "name_ar": "Turkmen News                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://turkmen.news/feed"},
    {"id": 10269 ,"name": "Report.az Azerbaijan               ", "name_ar": "Report.az Azerbaijan               ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://report.az/rss"},
    {"id": 10270 ,"name": "Baku Tribune                       ", "name_ar": "Baku Tribune                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://en.trend.az/rss"},
    {"id": 10271 ,"name": "Meydan TV Azerbaijan               ", "name_ar": "Meydan TV Azerbaijan               ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.meydan.tv/en/feed"},
    {"id": 10272 ,"name": "Azvision.az                        ", "name_ar": "Azvision.az                        ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://azvision.az/rss.xml"},
    {"id": 10273 ,"name": "OC Media Georgia                   ", "name_ar": "OC Media Georgia                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://oc-media.org/feed"},
    {"id": 10274 ,"name": "Tabula Georgia                     ", "name_ar": "Tabula Georgia                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.interpressnews.ge/en/rss"},
    {"id": 10275 ,"name": "Agenda GE Georgia                  ", "name_ar": "Agenda GE Georgia                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://interpressnews.ge/rss"},
    {"id": 10276 ,"name": "Georgia Today                      ", "name_ar": "Georgia Today                      ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://georgiatoday.ge/feed"},
    {"id": 10277 ,"name": "Mediamax Armenia                   ", "name_ar": "Mediamax Armenia                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://mediamax.am/en/rss/news"},
    {"id": 10278 ,"name": "Armenian Weekly                    ", "name_ar": "Armenian Weekly                    ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://armenianweekly.com/feed"},
    {"id": 10279 ,"name": "A1plus Armenia                     ", "name_ar": "A1plus Armenia                     ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://a1plus.am/en/rss"},
    {"id": 10280 ,"name": "EVN Report Armenia                 ", "name_ar": "EVN Report Armenia                 ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.evnreport.com/feed"},
    {"id": 10281 ,"name": "Caucasus Survey                    ", "name_ar": "Caucasus Survey                    ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://caucasussurvey.org/feed"},
    {"id": 10282 ,"name": "Transparency International         ", "name_ar": "Transparency International         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.occrp.org/en/feed"},
    {"id": 10283 ,"name": "The Markup                         ", "name_ar": "The Markup                         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://themarkup.org/feeds/rss.xml"},
    {"id": 10284 ,"name": "The Nation                         ", "name_ar": "The Nation                         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.thenation.com/feed/?xml"},
    {"id": 10285 ,"name": "Global Investigative Journalism Network", "name_ar": "Global Investigative Journalism Network", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.icij.org/rss"},
    {"id": 10286 ,"name": "The Sentry                         ", "name_ar": "The Sentry                         ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://thesentry.org/feed"},
    {"id": 10287 ,"name": "Disclose France                    ", "name_ar": "Disclose France                    ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://disclose.ngo/feed"},
    {"id": 10288 ,"name": "Correctiv Germany                  ", "name_ar": "Correctiv Germany                  ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://correctiv.org/feed"},
    {"id": 10289 ,"name": "ARIJ Arab Investigative            ", "name_ar": "ARIJ Arab Investigative            ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://arij.net/feed"},
    {"id": 10290 ,"name": "KRIK Serbia                        ", "name_ar": "KRIK Serbia                        ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.krik.rs/feed"},
    {"id": 10291 ,"name": "Rise Project Romania               ", "name_ar": "Rise Project Romania               ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.riseproject.ro/feed"},
    {"id": 10292 ,"name": "Atlatszo Hungary                   ", "name_ar": "Atlatszo Hungary                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://hungarytoday.hu/feed"},
    {"id": 10293 ,"name": "CIPER Chile                        ", "name_ar": "CIPER Chile                        ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://ciperchile.cl/feed"},
    {"id": 10294 ,"name": "ContraCorriente Honduras           ", "name_ar": "ContraCorriente Honduras           ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://contracorriente.red/feed"},
    {"id": 10295 ,"name": "InfoAmazonia                       ", "name_ar": "InfoAmazonia                       ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://infoamazonia.org/feed"},
    {"id": 10296 ,"name": "Rappler Investigative              ", "name_ar": "Rappler Investigative              ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://www.rappler.com/category/newsbreak/investigative/feed"},
    {"id": 10297 ,"name": "PCIJ Philippines                   ", "name_ar": "PCIJ Philippines                   ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://pcij.org/feed"},
    {"id": 10298 ,"name": "Mongabay Investigative             ", "name_ar": "Mongabay Investigative             ", "country": "أمريكا              ", "type": "صحيفة", "lang": "en", "url": "https://news.mongabay.com/feed"},

    # أوروبا
    {"id": 10299 ,"name": "Adevărul Romania                   ", "name_ar": "Adevărul Romania                   ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://adevarul.ro/rss"},
    {"id": 10300 ,"name": "BTA Bulgaria                       ", "name_ar": "BTA Bulgaria                       ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.bta.bg/en/news/rss"},
    {"id": 10301 ,"name": "Capital Bulgaria                   ", "name_ar": "Capital Bulgaria                   ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.capital.bg/rss"},
    {"id": 10302 ,"name": "Večernji List Croatia              ", "name_ar": "Večernji List Croatia              ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.vecernji.hr/feeds/latest"},
    {"id": 10303 ,"name": "Klix.ba Bosnia                     ", "name_ar": "Klix.ba Bosnia                     ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://radiosarajevo.ba/rss"},
    {"id": 10304 ,"name": "Dnevni Avaz                        ", "name_ar": "Dnevni Avaz                        ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.radiosarajevo.ba/rss"},
    {"id": 10305 ,"name": "Southeast European Times           ", "name_ar": "Southeast European Times           ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.setimes.com/rss.xml"},
    {"id": 10306 ,"name": "Politika Serbia                    ", "name_ar": "Politika Serbia                    ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.politika.rs/rss"},
    {"id": 10307 ,"name": "Euronews Albania                   ", "name_ar": "Euronews Albania                   ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://al.euronews.com/rss"},
    {"id": 10308 ,"name": "Budapest Business Journal          ", "name_ar": "Budapest Business Journal          ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://bbj.hu/feed"},
    {"id": 10309 ,"name": "Prague Monitor                     ", "name_ar": "Prague Monitor                     ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://praguemonitor.com/feed"},
    {"id": 10310 ,"name": "SME Slovakia                       ", "name_ar": "SME Slovakia                       ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.sme.sk/rss"},
    {"id": 10311 ,"name": "Denník N Slovakia                  ", "name_ar": "Denník N Slovakia                  ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://dennikn.sk/feed"},
    {"id": 10312 ,"name": "RTV Slovenija                      ", "name_ar": "RTV Slovenija                      ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.rtvslo.si/rss"},
    {"id": 10313 ,"name": "Polskie Radio                      ", "name_ar": "Polskie Radio                      ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.gazetapl.com/rss"},
    {"id": 10314 ,"name": "Gazeta.pl Poland                   ", "name_ar": "Gazeta.pl Poland                   ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://wiadomosci.gazeta.pl/pub/rss/wiadomosci_kraj.xml"},
    {"id": 10315 ,"name": "In.gr Greece                       ", "name_ar": "In.gr Greece                       ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.in.gr/feed"},
    {"id": 10316 ,"name": "Kathimerini Greece                 ", "name_ar": "Kathimerini Greece                 ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.protothema.gr/rss"},
    {"id": 10317 ,"name": "Vijesti Montenegro                 ", "name_ar": "Vijesti Montenegro                 ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.vijesti.me/rss"},
    {"id": 10318 ,"name": "Kosovo Online                      ", "name_ar": "Kosovo Online                      ", "country": "أوروبا              ", "type": "صحيفة", "lang": "en", "url": "https://www.kosovoonline.com/feed"},

    # إسبانيا
    {"id": 10319 ,"name": "20 Minutos España                  ", "name_ar": "20 Minutos España                  ", "country": "إسبانيا             ", "type": "صحيفة", "lang": "es", "url": "https://www.20minutos.es/rss"},
    {"id": 10320 ,"name": "elDiario.es                        ", "name_ar": "elDiario.es                        ", "country": "إسبانيا             ", "type": "صحيفة", "lang": "es", "url": "https://www.eldiario.es/rss"},
    {"id": 10321 ,"name": "Jornal de Negócios                 ", "name_ar": "Jornal de Negócios                 ", "country": "إسبانيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.jornaldenegocios.pt/rss"},
    {"id": 10322 ,"name": "Observador Portugal                ", "name_ar": "Observador Portugal                ", "country": "إسبانيا             ", "type": "صحيفة", "lang": "en", "url": "https://observador.pt/feed"},
    {"id": 10323 ,"name": "Jornal de Notícias                 ", "name_ar": "Jornal de Notícias                 ", "country": "إسبانيا             ", "type": "صحيفة", "lang": "en", "url": "https://www.rtp.pt/noticias/rss"},

    # إستونيا
    {"id": 10324 ,"name": "ERR Estonia                        ", "name_ar": "ERR Estonia                        ", "country": "إستونيا             ", "type": "صحيفة", "lang": "et", "url": "https://www.err.ee/rss"},
    {"id": 10325 ,"name": "ERR Russian Estonia                ", "name_ar": "ERR Russian Estonia                ", "country": "إستونيا             ", "type": "صحيفة", "lang": "et", "url": "https://rus.err.ee/rss"},

    # إسرائيل
    {"id": 10326 ,"name": "Jerusalem Post                     ", "name_ar": "Jerusalem Post                     ", "country": "إسرائيل             ", "type": "صحيفة", "lang": "en", "url": "https://www.jpost.com/Rss/RssFeedsHeadlines.aspx"},
    {"id": 10327 ,"name": "+972 Magazine                      ", "name_ar": "+972 Magazine                      ", "country": "إسرائيل             ", "type": "صحيفة", "lang": "en", "url": "https://www.972mag.com/feed"},
    {"id": 10328 ,"name": "Arutz Sheva                        ", "name_ar": "Arutz Sheva                        ", "country": "إسرائيل             ", "type": "صحيفة", "lang": "en", "url": "https://www.israelnationalnews.com/rss.aspx"},
    {"id": 10329 ,"name": "Walla News                         ", "name_ar": "Walla News                         ", "country": "إسرائيل             ", "type": "صحيفة", "lang": "en", "url": "https://www.ynet.co.il/rss/category/3082"},

    # إيران
    {"id": 10330 ,"name": "Fars News                          ", "name_ar": "Fars News                          ", "country": "إيران               ", "type": "صحيفة", "lang": "en", "url": "https://www.farsnews.ir/rss"},
    {"id": 10331 ,"name": "Mehr News                          ", "name_ar": "Mehr News                          ", "country": "إيران               ", "type": "صحيفة", "lang": "en", "url": "https://www.presstv.ir/rss"},
    {"id": 10332 ,"name": "Iran International TV              ", "name_ar": "Iran International TV              ", "country": "إيران               ", "type": "صحيفة", "lang": "en", "url": "https://www.iranintl.com/en/rss.xml"},

    # إيطاليا
    {"id": 10333 ,"name": "Il Fatto Quotidiano                ", "name_ar": "Il Fatto Quotidiano                ", "country": "إيطاليا             ", "type": "صحيفة", "lang": "it", "url": "https://www.ilfattoquotidiano.it/feed"},
    {"id": 10334 ,"name": "Internazionale                     ", "name_ar": "Internazionale                     ", "country": "إيطاليا             ", "type": "صحيفة", "lang": "it", "url": "https://www.internazionale.it/rss"},

    # الأردن
    {"id": 10335 ,"name": "الغد الأردنية                      ", "name_ar": "الغد الأردنية                      ", "country": "الأردن              ", "type": "صحيفة", "lang": "ar", "url": "https://alghad.com/rss"},
    {"id": 10336 ,"name": "سواليف الأردن                      ", "name_ar": "سواليف الأردن                      ", "country": "الأردن              ", "type": "صحيفة", "lang": "ar", "url": "https://sawaleif.com/feed"},
    {"id": 10337 ,"name": "Jordan News                        ", "name_ar": "Jordan News                        ", "country": "الأردن              ", "type": "صحيفة", "lang": "en", "url": "https://jordanews.net/rss"},
    {"id": 10338 ,"name": "الدستور الأردنية                   ", "name_ar": "الدستور الأردنية                   ", "country": "الأردن              ", "type": "صحيفة", "lang": "ar", "url": "https://www.jo24.net/rss"},
    {"id": 10339 ,"name": "Jo24 الأردن                        ", "name_ar": "Jo24 الأردن                        ", "country": "الأردن              ", "type": "صحيفة", "lang": "ar", "url": "https://jo24.net/feed"},
    {"id": 10340 ,"name": "القدس الفلسطينية                   ", "name_ar": "القدس الفلسطينية                   ", "country": "الأردن              ", "type": "صحيفة", "lang": "ar", "url": "https://www.qudsn.net/rss"},

    # الإمارات
    {"id": 10341 ,"name": "الاتحاد الإماراتية                 ", "name_ar": "الاتحاد الإماراتية                 ", "country": "الإمارات            ", "type": "صحيفة", "lang": "ar", "url": "https://www.alittihad.ae/rss"},
    {"id": 10342 ,"name": "الوطن الإماراتية                   ", "name_ar": "الوطن الإماراتية                   ", "country": "الإمارات            ", "type": "صحيفة", "lang": "ar", "url": "https://www.alwatan.com.ae/feed"},
    {"id": 10343 ,"name": "دبي نيوز                           ", "name_ar": "دبي نيوز                           ", "country": "الإمارات            ", "type": "صحيفة", "lang": "ar", "url": "https://www.emirates247.com/rss"},
    {"id": 10344 ,"name": "Time Out Dubai                     ", "name_ar": "Time Out Dubai                     ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://whatson.ae/feed"},
    {"id": 10345 ,"name": "Sharjah24                          ", "name_ar": "Sharjah24                          ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://sharjah24.ae/rss"},
    {"id": 10346 ,"name": "WAM Arabic                         ", "name_ar": "WAM Arabic                         ", "country": "الإمارات            ", "type": "صحيفة", "lang": "ar", "url": "https://wam.ae/ar/feed"},
    {"id": 10347 ,"name": "Arabian Business                   ", "name_ar": "Arabian Business                   ", "country": "الإمارات            ", "type": "صحيفة", "lang": "ar", "url": "https://www.businesstraveller.com/feed"},
    {"id": 10348 ,"name": "Gulf Business                      ", "name_ar": "Gulf Business                      ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://gulfbusiness.com/feed"},
    {"id": 10349 ,"name": "Forbes Middle East                 ", "name_ar": "Forbes Middle East                 ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://www.forbesmiddleeast.com/feed"},
    {"id": 10350 ,"name": "Business Traveller ME              ", "name_ar": "Business Traveller ME              ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://skift.com/feed"},
    {"id": 10351 ,"name": "Fintech Finance News               ", "name_ar": "Fintech Finance News               ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://ffnews.com/feed"},
    {"id": 10352 ,"name": "Construction Week UAE              ", "name_ar": "Construction Week UAE              ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://www.meed.com/rss"},
    {"id": 10353 ,"name": "Gulf Industry Online               ", "name_ar": "Gulf Industry Online               ", "country": "الإمارات            ", "type": "صحيفة", "lang": "en", "url": "https://www.gulfindustry.com/rss"},

    # البحرين
    {"id": 10354 ,"name": "البحرين اليوم                      ", "name_ar": "البحرين اليوم                      ", "country": "البحرين             ", "type": "صحيفة", "lang": "ar", "url": "https://www.bahraintoday.bh/feed"},
    {"id": 10355 ,"name": "الوطن البحرينية                    ", "name_ar": "الوطن البحرينية                    ", "country": "البحرين             ", "type": "صحيفة", "lang": "ar", "url": "https://albiladdaily.com/feed"},
    {"id": 10356 ,"name": "الوسط البحرينية                    ", "name_ar": "الوسط البحرينية                    ", "country": "البحرين             ", "type": "صحيفة", "lang": "ar", "url": "https://www.alwasatnews.com/rss"},
    {"id": 10357 ,"name": "Bahrain Mirror                     ", "name_ar": "Bahrain Mirror                     ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://bahrainmirror.com/rss.xml"},
    {"id": 10358 ,"name": "Al Bilad Bahrain EN                ", "name_ar": "Al Bilad Bahrain EN                ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://www.newsofbahrain.com/rss"},
    {"id": 10359 ,"name": "Al Bilad Bahrain                   ", "name_ar": "Al Bilad Bahrain                   ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://www.albiladpress.com/rss"},
    {"id": 10360 ,"name": "Bahrain News                       ", "name_ar": "Bahrain News                       ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://newsofbahrain.com/rss"},
    {"id": 10361 ,"name": "Bahrain Confidential               ", "name_ar": "Bahrain Confidential               ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://www.bahrainconfidential.net/rss"},
    {"id": 10362 ,"name": "BNA Bahrain Arabic                 ", "name_ar": "BNA Bahrain Arabic                 ", "country": "البحرين             ", "type": "صحيفة", "lang": "ar", "url": "https://www.bna.bh/ar/rss"},
    {"id": 10363 ,"name": "Bahrain Tribune                    ", "name_ar": "Bahrain Tribune                    ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://www.bahrainthisweek.com/feed"},
    {"id": 10364 ,"name": "Bahrain Stock Exchange             ", "name_ar": "Bahrain Stock Exchange             ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://www.bahrainstockexchange.com/rss"},
    {"id": 10365 ,"name": "Bahrain News Agency                ", "name_ar": "Bahrain News Agency                ", "country": "البحرين             ", "type": "صحيفة", "lang": "en", "url": "https://newsofbahrain.com/rss.xml"},

    # الجزائر
    {"id": 10366 ,"name": "الشروق الجزائرية                   ", "name_ar": "الشروق الجزائرية                   ", "country": "الجزائر             ", "type": "صحيفة", "lang": "ar", "url": "https://www.echoroukonline.com/rss"},
    {"id": 10367 ,"name": "النهار الجزائرية                   ", "name_ar": "النهار الجزائرية                   ", "country": "الجزائر             ", "type": "صحيفة", "lang": "ar", "url": "https://www.ennahar.dz/rss"},
    {"id": 10368 ,"name": "الجمهورية الجزائرية                ", "name_ar": "الجمهورية الجزائرية                ", "country": "الجزائر             ", "type": "صحيفة", "lang": "ar", "url": "https://www.algerie360.com/rss"},

    # الخليج
    {"id": 10369 ,"name": "Gulf Intelligence                  ", "name_ar": "Gulf Intelligence                  ", "country": "الخليج              ", "type": "رقمي", "lang": "en", "url": "https://www.gulf-intelligence.com/feed"},
    {"id": 10370 ,"name": "TradeArabia                        ", "name_ar": "TradeArabia                        ", "country": "الخليج              ", "type": "رقمي", "lang": "ar", "url": "https://www.tradearabia.com/news/rss.xml"},
    {"id": 10371 ,"name": "الشرق الخليجي                      ", "name_ar": "الشرق الخليجي                      ", "country": "الخليج              ", "type": "رقمي", "lang": "ar", "url": "https://al-sharq.com/rss.xml"},
    {"id": 10372 ,"name": "Arab Gulf States Institute         ", "name_ar": "Arab Gulf States Institute         ", "country": "الخليج              ", "type": "رقمي", "lang": "en", "url": "https://agsiw.org/feed"},
    {"id": 10373 ,"name": "Global Finance Magazine            ", "name_ar": "Global Finance Magazine            ", "country": "الخليج              ", "type": "رقمي", "lang": "en", "url": "https://www.gfmag.com/rss"},
    {"id": 10374 ,"name": "Gulf States Analytics              ", "name_ar": "Gulf States Analytics              ", "country": "الخليج              ", "type": "رقمي", "lang": "en", "url": "https://arabcenterdc.org/feed"},

    # الدنمارك
    {"id": 10375 ,"name": "DR Denmark                         ", "name_ar": "DR Denmark                         ", "country": "الدنمارك            ", "type": "صحيفة", "lang": "da", "url": "https://www.dr.dk/nyheder/service/feeds/senestenyt"},
    {"id": 10376 ,"name": "Jyllands-Posten                    ", "name_ar": "Jyllands-Posten                    ", "country": "الدنمارك            ", "type": "صحيفة", "lang": "da", "url": "https://jyllands-posten.dk/feed/news"},
    {"id": 10377 ,"name": "Information Denmark                ", "name_ar": "Information Denmark                ", "country": "الدنمارك            ", "type": "صحيفة", "lang": "en", "url": "https://www.information.dk/feed"},

    # السعودية
    {"id": 10378 ,"name": "Peninsula Qatar                    ", "name_ar": "Peninsula Qatar                    ", "country": "السعودية            ", "type": "صحيفة", "lang": "en", "url": "https://www.thepeninsulaqatar.com/rss"},
    {"id": 10379 ,"name": "سبق السعودية                       ", "name_ar": "سبق السعودية                       ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://sabq.org/rss"},
    {"id": 10380 ,"name": "Saudi Gazette Arabic               ", "name_ar": "Saudi Gazette Arabic               ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://www.sabq.org/rss"},
    {"id": 10381 ,"name": "الوطن السعودية                     ", "name_ar": "الوطن السعودية                     ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://alwatan.com.sa/rss"},
    {"id": 10382 ,"name": "عكاظ السعودية                      ", "name_ar": "عكاظ السعودية                      ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://okaz.com.sa/rss"},
    {"id": 10383 ,"name": "مكة السعودية                       ", "name_ar": "مكة السعودية                       ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://makkahnewspaper.com/rss"},
    {"id": 10384 ,"name": "عرب نيوز اقتصاد                    ", "name_ar": "عرب نيوز اقتصاد                    ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://www.skynewsarabia.com/rss/business"},
    {"id": 10385 ,"name": "إيلاف                              ", "name_ar": "إيلاف                              ", "country": "السعودية            ", "type": "صحيفة", "lang": "ar", "url": "https://elaph.com/feed"},
    {"id": 10386 ,"name": "180post KSA                        ", "name_ar": "180post KSA                        ", "country": "السعودية            ", "type": "صحيفة", "lang": "en", "url": "https://180post.com/feed"},

    # السويد
    {"id": 10387 ,"name": "Expressen                          ", "name_ar": "Expressen                          ", "country": "السويد              ", "type": "صحيفة", "lang": "sv", "url": "https://www.expressen.se/rss/nyheter"},
    {"id": 10388 ,"name": "Aftonbladet                        ", "name_ar": "Aftonbladet                        ", "country": "السويد              ", "type": "صحيفة", "lang": "sv", "url": "https://rss.aftonbladet.se/rss2/small/pages/sections/senastenytt"},
    {"id": 10389 ,"name": "Dagens Industri Sweden             ", "name_ar": "Dagens Industri Sweden             ", "country": "السويد              ", "type": "صحيفة", "lang": "en", "url": "https://www.di.se/rss"},
    {"id": 10390 ,"name": "The Local Sweden                   ", "name_ar": "The Local Sweden                   ", "country": "السويد              ", "type": "صحيفة", "lang": "en", "url": "https://www.thelocal.se/feeds/rss.php"},
    {"id": 10391 ,"name": "Swedish Radio SR                   ", "name_ar": "Swedish Radio SR                   ", "country": "السويد              ", "type": "صحيفة", "lang": "en", "url": "https://api.sr.se/api/rss/program/83?format=1"},

    # الشرق الأوسط
    {"id": 10392 ,"name": "Newlines Magazine                  ", "name_ar": "Newlines Magazine                  ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://newlinesmag.com/feed"},
    {"id": 10393 ,"name": "عربي21                             ", "name_ar": "عربي21                             ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://arabi21.com/feed"},
    {"id": 10394 ,"name": "RT عربي                            ", "name_ar": "RT عربي                            ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://arabic.rt.com/rss/world"},
    {"id": 10395 ,"name": "المشرق نيوز                        ", "name_ar": "المشرق نيوز                        ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://almashriq.info/feed"},
    {"id": 10396 ,"name": "إيران إنترناشيونال عربي            ", "name_ar": "إيران إنترناشيونال عربي            ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://www.iranintl.com/ar/rss.xml"},
    {"id": 10397 ,"name": "عربي بوست                          ", "name_ar": "عربي بوست                          ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://arabicpost.net/rss"},
    {"id": 10398 ,"name": "الأناضول عربي                      ", "name_ar": "الأناضول عربي                      ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://www.aa.com.tr/ar/rss/default"},
    {"id": 10399 ,"name": "درج ميديا                          ", "name_ar": "درج ميديا                          ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://daraj.media/rss"},
    {"id": 10400 ,"name": "مدى مصر                            ", "name_ar": "مدى مصر                            ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://www.madamasr.com/en/feed"},
    {"id": 10401 ,"name": "العربي الجديد أخبار                ", "name_ar": "العربي الجديد أخبار                ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://www.alaraby.co.uk/rss"},
    {"id": 10402 ,"name": "رأي اليوم                          ", "name_ar": "رأي اليوم                          ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "ar", "url": "https://raialyoum.com/feed"},
    {"id": 10403 ,"name": "Middle East Institute              ", "name_ar": "Middle East Institute              ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://carnegieendowment.org/rss"},
    {"id": 10404 ,"name": "Arab Center Washington DC          ", "name_ar": "Arab Center Washington DC          ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://arabcenterdc.org/rss"},
    {"id": 10405 ,"name": "Carnegie Middle East               ", "name_ar": "Carnegie Middle East               ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://carnegie-mec.org/feed"},
    {"id": 10406 ,"name": "Atlantic Council MENA              ", "name_ar": "Atlantic Council MENA              ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://carnegieendowment.org/feed"},
    {"id": 10407 ,"name": "Brookings Middle East              ", "name_ar": "Brookings Middle East              ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://www.brookings.edu/topic/middle-east/feed"},
    {"id": 10408 ,"name": "Carnegie Europe                    ", "name_ar": "Carnegie Europe                    ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://carnegieeurope.eu/rss"},
    {"id": 10409 ,"name": "United States Institute of Peace   ", "name_ar": "United States Institute of Peace   ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://carnegieendowment.org/rss.xml"},
    {"id": 10410 ,"name": "SIPRI News                         ", "name_ar": "SIPRI News                         ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://www.sipri.org/rss/news"},
    {"id": 10411 ,"name": "Aspire Academy Qatar               ", "name_ar": "Aspire Academy Qatar               ", "country": "الشرق الأوسط        ", "type": "تلفزيون", "lang": "en", "url": "https://aspireacademy.qa/en/news/rss"},

    # الصين
    {"id": 10412 ,"name": "Philippine Daily Inquirer          ", "name_ar": "Philippine Daily Inquirer          ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.inquirer.net/feed"},
    {"id": 10413 ,"name": "Inquirer.net                       ", "name_ar": "Inquirer.net                       ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://newsinfo.inquirer.net/feed"},
    {"id": 10414 ,"name": "Philstar Global                    ", "name_ar": "Philstar Global                    ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.philstar.com/rss/nation"},
    {"id": 10415 ,"name": "Khaosod English                    ", "name_ar": "Khaosod English                    ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.khaosodenglish.com/feed"},
    {"id": 10416 ,"name": "Prachatai Thailand                 ", "name_ar": "Prachatai Thailand                 ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://prachatai.com/english/rss"},
    {"id": 10417 ,"name": "Detik Indonesia                    ", "name_ar": "Detik Indonesia                    ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://news.detik.com/rss.xml"},
    {"id": 10418 ,"name": "VnExpress                          ", "name_ar": "VnExpress                          ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://vnexpress.net/rss/tin-moi-nhat.rss"},
    {"id": 10419 ,"name": "Bernama Malaysia                   ", "name_ar": "Bernama Malaysia                   ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.bernama.com.my/rss"},
    {"id": 10420 ,"name": "Cambodia Daily                     ", "name_ar": "Cambodia Daily                     ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://english.cambodiadaily.com/feed"},
    {"id": 10421 ,"name": "Irrawaddy Myanmar                  ", "name_ar": "Irrawaddy Myanmar                  ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.myanmar-now.org/feed"},
    {"id": 10422 ,"name": "Myanmar Now                        ", "name_ar": "Myanmar Now                        ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://myanmar-now.org/en/feed"},
    {"id": 10423 ,"name": "Nine News Australia                ", "name_ar": "Nine News Australia                ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.9news.com.au/rss"},
    {"id": 10424 ,"name": "Sky News Australia                 ", "name_ar": "Sky News Australia                 ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.skynews.com.au/rss"},
    {"id": 10425 ,"name": "Canberra Times                     ", "name_ar": "Canberra Times                     ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.canberratimes.com.au/rss.xml"},
    {"id": 10426 ,"name": "WA Today                           ", "name_ar": "WA Today                           ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.watoday.com.au/rss/feed.xml"},
    {"id": 10427 ,"name": "Herald Sun Melbourne               ", "name_ar": "Herald Sun Melbourne               ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.heraldsun.com.au/news/breaking-news/rss"},
    {"id": 10428 ,"name": "Courier-Mail Queensland            ", "name_ar": "Courier-Mail Queensland            ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.couriermail.com.au/news/rss"},
    {"id": 10429 ,"name": "The Advertiser SA                  ", "name_ar": "The Advertiser SA                  ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.adelaidenow.com.au/news/south-australia/rss"},
    {"id": 10430 ,"name": "NT News                            ", "name_ar": "NT News                            ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.ntnews.com.au/news/rss"},
    {"id": 10431 ,"name": "The Mercury Tasmania               ", "name_ar": "The Mercury Tasmania               ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.themercury.com.au/news/rss"},
    {"id": 10432 ,"name": "The West Australian                ", "name_ar": "The West Australian                ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://thewest.com.au/feed"},
    {"id": 10433 ,"name": "InDaily Adelaide                   ", "name_ar": "InDaily Adelaide                   ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.adelaidenow.com.au/rss"},
    {"id": 10434 ,"name": "The Conversation AU                ", "name_ar": "The Conversation AU                ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://theconversation.com/au/articles.atom"},
    {"id": 10435 ,"name": "ABC Rural Australia                ", "name_ar": "ABC Rural Australia                ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.abc.net.au/news/feed/52498/rss.xml"},
    {"id": 10436 ,"name": "Michael West Media                 ", "name_ar": "Michael West Media                 ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.michaelwest.com.au/feed"},
    {"id": 10437 ,"name": "Newsroom NZ                        ", "name_ar": "Newsroom NZ                        ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.newsroom.co.nz/feed"},
    {"id": 10438 ,"name": "Radio NZ News                      ", "name_ar": "Radio NZ News                      ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://feeds.rnz.org.nz/rss.xml"},
    {"id": 10439 ,"name": "Radio NZ                           ", "name_ar": "Radio NZ                           ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.tvnz.co.nz/one-news/rss"},
    {"id": 10440 ,"name": "Loop Fiji                          ", "name_ar": "Loop Fiji                          ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.loopfiji.com/feed"},
    {"id": 10441 ,"name": "The Spinoff NZ                     ", "name_ar": "The Spinoff NZ                     ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://thespinoff.co.nz/feed"},
    {"id": 10442 ,"name": "Otago Daily Times                  ", "name_ar": "Otago Daily Times                  ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.odt.co.nz/rss.xml"},
    {"id": 10443 ,"name": "NZ Newswire                        ", "name_ar": "NZ Newswire                        ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.nznewswire.co.nz/feed"},
    {"id": 10444 ,"name": "FBC News Fiji                      ", "name_ar": "FBC News Fiji                      ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.fbcnews.com.fj/feed"},
    {"id": 10445 ,"name": "Papua New Guinea Post-Courier      ", "name_ar": "Papua New Guinea Post-Courier      ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.postcourier.com.pg/feed"},
    {"id": 10446 ,"name": "Cook Islands News                  ", "name_ar": "Cook Islands News                  ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.cookislandsnews.com/feed"},
    {"id": 10447 ,"name": "Solomon Star                       ", "name_ar": "Solomon Star                       ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.solomonstarnews.com/feed"},
    {"id": 10448 ,"name": "Loop PNG                           ", "name_ar": "Loop PNG                           ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.looppng.com/feed"},
    {"id": 10449 ,"name": "Tonga Broadcasting                 ", "name_ar": "Tonga Broadcasting                 ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.tbcradio.to/feed"},
    {"id": 10450 ,"name": "Pacific Islands Report             ", "name_ar": "Pacific Islands Report             ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.pireport.org/rss"},
    {"id": 10451 ,"name": "Kaniva Tonga                       ", "name_ar": "Kaniva Tonga                       ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.kanivatonga.net/rss"},
    {"id": 10452 ,"name": "La Dépêche Polynésie               ", "name_ar": "La Dépêche Polynésie               ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://www.ladepeche.pf/rss.xml"},
    {"id": 10453 ,"name": "NC la 1ère                         ", "name_ar": "NC la 1ère                         ", "country": "الصين               ", "type": "صحيفة", "lang": "en", "url": "https://la1ere.francetvinfo.fr/rss"},

    # العراق
    {"id": 10454 ,"name": "بغداد اليوم                        ", "name_ar": "بغداد اليوم                        ", "country": "العراق              ", "type": "صحيفة", "lang": "ar", "url": "https://baghdadtoday.news/rss.xml"},
    {"id": 10455 ,"name": "ناس نيوز العراقية                  ", "name_ar": "ناس نيوز العراقية                  ", "country": "العراق              ", "type": "صحيفة", "lang": "ar", "url": "https://www.nasnews.com/feed"},
    {"id": 10456 ,"name": "شفق نيوز العراق                    ", "name_ar": "شفق نيوز العراق                    ", "country": "العراق              ", "type": "صحيفة", "lang": "ar", "url": "https://shafaq.com/ar/rss"},
    {"id": 10457 ,"name": "BasNews English                    ", "name_ar": "BasNews English                    ", "country": "العراق              ", "type": "صحيفة", "lang": "en", "url": "https://www.kurdistan24.net/rss"},
    {"id": 10458 ,"name": "العالم العراقية                    ", "name_ar": "العالم العراقية                    ", "country": "العراق              ", "type": "صحيفة", "lang": "ar", "url": "https://www.iraqinews.com/feed"},
    {"id": 10459 ,"name": "شبكة النبأ العراقية                ", "name_ar": "شبكة النبأ العراقية                ", "country": "العراق              ", "type": "صحيفة", "lang": "ar", "url": "https://www.annabaa.org/feed"},

    # الكويت
    {"id": 10460 ,"name": "الجريدة الكويتية                   ", "name_ar": "الجريدة الكويتية                   ", "country": "الكويت              ", "type": "صحيفة", "lang": "ar", "url": "https://aljarida.com/rss"},
    {"id": 10461 ,"name": "الأنباء الكويتية                   ", "name_ar": "الأنباء الكويتية                   ", "country": "الكويت              ", "type": "صحيفة", "lang": "ar", "url": "https://www.alwatan.com.kw/rss"},
    {"id": 10462 ,"name": "Arab Times Kuwait                  ", "name_ar": "Arab Times Kuwait                  ", "country": "الكويت              ", "type": "صحيفة", "lang": "en", "url": "https://www.arabtimesonline.com/feed"},
    {"id": 10463 ,"name": "مجلة الكويت                        ", "name_ar": "مجلة الكويت                        ", "country": "الكويت              ", "type": "صحيفة", "lang": "ar", "url": "https://www.kuwaitmag.com/feed"},
    {"id": 10464 ,"name": "Sada Kuwait                        ", "name_ar": "Sada Kuwait                        ", "country": "الكويت              ", "type": "صحيفة", "lang": "en", "url": "https://sadakuwait.com/feed"},
    {"id": 10465 ,"name": "Watanway Kuwait                    ", "name_ar": "Watanway Kuwait                    ", "country": "الكويت              ", "type": "صحيفة", "lang": "en", "url": "https://watanway.com/feed"},
    {"id": 10466 ,"name": "Al Shahed Kuwait                   ", "name_ar": "Al Shahed Kuwait                   ", "country": "الكويت              ", "type": "صحيفة", "lang": "en", "url": "https://www.anbaa.com/feed"},
    {"id": 10467 ,"name": "Q8 Today                           ", "name_ar": "Q8 Today                           ", "country": "الكويت              ", "type": "صحيفة", "lang": "en", "url": "https://www.q8today.com/rss"},
    {"id": 10468 ,"name": "الشاهد الكويتية                    ", "name_ar": "الشاهد الكويتية                    ", "country": "الكويت              ", "type": "صحيفة", "lang": "ar", "url": "https://www.alwatan.com.kw/feed"},
    {"id": 10469 ,"name": "الكويت نيوز                        ", "name_ar": "الكويت نيوز                        ", "country": "الكويت              ", "type": "صحيفة", "lang": "ar", "url": "https://kuwaitnews.com/feed"},
    {"id": 10470 ,"name": "البورصة الكويتية                   ", "name_ar": "البورصة الكويتية                   ", "country": "الكويت              ", "type": "صحيفة", "lang": "ar", "url": "https://www.kse.com.kw/rss"},
    {"id": 10471 ,"name": "Mubasher Kuwait                    ", "name_ar": "Mubasher Kuwait                    ", "country": "الكويت              ", "type": "صحيفة", "lang": "en", "url": "https://kw.mubasher.info/feeds/rss.xml"},

    # المغرب
    {"id": 10472 ,"name": "المساء المغربية                    ", "name_ar": "المساء المغربية                    ", "country": "المغرب              ", "type": "صحيفة", "lang": "ar", "url": "https://www.hespress.com/rss"},
    {"id": 10473 ,"name": "Medias24                           ", "name_ar": "Medias24                           ", "country": "المغرب              ", "type": "صحيفة", "lang": "en", "url": "https://www.yabiladi.com/rss/actualites.xml"},
    {"id": 10474 ,"name": "Medias24 المغرب                    ", "name_ar": "Medias24 المغرب                    ", "country": "المغرب              ", "type": "صحيفة", "lang": "ar", "url": "https://medias24.com/feed"},
    {"id": 10475 ,"name": "Alyaoum24 المغرب                   ", "name_ar": "Alyaoum24 المغرب                   ", "country": "المغرب              ", "type": "صحيفة", "lang": "ar", "url": "https://www.yabiladi.com/articles/rss.rss"},
    {"id": 10476 ,"name": "Goud.ma                            ", "name_ar": "Goud.ma                            ", "country": "المغرب              ", "type": "صحيفة", "lang": "en", "url": "https://www.goud.ma/feed"},
    {"id": 10477 ,"name": "أخبارنا المغرب                     ", "name_ar": "أخبارنا المغرب                     ", "country": "المغرب              ", "type": "صحيفة", "lang": "ar", "url": "https://akhbarona.com/feed"},
    {"id": 10478 ,"name": "Maroc Diplomatique                 ", "name_ar": "Maroc Diplomatique                 ", "country": "المغرب              ", "type": "صحيفة", "lang": "en", "url": "https://www.h24info.ma/feed"},

    # النرويج
    {"id": 10479 ,"name": "NRK Nyheter Norway                 ", "name_ar": "NRK Nyheter Norway                 ", "country": "النرويج             ", "type": "صحيفة", "lang": "no", "url": "https://www.nrk.no/toppsaker.rss"},
    {"id": 10480 ,"name": "VG Nett                            ", "name_ar": "VG Nett                            ", "country": "النرويج             ", "type": "صحيفة", "lang": "no", "url": "https://www.aftenposten.no/rss"},
    {"id": 10481 ,"name": "Dagbladet Norway                   ", "name_ar": "Dagbladet Norway                   ", "country": "النرويج             ", "type": "صحيفة", "lang": "no", "url": "https://www.dagbladet.no/rss"},
    {"id": 10482 ,"name": "E24 Norway                         ", "name_ar": "E24 Norway                         ", "country": "النرويج             ", "type": "صحيفة", "lang": "no", "url": "https://e24.no/rss"},
    {"id": 10483 ,"name": "Nettavisen Norway                  ", "name_ar": "Nettavisen Norway                  ", "country": "النرويج             ", "type": "صحيفة", "lang": "en", "url": "https://www.nettavisen.no/rss"},
    {"id": 10484 ,"name": "Document Norway                    ", "name_ar": "Document Norway                    ", "country": "النرويج             ", "type": "صحيفة", "lang": "en", "url": "https://www.document.no/feed"},
    {"id": 10485 ,"name": "The Local Norway                   ", "name_ar": "The Local Norway                   ", "country": "النرويج             ", "type": "صحيفة", "lang": "en", "url": "https://www.thelocal.no/feeds/rss.php"},

    # الهند
    {"id": 10486 ,"name": "Firstpost                          ", "name_ar": "Firstpost                          ", "country": "الهند               ", "type": "صحيفة", "lang": "en", "url": "https://www.firstpost.com/rss/world.xml"},
    {"id": 10487 ,"name": "LiveMint                           ", "name_ar": "LiveMint                           ", "country": "الهند               ", "type": "صحيفة", "lang": "en", "url": "https://www.livemint.com/rss/news"},
    {"id": 10488 ,"name": "Geo News                           ", "name_ar": "Geo News                           ", "country": "الهند               ", "type": "صحيفة", "lang": "en", "url": "https://www.geo.tv/rss"},
    {"id": 10489 ,"name": "Express Tribune                    ", "name_ar": "Express Tribune                    ", "country": "الهند               ", "type": "صحيفة", "lang": "en", "url": "https://tribune.com.pk/feed/home"},
    {"id": 10490 ,"name": "Samaa TV Pakistan                  ", "name_ar": "Samaa TV Pakistan                  ", "country": "الهند               ", "type": "صحيفة", "lang": "en", "url": "https://www.samaa.tv/feed"},
    {"id": 10491 ,"name": "Economy Next Sri Lanka             ", "name_ar": "Economy Next Sri Lanka             ", "country": "الهند               ", "type": "صحيفة", "lang": "en", "url": "https://economynext.com/feed"},

    # اليابان
    {"id": 10492 ,"name": "Asia Nikkei                        ", "name_ar": "Asia Nikkei                        ", "country": "اليابان             ", "type": "صحيفة", "lang": "en", "url": "https://www.scmp.com/rss/2/feed"},
    {"id": 10493 ,"name": "Asia Pacific Daily                 ", "name_ar": "Asia Pacific Daily                 ", "country": "اليابان             ", "type": "صحيفة", "lang": "en", "url": "https://asiapacificdaily.com/feed"},

    # اليمن
    {"id": 10494 ,"name": "عدن الغد                           ", "name_ar": "عدن الغد                           ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://adengd.net/feed"},
    {"id": 10495 ,"name": "المشهد اليمني                      ", "name_ar": "المشهد اليمني                      ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://almashhad-alyemeni.com/feed"},
    {"id": 10496 ,"name": "يمن فيوتشر                         ", "name_ar": "يمن فيوتشر                         ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://yemenfuture.net/feed"},
    {"id": 10497 ,"name": "اليمن الآن                         ", "name_ar": "اليمن الآن                         ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://www.yemenat.net/rss"},
    {"id": 10498 ,"name": "خبر اليمن                          ", "name_ar": "خبر اليمن                          ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://yemen24news.com/feed"},
    {"id": 10499 ,"name": "سودان تريبيون                      ", "name_ar": "سودان تريبيون                      ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://www.dabangasudan.org/feed"},
    {"id": 10500 ,"name": "الراكوبة السودانية                 ", "name_ar": "الراكوبة السودانية                 ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://www.alrakoba.net/feed"},
    {"id": 10501 ,"name": "النيلين السوداني                   ", "name_ar": "النيلين السوداني                   ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://www.alnilin.com/rss"},
    {"id": 10502 ,"name": "سودان دايلي                        ", "name_ar": "سودان دايلي                        ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://sudandaily.sd/feed"},
    {"id": 10503 ,"name": "الأخبار الموريتانية                ", "name_ar": "الأخبار الموريتانية                ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://alakhbar.info/rss"},
    {"id": 10504 ,"name": "موريتانيا الآن                     ", "name_ar": "موريتانيا الآن                     ", "country": "اليمن               ", "type": "صحيفة", "lang": "ar", "url": "https://www.sahara-media.com/feed"},
    {"id": 10505 ,"name": "Garowe Online                      ", "name_ar": "Garowe Online                      ", "country": "اليمن               ", "type": "صحيفة", "lang": "en", "url": "https://www.horseedmedia.net/feed"},
    {"id": 10506 ,"name": "Goobjoog Somalia                   ", "name_ar": "Goobjoog Somalia                   ", "country": "اليمن               ", "type": "صحيفة", "lang": "en", "url": "https://goobjoog.com/feed"},

    # اليونان
    {"id": 10507 ,"name": "Ta Nea Greece                      ", "name_ar": "Ta Nea Greece                      ", "country": "اليونان             ", "type": "صحيفة", "lang": "en", "url": "https://www.tanea.gr/rss"},
    {"id": 10508 ,"name": "Cyprus Mail                        ", "name_ar": "Cyprus Mail                        ", "country": "اليونان             ", "type": "صحيفة", "lang": "en", "url": "https://cyprus-mail.com/feed"},

    # بريطانيا
    {"id": 10509 ,"name": "The Guardian World                 ", "name_ar": "The Guardian World                 ", "country": "بريطانيا            ", "type": "صحيفة", "lang": "en", "url": "https://www.theguardian.com/international/rss"},
    {"id": 10510 ,"name": "Iran Wire                          ", "name_ar": "Iran Wire                          ", "country": "بريطانيا            ", "type": "صحيفة", "lang": "en", "url": "https://iranwire.com/en/feed"},
    {"id": 10511 ,"name": "openDemocracy UK                   ", "name_ar": "openDemocracy UK                   ", "country": "بريطانيا            ", "type": "صحيفة", "lang": "en", "url": "https://www.theguardian.com/commentisfree/rss"},
    {"id": 10512 ,"name": "RTÉ News                           ", "name_ar": "RTÉ News                           ", "country": "بريطانيا            ", "type": "صحيفة", "lang": "en", "url": "https://www.independent.ie/rss"},
    {"id": 10513 ,"name": "The Journal Ireland                ", "name_ar": "The Journal Ireland                ", "country": "بريطانيا            ", "type": "صحيفة", "lang": "en", "url": "https://www.thejournal.ie/feed"},

    # بلجيكا
    {"id": 10514 ,"name": "Telegraaf                          ", "name_ar": "Telegraaf                          ", "country": "بلجيكا              ", "type": "صحيفة", "lang": "nl", "url": "https://www.nu.nl/rss"},
    {"id": 10515 ,"name": "Trouw                              ", "name_ar": "Trouw                              ", "country": "بلجيكا              ", "type": "صحيفة", "lang": "nl", "url": "https://www.trouw.nl/nieuws/rss.xml"},
    {"id": 10516 ,"name": "Le Soir Belgium                    ", "name_ar": "Le Soir Belgium                    ", "country": "بلجيكا              ", "type": "صحيفة", "lang": "fr", "url": "https://www.lalibre.be/rss"},

    # تركيا
    {"id": 10517 ,"name": "Yeni Şafak                         ", "name_ar": "Yeni Şafak                         ", "country": "تركيا               ", "type": "صحيفة", "lang": "en", "url": "https://www.yenisafak.com/rss"},
    {"id": 10518 ,"name": "Bianet Turkey                      ", "name_ar": "Bianet Turkey                      ", "country": "تركيا               ", "type": "صحيفة", "lang": "en", "url": "https://bianet.org/bianet.rss"},
    {"id": 10519 ,"name": "T24 Turkey                         ", "name_ar": "T24 Turkey                         ", "country": "تركيا               ", "type": "صحيفة", "lang": "en", "url": "https://t24.com.tr/rss"},
    {"id": 10520 ,"name": "Duvar Turkey                       ", "name_ar": "Duvar Turkey                       ", "country": "تركيا               ", "type": "صحيفة", "lang": "en", "url": "https://tr.euronews.com/rss"},
    {"id": 10521 ,"name": "Ahval News                         ", "name_ar": "Ahval News                         ", "country": "تركيا               ", "type": "صحيفة", "lang": "en", "url": "https://ahvalnews.com/rss.xml"},
    {"id": 10522 ,"name": "Medyascope                         ", "name_ar": "Medyascope                         ", "country": "تركيا               ", "type": "صحيفة", "lang": "en", "url": "https://medyascope.tv/feed"},

    # تونس
    {"id": 10523 ,"name": "الصباح التونسية                    ", "name_ar": "الصباح التونسية                    ", "country": "تونس                ", "type": "صحيفة", "lang": "ar", "url": "https://www.leaders.com.tn/rss"},
    {"id": 10524 ,"name": "Leaders Tunisia                    ", "name_ar": "Leaders Tunisia                    ", "country": "تونس                ", "type": "صحيفة", "lang": "en", "url": "https://www.leaders.com.tn/rss.html"},
    {"id": 10525 ,"name": "Kapitalis Tunisia                  ", "name_ar": "Kapitalis Tunisia                  ", "country": "تونس                ", "type": "صحيفة", "lang": "en", "url": "https://www.webdo.tn/feed"},

    # دولي
    {"id": 10526 ,"name": "Deutsche Welle Africa              ", "name_ar": "Deutsche Welle Africa              ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://rss.dw.com/rdf/rss-en-africa"},
    {"id": 10527 ,"name": "Xinhua                             ", "name_ar": "Xinhua                             ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.xinhuanet.com/english/rss/worldrss.xml"},
    {"id": 10528 ,"name": "Japan Times                        ", "name_ar": "Japan Times                        ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.japantimes.co.jp/feed"},
    {"id": 10529 ,"name": "NDTV India                         ", "name_ar": "NDTV India                         ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://feeds.feedburner.com/ndtvnews-india-news"},
    {"id": 10530 ,"name": "Free Malaysia Today                ", "name_ar": "Free Malaysia Today                ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.freemalaysiatoday.com/feed"},
    {"id": 10531 ,"name": "Antara Indonesia                   ", "name_ar": "Antara Indonesia                   ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://en.antaranews.com/rss/news.xml"},
    {"id": 10532 ,"name": "Thai PBS World                     ", "name_ar": "Thai PBS World                     ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.thaipbsworld.com/category/world/feed"},
    {"id": 10533 ,"name": "Jordan News Agency Petra           ", "name_ar": "Jordan News Agency Petra           ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://jordanews.net/feed"},
    {"id": 10534 ,"name": "BNA Bahrain EN                     ", "name_ar": "BNA Bahrain EN                     ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.newsofbahrain.com/feed"},
    {"id": 10535 ,"name": "Medias24 Maroc                     ", "name_ar": "Medias24 Maroc                     ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.goud.ma/rss"},
    {"id": 10536 ,"name": "Andina Peru                        ", "name_ar": "Andina Peru                        ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://andina.pe/agencia/rss.aspx"},
    {"id": 10537 ,"name": "Agencia EFE America                ", "name_ar": "Agencia EFE America                ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.efenoticias.com/feed"},
    {"id": 10538 ,"name": "Vietnam News Agency                ", "name_ar": "Vietnam News Agency                ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://en.vietnamplus.vn/rss/home.rss"},
    {"id": 10539 ,"name": "China News Service                 ", "name_ar": "China News Service                 ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.chinanews.com.cn/rss/world.xml"},
    {"id": 10540 ,"name": "Pakistan APP                       ", "name_ar": "Pakistan APP                       ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.app.com.pk/feed"},
    {"id": 10541 ,"name": "BSS Bangladesh                     ", "name_ar": "BSS Bangladesh                     ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://bssnews.net/feed"},
    {"id": 10542 ,"name": "Ukrinform Ukraine                  ", "name_ar": "Ukrinform Ukraine                  ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "ru", "url": "https://www.ukrinform.net/rss"},
    {"id": 10543 ,"name": "UNIAN Ukraine                      ", "name_ar": "UNIAN Ukraine                      ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "ru", "url": "https://www.unian.net/rss"},
    {"id": 10544 ,"name": "Interfax Ukraine                   ", "name_ar": "Interfax Ukraine                   ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "ru", "url": "https://www.pravda.com.ua/eng/rss/view_news"},
    {"id": 10545 ,"name": "BELTA Belarus                      ", "name_ar": "BELTA Belarus                      ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://eng.belta.by/rss"},
    {"id": 10546 ,"name": "RIA Novosti                        ", "name_ar": "RIA Novosti                        ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://ria.ru/export/rss2/index.xml"},
    {"id": 10547 ,"name": "Armenpress Armenia                 ", "name_ar": "Armenpress Armenia                 ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.a1plus.am/en/rss"},
    {"id": 10548 ,"name": "Azertag Azerbaijan                 ", "name_ar": "Azertag Azerbaijan                 ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://azertag.az/en/rss"},
    {"id": 10549 ,"name": "APA Azerbaijan                     ", "name_ar": "APA Azerbaijan                     ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://en.apa.az/rss"},
    {"id": 10550 ,"name": "KazInform Kazakhstan               ", "name_ar": "KazInform Kazakhstan               ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "lv", "url": "https://lsm.lv/rss"},
    {"id": 10551 ,"name": "AGI Italy                          ", "name_ar": "AGI Italy                          ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "it", "url": "https://www.agi.it/rss.xml"},
    {"id": 10552 ,"name": "ANA Greece                         ", "name_ar": "ANA Greece                         ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.amna.gr/en/rss"},
    {"id": 10553 ,"name": "Agerpres Romania                   ", "name_ar": "Agerpres Romania                   ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://romania-insider.com/feed"},
    {"id": 10554 ,"name": "STA Slovenia                       ", "name_ar": "STA Slovenia                       ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.24ur.com/rss.xml"},
    {"id": 10555 ,"name": "MIA North Macedonia                ", "name_ar": "MIA North Macedonia                ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://mia.mk/feed"},
    {"id": 10556 ,"name": "GhanaWeb                           ", "name_ar": "GhanaWeb                           ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.ghanaweb.com/GhanaHomePage/rss"},
    {"id": 10557 ,"name": "ANA South Africa                   ", "name_ar": "ANA South Africa                   ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.anaenglish.com/feed"},
    {"id": 10558 ,"name": "Kenya News Agency                  ", "name_ar": "Kenya News Agency                  ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.kbc.co.ke/feed"},
    {"id": 10559 ,"name": "ENA Ethiopia EN                    ", "name_ar": "ENA Ethiopia EN                    ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.thereporterethiopia.com/rss"},
    {"id": 10560 ,"name": "New Era Namibia                    ", "name_ar": "New Era Namibia                    ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://neweralive.na/feed"},
    {"id": 10561 ,"name": "Rwanda News Agency                 ", "name_ar": "Rwanda News Agency                 ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.newtimes.co.rw/rss"},
    {"id": 10562 ,"name": "Angop Angola                       ", "name_ar": "Angop Angola                       ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.rfi.fr/en/africa/rss"},
    {"id": 10563 ,"name": "African Arguments                  ", "name_ar": "African Arguments                  ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://africanarguments.org/feed"},
    {"id": 10564 ,"name": "Africa Is a Country                ", "name_ar": "Africa Is a Country                ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://africasacountry.com/feed"},
    {"id": 10565 ,"name": "APS Senegal                        ", "name_ar": "APS Senegal                        ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.aps.sn/feed"},
    {"id": 10566 ,"name": "2M Maroc                           ", "name_ar": "2M Maroc                           ", "country": "دولي                ", "type": "وكالة أنباء", "lang": "en", "url": "https://www.maroc.ma/rss.xml"},
    {"id": 10567 ,"name": "Arab Digest                        ", "name_ar": "Arab Digest                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://thearabweekly.com/rss"},
    {"id": 10568 ,"name": "TRENDS Research                    ", "name_ar": "TRENDS Research                    ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://trendsresearch.org/feed"},
    {"id": 10569 ,"name": "The New Arab EN                    ", "name_ar": "The New Arab EN                    ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.newarab.com/rss.xml"},
    {"id": 10570 ,"name": "Arab News Saudi                    ", "name_ar": "Arab News Saudi                    ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.saudigazette.com.sa/rss"},
    {"id": 10571 ,"name": "Khaleej Times Sport                ", "name_ar": "Khaleej Times Sport                ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.supersport.com/rss"},
    {"id": 10572 ,"name": "Khaleej Times World                ", "name_ar": "Khaleej Times World                ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.khaleejtimes.com/feed/world"},
    {"id": 10573 ,"name": "SPA Economy                        ", "name_ar": "SPA Economy                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.spa.gov.sa/rss/economy.xml"},
    {"id": 10574 ,"name": "SPA Sports                         ", "name_ar": "SPA Sports                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.spa.gov.sa/rss/sport.xml"},
    {"id": 10575 ,"name": "Sabq Economy                       ", "name_ar": "Sabq Economy                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://sabq.org/rss/economy"},
    {"id": 10576 ,"name": "Sabq Sports                        ", "name_ar": "Sabq Sports                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://sabq.org/rss/sports"},
    {"id": 10577 ,"name": "Okaz Economy                       ", "name_ar": "Okaz Economy                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://okaz.com.sa/rss/economy"},
    {"id": 10578 ,"name": "العربية الاقتصادية                 ", "name_ar": "العربية الاقتصادية                 ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.skynewsarabia.com/rss"},
    {"id": 10579 ,"name": "Maaal Saudi                        ", "name_ar": "Maaal Saudi                        ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://argaam.com/ar/rss"},
    {"id": 10580 ,"name": "Arab Finance                       ", "name_ar": "Arab Finance                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.argaam.com/en/rss"},
    {"id": 10581 ,"name": "Saudi Aramco World                 ", "name_ar": "Saudi Aramco World                 ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://saudiaramcoworld.com/feed"},
    {"id": 10582 ,"name": "سيدتي                              ", "name_ar": "سيدتي                              ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.sayidaty.net/rss.xml"},
    {"id": 10583 ,"name": "MEED Business                      ", "name_ar": "MEED Business                      ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.meed.com/news/rss"},
    {"id": 10584 ,"name": "تقنية السعودية                     ", "name_ar": "تقنية السعودية                     ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.tqnia.com/feed"},
    {"id": 10585 ,"name": "Arab Business Intelligence         ", "name_ar": "Arab Business Intelligence         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.thearabweekly.com/rss"},
    {"id": 10586 ,"name": "Saudi 24 News                      ", "name_ar": "Saudi 24 News                      ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.saudi24news.com/feed"},
    {"id": 10587 ,"name": "Vision 2030 News                   ", "name_ar": "Vision 2030 News                   ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.saudi-gazette.com/feed"},
    {"id": 10588 ,"name": "Argaam Finance                     ", "name_ar": "Argaam Finance                     ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://argaam.com/rss"},
    {"id": 10589 ,"name": "Khaleej Times Opinion              ", "name_ar": "Khaleej Times Opinion              ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.khaleejtimes.com/feed/opinion"},
    {"id": 10590 ,"name": "CPI Arabia                         ", "name_ar": "CPI Arabia                         ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.cpiarabia.com/feed"},
    {"id": 10591 ,"name": "Arab Investor                      ", "name_ar": "Arab Investor                      ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://arabinvestor.com/feed"},
    {"id": 10592 ,"name": "القدس العربي                       ", "name_ar": "القدس العربي                       ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.alquds.com/feed"},
    {"id": 10593 ,"name": "Transitions Online                 ", "name_ar": "Transitions Online                 ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://tol.org/feed"},
    {"id": 10594 ,"name": "Science AAAS                       ", "name_ar": "Science AAAS                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.science.org/rss/news_current.xml"},
    {"id": 10595 ,"name": "The Lancet                         ", "name_ar": "The Lancet                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.thelancet.com/rssfeed/lancet_online.xml"},
    {"id": 10596 ,"name": "Quanta Magazine                    ", "name_ar": "Quanta Magazine                    ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.quantamagazine.org/feed"},
    {"id": 10597 ,"name": "ScienceAlert                       ", "name_ar": "ScienceAlert                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.sciencealert.com/feed"},
    {"id": 10598 ,"name": "Nautilus Magazine                  ", "name_ar": "Nautilus Magazine                  ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://nautil.us/feed"},
    {"id": 10599 ,"name": "Undark Science                     ", "name_ar": "Undark Science                     ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://undark.org/feed"},
    {"id": 10600 ,"name": "Guardian Science                   ", "name_ar": "Guardian Science                   ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.theguardian.com/science/rss"},
    {"id": 10601 ,"name": "NASA News                          ", "name_ar": "NASA News                          ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.nasa.gov/rss/dyn/breaking_news.rss"},
    {"id": 10602 ,"name": "Inside Climate News                ", "name_ar": "Inside Climate News                ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://insideclimatenews.org/feed"},
    {"id": 10603 ,"name": "DeSmog                             ", "name_ar": "DeSmog                             ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.desmog.com/feed"},
    {"id": 10604 ,"name": "The Third Pole                     ", "name_ar": "The Third Pole                     ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.thethirdpole.net/feed"},
    {"id": 10605 ,"name": "Guardian Environment               ", "name_ar": "Guardian Environment               ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.theguardian.com/environment/rss"},
    {"id": 10606 ,"name": "PBS NewsHour Science               ", "name_ar": "PBS NewsHour Science               ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.pbs.org/newshour/feeds/rss/science"},
    {"id": 10607 ,"name": "وكالة الأنباء القطرية              ", "name_ar": "وكالة الأنباء القطرية              ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://gulf-times.com/rss/ar"},
    {"id": 10608 ,"name": "QNA English                        ", "name_ar": "QNA English                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.thepeninsulaqatar.com/rss.xml"},
    {"id": 10609 ,"name": "الشرق القطرية                      ", "name_ar": "الشرق القطرية                      ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.al-sharq.com/rss.xml"},
    {"id": 10610 ,"name": "العرب القطرية                      ", "name_ar": "العرب القطرية                      ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.alarab.qa/feed"},
    {"id": 10611 ,"name": "بيان قطر                           ", "name_ar": "بيان قطر                           ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://gulf-times.com/rss"},
    {"id": 10612 ,"name": "لوسيل القطرية                      ", "name_ar": "لوسيل القطرية                      ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.thepeninsulaqatar.com/feed"},
    {"id": 10613 ,"name": "Gulf Times                         ", "name_ar": "Gulf Times                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.gulf-times.com/?format=feed&type=rss"},
    {"id": 10614 ,"name": "Qatar Living                       ", "name_ar": "Qatar Living                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.qatarisbooming.com/feed"},
    {"id": 10615 ,"name": "Marhaba Qatar                      ", "name_ar": "Marhaba Qatar                      ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.marhaba.qa/feed"},
    {"id": 10616 ,"name": "Qatar Day                          ", "name_ar": "Qatar Day                          ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.qatarday.com/feed"},
    {"id": 10617 ,"name": "Qatar Is Booming                   ", "name_ar": "Qatar Is Booming                   ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.qatarbooming.com/feed"},
    {"id": 10618 ,"name": "Qatar Business Review              ", "name_ar": "Qatar Business Review              ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.qatarbusinessreview.net/feed"},
    {"id": 10619 ,"name": "Oxford Business Group Qatar        ", "name_ar": "Oxford Business Group Qatar        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://oxfordbusinessgroup.com/qatar/rss"},
    {"id": 10620 ,"name": "الجزيرة وثائقية                    ", "name_ar": "الجزيرة وثائقية                    ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.aljazeeradoc.com/rss"},
    {"id": 10621 ,"name": "AJ+                                ", "name_ar": "AJ+                                ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://ajplus.net/rss"},
    {"id": 10622 ,"name": "BBC Health                         ", "name_ar": "BBC Health                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.bbci.co.uk/news/health/rss.xml"},
    {"id": 10623 ,"name": "BBC Entertainment                  ", "name_ar": "BBC Entertainment                  ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"},
    {"id": 10624 ,"name": "BBC Middle East                    ", "name_ar": "BBC Middle East                    ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.bbci.co.uk/news/world/middle_east/rss.xml"},
    {"id": 10625 ,"name": "BBC Asia                           ", "name_ar": "BBC Asia                           ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.bbci.co.uk/news/world/asia/rss.xml"},
    {"id": 10626 ,"name": "BBC Europe                         ", "name_ar": "BBC Europe                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.bbci.co.uk/news/world/europe/rss.xml"},
    {"id": 10627 ,"name": "BBC Americas                       ", "name_ar": "BBC Americas                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.bbc.co.uk/news/world/latin_america/rss.xml"},
    {"id": 10628 ,"name": "NPR Business                       ", "name_ar": "NPR Business                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.npr.org/1006/rss.xml"},
    {"id": 10629 ,"name": "NPR Science                        ", "name_ar": "NPR Science                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.npr.org/1007/rss.xml"},
    {"id": 10630 ,"name": "NPR Health                         ", "name_ar": "NPR Health                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.npr.org/1008/rss.xml"},
    {"id": 10631 ,"name": "NPR Books                          ", "name_ar": "NPR Books                          ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.npr.org/1003/rss.xml"},
    {"id": 10632 ,"name": "NPR Music                          ", "name_ar": "NPR Music                          ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://feeds.npr.org/1039/rss.xml"},
    {"id": 10633 ,"name": "AP Business                        ", "name_ar": "AP Business                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://apnews.com/hub/business/rss.xml"},
    {"id": 10634 ,"name": "AP Science                         ", "name_ar": "AP Science                         ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://apnews.com/hub/science/rss.xml"},
    {"id": 10635 ,"name": "AP Technology                      ", "name_ar": "AP Technology                      ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://apnews.com/hub/technology/rss.xml"},
    {"id": 10636 ,"name": "AP Lifestyle                       ", "name_ar": "AP Lifestyle                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://apnews.com/hub/lifestyle/rss.xml"},
    {"id": 10637 ,"name": "UNHCR                              ", "name_ar": "UNHCR                              ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.unocha.org/rss.xml"},
    {"id": 10638 ,"name": "OECD Newsroom                      ", "name_ar": "OECD Newsroom                      ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.wto.org/english/res_e/reser_e/rss_news_e.xml"},
    {"id": 10639 ,"name": "Natural Gas World                  ", "name_ar": "Natural Gas World                  ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.naturalgasworld.com/feed"},
    {"id": 10640 ,"name": "LNG World News                     ", "name_ar": "LNG World News                     ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.lngworldnews.com/feed"},
    {"id": 10641 ,"name": "Hydrocarbons Technology            ", "name_ar": "Hydrocarbons Technology            ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.oilandgasjournal.com/rss"},
    {"id": 10642 ,"name": "Tech Xplore                        ", "name_ar": "Tech Xplore                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://techxplore.com/rss-feed"},
    {"id": 10643 ,"name": "Harvard Business Review            ", "name_ar": "Harvard Business Review            ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.forbes.com/business/feed"},
    {"id": 10644 ,"name": "Fast Company                       ", "name_ar": "Fast Company                       ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.fastcompany.com/latest/rss"},
    {"id": 10645 ,"name": "CNBC Technology                    ", "name_ar": "CNBC Technology                    ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.cnbc.com/id/10000108/device/rss/rss.html"},
    {"id": 10646 ,"name": "beIN Sports عربي                   ", "name_ar": "beIN Sports عربي                   ", "country": "دولي                ", "type": "متخصص", "lang": "ar", "url": "https://www.beinsports.com/ar/rss"},
    {"id": 10647 ,"name": "Goal.com EN                        ", "name_ar": "Goal.com EN                        ", "country": "دولي                ", "type": "متخصص", "lang": "en", "url": "https://www.espn.com/espn/rss/soccer/news"},

    # روسيا
    {"id": 10648 ,"name": "Meduza English                     ", "name_ar": "Meduza English                     ", "country": "روسيا               ", "type": "صحيفة", "lang": "ru", "url": "https://meduza.io/rss/en/all"},

    # عُمان
    {"id": 10649 ,"name": "الشبيبة العُمانية                  ", "name_ar": "الشبيبة العُمانية                  ", "country": "عُمان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.alshabiba.com/rss"},
    {"id": 10650 ,"name": "الوطن العُمانية                    ", "name_ar": "الوطن العُمانية                    ", "country": "عُمان               ", "type": "صحيفة", "lang": "ar", "url": "https://alwatan.com/rss"},
    {"id": 10651 ,"name": "Muscat Daily                       ", "name_ar": "Muscat Daily                       ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://muscatdaily.com/feed"},
    {"id": 10652 ,"name": "الرؤية العُمانية                   ", "name_ar": "الرؤية العُمانية                   ", "country": "عُمان               ", "type": "صحيفة", "lang": "ar", "url": "https://alroya.om/rss"},
    {"id": 10653 ,"name": "عُمان 24                           ", "name_ar": "عُمان 24                           ", "country": "عُمان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.oman24news.com/rss"},
    {"id": 10654 ,"name": "Oman Economic Review               ", "name_ar": "Oman Economic Review               ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://www.oeronline.com/rss"},
    {"id": 10655 ,"name": "Muwatin Oman                       ", "name_ar": "Muwatin Oman                       ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://muwatin.net/feed"},
    {"id": 10656 ,"name": "Oman Tribune                       ", "name_ar": "Oman Tribune                       ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://www.muscatdaily.com/feed"},
    {"id": 10657 ,"name": "Muscat Press                       ", "name_ar": "Muscat Press                       ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://www.muscatpress.com/feed"},
    {"id": 10658 ,"name": "Oman Daily Observer                ", "name_ar": "Oman Daily Observer                ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://www.omanobserver.om/rss"},
    {"id": 10659 ,"name": "عُمان الاقتصادية                   ", "name_ar": "عُمان الاقتصادية                   ", "country": "عُمان               ", "type": "صحيفة", "lang": "ar", "url": "https://omaneconomy.om/rss"},
    {"id": 10660 ,"name": "Mubasher Oman                      ", "name_ar": "Mubasher Oman                      ", "country": "عُمان               ", "type": "صحيفة", "lang": "en", "url": "https://www.muscatdaily.com/rss"},

    # فرنسا
    {"id": 10661 ,"name": "L'Obs                              ", "name_ar": "L'Obs                              ", "country": "فرنسا               ", "type": "صحيفة", "lang": "fr", "url": "https://www.nouvelobs.com/rss.xml"},
    {"id": 10662 ,"name": "Les Échos                          ", "name_ar": "Les Échos                          ", "country": "فرنسا               ", "type": "صحيفة", "lang": "en", "url": "https://www.bfmtv.com/rss"},
    {"id": 10663 ,"name": "20 Minutes France                  ", "name_ar": "20 Minutes France                  ", "country": "فرنسا               ", "type": "صحيفة", "lang": "fr", "url": "https://www.20minutes.fr/feeds/rss-monde.xml"},
    {"id": 10664 ,"name": "Courrier International             ", "name_ar": "Courrier International             ", "country": "فرنسا               ", "type": "صحيفة", "lang": "fr", "url": "https://www.courrierinternational.com/feed/all/rss.xml"},
    {"id": 10665 ,"name": "La Croix                           ", "name_ar": "La Croix                           ", "country": "فرنسا               ", "type": "صحيفة", "lang": "fr", "url": "https://www.la-croix.com/rss.xml"},
    {"id": 10666 ,"name": "Het Laatste Nieuws                 ", "name_ar": "Het Laatste Nieuws                 ", "country": "فرنسا               ", "type": "صحيفة", "lang": "fr", "url": "https://www.hln.be/rss.xml"},
    {"id": 10667 ,"name": "De Morgen Belgium                  ", "name_ar": "De Morgen Belgium                  ", "country": "فرنسا               ", "type": "صحيفة", "lang": "fr", "url": "https://www.demorgen.be/rss.xml"},
    {"id": 10668 ,"name": "The Brussels Times                 ", "name_ar": "The Brussels Times                 ", "country": "فرنسا               ", "type": "صحيفة", "lang": "en", "url": "https://www.brusselstimes.com/feed"},
    {"id": 10669 ,"name": "Luxembourg Times                   ", "name_ar": "Luxembourg Times                   ", "country": "فرنسا               ", "type": "صحيفة", "lang": "en", "url": "https://luxtimes.lu/rss"},

    # فنلندا
    {"id": 10670 ,"name": "Ilta-Sanomat                       ", "name_ar": "Ilta-Sanomat                       ", "country": "فنلندا              ", "type": "صحيفة", "lang": "fi", "url": "https://www.is.fi/rss/uutiset.xml"},
    {"id": 10671 ,"name": "YLE Finland                        ", "name_ar": "YLE Finland                        ", "country": "فنلندا              ", "type": "صحيفة", "lang": "fi", "url": "https://feeds.yle.fi/uutiset/v1/recent.rss?publisherIds=YLE_UUTISET"},
    {"id": 10672 ,"name": "Hufvudstadsbladet                  ", "name_ar": "Hufvudstadsbladet                  ", "country": "فنلندا              ", "type": "صحيفة", "lang": "en", "url": "https://www.hbl.fi/feed"},

    # لاتفيا
    {"id": 10673 ,"name": "LSM Latvia                         ", "name_ar": "LSM Latvia                         ", "country": "لاتفيا              ", "type": "صحيفة", "lang": "lv", "url": "https://www.lsm.lv/en/rss"},
    {"id": 10674 ,"name": "TVNET Latvia                       ", "name_ar": "TVNET Latvia                       ", "country": "لاتفيا              ", "type": "صحيفة", "lang": "lv", "url": "https://www.tvnet.lv/rss"},
    {"id": 10675 ,"name": "Delfi Latvia                       ", "name_ar": "Delfi Latvia                       ", "country": "لاتفيا              ", "type": "صحيفة", "lang": "lv", "url": "https://www.delfi.lv/rss.xml"},
    {"id": 10676 ,"name": "Latvijas Avīze                     ", "name_ar": "Latvijas Avīze                     ", "country": "لاتفيا              ", "type": "صحيفة", "lang": "en", "url": "https://www.la.lv/feed"},

    # لبنان
    {"id": 10677 ,"name": "اللواء اللبنانية                   ", "name_ar": "اللواء اللبنانية                   ", "country": "لبنان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.al-liwa.net/rss"},
    {"id": 10678 ,"name": "الأخبار اللبنانية                  ", "name_ar": "الأخبار اللبنانية                  ", "country": "لبنان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.annahar.com/rss.xml"},
    {"id": 10679 ,"name": "عنب بلدي                           ", "name_ar": "عنب بلدي                           ", "country": "لبنان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.enabbaladi.net/rss"},
    {"id": 10680 ,"name": "تلفزيون سوريا                      ", "name_ar": "تلفزيون سوريا                      ", "country": "لبنان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.syriatv.org/feed"},
    {"id": 10681 ,"name": "أورينت نيوز سوريا                  ", "name_ar": "أورينت نيوز سوريا                  ", "country": "لبنان               ", "type": "صحيفة", "lang": "ar", "url": "https://www.enabbaladi.net/feed"},
    {"id": 10682 ,"name": "بلدي نيوز سوريا                    ", "name_ar": "بلدي نيوز سوريا                    ", "country": "لبنان               ", "type": "صحيفة", "lang": "ar", "url": "https://baladnews.com/feed"},

    # ليتوانيا
    {"id": 10683 ,"name": "15min Lithuania                    ", "name_ar": "15min Lithuania                    ", "country": "ليتوانيا            ", "type": "صحيفة", "lang": "lt", "url": "https://www.15min.lt/rss/naujienos"},
    {"id": 10684 ,"name": "Lrytas Lithuania                   ", "name_ar": "Lrytas Lithuania                   ", "country": "ليتوانيا            ", "type": "صحيفة", "lang": "lt", "url": "https://www.lrytas.lt/rss"},
    {"id": 10685 ,"name": "Verslo žinios LT                   ", "name_ar": "Verslo žinios LT                   ", "country": "ليتوانيا            ", "type": "صحيفة", "lang": "en", "url": "https://www.vz.lt/rss"},

    # مصر
    {"id": 10686 ,"name": "المصري اليوم                       ", "name_ar": "المصري اليوم                       ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.almasryalyoum.com/rss"},
    {"id": 10687 ,"name": "الشروق المصرية                     ", "name_ar": "الشروق المصرية                     ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.shorouknews.com/rss.xml"},
    {"id": 10688 ,"name": "مصر العربية                        ", "name_ar": "مصر العربية                        ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.masralarabia.net/feed"},
    {"id": 10689 ,"name": "بوابة اليوم                        ", "name_ar": "بوابة اليوم                        ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.alyaomonline.com/feed"},
    {"id": 10690 ,"name": "البديل المصري                      ", "name_ar": "البديل المصري                      ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://elbadil.com/feed"},
    {"id": 10691 ,"name": "صوت الأمة                          ", "name_ar": "صوت الأمة                          ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.soutalomma.com/rss"},
    {"id": 10692 ,"name": "عين مصر                            ", "name_ar": "عين مصر                            ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.ainmasralarabia.com/feed"},
    {"id": 10693 ,"name": "محيط مصر                           ", "name_ar": "محيط مصر                           ", "country": "مصر                 ", "type": "صحيفة", "lang": "ar", "url": "https://www.moheet.com/rss"},

    # ══════════════════════════════════════════
    # الجهات الحكومية القطرية (وزارات + هيئات + تويتر rsshub)
    # ══════════════════════════════════════════

    {"id": 10694 ,"name": "ديوان الأمير                                 ", "name_ar": "ديوان الأمير                                 ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/AmiriDiwan"},
    {"id": 10695 ,"name": "مجلس الوزراء القطري                          ", "name_ar": "مجلس الوزراء القطري                          ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/GCOQatar"},
    {"id": 10696 ,"name": "رئاسة مجلس الوزراء                           ", "name_ar": "رئاسة مجلس الوزراء                           ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://www.gco.gov.qa/ar/feed"},
    {"id": 10697 ,"name": "وزارة الداخلية القطرية                       ", "name_ar": "وزارة الداخلية                               ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOI_QatarEn"},
    {"id": 10698 ,"name": "وزارة الخارجية القطرية                       ", "name_ar": "وزارة الخارجية                               ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MofaQatar_AR"},
    {"id": 10699 ,"name": "وزارة الخارجية EN                            ", "name_ar": "وزارة الخارجية EN                            ", "country": "قطر", "type": "حكومي", "lang": "en", "url": "https://rsshub.app/twitter/user/MofaQatar_EN"},
    {"id": 10700 ,"name": "وزارة المالية القطرية                        ", "name_ar": "وزارة المالية                                ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOF_Qatar"},
    {"id": 10701 ,"name": "وزارة التربية والتعليم                       ", "name_ar": "وزارة التربية والتعليم                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOEQatar"},
    {"id": 10702 ,"name": "وزارة الصحة العامة                           ", "name_ar": "وزارة الصحة العامة                           ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOPHQatar"},
    {"id": 10703 ,"name": "وزارة العمل القطرية                          ", "name_ar": "وزارة العمل                                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOLQTR"},
    {"id": 10704 ,"name": "وزارة البيئة والمناخ                         ", "name_ar": "وزارة البيئة والتغير المناخي                 ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MECCC_Qatar"},
    {"id": 10705 ,"name": "وزارة الاتصالات وتقنية المعلومات             ", "name_ar": "وزارة الاتصالات                              ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MCITQatar"},
    {"id": 10706 ,"name": "وزارة التنمية الاجتماعية                     ", "name_ar": "وزارة التنمية الاجتماعية والأسرة             ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MSDF_Qatar"},
    {"id": 10707 ,"name": "وزارة الثقافة القطرية                        ", "name_ar": "وزارة الثقافة                                ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MC_Qatar"},
    {"id": 10708 ,"name": "وزارة التجارة والصناعة                       ", "name_ar": "وزارة التجارة والصناعة                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOCIQatar"},
    {"id": 10709 ,"name": "وزارة الشباب والرياضة                        ", "name_ar": "وزارة الشباب والرياضة                        ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MSYQatar"},
    {"id": 10710 ,"name": "وزارة العدل القطرية                          ", "name_ar": "وزارة العدل                                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/mojgovqa"},
    {"id": 10711 ,"name": "وزارة الأوقاف والشؤون الإسلامية              ", "name_ar": "وزارة الأوقاف                                ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/AwqafM"},
    {"id": 10712 ,"name": "وزارة البلديات والبيئة                       ", "name_ar": "وزارة البلديات والبيئة                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/albaladiya"},
    {"id": 10713 ,"name": "وزارة المواصلات والاتصالات                   ", "name_ar": "وزارة المواصلات                              ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/MOTQatar"},
    {"id": 10714 ,"name": "وكالة قطر للأنباء AR                         ", "name_ar": "وكالة قطر للأنباء                            ", "country": "قطر", "type": "وكالة أنباء", "lang": "ar", "url": "https://www.qna.org.qa/ar/rss"},
    {"id": 10715 ,"name": "وكالة قطر للأنباء EN                         ", "name_ar": "Qatar News Agency EN                         ", "country": "قطر", "type": "وكالة أنباء", "lang": "en", "url": "https://www.qna.org.qa/en/rss"},
    {"id": 10716 ,"name": "QNA Twitter                                  ", "name_ar": "وكالة قطر للأنباء تويتر                      ", "country": "قطر", "type": "وكالة أنباء", "lang": "ar", "url": "https://rsshub.app/twitter/user/QNAEnglish"},
    {"id": 10717 ,"name": "قطر تيليفزيون                                ", "name_ar": "قطر تليفزيون                                 ", "country": "قطر", "type": "تلفزيون", "lang": "ar", "url": "https://rsshub.app/twitter/user/AlKassTV"},
    {"id": 10718 ,"name": "بي ان سبورتس                                 ", "name_ar": "بي ان سبورتس                                 ", "country": "قطر", "type": "تلفزيون", "lang": "ar", "url": "https://rsshub.app/twitter/user/beINSPORTS"},
    {"id": 10719 ,"name": "مؤسسة قطر                                    ", "name_ar": "مؤسسة قطر                                    ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QF"},
    {"id": 10720 ,"name": "جهاز قطر للاستثمار                           ", "name_ar": "جهاز قطر للاستثمار QIA                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QatarQIA"},
    {"id": 10721 ,"name": "أشغال قطر                                    ", "name_ar": "أشغال - هيئة الأشغال العامة                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/AshghalQatar"},
    {"id": 10722 ,"name": "كهرماء قطر                                   ", "name_ar": "كهرماء                                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/kahramaa"},
    {"id": 10723 ,"name": "هيئة السياحة القطرية                         ", "name_ar": "هيئة السياحة القطرية                         ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/qtourism"},
    {"id": 10724 ,"name": "مؤسسة حمد الطبية                             ", "name_ar": "مؤسسة حمد الطبية                             ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/HMC_Qatar"},
    {"id": 10725 ,"name": "مؤسسة الرعاية الصحية الأولية                 ", "name_ar": "الرعاية الصحية الأولية                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/phcsg"},
    {"id": 10726 ,"name": "مركز قطر المالي QFC                          ", "name_ar": "مركز قطر المالي                              ", "country": "قطر", "type": "حكومي", "lang": "en", "url": "https://rsshub.app/twitter/user/QFCAuthority"},
    {"id": 10727 ,"name": "بورصة قطر                                    ", "name_ar": "بورصة قطر                                    ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QatarBursa"},
    {"id": 10728 ,"name": "قطر للسكك الحديدية                           ", "name_ar": "مترو الدوحة                                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/qrc_official"},
    {"id": 10729 ,"name": "قطر للطاقة                                   ", "name_ar": "قطر للطاقة                                   ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/qatarenergy"},
    {"id": 10730 ,"name": "قطر للطاقة RSS                               ", "name_ar": "قطر للطاقة أخبار                             ", "country": "قطر", "type": "حكومي", "lang": "en", "url": "https://www.qatarenergy.com.qa/En/MediaCentre/NewsReleases/PublishingImages/Pages/rss.aspx"},
    {"id": 10731 ,"name": "هيئة الطيران المدني قطر                      ", "name_ar": "هيئة الطيران المدني                          ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/CAAQATAR"},
    {"id": 10732 ,"name": "مواصلات قطر                                  ", "name_ar": "مواصلات                                      ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/Mowasalat_QAT"},
    {"id": 10733 ,"name": "بريد قطر                                     ", "name_ar": "بريد قطر                                     ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/Qatar_post"},
    {"id": 10734 ,"name": "بنك قطر للتنمية                              ", "name_ar": "بنك قطر للتنمية QDB                          ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QDB_Qatar"},
    {"id": 10735 ,"name": "الهلال الأحمر القطري                         ", "name_ar": "الهلال الأحمر القطري                         ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QRCS"},
    {"id": 10736 ,"name": "جامعة قطر                                    ", "name_ar": "جامعة قطر                                    ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QatarUniversity"},
    {"id": 10737 ,"name": "متاحف قطر                                    ", "name_ar": "متاحف قطر                                    ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/Qatar_Museums"},
    {"id": 10738 ,"name": "المكتبة الوطنية قطر                          ", "name_ar": "المكتبة الوطنية قطر                          ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QNLib"},
    {"id": 10739 ,"name": "قطر تشاريتي                                  ", "name_ar": "قطر تشاريتي                                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QatarCharity"},
    {"id": 10740 ,"name": "الجهاز المركزي للإحصاء                       ", "name_ar": "الجهاز المركزي للإحصاء PSA                   ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/psa_qatar"},
    {"id": 10741 ,"name": "وقود قطر                                     ", "name_ar": "وقود WOQOD                                   ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/WoqodQatar"},
    {"id": 10742 ,"name": "اللجنة العليا قطر 2022                       ", "name_ar": "اللجنة العليا للمشاريع والإرث                ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/theqatarsc"},
    {"id": 10743 ,"name": "المناطق الحرة قطر                            ", "name_ar": "المناطق الحرة بقطر QFZA                      ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QFZA_Qatar"},
    {"id": 10744 ,"name": "صندوق قطر للبحث العلمي                       ", "name_ar": "مجلس البحث العلمي QNRF                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QNRF_Qatar"},
    {"id": 10745 ,"name": "وكالة الفضاء القطرية                         ", "name_ar": "وكالة الفضاء القطرية                         ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QatarSpaceAgency"},
    {"id": 10746 ,"name": "هيئة الاتصالات قطر                           ", "name_ar": "هيئة الاتصالات CTRA                          ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/CTRA_Qatar"},
    {"id": 10747 ,"name": "هيئة الأسواق المالية                         ", "name_ar": "هيئة الأسواق المالية QFMA                    ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QFMA_Qatar"},
    {"id": 10748 ,"name": "هيئة حقوق الإنسان قطر                        ", "name_ar": "هيئة حقوق الإنسان                            ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/nhrcqatar"},
    {"id": 10749 ,"name": "معهد الدوحة للسياسات                         ", "name_ar": "معهد الدوحة للسياسات العامة                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/DohaInstitute"},
    {"id": 10750 ,"name": "مشيرب بروبرتيز                               ", "name_ar": "مشيرب للعقارات                               ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/Msheireb"},
    {"id": 10751 ,"name": "مدينة لوسيل                                  ", "name_ar": "مدينة لوسيل                                  ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/LusailCity_Q"},
    {"id": 10752 ,"name": "ميلاحة قطر                                   ", "name_ar": "ميلاحة                                       ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/milahaQatar"},
    {"id": 10753 ,"name": "الأرصاد الجوية قطر                           ", "name_ar": "الأرصاد الجوية قطر                           ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QMDQatar"},
    {"id": 10754 ,"name": "الجامعة العربية المفتوحة                     ", "name_ar": "الجامعة العربية المفتوحة                     ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/aou_qatar"},
    {"id": 10755 ,"name": "البنك المركزي القطري                         ", "name_ar": "البنك المركزي القطري QCB                     ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QCB_QatarCB"},
    {"id": 10756 ,"name": "شركة قطر للكهرباء والماء                     ", "name_ar": "قطر للكهرباء والماء                          ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/qewcQatar"},
    {"id": 10757 ,"name": "هيئة العقارات قطر                            ", "name_ar": "هيئة العقارات قطر                            ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/RealEstateQatar"},
    {"id": 10758 ,"name": "المجلس الوطني للسياحة                        ", "name_ar": "المجلس الوطني للسياحة                        ", "country": "قطر", "type": "حكومي", "lang": "ar", "url": "https://rsshub.app/twitter/user/QatarTourism"},
    {"id": 10759 ,"name": "الراية القطرية RSS                           ", "name_ar": "الراية                                       ", "country": "قطر", "type": "صحيفة", "lang": "ar", "url": "https://www.raya.com/home/rss"},
    {"id": 10760 ,"name": "Gulf Times Qatar                             ", "name_ar": "Gulf Times                                   ", "country": "قطر", "type": "صحيفة", "lang": "en", "url": "https://gulf-times.com/rss/tp"},
    {"id": 10761 ,"name": "Qatar Tribune                                ", "name_ar": "Qatar Tribune                                ", "country": "قطر", "type": "صحيفة", "lang": "en", "url": "https://www.qatar-tribune.com/rss/"},
    {"id": 10762 ,"name": "Lusail News قطر                              ", "name_ar": "لوسيل نيوز                                   ", "country": "قطر", "type": "رقمي", "lang": "ar", "url": "https://lusailnews.net/feed/"},
    {"id": 10763 ,"name": "ILoveQatar                                   ", "name_ar": "آي لاف قطر                                   ", "country": "قطر", "type": "رقمي", "lang": "en", "url": "https://www.iloveqatar.net/feed/"},
    {"id": 10764 ,"name": "Qatarday                                     ", "name_ar": "يوم قطر                                      ", "country": "قطر", "type": "رقمي", "lang": "en", "url": "https://www.qatarday.com/rss"},
    {"id": 10765 ,"name": "عرب تايمز قطر                                ", "name_ar": "عرب تايمز قطر                                ", "country": "قطر", "type": "رقمي", "lang": "ar", "url": "https://arabictimes.qa/feed/"},
    {"id": 10766 ,"name": "نبض قطر                                      ", "name_ar": "نبض قطر                                      ", "country": "قطر", "type": "رقمي", "lang": "ar", "url": "https://nabdqatar.com/feed/"},

    # ══════════════════════════════════════════
    # الجهات الحكومية القطرية (وزارات + هيئات + تويتر rsshub)
    # ══════════════════════════════════════════


    # حسابات إضافية صحيحة من البحث
    {"id": 10767 ,"name": "International Media Office Qatar             ", "name_ar": "مكتب الإعلام الدولي                          ", "country": "قطر", "type": "حكومي", "lang": "en", "url": "https://rsshub.app/twitter/user/IMO_Qatar"},
    {"id": 10768 ,"name": "Qatar Foundation RSS                         ", "name_ar": "مؤسسة قطر RSS                                ", "country": "قطر", "type": "حكومي", "lang": "en", "url": "https://www.qf.org.qa/rss.xml"},
    {"id": 10769 ,"name": "Qatar PR Network                             ", "name_ar": "قطر بي آر نتوورك                             ", "country": "قطر", "type": "رقمي", "lang": "ar", "url": "https://www.qatarprnetwork.com/RSSfeed.asp"},
    {"id": 10770 ,"name": "Qatar Stock Exchange RSS                     ", "name_ar": "بورصة قطر RSS                                ", "country": "قطر", "type": "حكومي", "lang": "en", "url": "https://www.qe.com.qa/web/venture-market/rss-feeds"},

]