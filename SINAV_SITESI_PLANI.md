# Sınav Hazırlık Sitesi - Detaylı Plan ve Analiz

**Referans Site:** https://komitedefteri.com/  
**Analiz Tarihi:** 2026  
**Hedef:** Benzer bir sınav sitesi geliştirmek, çıkmış sorular eklemek, konulara bölmek, doğru/yanlış soru tipi eklemek

---

## 1. MEVCUT SİTE ANALİZİ (komitedefteri.com)

### 1.1 Genel Yapı ve Navigasyon

| Bileşen | Açıklama |
|---------|----------|
| **Ana Seçim** | "Hangi dönemdesin?" → Dönem 1 (430 soru) / Dönem 2 (5708 soru) |
| **Komite Seçimi** | Dönem 2 için: Komite 1-5, Final, Büt (her biri ayrı JSON) |
| **3 Ana Bölüm** | Çıkmışlar, Test, Rastgele |
| **Tema** | Açık/Koyu mod desteği (localStorage) |
| **İlerleme** | "İlerlemeyi sıfırla" butonu |

### 1.2 Bölüm Detayları

#### A. Çıkmışlar (Past Questions)
- **Yıla Göre:** Akademik yıllar listesi (2019-20, 2021-22, 2022-23...)
- **Konuya Göre:** Dersler + soru sayısı + konu sayısı
  - Örn: "Anatomi 193 soru · 19 konu"
  - Her ders tıklandığında alt konular açılır

#### B. Test (Practice Test)
- **Cevap Modu:** "Hemen" veya "Sonda"
- Soru bazlı test çözme

#### C. Rastgele (Random)
- Tek tıkla rastgele soru
- Filtreler: **Ders**, **Yıl**

### 1.3 Veri Yapısı (JSON Dosyaları)

Her komite için ayrı JSON: `k1.json`, `k2.json`, `k3.json`, `k4.json`, `k5.json`

```json
{
  "id": "k1",
  "donem": 2,
  "label": "Komite 1",
  "exams": [
    { "id": "t1-1920", "label": "2019–2020", "short": "19–20", "count": 100 }
  ],
  "disc": [
    { "name": "Anatomi", "slot": 1, "count": 193 }
  ],
  "topics": {
    "Anatomi": [
      "Bazal çekirdekler", "Beyin damarları", ...
    ]
  },
  "qs": [
    {
      "id": "t1-1920-1",
      "e": "t1-1920",      // exam ID
      "n": 1,              // soru no
      "d": "Anatomi",      // ders
      "t": "Medulla oblongata",  // konu
      "ti": 9,             // konu index
      "s": "Soru metni...",        // stem
      "it": [],            // images
      "o": ["A", "B", "C", "D", "E"],  // seçenekler
      "a": "A",            // doğru cevap
      "sh": "Kısa açıklama",
      "lg": "Uzun açıklama (markdown)",
      "w": ["...", "...", "...", "...", "..."],  // her seçenek için yanlış açıklaması
      "kn": "",            // bilinen sorunlar
      "f": []              // flags
    }
  ]
}
```

### 1.4 Soru Özellikleri
- **5'li Çoktan Seçmeli** (A-E)
- **Doğru cevap** işaretli
- **Kısa açıklama** (sh)
- **Detaylı uzun açıklama** (lg) - Markdown destekli
- **Her yanlış seçenek için ayrı açıklama** (w array)
- **Resmi anahtardan cevaplar**, tartışmalı sorularda not

---

## 2. YENİ SİTE İÇİN GELİŞTİRME PLANI

### 2.1 Temel Mimari Kararları

| Konu | Öneri | Gerekçe |
|------|-------|---------|
| **Frontend** | React + TypeScript + Vite | Modern, hızlı, type-safe |
| **State Management** | Zustand / Redux Toolkit | Basit, performanslı |
| **Routing** | React Router v6 | Standart |
| **Styling** | Tailwind CSS | Utility-first, dark mode kolay |
| **Data** | Static JSON + IndexedDB | Offline çalışma, hızlı yükleme |
| **Search/Filter** | Fuse.js veya FlexSearch | Client-side fuzzy search |
| **PWA** | Workbox | Offline destekli, installable |
| **Deploy** | Vercel / Netlify / Cloudflare Pages | Ücretsiz, hızlı CI/CD |

### 2.2 Veri Modeli Genişletme (Yeni Özellikler İçin)

