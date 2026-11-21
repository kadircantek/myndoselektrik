# -*- coding: utf-8 -*-
"""
Tüm site metinleri (TR / EN / RU). Metni değiştirmek için burayı düzenleyin,
sonra `python build.py` çalıştırın.
"""

# ------------------------------------------------------------------
# HİZMET BÖLGELERİ (Yerel SEO için çok önemli)
# ------------------------------------------------------------------
AREAS = [
    ("Bodrum Merkez", "Bodrum Center", "Бодрум центр"),
    ("Yalıkavak", "Yalikavak", "Ялыкавак"),
    ("Gündoğan", "Gundogan", "Гюндоган"),
    ("Göltürkbükü", "Golturkbuku", "Гёльтюркбюкю"),
    ("Gölköy", "Golkoy", "Гёлькёй"),
    ("Torba", "Torba", "Торба"),
    ("Turgutreis", "Turgutreis", "Тургутрейс"),
    ("Gümüşlük", "Gumusluk", "Гюмюшлюк"),
    ("Bitez", "Bitez", "Битез"),
    ("Ortakent", "Ortakent", "Ортакент"),
    ("Yahşi", "Yahsi", "Яхши"),
    ("Konacık", "Konacik", "Конаджык"),
    ("Gümbet", "Gumbet", "Гюмбет"),
    ("Akyarlar", "Akyarlar", "Акъярлар"),
    ("Kadıkalesi", "Kadikalesi", "Кадыкалеси"),
    ("Güvercinlik", "Guvercinlik", "Гюверджинлик"),
    ("Yakaköy", "Yakakoy", "Якакёй"),
    ("Mumcular", "Mumcular", "Мумджулар"),
]

# ------------------------------------------------------------------
# HİZMETLER  (icon anahtarı, {lang: (başlık, açıklama)})
# ------------------------------------------------------------------
SERVICES = [
    ("smart", {
        "tr": ("Akıllı Ev Sistemleri", "Akıllı anahtar, priz, perde motoru ve sensör montajı. Işık, perde ve klimayı telefondan yönetin."),
        "en": ("Smart Home Systems", "Installation of smart switches, sockets, blind motors and sensors. Control lights, blinds and A/C from your phone."),
        "ru": ("Системы «Умный дом»", "Монтаж умных выключателей, розеток, моторов штор и датчиков. Управляйте светом, шторами и кондиционером с телефона."),
    }),
    ("auto", {
        "tr": ("Ev & Villa Otomasyonu", "Senaryo, zamanlayıcı ve sensörlü otomasyon kurulumu. Villa, otel ve işyerleri için uzaktan kontrol edilebilen sistemler."),
        "en": ("Home & Villa Automation", "Automation with scenes, timers and sensors. Remotely controllable systems for villas, hotels and businesses."),
        "ru": ("Автоматизация домов и вилл", "Автоматизация со сценариями, таймерами и датчиками. Системы с удалённым управлением для вилл, отелей и бизнеса."),
    }),
    ("plug", {
        "tr": ("Elektrik Tesisatı", "Yeni yapı ve villa elektrik tesisatı, pano montajı, topraklama, kaçak akım rölesi montajı. Yönetmeliğe uygun, temiz ve titiz işçilik."),
        "en": ("Electrical Installation", "Complete wiring for new builds and villas, distribution boards, earthing and RCD installation — clean, careful, code‑compliant workmanship."),
        "ru": ("Электромонтаж", "Монтаж электропроводки в новостройках и виллах: щиты, заземление, УЗО. Аккуратная работа строго по нормам."),
    }),
    ("wrench", {
        "tr": ("Tamir & Tadilat", "Eski tesisat yenileme, priz‑anahtar değişimi, sigorta ve kablo arızaları, tadilat sırasında elektrik altyapısının baştan kurulması."),
        "en": ("Repair & Renovation", "Rewiring old installations, socket & switch replacement, breaker and cable faults, complete electrical upgrades during renovations."),
        "ru": ("Ремонт и реконструкция", "Замена старой проводки, розеток и выключателей, устранение неисправностей автоматов и кабелей, полная модернизация при ремонте."),
    }),
    ("shield", {
        "tr": ("Bakım & Onarım", "Villa, site ve işletmeler için periyodik elektrik bakımı, pano kontrolü ve sezon öncesi güvenlik kontrolleri."),
        "en": ("Maintenance & Service", "Scheduled electrical maintenance for villas, complexes and businesses: panel checks and pre‑season safety checks."),
        "ru": ("Обслуживание и сервис", "Плановое обслуживание электрики вилл, комплексов и бизнеса: проверка щитов и проверка перед сезоном."),
    }),
    ("tree", {
        "tr": ("Çevre & Bahçe Aydınlatma", "Peyzaj, bahçe, havuz ve cephe aydınlatması. Ağaç aydınlatma, yol armatürleri ve LED havuz ışıklarının montajı."),
        "en": ("Garden & Outdoor Lighting", "Landscape, garden, pool and facade lighting. Installation of tree uplights, path lights and LED pool lights."),
        "ru": ("Ландшафтное освещение", "Освещение сада, бассейна и фасада. Монтаж подсветки деревьев, дорожек и LED‑освещения бассейна."),
    }),
    ("chandelier", {
        "tr": ("Avize Montajı", "Kristal, modern ve ağır avizelerin güvenli montajı. Yüksek tavanlarda montaj ve dimmer bağlantısı."),
        "en": ("Chandelier Installation", "Safe installation of crystal, modern and heavy chandeliers. Experts in high ceilings, double‑height spaces and dimmer connections."),
        "ru": ("Монтаж люстр", "Надёжный монтаж хрустальных, современных и тяжёлых люстр. Высокие потолки, двусветные пространства, подключение диммеров."),
    }),
    ("bolt", {
        "tr": ("7/24 Acil Elektrikçi", "Elektrik kesintisi, kısa devre, sigorta atması ya da yanık kokusu? Bodrum'un her yerine gece‑gündüz hızlı acil elektrik servisi."),
        "en": ("24/7 Emergency Electrician", "Power cut, short circuit, tripping breakers or burning smell? Fast emergency electrician service day and night across Bodrum."),
        "ru": ("Аварийный электрик 24/7", "Нет света, короткое замыкание, выбивает автомат или запах гари? Быстрый выезд электрика днём и ночью по всему Бодруму."),
    }),
]

