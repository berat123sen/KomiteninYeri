# Sınavlar Klasörü — Detaylı Analiz Raporu

**Tarih:** 6 Kasım 2026
**Klasör:** `sınavlar/`
**Amaç:** PDF'lerdeki çıkmış soruları yıl ve derse göre ayırıp site veri modeline uygun bir üretim hattı kurmak.

---

## 1. ÖZET

| Metrik | Değer |
|---|---|
| PDF dosyası | 6 |
| Toplam sayfa | 134 |
| Benzersiz sınav | **13** |
| Tahmini soru | **~1.300** (her sınav 100 soru) |
| Metin katmanı olan PDF | 2 (biri kısmen) |
| Taranmış / OCR gereken PDF | 4 |
| Cevap anahtarı tam olan sınav | 5 |
| Kısmi / doğrulama gereken | 5 |
| Cevap anahtarı olmayan | 2 |
| Çift kopya | 2 sınav (2017-2018, 2021) |

---

## 2. DOSYA BAZINDA BULGULAR

### 2.1 `2_241126_200803.pdf` — 90 sayfa (ANA DERLEME)

**İçinde 10 ayrı sınav var.** Çoğu taranmış, sadece 42-48 arası sayfalarda gömülü metin katmanı mevcut.

| Sınav | Sayfa | Soru | Cevap | Not |
|---|---|---|---|---|
| 2019 Dönem 1 TEM 2 | 1-11 (+12 boş) | 100 | Kısmi (71) | Başlık net |
| 2017-2018 Dönem 1 TEM 2 | 13-23 | 100 | Var (91) | **f02 ile çift kopya** |
| 2016-17? Dönem I Tem 2 | 24-33 | 100 | Kısmi (62) | Yıl + sayfa sırası doğrulanmalı |
| 2015-16? TEM II | 34-41 | 100 | Kısmi (70) | İlk sayfa çok bozuk |
| 2014 TEM II HAM (11.12.2014) | 42-48 | 100 | **Tam (100)** | Gömülü metin — mükemmel |
| 2014 1. Sınıf 2. YY | 49-56 | 100 | OCR kaçırdı | Görselde cevaplar var |
| 2013 1. Sınıf TEM 2 | 57-64, 67 (+65,66,68 boş) | 100 | Var | `CEVAP n X` formatı |
| 2011-2012 2. TEM | 69-76 | 100 | Kısmi (65) | |
| 2010-2011 Temel Bilimler II | 77-83 | 100 | **YOK** | Öğrenci işaretleri var |
| 2009-2010 Temel Bilimler II | 84-90 | 100 | **YOK** | Öğrenci işaretleri var |

**Kritik:** Aynı dosya içinde 10 farklı yıl var. Basit "1 PDF = 1 sınav" varsayımı kesinlikle çalışmaz.

### 2.2 `102 23-24 19 Haz 24 · 06·29·32 (1).pdf` — 8 sayfa

- **2023-2024 Dönem 1 TEM 2** (19 Haziran 2024)
- 100 soru, 8 sayfa
- Gömülü OCR metni var ama Türkçe karakterler bozuk (`Aagdakilerden bangii` gibi)
- Cevap formatı: `CEVAPB`, `CEVAP E`, `YANIT:D`
- 89 cevap tespit edildi → doğrulama gerekli

### 2.3 `2017-2018 Dönem-1 TEM-2.pdf` — 10 sayfa

- **2017-2018 Dönem 1 TEM 2**
- 100 soru, temiz tarama, su damgası var
- Cevap formatı: `CEVAP X` (satır içi)
- 91 cevap tespit edildi
- **f05 p13-23 ile birebir aynı sınav** → tek kopya tutulmalı

### 2.4 `2021 tem 2.pdf` — 9 sayfa

- **2021 Dönem 1 TEM 2** (başlık: `Döem 1- tem 2- 2021`)
- 100 soru, CamScanner taraması, temiz
- OCR zayıf (cevapların çoğu kaçtı)
- Ders sırası: HİSTOLOJİ → MİKROBİYOLOJİ → ... → DAVRANIŞ BİLİMLERİ