```typescript
// Mevcut + Yeni alanlar
interface Question {
  id: string;
  examId: string;
  number: number;
  discipline: string;              // "Anatomi", "Fizyoloji" (PDF'ten otomatik)
  topic: string;                   // "Kranial sinirler" (ayrı etiketleme işi)
  topicIndex: number;
  stem: string;                    // Soru metni
  images?: string[];               // Görsel referanslar
  options: string[];               // 5 şık (A-E)
  correctAnswer: 'A' | 'B' | 'C' | 'D' | 'E';
  shortExplanation: string;        // Kısa cevap
  longExplanation: string;         // Detaylı (markdown)
  wrongExplanations: string[];     // Her şık için neden yanlış
  knownIssues?: string;
  flags?: string[];

  // YENİ ALANLAR
  type: 'multiple_choice' | 'true_false' | 'multiple_select';
  difficulty: 'easy' | 'medium' | 'hard';
  tags: string[];                  // Ek etiketler
  source: string;                  // "2019 Dönem 1 TEM 2"
  year: number;                    // 2019
  isControversial: boolean;        // Tartışmalı mı?
  lastUpdated: string;             // ISO date

  // VERİ KALİTESİ (gerçek PDF'lerden gelen zorunlu alanlar)
  sourcePage: number;              // Orijinal PDF sayfası → "kaynağı gör" için
  answerStatus: 'official' | 'derived' | 'missing';
  confidence: number;              // 0-1 OCR/parse güveni
  reviewStatus: 'auto' | 'approved' | 'needs_review';
  duplicateOf?: string;            // Çift kopya ise diğer soru id'si
}

interface Discipline {
  id: string;
  name: string;
  slot: number;
  questionCount: number;
  topics: Topic[];
  color?: string;                  // UI için renk
  icon?: string;                   // Lucide/heroicons adı
}

interface Topic {
  id: string;
  name: string;
  disciplineId: string;
  questionCount: number;
  subTopics?: string[];            // Alt konular
}

interface ExamSession {
  id: string;                      // "2019-tem2"
  label: string;                   // "2019 Dönem 1 TEM 2"
  shortLabel: string;              // "2019 TEM 2"
  year: string;                    // "2019-2020"
  period: number;                  // 1 veya 2
  term: string;                    // "TEM 2"
  questionCount: number;
  date?: string;                   // ISO
  sourceFile: string;              // "2_241126_200803.pdf"
  sourcePages: number[];           // [1,2,...,11]
  answerStatus: 'official' | 'derived' | 'missing';
  ocrQuality: 'embedded' | 'good' | 'medium' | 'poor';
  notes?: string;
}
```

### 2.3 Özellik Listesi (MVP → Gelişmiş)

#### 🎯 **MVP (Minimum Viable Product) - 4-6 Hafta**

| # | Özellik | Öncelik | Tahmini Süre |
|---|---------|---------|--------------|
| 1 | Proje kurulumu (React+TS+Tailwind+Vite) | Yüksek | 1 gün |
| 2 | Veri yapısı tasarımı + JSON şeması | Yüksek | 2 gün |
| 3 | **PDF → JSON üretim hattı** (sınav sınırı, OCR, parser) | Yüksek | 5-7 gün |
| 4 | Ana sayfa: Yıl/Dönem seçimi (localStorage) | Yüksek | 2 gün |
| 5 | **Çıkmışlar** - Yıla göre listeleme | Yüksek | 3 gün |
| 6 | **Çıkmışlar** - Derse/Konuya göre listeleme (ağaç yapısı) | Yüksek | 4 gün |
| 7 | Soru görüntüleme sayfası (detay + kaynak sayfa) | Yüksek | 3 gün |
| 8 | **Test Modu** - Hemen/Sonda cevap seçeneği | Yüksek | 4 gün |
| 9 | **Rastgele Soru** - Filtrelerle (Ders/Yıl) | Orta | 2 gün |
| 10 | Koyu/Açık tema + localStorage | Orta | 1 gün |
| 11 | İlerleme takibi (çözülen/doğru/yanlış) | Yüksek | 3 gün |
| 12 | PWA manifest + Service Worker | Orta | 2 gün |
| 13 | Responsive tasarım (mobile-first) | Yüksek | Sürekli |

#### 🚀 **Gelişmiş Özellikler - 6-10 Hafta**

| # | Özellik | Açıklama |
|---|---------|----------|
| 13 | **Doğru/Yanlış Soru Tipi** | Yeni `type: 'true_false'` + özel UI |
| 14 | **Çoklu Doğru (Multiple Select)** | "Aşağıdakilerden hangileri doğrudur?" |
| 15 | **Akıllı Filtreleme** | Konu + Zorluk + Yıl + Tür kombine |
| 16 | **Arama** | Soru metni, konu, açıklama içinde tam metin arama |
| 17 | **Sınav Simülasyonu** | Zamanlı, realistic test deneyimi |
| 18 | **İstatistik Dashboard** | Konu bazlı başarı, zayıf alanlar, trend grafikleri |
| 19 | **Spaced Repetition (Aralıklı Tekrar)** | Anki/FSRS algoritması ile hatırlatma |
| 20 | **Yanlış Soru Bankası** | Kullanıcının yanlış yaptığı sorular otomatik toplanır |
| 21 | **Not Alma / Bookmark** | Sorulara kişisel not ekleme |
| 22 | **Topluluk Özellikleri** | Soru tartışma, alternatif çözümler |
| 23 | **PDF Export** | Test/yanlışlar PDF olarak indirme |
| 24 | **Çoklu Dil** | TR/EN (ileride) |
| 25 | **Backend API** | Kullanıcı hesapları, senkronizasyon, leaderboard |

### 2.4 Doğru/Yanlış (True/False) Soru Tipi Tasarımı

