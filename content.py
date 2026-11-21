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
        "tr": ("Akıllı Ev Sistemleri", "KNX, Zigbee ve Wi‑Fi tabanlı akıllı ev kurulumu. Işık, perde, klima, kamera ve alarmı tek uygulamadan, sesle ya da telefonla yönetin."),
        "en": ("Smart Home Systems", "KNX, Zigbee and Wi‑Fi smart home installation. Control lights, blinds, A/C, cameras and alarms from one app, by voice or phone."),
        "ru": ("Системы «Умный дом»", "Установка умного дома на KNX, Zigbee и Wi‑Fi. Свет, шторы, кондиционер, камеры и сигнализация — в одном приложении, голосом или со смартфона."),
    }),
    ("auto", {
        "tr": ("Ev & Villa Otomasyonu", "Senaryo, zamanlayıcı ve sensörlerle tam otomasyon. Villa, otel ve işyerleri için enerji tasarruflu, uzaktan erişimli otomasyon projeleri."),
        "en": ("Home & Villa Automation", "Full automation with scenes, timers and sensors. Energy‑saving, remotely accessible automation for villas, hotels and businesses."),
        "ru": ("Автоматизация домов и вилл", "Полная автоматизация: сценарии, таймеры, датчики. Энергосберегающие проекты с удалённым доступом для вилл, отелей и бизнеса."),
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
        "tr": ("Bakım & Onarım", "Villa, site ve işletmeler için periyodik elektrik bakımı, pano kontrolü, termal ölçüm ve sezon öncesi güvenlik kontrolleri."),
        "en": ("Maintenance & Service", "Scheduled electrical maintenance for villas, complexes and businesses: panel checks, thermal inspection and pre‑season safety checks."),
        "ru": ("Обслуживание и сервис", "Плановое обслуживание электрики вилл, комплексов и бизнеса: проверка щитов, тепловизионный контроль, проверка перед сезоном."),
    }),
    ("tree", {
        "tr": ("Çevre & Bahçe Aydınlatma", "Peyzaj, bahçe, havuz ve cephe aydınlatması. Ağaç uplight, yol armatürleri ve LED havuz ışıklarıyla villanızı geceleri bir esere dönüştürün."),
        "en": ("Garden & Outdoor Lighting", "Landscape, garden, pool and facade lighting. Tree uplights, path lights and LED pool lights that turn your villa into a night‑time masterpiece."),
        "ru": ("Ландшафтное освещение", "Освещение сада, бассейна и фасада. Подсветка деревьев, дорожек и LED‑свет в бассейне превратят вашу виллу в шедевр ночью."),
    }),
    ("chandelier", {
        "tr": ("Avize Montajı", "Kristal, modern ve ağır avizelerin güvenli montajı. Yüksek tavan, galeri boşluğu ve dimmer bağlantısında uzman işçilik."),
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
    ("hero", {"tr": ("Yalıkavak", "Lüks villa cephe & havuz aydınlatması"), "en": ("Yalikavak", "Luxury villa facade & pool lighting"), "ru": ("Ялыкавак", "Подсветка фасада и бассейна виллы")}),
    ("chandelier", {"tr": ("Bodrum Merkez", "Kristal avize montajı – yüksek tavan"), "en": ("Bodrum Center", "Crystal chandelier – high ceiling install"), "ru": ("Бодрум", "Монтаж хрустальной люстры")}),
    ("electrical-panel", {"tr": ("Bitez", "Elektrik panosu yenileme"), "en": ("Bitez", "Distribution board upgrade"), "ru": ("Битез", "Замена электрощита")}),
    ("garden-lighting", {"tr": ("Göltürkbükü", "Peyzaj & bahçe aydınlatma"), "en": ("Golturkbuku", "Landscape & garden lighting"), "ru": ("Гёльтюркбюкю", "Ландшафтное освещение сада")}),
    ("led-lighting", {"tr": ("Konacık", "Gizli LED şerit aydınlatma"), "en": ("Konacik", "Hidden LED strip lighting"), "ru": ("Конаджык", "Скрытая LED‑подсветка")}),
    ("pool-lighting", {"tr": ("Turgutreis", "LED havuz aydınlatma sistemi"), "en": ("Turgutreis", "LED pool lighting system"), "ru": ("Тургутрейс", "LED‑освещение бассейна")}),
    ("smart-home", {"tr": ("Gündoğan", "Akıllı ev otomasyon paneli"), "en": ("Gundogan", "Smart home automation panel"), "ru": ("Гюндоган", "Панель умного дома")}),
    ("renovation", {"tr": ("Gümbet", "Komple elektrik tesisatı yenileme"), "en": ("Gumbet", "Complete electrical rewiring"), "ru": ("Гюмбет", "Полная замена проводки")}),
]

# ------------------------------------------------------------------
# SSS / FAQ (FAQPage schema ile Google'da zengin sonuç)
# ------------------------------------------------------------------
FAQ = {
    "tr": [
        ("Bodrum'da 7/24 acil elektrikçi hizmeti veriyor musunuz?", "Evet. Bodrum merkez, Yalıkavak, Turgutreis, Gündoğan, Bitez ve tüm Bodrum yarımadasında gece‑gündüz, hafta sonu ve bayramlar dahil acil elektrik arıza servisi veriyoruz. Telefon veya WhatsApp ile hemen ulaşabilirsiniz."),
        ("Malzemeyi siz mi sağlıyorsunuz?", "Hayır, malzeme satışı yapmıyoruz. Avize, armatür, akıllı ev cihazı gibi ürünleri siz alıyorsunuz; biz montajını ve bağlantısını yapıyoruz. İsterseniz satın almadan önce hangi ürünün uygun olduğu konusunda ücretsiz bilgi veriyoruz."),
        ("Hangi bölgelere hizmet veriyorsunuz?", "Bodrum Merkez, Yalıkavak, Gündoğan, Göltürkbükü, Gölköy, Torba, Turgutreis, Gümüşlük, Bitez, Ortakent, Yahşi, Konacık, Gümbet, Akyarlar, Kadıkalesi, Güvercinlik, Yakaköy ve Mumcular dahil tüm Bodrum'a hizmet veriyoruz."),
        ("Mevcut evime kırıp dökmeden akıllı ev sistemi kurulabilir mi?", "Evet. Kablosuz (Zigbee / Wi‑Fi) akıllı anahtar, priz, perde motoru ve sensörlerle mevcut tesisatı bozmadan evinizi akıllı hale getiriyoruz. Yeni yapılarda ise kablolu KNX altyapısı öneriyoruz."),
        ("Akıllı ev sistemi kurulumu ne kadar sürer?", "Bir daire için kablosuz akıllı ev kurulumu genellikle 1 gün sürer. Villalarda kapsamlı otomasyon projelerinin montajı 2–7 gün arasında tamamlanır."),
        ("Ağır ve yüksek tavanlı avize montajı yapıyor musunuz?", "Evet. Kristal ve ağır avizeleri uygun taşıyıcı ankrajlarla, gerektiğinde iskele kurarak 6–8 metre yüksekliğe kadar güvenle monte ediyor, dimmer ve akıllı kontrol bağlantısını yapıyoruz."),
        ("Elektrik tesisatı ne zaman yenilenmeli?", "Sigortalar sık atıyorsa, prizlerde ısınma veya yanık kokusu varsa, tesisat 20 yıldan eskiyse ya da kaçak akım rölesi yoksa tesisatınızın kontrol edilip yenilenmesi gerekir."),
        ("Keşif ve fiyat teklifi ücretli mi?", "Bodrum içindeki projeler için keşif ve fiyat teklifi ücretsizdir. Arıza servislerinde ise ücret, işe başlamadan önce net olarak bildirilir."),
        ("Yaptığınız işlere garanti veriyor musunuz?", "Evet. Yaptığımız tüm montaj ve işçilik garantilidir. Montaj sonrası destek ve periyodik bakım anlaşmaları da sunuyoruz."),
        ("Yabancı müşterilerle İngilizce veya Rusça iletişim kurabiliyor musunuz?", "Evet. Bodrum'da yaşayan yabancı villa sahipleri ve site yönetimleri ile İngilizce ve Rusça iletişim kuruyor, teklif ve faturaları istenen dilde hazırlıyoruz."),
    ],
    "en": [
        ("Do you offer a 24/7 emergency electrician in Bodrum?", "Yes. We provide day and night emergency electrical repair across Bodrum Center, Yalikavak, Turgutreis, Gundogan, Bitez and the entire Bodrum peninsula — including weekends and holidays. Call or WhatsApp us any time."),
        ("Do you supply the materials?", "No, we don't sell materials. You purchase the products (chandeliers, fixtures, smart home devices etc.) and we take care of the installation and wiring. We're happy to advise you for free on what to buy beforehand."),
        ("Which areas do you cover?", "We cover all of Bodrum including Bodrum Center, Yalikavak, Gundogan, Golturkbuku, Golkoy, Torba, Turgutreis, Gumusluk, Bitez, Ortakent, Yahsi, Konacik, Gumbet, Akyarlar, Kadikalesi, Guvercinlik, Yakakoy and Mumcular."),
        ("Can you install a smart home without breaking walls?", "Yes. Using wireless (Zigbee / Wi‑Fi) smart switches, sockets, blind motors and sensors we upgrade your home without touching the existing wiring. For new builds we recommend a wired KNX system."),
        ("How long does a smart home installation take?", "A wireless smart home setup for an apartment usually takes 1 day. Comprehensive villa automation projects are installed within 2–7 days."),
        ("Do you install heavy chandeliers on high ceilings?", "Yes. We safely mount crystal and heavy chandeliers with proper anchoring — using scaffolding when needed — up to 6–8 metres high, including dimmer and smart control connections."),
        ("When should electrical wiring be replaced?", "If breakers trip often, sockets get hot or smell burnt, the wiring is older than 20 years, or there is no RCD (residual current device), your installation should be inspected and renewed."),
        ("Is the site visit and quote free?", "Site visits and quotes are free for projects within Bodrum. For emergency repairs, the price is clearly stated before any work begins."),
        ("Do you guarantee your work?", "Yes. All our installation work and workmanship is guaranteed. We also offer after‑installation support and maintenance contracts."),
        ("Do you speak English and Russian?", "Yes. We work with many international villa owners and property managers in Bodrum and communicate in English and Russian, with quotes and invoices in your preferred language."),
    ],
    "ru": [
        ("Есть ли у вас аварийный электрик 24/7 в Бодруме?", "Да. Мы выезжаем днём и ночью, включая выходные и праздники, по всему полуострову Бодрум: центр Бодрума, Ялыкавак, Тургутрейс, Гюндоган, Битез и другие районы. Звоните или пишите в WhatsApp."),
        ("Вы продаёте материалы?", "Нет, мы не продаём материалы. Оборудование (люстры, светильники, устройства умного дома и т.д.) покупаете вы, а мы выполняем монтаж и подключение. Перед покупкой бесплатно подскажем, что лучше выбрать."),
        ("В каких районах вы работаете?", "Мы работаем по всему Бодруму: центр Бодрума, Ялыкавак, Гюндоган, Гёльтюркбюкю, Гёлькёй, Торба, Тургутрейс, Гюмюшлюк, Битез, Ортакент, Яхши, Конаджык, Гюмбет, Акъярлар, Кадыкалеси, Гюверджинлик, Якакёй и Мумджулар."),
        ("Можно ли сделать умный дом без штробления стен?", "Да. С помощью беспроводных (Zigbee / Wi‑Fi) выключателей, розеток, моторов штор и датчиков мы делаем дом умным, не трогая существующую проводку. Для новостроек рекомендуем проводную систему KNX."),
        ("Сколько времени занимает установка умного дома?", "Беспроводной умный дом для квартиры обычно устанавливается за 1 день. Комплексные проекты автоматизации вилл монтируются за 2–7 дней."),
        ("Монтируете ли вы тяжёлые люстры на высоких потолках?", "Да. Мы надёжно монтируем хрустальные и тяжёлые люстры с правильным креплением, при необходимости с лесами, на высоте до 6–8 метров, с подключением диммера и умного управления."),
        ("Когда нужно менять электропроводку?", "Если часто выбивает автоматы, розетки греются или пахнут гарью, проводке более 20 лет или нет УЗО — электрику нужно проверить и обновить."),
        ("Выезд и смета бесплатные?", "Для проектов в пределах Бодрума выезд и смета бесплатны. При аварийном ремонте стоимость сообщается до начала работ."),
        ("Даёте ли вы гарантию на работы?", "Да. На все работы предоставляется гарантия, мы отвечаем за качество каждого монтажа. Также предлагаем сервисное обслуживание."),
        ("Вы общаетесь на русском и английском?", "Да. Мы работаем со многими иностранными владельцами вилл в Бодруме, общаемся на русском и английском, сметы и счета готовим на удобном вам языке."),
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
        ("Smart home without breaking a single wall. Blinds, lights and A/C all on my phone. Excellent work and great English.", "Michael B.", "Turgutreis"),
    ],
    "ru": [
        ("Ночью пропал свет — приехали за 30 минут. Работают чисто и профессионально. Лучший электрик в Бодруме!", "Елена П.", "Ялыкавак"),
        ("Сделали всё освещение сада и бассейна на нашей вилле. Гости каждый вечер в восторге!", "Андрей и Ольга С.", "Тургутрейс"),
        ("Умный дом без ремонта стен: шторы, свет, кондиционер — всё в телефоне. Общались на русском, очень удобно.", "Дмитрий К.", "Гюндоган"),
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
    nav_services="Hizmetler", nav_smart="Akıllı Ev", nav_gallery="Projeler", nav_areas="Bölgeler", nav_faq="SSS", nav_contact="İletişim",
    call="Hemen Ara", topbar="7/24 acil elektrikçi – Bodrum'un her yerine hızlı servis:",
    badge="Bodrum'un Lider Elektrik & Aydınlatma Ustası",
    h1='Bodrum Elektrikçi<br><span class="glow-text">Güvenli Elektrik, Kusursuz Montaj.</span>',
    lead="Elektrik tesisatından akıllı ev otomasyonuna, avize montajından villa bahçe aydınlatmasına kadar — Bodrum'da 7/24 güvenilir, sertifikalı ve kusursuz elektrik hizmeti.",
    cta_call="Hemen Ara", cta_wa="WhatsApp'tan Yaz",
    s_years="Yıllık Deneyim", s_jobs="Tamamlanan İş", s_support="Acil Destek", s_areas="Hizmet Bölgesi",
    bulb_hint="Ampule dokun – ışıkları aç / kapat",
    ticker_suffix="Elektrikçi",
    sv_k="Hizmetlerimiz", sv_t="Bodrum'da Elektrikle İlgili Her Şey", sv_p="Villa, daire, otel ve işyerleri için profesyonel elektrik montaj ve işçilik hizmeti. Malzemeyi siz alın, montajı biz yapalım.",
    sm_k="Akıllı Ev & Otomasyon", sm_t="Evinizi Parmağınızın Ucuyla Yönetin",
    sm_p="Aşağıdaki paneli deneyin! Bodrum'daki villanızı dünyanın neresinde olursanız olun telefonunuzdan kontrol edin.",
    sm_1="Işık, perde, klima ve havuz kontrolü tek uygulamada", sm_2="Siri, Alexa ve Google Asistan ile sesli kontrol", sm_3="Kamera, alarm ve kaçak su sensörleriyle tam güvenlik", sm_4="%30'a varan enerji tasarrufu",
    pn_t="Villa Kontrol Paneli", pn_on="Bağlı", z_living="Salon Işıkları", z_led="LED Şerit", z_garden="Bahçe", z_pool="Havuz", z_curtain="Perdeler",
    sc_movie="🎬 Film Modu", sc_dinner="🍷 Akşam Yemeği", sc_all="☀️ Tümü Açık", sc_off="🌙 Tümü Kapalı", room_tag="Canlı demo – düğmelere dokunun",
    sm_cta="Akıllı Ev Teklifi Al",
    wy_k="Neden Biz?", wy_t="Bodrum'un Güvendiği Elektrik Ekibi",
    w1t="7/24 Hızlı Servis", w1p="Acil arızalarda Bodrum'un her noktasına en kısa sürede ulaşıyoruz.",
    w2t="Sertifikalı Usta", w2p="Yönetmeliğe uygun, belgeli ve sigortalı profesyonel işçilik.",
    w3t="Şeffaf Fiyat", w3p="Ücretsiz keşif, net teklif. Sürpriz ücret yok.",
    w4t="Garantili İş", w4p="Temiz çalışma, işi bitirince toparlanmış alan ve işçilik garantisi.",
    gl_k="Projelerimiz", gl_t="Bodrum'da Hayata Geçirdiğimiz Işıklar", gl_p="Villa aydınlatmasından akıllı ev projelerine, yaptığımız işlerden bazıları.",
    ar_k="Hizmet Bölgeleri", ar_t="Bodrum'un Her Köşesindeyiz", ar_p="Bodrum yarımadasının tamamında elektrik, akıllı ev ve aydınlatma hizmeti veriyoruz.",
    ar_text="Bodrum elektrikçi arıyorsanız doğru yerdesiniz. Yalıkavak elektrikçi, Turgutreis elektrikçi, Gündoğan elektrikçi, Bitez elektrikçi, Gümbet elektrikçi, Ortakent elektrikçi ve Konacık elektrikçi olarak; acil elektrik arızası, elektrik tesisatı, akıllı ev sistemleri, avize montajı, bahçe ve havuz aydınlatması için Bodrum'un tamamına hizmet veriyoruz.",
    ts_k="Müşteri Yorumları", ts_t="Müşterilerimiz Ne Diyor?",
    fq_k="Sıkça Sorulan Sorular", fq_t="Merak Ettikleriniz",
    ct_k="İletişim", ct_t="Işığınızı Birlikte Yakalım", ct_p="Ücretsiz keşif ve fiyat teklifi için hemen arayın ya da formu doldurun – size WhatsApp'tan dönelim.",
    c_phone="Telefon (7/24)", c_wa="WhatsApp", c_mail="E‑posta", c_area="Hizmet Bölgesi", c_area_v="Bodrum, Muğla – tüm yarımada", c_hours="Çalışma Saatleri", c_hours_v="7 gün 24 saat",
    f_name="Adınız", f_phone="Telefonunuz", f_service="Hizmet", f_msg="Mesajınız", f_send="WhatsApp ile Gönder", f_hello="Merhaba, web sitenizden ulaşıyorum.", f_ph_msg="Örn: Yalıkavak'taki villam için bahçe aydınlatması istiyorum...",
    map_title="Bodrum hizmet bölgesi haritası",
    ft_about="Bodrum'da elektrik tesisatı, akıllı ev sistemleri, otomasyon, avize montajı, bakım onarım ve çevre aydınlatma alanında 7/24 profesyonel hizmet.",
    ft_services="Hizmetler", ft_areas="Bölgeler", rights="Tüm hakları saklıdır.",
    seo="Bodrum elektrikçi, Bodrum elektrik ustası ve Bodrum acil elektrikçi hizmetlerinde 7/24 yanınızdayız. Bodrum elektrik tesisatı, elektrik arıza tamiri, sigorta ve pano montajı, kaçak akım rölesi, topraklama, priz ve anahtar değişimi, Bodrum akıllı ev sistemleri, KNX ev otomasyonu, villa otomasyonu, akıllı aydınlatma, Bodrum avize montajı, LED aydınlatma, peyzaj ve bahçe aydınlatma, havuz aydınlatma, cephe aydınlatma, elektrik bakım onarım ve tadilat işleri. Yalıkavak, Gündoğan, Göltürkbükü, Gölköy, Torba, Turgutreis, Gümüşlük, Bitez, Ortakent, Yahşi, Konacık, Gümbet, Akyarlar, Kadıkalesi ve Muğla Bodrum genelinde en yakın elektrikçi.",
    lang_pop="Bu sayfayı tercih ettiğiniz dilde görüntüleyin:", full="Türkçe",
),
"en": dict(
    lang="en", locale="en_GB", path="en/",
    wa_text="Hello, I would like to use your electrical services. Could you give me some information?",
    title="Electrician in Bodrum | Myndos Elektrik – 24/7 Smart Home & Lighting",
    desc="Myndos Elektrik – trusted electrician in Bodrum – 24/7 emergency repairs, electrical installation, smart home & automation, chandelier installation, garden and pool lighting. Yalikavak, Turgutreis, Gundogan & all Bodrum.",
    keywords="myndos elektrik, electrician bodrum, bodrum electrician, emergency electrician bodrum, 24/7 electrician bodrum, english speaking electrician bodrum, electrician yalikavak, electrician turgutreis, electrician gundogan, electrician bitez, electrician gumbet, electrician torba, electrician golturkbuku, smart home bodrum, home automation bodrum, villa automation turkey, KNX bodrum, chandelier installation bodrum, garden lighting bodrum, landscape lighting bodrum, pool lighting bodrum, led lighting bodrum, electrical installation bodrum, rewiring bodrum, electrical repair bodrum, villa electrician bodrum, electrician near me bodrum, electrician mugla turkey",
    nav_services="Services", nav_smart="Smart Home", nav_gallery="Projects", nav_areas="Areas", nav_faq="FAQ", nav_contact="Contact",
    call="Call Now", topbar="24/7 emergency electrician – fast service anywhere in Bodrum:",
    badge="Bodrum's Premium Electrical & Lighting Experts",
    h1='Electrician in Bodrum<br><span class="glow-text">Safe Wiring, Flawless Installation.</span>',
    lead="From electrical installations to smart home automation, from chandelier mounting to luxury villa garden lighting — reliable, certified, flawless electrical services in Bodrum, 24/7. English spoken.",
    cta_call="Call Now", cta_wa="Message on WhatsApp",
    s_years="Years Experience", s_jobs="Completed Jobs", s_support="Emergency Support", s_areas="Service Areas",
    bulb_hint="Tap the bulb – switch the lights on / off",
    ticker_suffix="Electrician",
    sv_k="Our Services", sv_t="Everything Electrical in Bodrum", sv_p="Professional electrical installation and workmanship for villas, apartments, hotels and businesses. You buy the products — we install them perfectly.",
    sm_k="Smart Home & Automation", sm_t="Control Your Home at Your Fingertips",
    sm_p="Try the panel below! Control your Bodrum villa from your phone, wherever you are in the world.",
    sm_1="Lights, blinds, A/C and pool control in one app", sm_2="Voice control with Siri, Alexa and Google Assistant", sm_3="Total security with cameras, alarms and leak sensors", sm_4="Up to 30% energy savings",
    pn_t="Villa Control Panel", pn_on="Online", z_living="Living Room", z_led="LED Strip", z_garden="Garden", z_pool="Pool", z_curtain="Blinds",
    sc_movie="🎬 Movie Mode", sc_dinner="🍷 Dinner", sc_all="☀️ All On", sc_off="🌙 All Off", room_tag="Live demo – tap the switches",
    sm_cta="Get a Smart Home Quote",
    wy_k="Why Choose Us", wy_t="The Electrical Team Bodrum Trusts",
    w1t="24/7 Fast Response", w1p="We reach every corner of Bodrum as quickly as possible for emergencies.",
    w2t="Certified Electricians", w2p="Licensed, insured, code‑compliant professional workmanship.",
    w3t="Transparent Pricing", w3p="Free site visit, clear quote. No hidden fees.",
    w4t="Guaranteed Work", w4p="Clean work, a tidy site when we leave and a workmanship guarantee.",
    gl_k="Our Projects", gl_t="Lights We Have Brought to Life in Bodrum", gl_p="From villa lighting to smart home projects — a selection of our work.",
    ar_k="Service Areas", ar_t="Every Corner of Bodrum", ar_p="Electrical, smart home and lighting services across the entire Bodrum peninsula.",
    ar_text="Looking for an electrician in Bodrum? You're in the right place. As your local electrician in Yalikavak, Turgutreis, Gundogan, Bitez, Gumbet, Ortakent and Konacik, we handle emergency repairs, electrical installations, smart home systems, chandelier installation and garden & pool lighting throughout Bodrum.",
    ts_k="Reviews", ts_t="What Our Clients Say",
    fq_k="FAQ", fq_t="Frequently Asked Questions",
    ct_k="Contact", ct_t="Let's Light Up Your Home", ct_p="Call now for a free site visit and quote, or fill in the form and we'll get back to you on WhatsApp.",
    c_phone="Phone (24/7)", c_wa="WhatsApp", c_mail="Email", c_area="Service Area", c_area_v="Bodrum, Mugla – entire peninsula", c_hours="Working Hours", c_hours_v="7 days, 24 hours",
    f_name="Your Name", f_phone="Your Phone", f_service="Service", f_msg="Your Message", f_send="Send via WhatsApp", f_hello="Hello, I'm contacting you from your website.", f_ph_msg="E.g. I need garden lighting for my villa in Yalikavak...",
    map_title="Bodrum service area map",
    ft_about="Professional 24/7 electrical installation, smart home systems, automation, chandelier installation, maintenance and outdoor lighting in Bodrum.",
    ft_services="Services", ft_areas="Areas", rights="All rights reserved.",
    seo="Electrician in Bodrum available 24/7: emergency electrician, electrical installation and rewiring, fault finding and repair, distribution boards, RCDs, earthing, sockets and switches, smart home systems, KNX home automation, villa automation, smart lighting, chandelier installation, LED lighting, landscape and garden lighting, pool lighting, facade lighting, electrical maintenance and renovation. English and Russian speaking electrician serving Yalikavak, Gundogan, Golturkbuku, Golkoy, Torba, Turgutreis, Gumusluk, Bitez, Ortakent, Yahsi, Konacik, Gumbet, Akyarlar, Kadikalesi and all of Bodrum, Mugla, Turkey.",
    lang_pop="View this page in your preferred language:", full="English",
),
"ru": dict(
    lang="ru", locale="ru_RU", path="ru/",
    wa_text="Здравствуйте, хочу воспользоваться вашими услугами электрика. Можно узнать подробнее?",
    title="Электрик в Бодруме 24/7 | Myndos Elektrik – умный дом, освещение",
    desc="Myndos Elektrik – электрик в Бодруме 24/7: аварийный выезд, электромонтаж, умный дом и автоматизация, монтаж люстр, освещение сада и бассейна. Ялыкавак, Тургутрейс, Гюндоган и весь Бодрум. Говорим по‑русски.",
    keywords="myndos elektrik, электрик бодрум, электрик в бодруме, русский электрик бодрум, русскоговорящий электрик турция, аварийный электрик бодрум, электрик 24/7 бодрум, электрик ялыкавак, электрик тургутрейс, электрик гюндоган, электрик битез, электрик гюмбет, умный дом бодрум, умный дом турция, автоматизация виллы бодрум, KNX бодрум, монтаж люстры бодрум, освещение сада бодрум, ландшафтное освещение бодрум, освещение бассейна бодрум, LED подсветка бодрум, электромонтаж бодрум, замена проводки бодрум, ремонт электрики бодрум, электрик для виллы турция, электрик мугла",
    nav_services="Услуги", nav_smart="Умный дом", nav_gallery="Проекты", nav_areas="Районы", nav_faq="Вопросы", nav_contact="Контакты",
    call="Позвонить", topbar="Аварийный электрик 24/7 – быстрый выезд по всему Бодруму:",
    badge="Премиальные электромонтажные работы в Бодруме",
    h1='Электрик в Бодруме<br><span class="glow-text">Надёжная электрика, безупречный монтаж.</span>',
    lead="От электромонтажа до умного дома, от монтажа люстр до освещения сада роскошной виллы — надёжные, сертифицированные электроуслуги в Бодруме 24/7. Говорим по‑русски.",
    cta_call="Позвонить", cta_wa="Написать в WhatsApp",
    s_years="Лет опыта", s_jobs="Выполненных работ", s_support="Аварийная служба", s_areas="Районов",
    bulb_hint="Нажмите на лампу – включите / выключите свет",
    ticker_suffix="электрик",
    sv_k="Наши услуги", sv_t="Всё по электрике в Бодруме", sv_p="Профессиональный электромонтаж для вилл, квартир, отелей и бизнеса. Вы покупаете оборудование — мы безупречно его монтируем.",
    sm_k="Умный дом и автоматизация", sm_t="Управляйте домом одним касанием",
    sm_p="Попробуйте панель ниже! Управляйте своей виллой в Бодруме со смартфона из любой точки мира.",
    sm_1="Свет, шторы, кондиционер и бассейн в одном приложении", sm_2="Голосовое управление: Siri, Alexa, Google Ассистент, Алиса", sm_3="Полная безопасность: камеры, сигнализация, датчики протечки", sm_4="Экономия энергии до 30%",
    pn_t="Панель управления виллой", pn_on="Онлайн", z_living="Гостиная", z_led="LED‑лента", z_garden="Сад", z_pool="Бассейн", z_curtain="Шторы",
    sc_movie="🎬 Кино", sc_dinner="🍷 Ужин", sc_all="☀️ Всё вкл.", sc_off="🌙 Всё выкл.", room_tag="Живое демо – нажимайте кнопки",
    sm_cta="Рассчитать умный дом",
    wy_k="Почему мы", wy_t="Электрики, которым доверяет Бодрум",
    w1t="Быстрый выезд 24/7", w1p="При авариях приезжаем в любую точку Бодрума в кратчайшие сроки.",
    w2t="Сертифицированные мастера", w2p="Лицензированная, застрахованная работа по нормам.",
    w3t="Честные цены", w3p="Бесплатный выезд и прозрачная смета. Без скрытых платежей.",
    w4t="Гарантия", w4p="Чистая работа, порядок после монтажа и гарантия.",
    gl_k="Наши проекты", gl_t="Свет, который мы создали в Бодруме", gl_p="От освещения вилл до умных домов — некоторые из наших работ.",
    ar_k="Районы обслуживания", ar_t="Мы работаем по всему Бодруму", ar_p="Электрика, умный дом и освещение на всём полуострове Бодрум.",
    ar_text="Ищете электрика в Бодруме? Вы по адресу. Мы — ваш электрик в Ялыкаваке, Тургутрейсе, Гюндогане, Битезе, Гюмбете, Ортакенте и Конаджыке: аварийный ремонт, электромонтаж, умный дом, монтаж люстр, освещение сада и бассейна по всему Бодруму.",
    ts_k="Отзывы", ts_t="Что говорят клиенты",
    fq_k="Вопросы", fq_t="Частые вопросы",
    ct_k="Контакты", ct_t="Давайте зажжём свет вместе", ct_p="Позвоните для бесплатного выезда и сметы или заполните форму — мы ответим в WhatsApp.",
    c_phone="Телефон (24/7)", c_wa="WhatsApp", c_mail="Эл. почта", c_area="Район работы", c_area_v="Бодрум, Мугла – весь полуостров", c_hours="Часы работы", c_hours_v="7 дней, 24 часа",
    f_name="Ваше имя", f_phone="Ваш телефон", f_service="Услуга", f_msg="Сообщение", f_send="Отправить в WhatsApp", f_hello="Здравствуйте, пишу с вашего сайта.", f_ph_msg="Например: нужно освещение сада для виллы в Ялыкаваке...",
    map_title="Карта района обслуживания Бодрум",
    ft_about="Профессиональный электромонтаж, умный дом, автоматизация, монтаж люстр, обслуживание и наружное освещение в Бодруме 24/7.",
    ft_services="Услуги", ft_areas="Районы", rights="Все права защищены.",
    seo="Электрик в Бодруме 24/7: аварийный электрик, электромонтаж и замена проводки, поиск и устранение неисправностей, электрощиты, УЗО, заземление, розетки и выключатели, умный дом, автоматизация KNX, автоматизация виллы, умное освещение, монтаж люстр, LED‑освещение, ландшафтное освещение сада, освещение бассейна, подсветка фасада, обслуживание и ремонт электрики. Русскоговорящий электрик в Ялыкаваке, Гюндогане, Гёльтюркбюкю, Гёлькёе, Торбе, Тургутрейсе, Гюмюшлюке, Битезе, Ортакенте, Яхши, Конаджыке, Гюмбете, Акъярларе и по всему Бодруму, Мугла, Турция.",
    lang_pop="Открыть страницу на выбранном языке:", full="Русский",
),
}