### 2.5 `2022_TEM2_241126_201709 (1).pdf` — 9 sayfa

- **2021 sınavının ters sayfa sıralı kopyası** (p1 = 2021 p9, p2 = p8, … p9 = 2021 p1)
- Yeni bir 2022 sınavı DEĞİL
- **Kullanılmamalı / arşive alınmalı**

### 2.6 `DÖNEM 1 TEM 2 24-25.pdf` — 8 sayfa

- **2024-2025 Dönem 1 TEM 2**
- 100 soru, temiz tarama
- 96 cevap tespit edildi (yüksek doğruluk)
- 2021 sınavıyla bazı sorular ortak/benzer (soru tekrarı normal)

---

## 3. ORTAYA ÇIKAN TEKNİK GERÇEKLER

### 3.1 Cevap anahtarı formatları çeşitli

Aynı veri içinde şu formatlar var:

```
CEVAP B          YANIT: A          Cevap: C
CEVAPB            Yanıt:D          CEVAP; D
Cevap 1 D         CEVAP 10 C       CEVAP: 2:E
```

→ Parser **esnek** olmalı; tek bir regex yetmez. Her sınav için "format profili" tutulmalı.

### 3.2 Bazı sınavlarda cevap anahtarı yok

2009-2010 ve 2010-2011 sınavlarında basılı anahtar yok; sadece öğrencinin kurşun kalem işaretleri var. Bunlar **güvenilir cevap kaynağı değildir**.
→ Site veri modelinde `answerStatus: "official" | "derived" | "missing"` alanı olmalı.
→ "Cevap anahtarı eksik" olan sorular test modunda gösterilmemeli veya "cevapsız" olarak işaretlenmeli.

### 3.3 Sayfa sırası bozuk sınavlar var

- `2022_TEM2...` tamamen ters.
- f05 p24-33 sınavında p25 q14 ile başlıyor; q1-13 başka sayfada veya eksik.

→ Import hattında **sayfa sırası doğrulama** adımı zorunlu. Otomatik sıralama + manuel onay.

### 3.4 OCR kalitesi sayfaya göre değişiyor

- Gömülü metin (f05 p42-48): mükemmel.
- CamScanner temiz tarama (2021, 2024-25): iyi.
- Su damgalı / düşük kontrast (2017-18, 2023-24): orta.
- El yazısı / bozuk ilk sayfa (f05 p34): kötü.

→ Tek OCR geçişi yetmez. **Çoklu PSM + DPI** denemesi, en iyi sonucu seçme, şüpheli satırları işaretleme gerekir.

### 3.5 PDF'lerde "konu" bilgisi YOK

PDF'ler yalnızca **ders** düzeyinde ayrım içeriyor:
`BİYOKİMYA (1-36. SORULAR)`, `HİSTOLOJİ (8-13. SORULAR)`, `FİZYOLOJİ (81-90. SORULAR)` …

Alt konu (ör. "Kranial sinirler", "Aksiyon potansiyeli") PDF'te yazmıyor.
→ Konu etiketleme ayrı bir iş:
  1. Ders düzeyi otomatik çıkarılır (hazır).
  2. Alt konu için ya senin vereceğin taksonomi + kural tabanlı eşleştirme, ya da AI destekli ön etiketleme + manuel onay gerekir.

---

## 4. ÖNERİLEN ÜRETİM HATTI (PDF → SİTE VERİSİ)

```
sınavlar/*.pdf
      │
      ▼
[1] PDF envanteri        → kaç sayfa, metin katmanı var mı?
      │
      ▼
[2] Sınav sınırı tespiti → başlık + "(1-x SORULAR)" + soru no sıfırlanması
      │
      ▼
[3] Sayfa sırası onarımı → ters/karışık sayfaları düzelt, boşları at
      │
      ▼
[4] OCR / metin çıkarma  → gömülü metin varsa onu kullan, yoksa OCR
      │
      ▼
[5] Soru ayrıştırma      → numara, stem, A-E, cevap, ders
      │
      ▼
[6] Cevap doğrulama      → resmi anahtar / format profili / manuel
      │
      ▼
[7] Çift kopya kontrolü  → metin benzerliği (MinHash / Jaccard)
      │
      ▼
[8] Konu etiketleme      → ders → alt konu (taksonomi + manuel onay)
      │
      ▼
[9] Kalite kontrol       → eksik şık, boş cevap, bozuk Türkçe, tekrar
      │
      ▼
[10] JSON üretimi        → data/exams/<yil>.json + index.json
```