ICONS = {
    "smart": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M9.5 15a3.5 3.5 0 015 0"/><path d="M7.5 12.5a6.5 6.5 0 019 0"/><path d="M12 18h.01"/>',
    "auto": '<rect x="5" y="5" width="14" height="14" rx="3"/><rect x="9" y="9" width="6" height="6" rx="1"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
    "plug": '<path d="M9 2v6M15 2v6"/><path d="M6 8h12v3a6 6 0 01-12 0z"/><path d="M12 17v5"/>',
    "wrench": '<path d="M14.7 6.3a4 4 0 00-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 005.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "shield": '<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
    "tree": '<path d="M12 22v-7"/><path d="M12 2C8 2 6 5 6 8c0 3 2.5 5 6 5s6-2 6-5c0-3-2-6-6-6z"/><path d="M6 22h12"/><path d="M3 18l2.5-1M21 18l-2.5-1M12 13l-2 2M12 15l2-2"/>',
    "chandelier": '<path d="M12 2v5"/><path d="M4 10c0 2.5 3.5 4 8 4s8-1.5 8-4"/><path d="M4 10V8m16 2V8M12 14v2"/><circle cx="4" cy="12.5" r="1.4"/><circle cx="20" cy="12.5" r="1.4"/><path d="M12 16l-2 3h4z"/><path d="M12 19v2"/>',
    "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
}

# ------------------------------------------------------------------
# GALERİ (dosya, {lang: (bölge, başlık)})
# ------------------------------------------------------------------
GALLERY = [
    ("hero", {"tr": ("Aydınlatma", "Villa cephe ve havuz aydınlatması"), "en": ("Lighting", "Villa facade and pool lighting"), "ru": ("Освещение", "Подсветка фасада и бассейна виллы")}),
    ("chandelier", {"tr": ("Avize Montajı", "Yüksek tavan avize montajı"), "en": ("Chandeliers", "High‑ceiling chandelier installation"), "ru": ("Люстры", "Монтаж люстры на высоком потолке")}),
    ("electrical-panel", {"tr": ("Tesisat", "Elektrik panosu montajı"), "en": ("Installation", "Distribution board installation"), "ru": ("Электромонтаж", "Монтаж электрощита")}),
    ("garden-lighting", {"tr": ("Bahçe Aydınlatma", "Peyzaj ve bahçe aydınlatması"), "en": ("Garden Lighting", "Landscape and garden lighting"), "ru": ("Освещение сада", "Ландшафтное освещение")}),
    ("led-lighting", {"tr": ("LED", "Gizli LED şerit aydınlatma"), "en": ("LED", "Hidden LED strip lighting"), "ru": ("LED", "Скрытая LED‑подсветка")}),
    ("pool-lighting", {"tr": ("Havuz", "LED havuz aydınlatması"), "en": ("Pool", "LED pool lighting"), "ru": ("Бассейн", "LED‑освещение бассейна")}),
    ("smart-home", {"tr": ("Akıllı Ev", "Akıllı ev kontrol paneli"), "en": ("Smart Home", "Smart home control panel"), "ru": ("Умный дом", "Панель умного дома")}),
    ("renovation", {"tr": ("Tadilat", "Elektrik tesisatı yenileme"), "en": ("Renovation", "Electrical rewiring"), "ru": ("Ремонт", "Замена проводки")}),
]

