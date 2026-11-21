# -*- coding: utf-8 -*-
"""
Site oluşturucu:  python build.py
Çıktı: index.html (TR), en/index.html, ru/index.html, sitemap.xml, robots.txt
"""
import json, re, datetime
from urllib.parse import quote
from pathlib import Path
from content import AREAS, SERVICES, ICONS, GALLERY, FAQ, TESTIMONIALS, T

# =================== FİRMA BİLGİLERİ – BURAYI DÜZENLEYİN ===================
CFG = dict(
    BRAND="Myndos Elektrik",
    LOGO_A="Myndos", LOGO_B="Elektrik",
    PHONE_DISPLAY="0533 582 32 01",
    PHONE_TEL="+905335823201",          # tel: linki (boşluksuz)
    WHATSAPP="905335823201",            # wa.me için, + olmadan
    EMAIL="myndos.elektirik@outlook.com",
    DOMAIN="https://myndoselektrik.pages.dev",   # sondaki / olmadan
    YEARS=15, JOBS=2500,
    INSTAGRAM="https://www.instagram.com/",
    GOOGLE_MAPS="https://maps.google.com/?q=Bodrum",  # Google İşletme profil linkiniz
    LAT=37.0344, LNG=27.4305,
)
# ===========================================================================

ROOT = Path(__file__).parent
LANGS = ["tr", "en", "ru"]
LI = {"tr": 0, "en": 1, "ru": 2}

def svg(icon):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg>'

PIN = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s7-6.2 7-12a7 7 0 10-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M22 16.9v3a2 2 0 01-2.2 2 19.8 19.8 0 01-8.6-3.1 19.5 19.5 0 01-6-6A19.8 19.8 0 012.1 4.2 2 2 0 014.1 2h3a2 2 0 012 1.7c.1 1 .4 1.9.7 2.8a2 2 0 01-.5 2.1L8 9.9a16 16 0 006 6l1.3-1.3a2 2 0 012.1-.4c.9.3 1.8.6 2.8.7a2 2 0 011.7 2z"/></svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.2-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 21.8c-1.8 0-3.5-.5-5-1.4l-.4-.2-3.7 1 1-3.6-.2-.4A9.8 9.8 0 1112 21.8zM20.5 3.5A11.8 11.8 0 002 17.7L.3 24l6.4-1.7A11.8 11.8 0 0024 12c0-3.2-1.2-6.2-3.5-8.5z"/></svg>'
MAIL_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>'
CLOCK_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'


def url(lang):
    return f'{CFG["DOMAIN"]}/{T[lang]["path"]}'


