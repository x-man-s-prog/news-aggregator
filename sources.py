# قائمة مصادر الأخبار مع روابط RSS — 800 مصدر
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

]