Her adım **rapor** üretmeli: kaç soru çıktı, kaçı şüpheli, hangi sayfada sorun var.

---

## 5. SİTE VERİ MODELİNE YANSIMALAR

Mevcut plandaki şemaya şu alanlar eklenmeli:

```typescript
interface Exam {
  id: string;                 // "2019-tem2"
  year: string;               // "2019-2020"
  period: 1 | 2;
  term: string;               // "TEM 2"
  sourceFile: string;         // "2_241126_200803.pdf"
  sourcePages: number[];      // [1,2,...,11]
  questionCount: number;
  answerStatus: "official" | "derived" | "missing";
  ocrQuality: "embedded" | "good" | "medium" | "poor";
  notes?: string;
}

interface Question {
  // ... mevcut alanlar
  sourcePage: number;         // PDF sayfa numarası (orijinali göster)
  answerStatus: "official" | "derived" | "missing";
  confidence: number;         // 0-1 (OCR/parse güveni)
  reviewStatus: "auto" | "approved" | "needs_review";
  duplicateOf?: string;       // çift kopya ise diğer soru id'si
}
```

**UI karşılığı:**
- Soru kartında "Kaynak: 2019 TEM 2 · s. 4" bağlantısı → orijinal PDF sayfasını görüntüle.
- "Cevap anahtarı eksik" uyarısı → test modunda o soruyu atla.
- Admin/editör ekranı: şüpheli soruları tek tek onaylama.

---

## 6. İÇERİK ÜRETİM İŞ YÜKÜ TAHMİNİ

| İş | Otomatik | Manuel | Tahmini süre |
|---|---|---|---|
| 13 sınavın sınırlarını ayırma | %70 | %30 | 2-3 saat |
| OCR + soru ayrıştırma | %80 | %20 | 4-6 saat |
| Cevap doğrulama | %60 | %40 | 3-5 saat |
| Konu etiketleme (1.300 soru) | %70 ön etiket | %30 onay | 5-8 saat |
| Kalite kontrol + düzeltme | %50 | %50 | 6-10 saat |
| **Toplam** | | | **~20-32 saat** |

Bu, ilk 1.300 soru için gerçekçi bir efor. Sonraki yıllar geldikçe hat oturmuş olacağı için süre düşer.

---

## 7. SANA SORULAR (PLAN İÇİN KRİTİK)

1. **Çift kopyalar:** 2017-2018 ve 2021 için hangi dosya "ana kaynak" olsun? (Öneri: `2017-2018...pdf` ve `2021 tem 2.pdf`; `2022_TEM2...` arşive.)
2. **Eksik cevap anahtarları:** 2009-10 ve 2010-11 için resmi anahtar bulabilir misin? Bulamazsak bu iki sınavı "cevapsız / sadece okuma" modunda mı yayınlayalım?
3. **Yıl doğrulama:** f05 p24-33 ve p34-41 sınavlarının yılları belirsiz. Senin okul arşivinden doğrulayabilir misin?
4. **Konu taksonomisi:** Ders altı konu listesini sen mi vereceksin, yoksa ben mi önereyim (tıp müfredatına göre) + sen onaylayacak mısın?
5. **Kapsam:** Sadece Dönem 1 / TEM 2 mi, yoksa başka dönemler de gelecek mi?

---

## 8. SONUÇ

Klasör, siteyi kurmak için **yeterli ve değerli** bir başlangıç sağlıyor: 13 sınav, ~1.300 soru.
Ancak veri "temiz" değil; **ham PDF → yapılandırılmış JSON** arasında ciddi bir üretim hattı kurmak gerekiyor. Plan bu gerçeğe göre güncellendi.