```typescript
// True/False sorusu örneği
{
  "id": "tf-k1-anatomi-001",
  "type": "true_false",
  "stem": "N. vagus, dilin genel duyusunu taşır.",
  "correctAnswer": false,  // YANLIŞ
  "options": ["Doğru", "Yanlış"],
  "shortExplanation": "Dilin genel duyusu N. trigeminus ve N. glossopharyngeus ile taşınır.",
  "longExplanation": "N. vagus dilden genel visseral duyu **almaz**...\n\n**Detay:** ...",
  "explanationIfTrue": "Bu ifade yanlıştır çünkü...",
  "explanationIfFalse": "Bu ifade doğrudur çünkü dilin genel duyusu...",
  "discipline": "Anatomi",
  "topic": "Kranial sinirler",
  "difficulty": "medium",
  "tags": ["kranial-sinirler", "vagus-siniri", "duyu-yollari"]
}
```

**UI Farkları:**
- 2 şık: "Doğru" / "Yanlış" (veya "True" / "False")
- Cevap sonrası: Her iki durum için de ayrı açıklama
- Hızlı çözüm için optimize edilmiş kart tasarımı

### 2.5 Konu (Topic) Hiyerarşisi ve Navigasyon

```
Dönem 2
  └── Komite 1
        ├── Çıkmışlar
        │     ├── Yıla Göre
        │     │     ├── 2024-2025 (108 soru)
        │     │     └── 2023-2024 (110 soru)
        │     └── Konuya Göre
        │           ├── Anatomi (193 soru · 19 konu)
        │           │     ├── Bazal çekirdekler (12 soru)
        │           │     ├── Beyin damarları (8 soru)
        │           │     └── ...
        │           ├── Fizyoloji (169 soru · 18 konu)
        │           └── ...
        ├── Test Modu
        └── Rastgele Soru
```

### 2.6 Veri Yönetimi Stratejisi

> **Güncelleme (6 Kasım 2026):** Gerçek veri seti incelendi. Veri komite bazlı değil, **yıl/dönem bazlı** geliyor.
> `sınavlar/` klasöründe 13 benzersiz sınav (~1.300 soru) var. Ayrıntı: `_analiz/KLASOR_ANALIZI.md`

#### Seçenek A: Static JSON (Basit, Performanslı) — ÖNERİLEN
```
/public/data/
  ├── index.json                 // Sınav listesi + ders/konu meta
  ├── exams/
  │     ├── 2009-2010.json
  │     ├── 2010-2011.json
  │     ├── ...
  │     └── 2024-2025.json
  └── search-index.json          // FlexSearch için
```
- Her sınav ayrı JSON → lazy load (sadece seçilen yıl iner)
- Build zamanında işlenir, CDN'den servis edilir
- Kullanıcı verisi (ilerleme, notlar) → IndexedDB
- `index.json` küçük kalır; yıl listesi + ders/konu özeti taşır

#### Seçenek B: Hybrid (Static + API)
- Static: Sorular, açıklamalar (değişmez)
- API: Kullanıcı verileri, yeni sorular, topluluk içerikleri
- Sync stratejisi: Offline-first, online olduğunda sync

#### Seçenek C: Headless CMS (Strapi, Sanity, Directus)
- İçerik yönetimi kolaylığı
- Ekip çalışması için uygun
- Daha karmaşık altyapı

**Öneri:** Başlangıçta **Seçenek A** (Static JSON + IndexedDB). Site büyürse B'ye geçiş.

### 2.7 Veri İçe Aktarma (Import) Süreci

> **Güncelleme:** Giriş verisi artık Excel değil, **ham taranmış PDF**. Hat buna göre yeniden tasarlandı.

#### 10 Adımlı PDF → JSON Hattı

```
sınavlar/*.pdf
  [1] Envanter        → sayfa sayısı, metin katmanı var mı?
  [2] Sınav sınırı    → başlık + "(1-x SORULAR)" + soru no sıfırlanması
  [3] Sayfa sırası    → ters/karışık sayfaları onar, boşları at
  [4] Metin/OCR       → gömülü metin varsa kullan; yoksa çoklu PSM/DPI OCR
  [5] Ayrıştırma      → numara, stem, A-E, cevap, ders
  [6] Cevap doğrulama → resmi anahtar / format profili / manuel
  [7] Kopya kontrolü  → Metin benzerliği (Jaccard/MinHash)
  [8] Konu etiketleme → ders → alt konu (taksonomi + manuel onay)
  [9] Kalite kontrol  → eksik şık, boş cevap, bozuk Türkçe, tekrar
  [10] JSON üretimi   → data/exams/<yil>.json + index.json
```

#### Gerçeklerden çıkan zorunlu kurallar

| Gerçek | Kural |
|---|---|
| Bir PDF'de 10 sınav var | "1 PDF = 1 sınav" varsayımı yasak; sınav sınırı tespiti zorunlu |
| Çift kopyalar var (2017-18, 2021) | Metin benzerliği ile tekilleştirme; kaynak önceliği tanımla |
| Cevap formatı 5+ çeşit | Esnek parser + sınav bazlı "format profili" |
| 2 sınavda cevap anahtarı yok | `answerStatus: missing`; test modunda gösterme |
| Sayfa sırası bozuk | Otomatik sıralama + manuel onay adımı |
| PDF'te konu yok | Konu etiketleme ayrı iş (AI ön etiket + manuel onay) |