# ------------------------------------------------------------------
# SSS / FAQ (FAQPage schema ile Google'da zengin sonuç)
# ------------------------------------------------------------------
FAQ = {
    "tr": [
        ("Bodrum'da 7/24 acil elektrikçi hizmeti veriyor musunuz?", "Evet. Bodrum merkez, Yalıkavak, Turgutreis, Gündoğan, Bitez ve tüm Bodrum yarımadasında gece‑gündüz, hafta sonu ve bayramlar dahil acil elektrik arıza servisi veriyoruz. Telefon veya WhatsApp ile hemen ulaşabilirsiniz."),
        ("Malzemeyi siz mi sağlıyorsunuz?", "Hayır, malzeme satışı yapmıyoruz. Avize, armatür, akıllı ev cihazı gibi ürünleri siz alıyorsunuz; biz montajını ve bağlantısını yapıyoruz. İsterseniz satın almadan önce hangi ürünün uygun olduğu konusunda ücretsiz bilgi veriyoruz."),
        ("Hangi bölgelere hizmet veriyorsunuz?", "Bodrum Merkez, Yalıkavak, Gündoğan, Göltürkbükü, Gölköy, Torba, Turgutreis, Gümüşlük, Bitez, Ortakent, Yahşi, Konacık, Gümbet, Akyarlar, Kadıkalesi, Güvercinlik, Yakaköy ve Mumcular dahil tüm Bodrum'a hizmet veriyoruz."),
        ("Mevcut evime kırıp dökmeden akıllı ev sistemi kurulabilir mi?", "Evet. Kablosuz akıllı anahtar, priz, perde motoru ve sensörlerle mevcut tesisatı bozmadan montaj yapıyoruz."),
        ("Akıllı ev sistemi kurulumu ne kadar sürer?", "İşin büyüklüğüne göre değişir. Evi gördükten sonra ne kadar süreceğini net olarak söylüyoruz."),
        ("Ağır ve yüksek tavanlı avize montajı yapıyor musunuz?", "Evet. Kristal ve ağır avizeleri uygun bağlantı elemanlarıyla, yüksek tavanlarda da güvenle monte ediyor; dimmer ve akıllı kontrol bağlantısını yapıyoruz."),
        ("Elektrik tesisatı ne zaman yenilenmeli?", "Sigortalar sık atıyorsa, prizlerde ısınma veya yanık kokusu varsa, tesisat 20 yıldan eskiyse ya da kaçak akım rölesi yoksa tesisatınızın kontrol edilip yenilenmesi gerekir."),
        ("Fiyatı ne zaman öğrenebilirim?", "İşi gördükten sonra, işe başlamadan önce fiyatı net olarak söylüyoruz. Sonradan sürpriz ücret çıkmaz."),
        ("Yaptığınız işlere garanti veriyor musunuz?", "Evet. Yaptığımız montaj ve işçilikte bir sorun çıkarsa tekrar gelip ilgileniyoruz."),
        ("Yabancı müşteriler size kendi dilinde ulaşabilir mi?", "Evet. WhatsApp'tan İngilizce veya Rusça yazabilirsiniz; mesajınızı çeviri ile anlayıp size dönüş yapıyoruz."),
    ],
    "en": [
        ("Do you offer a 24/7 emergency electrician in Bodrum?", "Yes. We provide day and night emergency electrical repair across Bodrum Center, Yalikavak, Turgutreis, Gundogan, Bitez and the entire Bodrum peninsula — including weekends and holidays. Call or WhatsApp us any time."),
        ("Do you supply the materials?", "No, we don't sell materials. You purchase the products (chandeliers, fixtures, smart home devices etc.) and we take care of the installation and wiring. We're happy to advise you for free on what to buy beforehand."),
        ("Which areas do you cover?", "We cover all of Bodrum including Bodrum Center, Yalikavak, Gundogan, Golturkbuku, Golkoy, Torba, Turgutreis, Gumusluk, Bitez, Ortakent, Yahsi, Konacik, Gumbet, Akyarlar, Kadikalesi, Guvercinlik, Yakakoy and Mumcular."),
        ("Can you install a smart home without breaking walls?", "Yes. We install wireless smart switches, sockets, blind motors and sensors without touching the existing wiring."),
        ("How long does a smart home installation take?", "It depends on the size of the job. Once we see the property we tell you clearly how long it will take."),
        ("Do you install heavy chandeliers on high ceilings?", "Yes. We safely mount crystal and heavy chandeliers with proper fixings, including on high ceilings, and connect dimmers and smart controls."),
        ("When should electrical wiring be replaced?", "If breakers trip often, sockets get hot or smell burnt, the wiring is older than 20 years, or there is no RCD (residual current device), your installation should be inspected and renewed."),
        ("When will I know the price?", "After seeing the job and before starting, we tell you the price clearly. No surprise charges afterwards."),
        ("Do you guarantee your work?", "Yes. If there is any problem with our installation or workmanship, we come back and fix it."),
        ("Can I contact you in English?", "Yes. Just send us a WhatsApp message in English — we use translation to understand your request and reply to you."),
    ],
    "ru": [
        ("Есть ли у вас аварийный электрик 24/7 в Бодруме?", "Да. Мы выезжаем днём и ночью, включая выходные и праздники, по всему полуострову Бодрум: центр Бодрума, Ялыкавак, Тургутрейс, Гюндоган, Битез и другие районы. Звоните или пишите в WhatsApp."),
        ("Вы продаёте материалы?", "Нет, мы не продаём материалы. Оборудование (люстры, светильники, устройства умного дома и т.д.) покупаете вы, а мы выполняем монтаж и подключение. Перед покупкой бесплатно подскажем, что лучше выбрать."),
        ("В каких районах вы работаете?", "Мы работаем по всему Бодруму: центр Бодрума, Ялыкавак, Гюндоган, Гёльтюркбюкю, Гёлькёй, Торба, Тургутрейс, Гюмюшлюк, Битез, Ортакент, Яхши, Конаджык, Гюмбет, Акъярлар, Кадыкалеси, Гюверджинлик, Якакёй и Мумджулар."),
        ("Можно ли сделать умный дом без штробления стен?", "Да. Мы монтируем беспроводные умные выключатели, розетки, моторы штор и датчики, не трогая существующую проводку."),
        ("Сколько времени занимает установка умного дома?", "Зависит от объёма работ. Посмотрев объект, мы точно скажем, сколько это займёт."),
        ("Монтируете ли вы тяжёлые люстры на высоких потолках?", "Да. Мы надёжно монтируем хрустальные и тяжёлые люстры с правильным креплением, в том числе на высоких потолках, и подключаем диммеры и умное управление."),
        ("Когда нужно менять электропроводку?", "Если часто выбивает автоматы, розетки греются или пахнут гарью, проводке более 20 лет или нет УЗО — электрику нужно проверить и обновить."),
        ("Когда я узнаю цену?", "Посмотрев объект, до начала работ мы чётко называем цену. Никаких неожиданных доплат."),
        ("Даёте ли вы гарантию на работы?", "Да. Если с нашим монтажом возникнет проблема, мы приедем и всё исправим."),
        ("Можно написать вам на русском языке?", "Да. Напишите нам в WhatsApp на русском — мы переведём сообщение и ответим вам."),
    ],
}

