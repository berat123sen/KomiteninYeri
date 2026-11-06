# Sınav Platformu

Çukurova Üniversitesi Tıp Fakültesi **Dönem 1 / TEM 2** çıkmış soruları için modern bir çalışma platformu.

> Resmî bir üniversite sitesi değildir. Soruların hakları ilgili fakülteye aittir.

## Özellikler

- **Çıkmışlar** — yıla ve derse göre ayrılmış arşiv
- **Ders filtreleri** — Biyokimya, Histoloji, Fizyoloji, Biyofizik, Mikrobiyoloji ve diğerleri
- **Test modu** — anında geri bildirim veya sonda toplu değerlendirme; süre, soru haritası, ders bazında sonuç
- **Rastgele soru** — sınav ve ders filtreleriyle 5/10/20/50 soruluk pratik seansları
- **İlerleme takibi** — cevaplar tarayıcıdaki IndexedDB'de saklanır; ders bazında doğruluk oranları
- **Kaynak şeffaflığı** — her soruda kaynak PDF sayfası bağlantısı ve cevap durumu etiketi
- **Açık / koyu tema**, mobil uyumlu arayüz

## Teknoloji

| Katman | Teknoloji |
|---|---|
| UI | React 18 + TypeScript |
| Build | Vite 6 |
| Stil | Tailwind CSS v4 |
| Yönlendirme | React Router 7 |
| Durum | Zustand |
| Kalıcılık | IndexedDB (`idb`) |
| İkonlar | lucide-react |

Veriler statik JSON olarak `public/data/` altında tutulur; sunucu veya veritabanı gerekmez.

## Kurulum

```bash
npm install
npm run dev
```

Üretim derlemesi:

```bash
npm run build
npm run preview
```

## Veri yapısı

```text
public/
  data/
    index.json                   # sınav listesi (özet)
    exams/
      2024-2025-tem-2.json       # sınav + 105 soru
  kaynak/
    2024-2025-tem-2.pdf          # "Kaynak PDF" bağlantıları için
```

`index.json`:

```json
{
  "version": 1,
  "exams": [
    {
      "id": "2024-2025-tem-2",
      "label": "2024-2025 Dönem 1 TEM 2",
      "year": "2024-2025",
      "period": 1,
      "term": "TEM 2",
      "questionCount": 105,
      "answerStatus": "official",
      "disciplines": [{ "id": "histoloji", "name": "Histoloji", "questionCount": 9, "first": 1, "last": 9 }]
    }
  ]
}
```

Soru kaydı:

```json
{
  "id": "2024-2025-tem-2-q001",
  "examId": "2024-2025-tem-2",
  "number": 1,
  "disciplineId": "histoloji",
  "discipline": "Histoloji",
  "type": "multiple_choice",
  "stem": "Soru kökü…",
  "options": ["A şıkkı", "B şıkkı", "C şıkkı", "D şıkkı", "E şıkkı"],
  "correctAnswer": "E",
  "sourcePage": 1,
  "answerStatus": "official",
  "confidence": 0.99,
  "reviewStatus": "approved",
  "note": "Varsa açıklama"
}
```

### Cevap durumları

| Değer | Anlamı |
|---|---|
| `official` | Cevap, sınavın basılı resmî cevap anahtarından alındı. |
| `derived` | Basılı cevap okunamadığı için soru AI ile çözüldü; arayüzde ayrıca işaretlenir. |
| `missing` | Cevap henüz eklenmedi. |

## Yeni sınav ekleme

1. PDF'yi `public/kaynak/<exam-id>.pdf` olarak kopyala.
2. Soruları `public/data/exams/<exam-id>.json` dosyasına ekle.
3. `public/data/index.json` içindeki `exams` listesine özet kaydı ekle.
4. `sourcePage` alanlarını PDF sayfa numaralarıyla eşleştir.
5. `npm run build` ile doğrula.

Pilot veri üretimi için kullanılan betik: `../_analiz/build_2024_2025.py`.

## Vercel'e dağıtım

Proje kökünde `vercel.json` SPA yönlendirmelerini içerir.

```bash
npm i -g vercel
vercel
vercel --prod
```

Ya da GitHub'a push edip Vercel panelinden içe aktar:

- Framework preset: **Vite**
- Build command: `npm run build`
- Output directory: `dist`

## Mevcut durum

- **2024-2025 Dönem 1 TEM 2** — 105 soru yayında (1-100 + ENTEGRE 101-105).
  - 5, 91 ve 98. soruların basılı cevabı kaynakta okunamadığı için AI çözümü olarak işaretlendi.
- Diğer yıllar aynı doğrulama hattından geçirilerek eklenecek.