#### Desteklenen Giriş Formatları
| Format | Açıklama |
|--------|----------|
| PDF (taranmış) | Ana kaynak; OCR + manuel doğrulama |
| PDF (metin katmanlı) | Doğrudan metin çıkarma |
| Excel (.xlsx) | Manuel düzeltme / toplu düzenleme aracı |
| JSON | Nihai site formatı |

#### Import Script Özellikleri
- Sınav sınırı ve sayfa sırası tespiti
- OCR kalite skoru + şüpheli satır işaretleme
- Duplicate detection (Jaccard / MinHash)
- Veri doğrulama (5 şık, A-E cevap, boş alan)
- Raporlama: sınav başına çıkarılan soru / şüpheli / eksik sayısı

### 2.8 GERÇEK KLASÖR ENVANTERİ (6 Kasım 2026)

`d:\...\sınavlar\` klasörünün analizi. Tam rapor: `_analiz/KLASOR_ANALIZI.md`
Makine-okunur: `_analiz/exam_manifest.json`

**Toplam: 6 PDF · 134 sayfa · 13 benzersiz sınav · ~1.300 soru**

| # | Yıl / Dönem | Kaynak PDF | Sayfa | Cevap durumu |
|---|---|---|---|---|
| 1 | 2009-2010 · Temel Bilimler II | 2_241126... | 84-90 | ❌ Yok |
| 2 | 2010-2011 · Temel Bilimler II | 2_241126... | 77-83 | ❌ Yok |
| 3 | 2011-2012 · 2. TEM | 2_241126... | 69-76 | ⚠️ Kısmi |
| 4 | 2013 · 1. Sınıf TEM 2 | 2_241126... | 57-64,67 | ✅ Var |
| 5 | 2014 · 1. Sınıf 2. YY | 2_241126... | 49-56 | ⚠️ OCR kaçırdı |
| 6 | 2014 · TEM II HAM | 2_241126... | 42-48 | ✅ Tam (gömülü metin) |
| 7 | 2015-16? · TEM II | 2_241126... | 34-41 | ⚠️ Kısmi |
| 8 | 2016-17? · Dönem I Tem 2 | 2_241126... | 24-33 | ⚠️ Kısmi + sıra bozuk |
| 9 | 2017-2018 · Dönem 1 TEM 2 | 2017-2018...pdf | 1-10 | ✅ Var |
| 10 | 2019 · Dönem 1 TEM 2 | 2_241126... | 1-11 | ⚠️ Kısmi |
| 11 | 2021 · Dönem 1 TEM 2 | 2021 tem 2.pdf | 1-9 | ⚠️ Zayıf OCR |
| 12 | 2023-2024 · Dönem 1 TEM 2 | 102 23-24...pdf | 1-8 | ⚠️ Kısmi |
| 13 | 2024-2025 · Dönem 1 TEM 2 | DÖNEM 1 TEM 2 24-25.pdf | 1-8 | ✅ Var |

**Çift kopyalar (tekilleştirilecek):**
- `2017-2018 Dönem-1 TEM-2.pdf` = `2_241126_200803.pdf` s.13-23
- `2022_TEM2_241126_201709 (1).pdf` = `2021 tem 2.pdf` (sayfaları ters sırada)

**Dikkat:** PDF'lerde yalnızca **ders** (BİYOKİMYA, HİSTOLOJİ, FİZYOLOJİ...) bilgisi var. Alt **konu** bilgisi yok → konu etiketleme ayrı bir üretim adımı.

---

## 3. TEKNİK ALTYAPI VE KOD YAPISI

### 3.1 Klasör Yapısı

```
src/
├── components/
│   ├── ui/                    # Temel UI (Button, Card, Input, Modal)
│   ├── layout/                # Header, Footer, Sidebar
│   ├── question/              # QuestionCard, QuestionDetail, AnswerExplanation
│   ├── test/                  # TestMode, TestResult, Timer
│   ├── navigation/            # PeriodSelector, CommitteeSelector, TopicTree
│   └── charts/                # ProgressChart, StatsDashboard
├── pages/
│   ├── Home.tsx               # Dönem/Komite seçimi
│   ├── PastQuestions.tsx      # Çıkmışlar (Year/Topic tabs)
│   ├── TestMode.tsx           # Test modu
│   ├── RandomQuestion.tsx     # Rastgele soru
│   ├── QuestionDetail.tsx     # Soru detay
│   ├── Statistics.tsx         # İstatistikler
│   └── Settings.tsx           # Ayarlar
├── hooks/
│   ├── useQuestions.ts        # Soru verisi yönetimi
│   ├── useProgress.ts         # İlerleme takibi (IndexedDB)
│   ├── useTheme.ts            # Tema yönetimi
│   └── useFilters.ts          # Filtre state'i
├── store/
│   ├── questionStore.ts       # Soru cache'i
│   ├── progressStore.ts       # Kullanıcı ilerlemesi
│   └── uiStore.ts             # UI state (modals, sidebar)
├── utils/
│   ├── data-loader.ts         # JSON yükleme, parsing
│   ├── search.ts              # FlexSearch wrapper
│   ├── statistics.ts          # Hesaplamalar
│   ├── export.ts              # PDF/CSV export
│   └── validators.ts          # Veri doğrulama
├── types/
│   └── index.ts               # Tüm TypeScript interface'leri
├── data/                      # Build-time işlenen veriler
│   └── index.ts
└── styles/
    └── globals.css