def build(lang):
    t = dict(T[lang]); i = LI[lang]
    base = "" if lang == "tr" else "../"
    t.update({k: str(v) for k, v in CFG.items()})
    t["base"] = base
    t["canonical"] = url(lang)
    t["wa_msg"] = quote(t["wa_text"])

    # Language switcher + hreflang
    t["hreflang"] = "\n".join(f'<link rel="alternate" hreflang="{l}" href="{url(l)}">' for l in LANGS) + \
        f'\n<link rel="alternate" hreflang="x-default" href="{url("tr")}">'
    t["og_alt"] = "\n".join(f'<meta property="og:locale:alternate" content="{T[l]["locale"]}">' for l in LANGS if l != lang)
    t["lang_links"] = "".join(
        f'<a href="{base}{T[l]["path"]}" hreflang="{l}" lang="{l}" data-full="{T[l]["full"]}"{" class=active aria-current=page" if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS)

    # Ticker
    items = "".join(f'<span>{a[i]} {t["ticker_suffix"]}</span>' if lang != "ru" else f'<span>Электрик {a[i]}</span>' for a in AREAS)
    t["ticker"] = items + items.replace("<span>", '<span aria-hidden="true">')

    # Services
    t["services_html"] = "".join(
        f'<article class="card tilt reveal d{n % 4}"><span class="num">0{n + 1}</span><div class="ico">{svg(ic)}</div>'
        f'<h3>{d[lang][0]}</h3><p>{d[lang][1]}</p></article>' for n, (ic, d) in enumerate(SERVICES))
    t["service_options"] = "".join(f"<option>{d[lang][0]}</option>" for _, d in SERVICES)
    t["footer_services"] = "".join(f'<li><a href="#services">{d[lang][0]}</a></li>' for _, d in SERVICES)
    t["footer_areas"] = "".join(f'<li>{a[i]}</li>' for a in AREAS[:9])

    # Gallery
    t["gallery_html"] = "".join(
        f'<figure class="g-item reveal"><picture><source srcset="{base}assets/img/{f}.webp" type="image/webp">'
        f'<img src="{base}assets/img/{f}.jpg" alt="{d[lang][1]} – {d[lang][0]}, Bodrum" loading="lazy" decoding="async" width="1376" height="768"></picture>'
        f'<figcaption><small>{d[lang][0]}</small>{d[lang][1]}</figcaption></figure>' for f, d in GALLERY)

    # Areas
    suffix = {"tr": " Elektrikçi", "en": " Electrician", "ru": ""}[lang]
    pre = "Электрик " if lang == "ru" else ""
    t["areas_html"] = "".join(f'<span class="area">{PIN}{pre}{a[i]}{suffix}</span>' for a in AREAS)

    # Testimonials
    t["testi_html"] = "".join(
        f'<blockquote class="t-card reveal d{n}"><div class="stars" aria-label="5/5">★★★★★</div><p>“{q}”</p><b>{who}</b><small>{where}</small></blockquote>'
        for n, (q, who, where) in enumerate(TESTIMONIALS[lang]))

    # FAQ
    t["faq_html"] = "".join(
        f'<details class="reveal"{" open" if n == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
        for n, (q, a) in enumerate(FAQ[lang]))

    # Structured data
    biz = {
        "@context": "https://schema.org",
        "@type": "Electrician",
        "@id": CFG["DOMAIN"] + "/#business",
        "name": CFG["BRAND"],
        "description": t["desc"],
        "url": url(lang),
        "telephone": CFG["PHONE_TEL"],
        "email": CFG["EMAIL"],
        "image": [f'{CFG["DOMAIN"]}/assets/img/{g[0]}.jpg' for g in GALLERY[:4]],
        "logo": CFG["DOMAIN"] + "/assets/img/favicon.svg",
        "priceRange": "₺₺",
        "address": {"@type": "PostalAddress", "addressLocality": "Bodrum", "addressRegion": "Muğla", "postalCode": "48400", "addressCountry": "TR"},
        "geo": {"@type": "GeoCoordinates", "latitude": CFG["LAT"], "longitude": CFG["LNG"]},
        "areaServed": [{"@type": "Place", "name": f"{a[0]}, Bodrum"} for a in AREAS],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"}],
        "knowsLanguage": ["tr", "en", "ru"],
        "hasOfferCatalog": {"@type": "OfferCatalog", "name": t["sv_k"],
            "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": d[lang][0], "description": d[lang][1], "areaServed": "Bodrum"}} for _, d in SERVICES]},
        "sameAs": [CFG["INSTAGRAM"], CFG["GOOGLE_MAPS"]],
    }
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[lang]]}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": CFG["BRAND"], "url": url(lang), "inLanguage": lang}
    t["schema"] = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in (biz, faq, site))

    t["icon_phone"], t["icon_wa"], t["icon_mail"], t["icon_clock"], t["icon_pin"] = PHONE_SVG, WA_SVG, MAIL_SVG, CLOCK_SVG, PIN

    html = (ROOT / "template.html").read_text(encoding="utf-8")
    def rep(m):
        k = m.group(1)
        if k not in t:
            raise KeyError(f"Missing key {k} for {lang}")
        return t[k]
    html = re.sub(r"\{\{(\w+)\}\}", rep, html)
    out = ROOT / T[lang]["path"] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("built", out)


def extras():
    today = datetime.date.today().isoformat()
    alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url(l)}"/>' for l in LANGS)
    urls = "".join(f'<url><loc>{url(l)}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>{"1.0" if l == "tr" else "0.9"}</priority>{alts}</url>' for l in LANGS)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}</urlset>\n', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {CFG['DOMAIN']}/sitemap.xml\n", encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(json.dumps({
        "name": CFG["BRAND"], "short_name": CFG["LOGO_A"] + " " + CFG["LOGO_B"], "start_url": "/", "display": "standalone",
        "background_color": "#06070b", "theme_color": "#06070b",
        "icons": [{"src": "/assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml"}]}, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    for l in LANGS:
        build(l)
    extras()