TESTIMONIALS = {
    "tr": [
        ("Gece 2'de elektrik kesildi, 30 dakikada geldiler. Çok temiz ve profesyonel çalıştılar. Bodrum'da en güvendiğim elektrikçi.", "Mehmet K.", "Yalıkavak"),
        ("Villamızın tüm bahçe ve havuz aydınlatmasının montajını yaptılar. Akşamları misafirlerimiz hayran kalıyor!", "Ayşe & Can T.", "Göltürkbükü"),
        ("Evimizi kırıp dökmeden akıllı ev yaptılar. Perde, ışık, klima hepsi telefonda. Harika iş.", "Selin D.", "Bitez"),
    ],
    "en": [
        ("Our power went out at 2am and they arrived within 30 minutes. Clean, professional and fair. The electrician we trust in Bodrum.", "James R.", "Yalikavak"),
        ("They installed the full garden and pool lighting for our villa. Our guests are amazed every evening!", "Sarah & Tom W.", "Gundogan"),
        ("Smart home without breaking a single wall. Blinds, lights and A/C all on my phone. Excellent work.", "Michael B.", "Turgutreis"),
    ],
    "ru": [
        ("Ночью пропал свет — приехали за 30 минут. Работают чисто и профессионально. Лучший электрик в Бодруме!", "Елена П.", "Ялыкавак"),
        ("Сделали всё освещение сада и бассейна на нашей вилле. Гости каждый вечер в восторге!", "Андрей и Ольга С.", "Тургутрейс"),
        ("Умный дом без ремонта стен: шторы, свет, кондиционер — всё в телефоне. Очень довольны.", "Дмитрий К.", "Гюндоган"),
    ],
}