```

### 3.2 Performans Optimizasyonları

| Teknik | Uygulama Alanı |
|--------|----------------|
| **Code Splitting** | Her sayfa lazy load (`React.lazy`) |
| **Virtual Scrolling** | Uzun soru listeleri (react-window) |
| **Memoization** | `React.memo`, `useMemo`, `useCallback` |
| **IndexedDB** | Kullanıcı verisi, offline cache (idb library) |
| **Service Worker** | Static asset caching, offline support |
| **Image Optimization** | WebP, lazy loading, blur placeholder |
| **Bundle Analysis** | `vite-bundle-analyzer` ile takip |

### 3.3 Test Stratejisi

| Seviye | Araç | Kapsam |
|--------|------|--------|
| **Unit** | Vitest | Hook'lar, utils, store logic |
| **Integration** | Vitest + React Testing Library | Component etkileşimleri |
| **E2E** | Playwright | Kritik kullanıcı yolları |
| **Visual** | Storybook | UI bileşen katalogı |
| **Type Check** | `tsc --noEmit` | CI'de zorunlu |

---

## 4. KULLANICI DENEYİMİ (UX) TASARIM PRENSİPLERİ

### 4.1 Ana Ekranlar

#### **Ekran 1: Hoş Geldiniz / Dönem Seçimi**
- Temiz, odaklanmış tasarım
- "Hangi dönemdesin?" başlığı
- İki büyük kart: Dönem 1 / Dönem 2
- Her kartta soru sayısı rozeti
- Seçim anında localStorage'a kaydedilir

#### **Ekran 2: Komite Seçimi (Dialog/Bottom Sheet)**
- Grid layout: Komite 1-5, Final, Büt
- Her kartta: numara, isim, soru sayısı
- "DÖNEMLER" butonu ile geri dönüş
- Seçili komite header'da badge olarak görünür

#### **Ekran 3: Ana Navigasyon (3 Sekme)**
```
┌─────────────────────────────────────┐
│  Komite Defteri    [Dönem 2 · K1]  │
├─────────────────────────────────────┤
│ [Çıkmışlar] [Test] [Rastgele]       │
├─────────────────────────────────────┤
│                                     │
│   İçerik Alanı                      │
│                                     │
└─────────────────────────────────────┘
```

#### **Ekran 4: Çıkmışlar - Konuya Göre**
- Sol: Ders listesi (accordion/tree)
- Sağ: Seçili dersin konuları + soru sayıları
- Her konu tıklanabilir → soru listesi
- "İlerlemeyi sıfırla" butonu

#### **Ekran 5: Soru Detay / Test Modu**
- Soru metni (büyük, okunabilir)
- Şıklar (radio buttons / true-false toggle)
- "Cevapla" butonu
- Sonuç anında: ✓/✗ renkli feedback
- Açıklama paneli (açılır/kapanır): Kısa → Uzun → Yanlış seçenek açıklamaları
- Navigasyon: Önceki/Sonraki, Soru numarasına atla

### 4.2 Renk Sistemi (Tailwind + CSS Variables)

```css
:root {
  /* Light */
  --bg-primary: #fafafa;
  --bg-secondary: #ffffff;
  --text-primary: #171717;
  --text-secondary: #525252;
  --accent: #2563eb;        /* Blue 600 */
  --accent-hover: #1d4ed8;
  --correct: #16a34a;       /* Green 600 */
  --wrong: #dc2626;         /* Red 600 */
  --warning: #ea580c;       /* Orange 600 */
  --border: #e5e5e5;
}

[data-theme="dark"] {
  --bg-primary: #0a0a0a;
  --bg-secondary: #171717;
  --text-primary: #fafafa;
  --text-secondary: #a3a3a3;
  --accent: #3b82f6;
  --correct: #22c55e;
  --wrong: #ef4444;
  --border: #272727;
}
```

**Ders Renkleri** (Konu kartları için):
- Anatomi: `#ef4444` (Kırmızı)
- Fizyoloji: `#3b82f6` (Mavi)
- Biyokimya: `#22c55e` (Yeşil)
- Histoloji: `#f97316` (Turuncu)
- Mikrobiyoloji: `#a855f7` (Mor)
- Patoloji: `#ec4899` (Pembe)
- Farmakoloji: `#06b6d4` (Cyan)
- Diğerler: Otomatik palette

### 4.3 Erişilebilirlik (a11y)

