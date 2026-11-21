# Bodrum Elektrik – Web Sitesi

Statik, çok hızlı, 3 dilli (TR / EN / RU) ve SEO uyumlu site. Sunucu tarafında hiçbir şey gerekmez – her hostingde çalışır.

## Klasör yapısı
| Dosya | Ne işe yarar |
|---|---|
| `build.py` | **Firma bilgileri (telefon, WhatsApp, e‑posta, domain)** en üstte. Siteyi oluşturur. |
| `content.py` | Tüm metinler (hizmetler, SSS, yorumlar, bölgeler) – 3 dilde |
| `template.html` | Sayfa iskeleti |
| `assets/` | CSS, JS, görseller |
| `index.html`, `en/`, `ru/` | **Oluşturulan site** (bunları yayına alın) |
| `sitemap.xml`, `robots.txt` | Google için |

## Değişiklik yapınca
```
python build.py
```

## Yayına alma
`index.html`, `en/`, `ru/`, `assets/`, `sitemap.xml`, `robots.txt`, `site.webmanifest` dosyalarını hostinge yükleyin
(Netlify / Cloudflare Pages / Firebase Hosting ücretsiz ve çok hızlıdır).

## Google'da 1. sıraya çıkmak için YAPILMASI GEREKENLER
1. **Domain al** (ör. bodrumelektrikci.com) → `build.py` içindeki `DOMAIN` değerini değiştir.
2. **Google Search Console**'a siteyi ekle, `sitemap.xml` gönder.
3. **Google İşletme Profili** (en önemli adım!): web sitesi linkini ekle, kategori: *Elektrikçi*, hizmet bölgelerine tüm Bodrum mahallelerini ekle, gerçek iş fotoğrafları yükle, haftada 1 gönderi paylaş.
4. **Müşterilerden Google yorumu iste** – yorum sayısı yerel sıralamada çok belirleyici.
5. `content.py` içindeki örnek müşteri yorumlarını **gerçek yorumlarla** değiştir.
6. Gerçek iş fotoğraflarını `assets/img/` içine koy (yapay zeka görsellerinin yerine zamanla).
7. Instagram ve Google Maps linklerini `build.py`'de güncelle.