# ------------------------------------------------------------------
# GENEL METİNLER
# ------------------------------------------------------------------
T = {
"tr": dict(
    lang="tr", locale="tr_TR", path="",
    wa_text="Merhaba, elektrik hizmetinizden faydalanmak istiyorum. Bilgi alabilir miyim?",
    title="Bodrum Elektrikçi | Myndos Elektrik – 7/24 Akıllı Ev & Aydınlatma",
    desc="Myndos Elektrik: Bodrum elektrikçi – 7/24 acil arıza, elektrik tesisatı, akıllı ev sistemleri, otomasyon, avize montajı, bahçe ve çevre aydınlatma. Yalıkavak'tan Turgutreis'e tüm Bodrum'a hızlı servis.",
    keywords="myndos elektrik, bodrum elektrikçi, bodrum elektrik ustası, bodrum acil elektrikçi, bodrum 7/24 elektrikçi, nöbetçi elektrikçi bodrum, bodrum elektrik arıza, bodrum elektrik tesisatı, bodrum akıllı ev sistemleri, bodrum ev otomasyonu, bodrum villa otomasyonu, bodrum KNX, bodrum avize montajı, bodrum bahçe aydınlatma, bodrum peyzaj aydınlatma, bodrum çevre aydınlatma, bodrum havuz aydınlatma, bodrum led aydınlatma, bodrum elektrik bakım onarım, bodrum elektrik tadilat, bodrum pano montajı, bodrum sigorta tamiri, yalıkavak elektrikçi, turgutreis elektrikçi, gündoğan elektrikçi, bitez elektrikçi, gümbet elektrikçi, ortakent elektrikçi, konacık elektrikçi, göltürkbükü elektrikçi, gölköy elektrikçi, torba elektrikçi, gümüşlük elektrikçi, yahşi elektrikçi, akyarlar elektrikçi, muğla elektrikçi, en yakın elektrikçi, villa elektrikçi bodrum",
    nav_services="Hizmetler", nav_smart="Akıllı Ev", nav_gallery="Örnekler", nav_areas="Bölgeler", nav_faq="SSS", nav_contact="İletişim",
    call="Hemen Ara", topbar="7/24 acil elektrikçi – Bodrum'un her yerine hızlı servis:",
    badge="Bodrum Geneli 7/24 Elektrik Hizmeti",
    h1='Bodrum Elektrikçi<br><span class="glow-text">Güvenli Elektrik, Temiz İşçilik.</span>',
    lead="Elektrik tesisatı, arıza onarımı, akıllı ev sistemleri, avize montajı ve bahçe aydınlatması. Bodrum'un tüm bölgelerinde hızlı, temiz ve garantili işçilik.",
    cta_call="Hemen Ara", cta_wa="WhatsApp'tan Yaz",
    s_years="Yıllık Deneyim", s_jobs="Tamamlanan İş", s_support="Acil Destek", s_areas="Hizmet Bölgesi",
    bulb_hint="Ampule dokun – ışıkları aç / kapat",
    ticker_suffix="Elektrikçi",
    sv_k="Hizmetlerimiz", sv_t="Bodrum Genelinde Elektrik Hizmetleri", sv_p="Villa, daire, otel ve işyerleri için elektrik montaj ve onarım hizmeti. Malzemeyi siz alırsınız, montajı biz yaparız.",
    sm_k="Akıllı Ev & Otomasyon", sm_t="Akıllı Ev Sistemleri",
    sm_p="Akıllı anahtar, priz, perde motoru ve sensörlerin montajını yapıyoruz. Aşağıdaki örnek panelden nasıl çalıştığını deneyebilirsiniz.",
    sm_1="Işık, perde ve klimayı telefondan kontrol", sm_2="Google, Alexa veya Siri sesli asistan bağlantısı", sm_3="Kamera ve alarm sistemi bağlantısı", sm_4="Zamanlayıcı ve senaryo ayarları",
    pn_t="Örnek Kontrol Paneli", pn_on="Bağlı", z_living="Salon Işıkları", z_led="LED Şerit", z_garden="Bahçe", z_pool="Havuz", z_curtain="Perdeler",
    sc_movie="🎬 Film Modu", sc_dinner="🍷 Akşam Yemeği", sc_all="☀️ Tümü Açık", sc_off="🌙 Tümü Kapalı", room_tag="Örnek – düğmelere dokunun",
    sm_cta="Bilgi Al",
    wy_k="Neden Biz?", wy_t="Neden Myndos Elektrik?",
    w1t="7/24 Hızlı Servis", w1p="Acil arızalarda Bodrum'un her bölgesine hızlı ulaşıyoruz.",
    w2t="Düzgün İşçilik", w2p="Yönetmeliğe uygun, temiz ve düzenli çalışma.",
    w3t="Şeffaf Fiyat", w3p="Fiyatı işe başlamadan önce net olarak söylüyoruz.",
    w4t="Garantili İş", w4p="Yaptığımız işin arkasındayız.",
    gl_k="Örnekler", gl_t="Hizmet Örnekleri", gl_p="Yaptığımız iş türlerinden örnekler.",
    ar_k="Hizmet Bölgeleri", ar_t="Hizmet Verdiğimiz Bölgeler", ar_p="Bodrum yarımadasının tamamında hizmet veriyoruz.",
    ar_text="Yalıkavak, Turgutreis, Gündoğan, Bitez, Gümbet, Ortakent, Konacık ve Bodrum'un diğer tüm bölgelerinde elektrik arızası, tesisat, akıllı ev, avize montajı ve aydınlatma işleri için bize ulaşabilirsiniz.",
    ts_k="Müşteri Yorumları", ts_t="Müşterilerimiz Ne Diyor?",
    fq_k="Sıkça Sorulan Sorular", fq_t="Merak Ettikleriniz",
    ct_k="İletişim", ct_t="Bize Ulaşın", ct_p="Fiyat bilgisi ve randevu için arayın ya da formu doldurun, size WhatsApp'tan dönelim.",
    c_phone="Telefon (7/24)", c_wa="WhatsApp", c_mail="E‑posta", c_area="Hizmet Bölgesi", c_area_v="Bodrum, Muğla – tüm yarımada", c_hours="Çalışma Saatleri", c_hours_v="7 gün 24 saat",
    f_name="Adınız", f_phone="Telefonunuz", f_service="Hizmet", f_msg="Mesajınız", f_send="WhatsApp ile Gönder", f_hello="Merhaba, web sitenizden ulaşıyorum.", f_ph_msg="Örn: Yalıkavak'taki villam için bahçe aydınlatması istiyorum...",
    map_title="Bodrum hizmet bölgesi haritası",
    ft_about="Bodrum'da elektrik tesisatı, akıllı ev sistemleri, otomasyon, avize montajı, bakım onarım ve çevre aydınlatma alanında 7/24 profesyonel hizmet.",
    ft_services="Hizmetler", ft_areas="Bölgeler", rights="Tüm hakları saklıdır.",
    seo="Myndos Elektrik; Bodrum ve çevresinde elektrik tesisatı, elektrik arıza onarımı, pano ve sigorta işleri, bakım onarım, akıllı ev ve otomasyon sistemleri, avize montajı, LED, bahçe, havuz ve cephe aydınlatması montajı yapmaktadır. Hizmet bölgeleri: Bodrum Merkez, Yalıkavak, Gündoğan, Göltürkbükü, Gölköy, Torba, Turgutreis, Gümüşlük, Bitez, Ortakent, Yahşi, Konacık, Gümbet, Akyarlar ve Kadıkalesi.",
    lang_pop="Bu sayfayı tercih ettiğiniz dilde görüntüleyin:", full="Türkçe",
),
"en": dict(
    lang="en", locale="en_GB", path="en/",
    wa_text="Hello, I would like to use your electrical services. Could you give me some information?",
    title="Electrician in Bodrum | Myndos Elektrik – 24/7 Smart Home & Lighting",
    desc="Myndos Elektrik – trusted electrician in Bodrum – 24/7 emergency repairs, electrical installation, smart home & automation, chandelier installation, garden and pool lighting. Yalikavak, Turgutreis, Gundogan & all Bodrum.",
    keywords="myndos elektrik, electrician bodrum, bodrum electrician, emergency electrician bodrum, 24/7 electrician bodrum, electrician yalikavak, electrician turgutreis, electrician gundogan, electrician bitez, electrician gumbet, electrician torba, electrician golturkbuku, smart home bodrum, home automation bodrum, villa automation turkey, KNX bodrum, chandelier installation bodrum, garden lighting bodrum, landscape lighting bodrum, pool lighting bodrum, led lighting bodrum, electrical installation bodrum, rewiring bodrum, electrical repair bodrum, villa electrician bodrum, electrician near me bodrum, electrician mugla turkey",
    nav_services="Services", nav_smart="Smart Home", nav_gallery="Examples", nav_areas="Areas", nav_faq="FAQ", nav_contact="Contact",
    call="Call Now", topbar="24/7 emergency electrician – fast service anywhere in Bodrum:",
    badge="24/7 Electrical Service Across Bodrum",
    h1='Electrician in Bodrum<br><span class="glow-text">Safe Wiring, Clean Workmanship.</span>',
    lead="Electrical installation, fault repair, smart home systems, chandelier installation and garden lighting. Fast, clean and guaranteed workmanship across all of Bodrum.",
    cta_call="Call Now", cta_wa="Message on WhatsApp",
    s_years="Years Experience", s_jobs="Completed Jobs", s_support="Emergency Support", s_areas="Service Areas",
    bulb_hint="Tap the bulb – switch the lights on / off",
    ticker_suffix="Electrician",
    sv_k="Our Services", sv_t="Electrical Services Across Bodrum", sv_p="Electrical installation and repair for villas, apartments, hotels and businesses. You buy the products — we install them.",
    sm_k="Smart Home & Automation", sm_t="Smart Home Systems",
    sm_p="We install smart switches, sockets, blind motors and sensors. Try the example panel below to see how it works.",
    sm_1="Control lights, blinds and A/C from your phone", sm_2="Google, Alexa or Siri voice assistant setup", sm_3="Camera and alarm system connection", sm_4="Timers and scene settings",
    pn_t="Example Control Panel", pn_on="Online", z_living="Living Room", z_led="LED Strip", z_garden="Garden", z_pool="Pool", z_curtain="Blinds",
    sc_movie="🎬 Movie Mode", sc_dinner="🍷 Dinner", sc_all="☀️ All On", sc_off="🌙 All Off", room_tag="Example – tap the switches",
    sm_cta="Get Info",
    wy_k="Why Choose Us", wy_t="Why Myndos Elektrik?",
    w1t="24/7 Fast Response", w1p="We reach every part of Bodrum quickly for emergencies.",
    w2t="Proper Workmanship", w2p="Clean, tidy and code‑compliant work.",
    w3t="Transparent Pricing", w3p="We tell you the price clearly before we start.",
    w4t="Guaranteed Work", w4p="We stand behind our work.",
    gl_k="Examples", gl_t="Service Examples", gl_p="Examples of the types of work we do.",
    ar_k="Service Areas", ar_t="Areas We Serve", ar_p="We work across the entire Bodrum peninsula.",
    ar_text="Contact us for electrical faults, installation, smart home, chandelier installation and lighting work in Yalikavak, Turgutreis, Gundogan, Bitez, Gumbet, Ortakent, Konacik and all other areas of Bodrum.",
    ts_k="Reviews", ts_t="What Our Clients Say",
    fq_k="FAQ", fq_t="Frequently Asked Questions",
    ct_k="Contact", ct_t="Contact Us", ct_p="Call for pricing and appointments, or fill in the form and we'll get back to you on WhatsApp.",
    c_phone="Phone (24/7)", c_wa="WhatsApp", c_mail="Email", c_area="Service Area", c_area_v="Bodrum, Mugla – entire peninsula", c_hours="Working Hours", c_hours_v="7 days, 24 hours",
    f_name="Your Name", f_phone="Your Phone", f_service="Service", f_msg="Your Message", f_send="Send via WhatsApp", f_hello="Hello, I'm contacting you from your website.", f_ph_msg="E.g. I need garden lighting for my villa in Yalikavak...",
    map_title="Bodrum service area map",
    ft_about="Professional 24/7 electrical installation, smart home systems, automation, chandelier installation, maintenance and outdoor lighting in Bodrum.",
    ft_services="Services", ft_areas="Areas", rights="All rights reserved.",
    seo="Myndos Elektrik provides electrical installation, fault repair, distribution boards and breakers, maintenance, smart home and automation systems, chandelier installation, LED, garden, pool and facade lighting installation in Bodrum and the surrounding area. Service areas: Bodrum Center, Yalikavak, Gundogan, Golturkbuku, Golkoy, Torba, Turgutreis, Gumusluk, Bitez, Ortakent, Yahsi, Konacik, Gumbet, Akyarlar and Kadikalesi.",
    lang_pop="View this page in your preferred language:", full="English",
),
"ru": dict(
    lang="ru", locale="ru_RU", path="ru/",
    wa_text="Здравствуйте, хочу воспользоваться вашими услугами электрика. Можно узнать подробнее?",
    title="Электрик в Бодруме 24/7 | Myndos Elektrik – умный дом, освещение",
    desc="Myndos Elektrik – электрик в Бодруме 24/7: аварийный выезд, электромонтаж, умный дом и автоматизация, монтаж люстр, освещение сада и бассейна. Ялыкавак, Тургутрейс, Гюндоган и весь Бодрум. Пишите в WhatsApp на русском.",
    keywords="myndos elektrik, электрик бодрум, электрик в бодруме, аварийный электрик бодрум, электрик 24/7 бодрум, электрик ялыкавак, электрик тургутрейс, электрик гюндоган, электрик битез, электрик гюмбет, умный дом бодрум, умный дом турция, автоматизация виллы бодрум, KNX бодрум, монтаж люстры бодрум, освещение сада бодрум, ландшафтное освещение бодрум, освещение бассейна бодрум, LED подсветка бодрум, электромонтаж бодрум, замена проводки бодрум, ремонт электрики бодрум, электрик для виллы турция, электрик мугла",
    nav_services="Услуги", nav_smart="Умный дом", nav_gallery="Примеры", nav_areas="Районы", nav_faq="Вопросы", nav_contact="Контакты",
    call="Позвонить", topbar="Аварийный электрик 24/7 – быстрый выезд по всему Бодруму:",
    badge="Электрик 24/7 по всему Бодруму",
    h1='Электрик в Бодруме<br><span class="glow-text">Надёжная электрика, аккуратная работа.</span>',
    lead="Электромонтаж, ремонт неисправностей, умный дом, монтаж люстр и освещение сада. Быстро, аккуратно и с гарантией по всему Бодруму. Пишите в WhatsApp на русском.",
    cta_call="Позвонить", cta_wa="Написать в WhatsApp",
    s_years="Лет опыта", s_jobs="Выполненных работ", s_support="Аварийная служба", s_areas="Районов",
    bulb_hint="Нажмите на лампу – включите / выключите свет",
    ticker_suffix="электрик",
    sv_k="Наши услуги", sv_t="Электроуслуги по всему Бодруму", sv_p="Электромонтаж и ремонт для вилл, квартир, отелей и бизнеса. Оборудование покупаете вы — монтаж делаем мы.",
    sm_k="Умный дом и автоматизация", sm_t="Системы умного дома",
    sm_p="Мы монтируем умные выключатели, розетки, моторы штор и датчики. Попробуйте пример панели ниже, чтобы увидеть, как это работает.",
    sm_1="Управление светом, шторами и кондиционером с телефона", sm_2="Подключение голосовых ассистентов Google, Alexa, Siri", sm_3="Подключение камер и сигнализации", sm_4="Таймеры и сценарии",
    pn_t="Пример панели управления", pn_on="Онлайн", z_living="Гостиная", z_led="LED‑лента", z_garden="Сад", z_pool="Бассейн", z_curtain="Шторы",
    sc_movie="🎬 Кино", sc_dinner="🍷 Ужин", sc_all="☀️ Всё вкл.", sc_off="🌙 Всё выкл.", room_tag="Пример – нажимайте кнопки",
    sm_cta="Узнать подробнее",
    wy_k="Почему мы", wy_t="Почему Myndos Elektrik?",
    w1t="Быстрый выезд 24/7", w1p="При авариях быстро приезжаем в любой район Бодрума.",
    w2t="Аккуратная работа", w2p="Чисто, аккуратно и по нормам.",
    w3t="Честные цены", w3p="Называем цену до начала работ.",
    w4t="Гарантия", w4p="Отвечаем за свою работу.",
    gl_k="Примеры", gl_t="Примеры работ", gl_p="Примеры видов работ, которые мы выполняем.",
    ar_k="Районы обслуживания", ar_t="Районы обслуживания", ar_p="Работаем на всём полуострове Бодрум.",
    ar_text="Обращайтесь к нам по неисправностям электрики, электромонтажу, умному дому, монтажу люстр и освещению в Ялыкаваке, Тургутрейсе, Гюндогане, Битезе, Гюмбете, Ортакенте, Конаджыке и других районах Бодрума.",
    ts_k="Отзывы", ts_t="Что говорят клиенты",
    fq_k="Вопросы", fq_t="Частые вопросы",
    ct_k="Контакты", ct_t="Свяжитесь с нами", ct_p="Позвоните, чтобы узнать цену и записаться, или заполните форму — мы ответим в WhatsApp.",
    c_phone="Телефон (24/7)", c_wa="WhatsApp", c_mail="Эл. почта", c_area="Район работы", c_area_v="Бодрум, Мугла – весь полуостров", c_hours="Часы работы", c_hours_v="7 дней, 24 часа",
    f_name="Ваше имя", f_phone="Ваш телефон", f_service="Услуга", f_msg="Сообщение", f_send="Отправить в WhatsApp", f_hello="Здравствуйте, пишу с вашего сайта.", f_ph_msg="Например: нужно освещение сада для виллы в Ялыкаваке...",
    map_title="Карта района обслуживания Бодрум",
    ft_about="Профессиональный электромонтаж, умный дом, автоматизация, монтаж люстр, обслуживание и наружное освещение в Бодруме 24/7.",
    ft_services="Услуги", ft_areas="Районы", rights="Все права защищены.",
    seo="Myndos Elektrik выполняет электромонтаж, ремонт неисправностей, работы с электрощитами и автоматами, обслуживание, монтаж систем умного дома и автоматизации, монтаж люстр, LED‑подсветки, освещения сада, бассейна и фасада в Бодруме и окрестностях. Районы: центр Бодрума, Ялыкавак, Гюндоган, Гёльтюркбюкю, Гёлькёй, Торба, Тургутрейс, Гюмюшлюк, Битез, Ортакент, Яхши, Конаджык, Гюмбет, Акъярлар и Кадыкалеси.",
    lang_pop="Открыть страницу на выбранном языке:", full="Русский",
),
}