- Semantik HTML (`<main>`, `<nav>`, `<section>`, `<article>`)
- ARIA labels, roles
- Klavye navigasyonu (Tab, Enter, Space, Arrow keys)
- Focus indicators (görünür outline)
- Renk kontrastı (WCAG AA)
- Screen reader testleri (NVDA, VoiceOver)
- `prefers-reduced-motion` desteği

---

## 5. GELİŞTİRME AŞAMALARI VE ZAMAN ÇİZELGESİ

### Hafta 1-2: Kurulum ve Temel Altyapı
- [ ] Repo oluştur, Vite+React+TS+Tailwind kur
- [ ] ESLint, Prettier, Husky, lint-staged
- [ ] TypeScript strict mode, path aliases
- [ ] Tailwind config (colors, fonts, dark mode)
- [ ] Storybook kurulumu
- [ ] CI/CD pipeline (GitHub Actions → Vercel)

### Hafta 3-4: Veri Hattı ve Ana Sayfa
- [ ] PDF envanteri + sınav manifestosu (`exam_manifest.json`)
- [ ] Sınav sınırı + sayfa sırası tespiti (script)
- [ ] OCR / gömülü metin çıkarma + parser
- [ ] Cevap formatı profilleri + doğrulama raporu
- [ ] Çift kopya tekilleştirme
- [ ] JSON data loader (lazy load)
- [ ] TypeScript types tanımla
- [ ] Yıl/Dönem seçimi sayfası
- [ ] localStorage persistence
- [ ] Header: Yıl seçici dropdown/dialog

### Hafta 5-7: Çıkmışlar Bölümü
- [ ] Yıla göre listeleme (accordion/yıllar)
- [ ] Derse/Konuya göre: Ders tree navigasyonu
- [ ] Konu detay -> soru listesi
- [ ] Soru detay sayfası (tüm açıklamalar + "kaynak PDF sayfası")
- [ ] URL routing: `/yil/2019/tem-2/ders/anatomi`

### Hafta 8-9: Test Modu ve Rastgele
- [ ] Test modu: Soru çözme akışı
- [ ] Cevap modu: Hemen / Sonda (toggle)
- [ ] Test sonucu özeti (puan, süre, detay)
- [ ] Rastgele soru: Filtreler (Ders, Yıl, Tür)
- [ ] Keyboard shortcuts (j/k, 1-5, space)

### Hafta 10-11: İlerleme ve PWA
- [ ] IndexedDB ile ilerleme kaydı
- [ ] Çözülen/Doğru/Yanlış rozetleri
- [ ] "İlerlemeyi sıfırla" fonksiyonu
- [ ] PWA: manifest, service worker, offline
- [ ] Install prompt

### Hafta 12-13: Doğru/Yanlış ve Gelişmiş Soru Tipleri
- [ ] `true_false` tipi ekle
- [ ] `multiple_select` tipi ekle
- [ ] Soru tipi discriminated union ile render
- [ ] Import scripti (Excel/CSV → JSON)
- [ ] Veri doğrulama raporu

### Hafta 14-16: İstatistikler ve Dashboard
- [ ] Genel istatistik kartları
- [ ] Ders bazlı başarı grafikleri (Recharts)
- [ ] Zaman serisi (günlük/haftalık çözüm)
- [ ] Zayıf alan analizi
- [ ] Export: PDF/CSV

### Hafta 17+: İleri Seviye (Opsiyonel)
- [ ] Spaced Repetition algoritması
- [ ] Yanlış soru bankası
- [ ] Kullanıcı hesapları (Firebase Auth / Supabase)
- [ ] Bulut senkronizasyonu
- [ ] Topluluk: Yorumlar, alternatif çözümler

---

## 6. VERİ GİRİŞİ VE YÖNETİMİ (İÇERİK EKİBİ İÇİN)

### 6.1 İçerik Giriş Şablonu (Excel)

| Sütun | Zorunlu | Açıklama | Örnek |
|-------|---------|----------|-------|
| `id` | Hayır | Otomatik üretilir | `tf-k1-anatomi-001` |
| `type` | Evet | `multiple_choice` / `true_false` / `multiple_select` | `true_false` |
| `stem` | Evet | Soru metni | `N. vagus dilin genel duyusunu taşır.` |
| `option_a` | MC için | A şıkkı | `Doğru` |
| `option_b` | MC için | B şıkkı | `Yanlış` |
| `option_c` | MC için | C şıkkı | - |
| `option_d` | MC için | D şıkkı | - |
| `option_e` | MC için | E şıkkı | - |
| `correct` | Evet | Doğru cevap (A-E veya true/false) | `false` |
| `short_explanation` | Evet | Kısa cevap | `Dilin genel duyusu V3 ve IX ile taşınır.` |
| `long_explanation` | Hayır | Markdown detaylı açıklama | `## Detaylı Açıklama\n...` |
| `wrong_explanations` | Hayır | Her şık için neden yanlış (JSON array) | `["...", "..."]` |
| `discipline` | Evet | Ders adı | `Anatomi` |
| `topic` | Evet | Konu adı | `Kranial sinirler` |
| `sub_topic` | Hayır | Alt konu | `Vagus siniri` |
| `year` | Evet | Sınav yılı | `2024` |
| `exam_session` | Evet | Oturum | `2024-2025 Final` |
| `difficulty` | Hayır | `easy`/`medium`/`hard` | `medium` |
| `tags` | Hayır | Virgülle ayrılmış etiketler | `kranial-sinirler,vagus` |
| `source` | Hayır | Kaynak | `TUS 2024 Final` |
| `is_controversial` | Hayır | Tartışmalı mı? | `false` |
| `notes` | Hayır | Editör notları | `Resmi anahtar A` |

### 6.2 Import Süreci

```bash
# 1. Excel dosyasını data/raw/ klasüne koy
# 2. Scripti çalıştır
npm run import:questions data/raw/yeni_sorular.xlsx

# 3. Çıktı: data/processed/k1_new.json
# 4. Validasyon raporu: logs/import-report.json
# 5. Mevcut veriyle birleştir (merge script)
npm run data:merge

# 6. Build ve deploy
npm run build && vercel --prod
```

### 6.3 Kalite Kontrol Listesi (Her Soru İçin)

- [ ] Soru metni net, belirsizlik yok
- [ ] 5 şık (MC) / 2 şık (TF) tam ve benzersiz
- [ ] Doğru cevap resmi anahtarla eşleşiyor
- [ ] Kısa açıklama 1-2 cümle, öz
- [ ] Uzun açıklama: neden doğru, neden diğerleri yanlış
- [ ] Her yanlış şık için özel açıklama var
- [ ] Ders/Konu sınıflandırması tutarlı
- [ ] Zorluk seviyesi uygun
- [ ] Tarih/Yıl doğru
- [ ] Tartışmalıysa `is_controversial: true` ve `notes` dolu

---

## 7. ÖLÇÜM VE BAŞARI KRİTERLERİ

### 7.1 Teknik Metrikler
| Metrik | Hedef |
|--------|-------|
| First Contentful Paint | < 1.5s |
| Time to Interactive | < 3s |
| Bundle Size (gzipped) | < 150KB |
| Lighthouse Performance | > 90 |
| Lighthouse Accessibility | 100 |
| Lighthouse Best Practices | > 90 |
| Lighthouse SEO | > 90 |

### 7.2 Kullanım Metrikleri (Analytics - Plausible/Umami)
| Metrik | Hedef |
|--------|-------|
| Günlük Aktif Kullanıcı (DAU) | 1000+ (3 ay sonra) |
| Oturum Süresi | > 15 dk |
| Günlük Soru Çözüm | > 50/usuario |
| Test Tamamlama Oranı | > 70% |
| Geri Dönüş Oranı (D7) | > 40% |

### 7.3 İçerik Metrikleri
- Toplam soru sayısı: 10,000+ (hedef)
- Konu kapsamı: TUS müfredatının %100'ü
- Soru başına ortalama açıklama uzunluğu: > 200 karakter
- Doğru/yanlış oranı: %60-70 doğru (gerçekçi zorluk)

---

## 8. RİSKLER VE MİTİGASYON

| Risk | Olasılık | Etki | Mitigasyon |
|------|----------|------|------------|
| Telif hakkı (soru metinleri) | Yüksek | Yüksek | Resmi açıklanan sorular, kendi yeniden yazımı, eğitim amaçlı kullanım disclaimer |
| Veri kalitesi (yanlış cevaplar) | Orta | Yüksek | Çift kontrol, topluluk raporlama, "şikayet et" butonu |
| Performans (büyük veri) | Orta | Orta | Virtual scroll, lazy load, IndexDB cache |
| Mobil uyumluluk | Düşük | Yüksek | Mobile-first tasarım, sürekli test |
| SEO (SPA) | Orta | Orta | Static generation (Vite SSG), sitemap, meta tags |
| Veri kaybı (localStorage) | Düşük | Orta | IndexedDB + export/import + cloud sync (gelecekte) |

---

## 9. GELİŞTİRME EKİBİ ROLLERİ (Öneri)

| Rol | Sorumluluk |
|-----|------------|
| **Full-stack Developer (1-2)** | Frontend + Import scriptleri + Deploy |
| **Medical Content Editor (1-2)** | Soru girişi, doğrulama, konu haritalama |
| **UI/UX Designer (1)** | Figma tasarımları, design system, a11y |
| **DevOps (Part-time)** | CI/CD, monitoring, analytics |

---

## 10. ILK ADIMLAR (BAŞLANGIÇ İÇİN CHECKLIST)

> **Güncel durum:** `sınavlar/` klasöründe 6 PDF / 13 sınav hazır. Veri hattı analizi tamamlandı (`_analiz/`).

### Bu Hafta Yapılacaklar:
- [x] Klasör analizi + sınav manifestosu
- [x] OCR altyapısı (Tesseract + Türkçe) testi
- [ ] GitHub repo oluştur: `sinav-platformu`
- [ ] `npm create vite@latest . -- --template react-ts`
- [ ] Tailwind, ESLint, Prettier, Husky kur
- [ ] `src/types/index.ts` — Exam/Question interface'leri
- [ ] `exam_manifest.json` → `public/data/index.json` dönüşümü
- [ ] Veri yükleme hook'u: `useQuestions.ts`
- [ ] Ana sayfa: Yıl/Dönem seçimi UI
- [ ] Vercel'e deploy et (preview URL al)

### Önümüzdeki 2 Hafta:
- [ ] Sınav sınırı + sayfa sırası scripti
- [ ] Soru parser + cevap format profilleri
- [ ] İlk 2 sınavı (2024-25, 2023-24) tam JSON'a çevir
- [ ] Ders ağacı navigasyon komponenti
- [ ] Soru detay sayfası (kaynak PDF sayfası bağlantısıyla)
- [ ] Test modu temel akışı
- [ ] IndexedDB progress store

---

## 11. FAYDALI KAYNAKLAR VE ARAÇLAR

### Kütüphaneler
| Kategori | Kütüphane |
|----------|-----------|
| State | `zustand` |
| Router | `react-router-dom` |
| Forms | `react-hook-form` + `zod` |
| Charts | `recharts` |
| Search | `flexsearch` |
| Date | `date-fns` |
| Icons | `lucide-react` |
| PDF | `@react-pdf/renderer` |
| Excel | `xlsx` (import), `exceljs` (export) |
| IndexedDB | `idb` |
| Testing | `vitest`, `@testing-library/react`, `playwright` |

### Tasarım İçin
- Figma Community: "Medical Dashboard", "Education App" şablonları
- Tailwind UI (ücretsiz bileşenler)
- Heroicons / Lucide (ikon seti)

### Referans Siteler (İlham için)
1. **komitedefteri.com** - Ana referans
2. **AnkiWeb** - Spaced repetition
3. **UWorld** - Test arayüzü, açıklama kalitesi
4. **Amboss** - Konu haritalama, entegre kaynak
5. **Khan Academy** - İlerleme takibi, mastery system
6. **Brilliant.org** - İnteraktif soru tipleri

---

## 12. ÖZET VE ÖNERİLER

### Güçlü Yönleri (komitedefteri.com'dan alınacaklar)
✅ Temiz, odaklanmış UI  
✅ Yıla/Konuya göre çift navigasyon  
✅ Detaylı açıklamalar (kısa + uzun + her şık için)  
✅ Resmi anahtar dayalı doğruluk  
✅ Offline-first mimari (static JSON)  
✅ Tema desteği  
✅ İlerleme takibi  

### Eklenecek/Yükseltilecekler
🆕 **Doğru/Yanlış soru tipi** (hızlı çözüm için)  
🆕 **Çoklu doğru (Multiple Select)**  
🆕 **Gelişmiş arama ve filtreleme**  
🆕 **İstatistik dashboard** (zayıf alan analizi)  
🆕 **Spaced Repetition** (kalıcı öğrenme)  
🆕 **Yanlış soru bankası** (otomatik)  
🆕 **Kullanıcı hesapları + bulut senkron**  
🆕 **Topluluk tartışma**  
🆕 **PDF/CSV export**  
🆕 **Mobil uygulama (Capacitor/Tauri)**  

### Teknik Borçlanmayı Önleme
- **Day 1:** TypeScript strict, ESLint, test altyapısı
- **Her PR:** Type check + lint + test geçmeli
- **Haftalık:** Bundle size analizi, Lighthouse CI
- **Her release:** Changelog, semantic versioning

---

## 13. ALINAN KARARLAR (6 Kasım 2026)

| # | Konu | KARAR |
|---|---|---|
| 1 | **Çift kopyalar** | Arşive alınmayacak. 2021 + 2022 PDF'leri **birlikte taranıp birleştirilecek**; birinde görünmeyen sorular diğerinden alınacak. 2017-18 için de aynı prensip. |
| 2 | **Eksik cevap anahtarları** | Resmi anahtar yoksa sorular **dikkatli şekilde AI tarafından çözülecek**; `answerStatus: "derived"` + `reviewStatus: "approved"` olarak işaretlenecek. |
| 3 | **Belirsiz yıllar** | Doğrulanamıyor → yıl iddia edilmeyecek. `year: "bilinmiyor"` + kaynak sırası kullanılacak. |
| 4 | **Konu ayrımı** | Alt konu YOK. Sadece **ders düzeyinde** ayrım (Biyokimya, Histoloji, Fizyoloji...). |
| 5 | **Kapsam** | Sadece **Dönem 1 / TEM 2**. |

### Uygulama sırası
1. `sinav-platformu` reposu + iskelet.
2. **Pilot: 2024-2025** sınavını uçtan uca JSON'a çevir.
3. Site: yıl seçimi → ders listesi → soru/test/rastgele.
4. Pilot çalışınca kalan sınavları aynı hatla işle (2021+2022 birleşik, cevapsızlar AI çözümlü).

---

**Bu plan, komitedefteri.com'un başarılı yapısını alırken; modern web teknolojileri, gelişmiş öğrenme bilimleri (spaced repetition, analytics), ve genişletilebilir mimari ile çok daha güçlü bir platform hedefler.**

**Hazırlayan:** AI Assistant  
**Tarih:** 2026  
**Versiyon:** 1.0