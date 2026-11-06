# -*- coding: utf-8 -*-
"""2024-2025 Dönem 1 TEM 2 sınavını JSON'a dönüştürür.
Kaynak: sınavlar/DÖNEM 1 TEM 2 24-25.pdf (8 sayfa, 105 soru).
Metinler taranmış sayfalardan tek tek okunarak doğrulanmıştır.
"""
import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EXAM_ID = "2024-2025-tem-2"
OUT_DIR = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data"
EXAM_DIR = os.path.join(OUT_DIR, "exams")
os.makedirs(EXAM_DIR, exist_ok=True)

DISC = {
    "histoloji": "Histoloji",
    "fizyoloji": "Fizyoloji",
    "biyokimya": "Biyokimya",
    "biyofizik": "Biyofizik",
    "mikrobiyoloji": "Mikrobiyoloji",
    "davranis-bilimleri": "Davranış Bilimleri",
    "tip-tarihi-etik": "Tıp Tarihi ve Etik",
    "sbet": "SBET",
    "entegre": "Entegre",
}

QUESTIONS = []


def add(n, disc, stem, opts, ans, page, status="official", conf=0.99, note=None):
    assert len(opts) == 5, f"Soru {n}: 5 şık değil ({len(opts)})"
    assert ans in "ABCDE", f"Soru {n}: geçersiz cevap {ans}"
    rec = {
        "id": f"{EXAM_ID}-q{n:03d}",
        "examId": EXAM_ID,
        "number": n,
        "disciplineId": disc,
        "discipline": DISC[disc],
        "type": "multiple_choice",
        "stem": stem.strip(),
        "options": [o.strip() for o in opts],
        "correctAnswer": ans,
        "sourcePage": page,
        "answerStatus": status,
        "confidence": conf,
        "reviewStatus": "approved",
    }
    if note:
        rec["note"] = note
    QUESTIONS.append(rec)


# ------------------------- HİSTOLOJİ (1-9) -------------------------
add(1, "histoloji",
    "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.",
    [
        "Histoloji terimi, doku anlamına gelen histos ve bilim/çalışma anlamına gelen logos kelimelerinin birleşmesiyle oluşmuştur.",
        "Embriyoloji fertilizasyondan doğuma kadar insanın normal gelişimini inceleyen bilim alanıdır.",
        "Normal yapı ve gelişim yanında, hücre ve doku hasarının mikroskobik düzeyde araştırılması, kök hücre biyolojisi, rejeneratif tıp araştırmaları ile in vitro fertilizasyon da Histoloji ve Embriyolojinin çalışma alanları içerisinde yer alır.",
        "İnsan vücudunu oluşturan esas yapısal bileşenler; hücreler, hücrelerarası maddeler ve vücut sıvılarıdır.",
        "Canlıların temel yapısal biriminin hücre olduğu gerçeği elektron mikroskobunun keşfi ile ortaya konulmuştur.",
    ], "E", 1)

add(2, "histoloji",
    "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.",
    [
        "Histoloji, hücre, doku ve organların normal yapısını mikroskop ile inceleyen bilim alanıdır.",
        "Mikroskobik incelemelerde en önemli olan iki faktör, büyütme ve ayırma gücüdür.",
        "İnsan gözünün ayırma gücü hücrelerin ayırt edilmesi için yeterlidir.",
        "Histoloji bilim alanının gelişiminde; hücrenin tanımlanması, hücre teorisinin ortaya konulması ve elektron mikroskobunun keşfi çok önemli aşamalardır.",
        "Histoloji ve Embriyoloji bilim alanının gelişim sürecinde; Robert Hooke ilk defa hücreyi tanımlarken, hücrelerde bir çekirdeğin varlığı Robert Brown tarafından keşfedilmiştir.",
    ], "C", 1)

add(3, "histoloji",
    "Elektron mikroskobik doku takibi sürecinde aşağıdakilerden hangileri kullanılır?\nI. Gömme materyali olarak Rezin\nII. Tespit solüsyonu (fiksatif) olarak Formalin\nIII. Kesit almak için Ultramikrotom\nIV. Boyama için Uranil asetat-Kurşun sitrat\nV. Şeffaflandırma için Ksilol",
    ["I, III, IV", "I, II, V", "II, IV, V", "I, II, V", "II, III, IV"],
    "A", 1)

add(4, "histoloji",
    "Kollajen lifleri boyamak için hangi histokimyasal yöntem tercih edilebilir?",
    ["Gümüşleme", "Periyodik Asit Shift (PAS)", "Masson Trikrom", "Hematoksilen-Eozin", "Van Gieson"],
    "C", 1)

add(5, "histoloji",
    "Lizozomlarla ilgili olarak aşağıdakilerden hangisi yanlıştır?",
    [
        "Lizozomal membranın iç yüzeyde glikozillenmiş olması ve lizobifosfatidik asit içeriğinin fazla olması lizozomun kendi hidrolitik enzimlerinden etkilenmesini önler.",
        "Lizozomal membran proteinleri endozomlarda sentezlenerek lizozoma aktarılır.",
        "Fagositoz, reseptör aracılı endositoz ve otofaji gibi süreçlerde aktif rol oynayan organellerdir.",
        "Lipazlar, proteazlar, nükleazlar gibi yıkıcı enzimler içerirler.",
        "Özellikle aktif fagositoz yapan makrofaj ve nötrofil gibi hücrelerde bol miktarda bulunurlar.",
    ], "B", 1, status="derived", conf=0.9,
    note="Bu sorunun basılı cevabı sayfada yer almıyor; AI tarafından çözüldü.")

add(6, "histoloji",
    "Nöral ya da hormonal bir uyaran varlığında, hücreye kalsiyum girişi ile, depolanmış salgı granüllerinin içeriğinin hücrenin plazma membranından dış ortama iletilmesi hangi yolla gerçekleşir?",
    [
        "Reseptör aracılı endositoz",
        "Pinositoz",
        "Ekzositozun konstütif yolağı",
        "Ekzositozun düzenlenmiş salgı yolağı",
        "Fagositoz",
    ], "D", 1)

add(7, "histoloji",
    "İçeriğindeki oksidatif enzimlerle hücredeki toksik moleküllerin parçalanmasını sağlayan, yağ asitlerinin β-oksidasyonunu gerçekleştiren, karaciğer ve böbrekte yaygın olarak bulunan organel hangisidir?",
    [
        "Golgi Kompleksi",
        "Endozom",
        "Peroksizom",
        "Mitokondriyon",
        "Granüler Endoplazmik Retikulum",
    ], "C", 1)

add(8, "histoloji",
    "Mikrotübüllerle ilgili olarak aşağıdakilerden hangisi yanlıştır?",
    [
        "Eksi uçlarından mikrotübül organize edici merkezde bulunan perisentrioler cisimcikteki γ-nükleasyon bölgelerine tutunan, α ve β tübülin dimerlerinden oluşan içi boş protein tüpleridir.",
        "Hücre içi transport, hücre hareketi ve mitoz sırasında mitotik iğ oluşumunda fonksiyon görürler.",
        "Polimerizasyon (uzama), depolimerizasyon (kısalma) hızları mikrotübül ilişkili proteinlerle denge halinde tutulur.",
        "Silya ve flagellanın yapısında 9+2 lik aksonem düzeninde bulunurlar ve bu hücre uzantılarında mikrotübüller stabildir (uzayıp kısalmazlar).",
        "Mikrovillusların yapısını oluştururlar.",
    ], "E", 1)

add(9, "histoloji",
    "Hücre çekirdeği ile ilgili olarak verilen seçeneklerden hangisi yanlıştır?",
    [
        "Her hücrede farklı şekil, boyut ve sayıda bulunabilir.",
        "İki tabakalı membran içerir.",
        "İç çekirdek membranına tutunan ara filaman olan laminler burada destek fonksiyonu gören nüklear laminayı oluşturur.",
        "Aktif olarak çeşitli moleküller üreten sinir hücreleri ve karaciğer hücreleri gibi hücrelerde kromatin sıkıca paketlenmiş olup, çekirdek hiperkromatiktir.",
        "Çekirdek ve sitoplazma arasındaki molekül geçişi nüklear por kompleksi ile sağlanmaktadır.",
    ], "D", 1)

# ------------------------- FİZYOLOJİ (10-19) -------------------------
add(10, "fizyoloji",
    "Claude Bernard’ın “milieu” ortamları ile bunlara karşılık gelen vücut sıvı bölükleri arasında yapılan aşağıdaki eşleştirmelerden hangisi doğrudur?",
    [
        "Milieu interior — Hücre içi sıvı; Milieu exterior — İnterstisyel sıvı",
        "Milieu interior — Hücre dışı sıvı; Milieu exterior — Plazma sıvısı",
        "Milieu interior — İnterstisyel sıvı; Milieu exterior — Transsellüler sıvı",
        "Milieu interior — Hücre içi sıvı; Milieu exterior — Organizma dışı ortam",
        "Milieu interior — Hücre dışı sıvı; Milieu exterior — Organizma dışı ortam",
    ], "E", 1)

add(11, "fizyoloji",
    "Aşağıdakilerden hangileri pozitif geri bildirim devreleri şeklinde çalışır?\nI. Kan basıncının düzenlenmesini sağlayan barorefleks mekanizma\nII. Kanayan damardaki kanamayı durduran pıhtılaşma mekanizması\nIII. Doğum sırasında rahimde art arda gelişen kasılmaların mekanizması\nIV. Kan glükoz düzeyini ayarlayan insülin mekanizması",
    ["I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV"],
    "B", 2)

add(12, "fizyoloji",
    "Tay-Sacks hastalığına yol açan mutasyona uğramış heksosaminidaz A enzimi aşağıdaki hücre organellerinden hangisinde bulunur?",
    ["Golgi aygıtı", "Peroksizom", "Mitokondri", "Sentrozom", "Lizozom"],
    "E", 2)

add(13, "fizyoloji",
    "Aşağıdakilerden hangileri mitokondrilerin enerji üretimi dışındaki işlevleri arasında bulunur?\nI) Apoptozda rol oynamaları\nII) Ca²⁺ depolamaları\nIII) Kondroitin sülfat üretmeleri\nIV) Hasarlı organeli sindirmeleri",
    ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"],
    "A", 2)

add(14, "fizyoloji",
    "Aşağıdakilerden hangileri hücre iskeletinin elemanları olarak ara filament ailesindendir?\nI) Dinein\nII) Vimentin\nIII) Kinezin\nIV) Desmin",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "III ve IV"],
    "D", 2)

add(15, "fizyoloji",
    "Aşağıdakilerden hangileri bir molekülün hücre dışından hücre içine difüzyonunu azaltıcı yönde etki eden parametreler arasında yer alır?\nI) Mutlak sıcaklık\nII) Sıvı ortamın viskozitesi\nIII) Molekülün yarıçapı\nIV) Boltzmann sabiti",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "I ve IV"],
    "B", 2)

add(16, "fizyoloji",
    "ATP bağlayıcı kaset (ABC) taşıyıcıları aşağıdaki maddelerden hangilerinin taşınmasında rol oynar?\nI) Vitamin\nII) Ca²⁺\nIII) Ksenobiyotik\nIV) H⁺",
    ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"],
    "C", 2)

add(17, "fizyoloji",
    "Koleranın tedavisinde ağızdan verilen suyun içindeki Na⁺’un sindirim kanalından epitel hücresinin içine emilimi aşağıdaki taşıyıcı mekanizmaların hangisi aracılığıyla gerçekleşir?",
    ["Endositoz", "Basit difüzyon", "Primer aktif taşıma", "Sekonder aktif taşıma", "Kolaylaştırılmış difüzyon"],
    "D", 2)

add(18, "fizyoloji",
    "Fosfodiesteraz enzimi aşağıdakilerden hangisini etkisiz hale getirir?",
    ["IP3", "DAG", "cGMP", "NF-κB", "PGE₂"],
    "C", 2)

add(19, "fizyoloji",
    "Nitrik oksidin aktive ettiği reseptör ile bu aktivasyon sonucu oluşan ikinci habercı aşağıdaki seçeneklerden hangisinde doğru olarak eşleştirilmiştir?",
    [
        "Tirozin kinaz — IP₃",
        "Serin treonin kinaz — cAMP",
        "Adenilil siklaz — cAMP",
        "Fosfataz — cGMP",
        "Guanilil siklaz — cGMP",
    ], "E", 2)

# ------------------------- BİYOKİMYA (20-58) -------------------------
add(20, "biyokimya",
    "Aşağıdakilerden hangisi lipit sindirim için yanlıştır?",
    [
        "Barsak hücreleri apo B48 üretir.",
        "Pankreatik lipaz etkisi ile trigliseritler monoasilgliserol ve serbest yağ asidine yıkılır.",
        "Barsak epitel hücrelerinde tekrar trigliserit sentezlenir.",
        "Lingual lipaz ve Gastrik lipaz’ın aktivasyonu için Ko-lipaz’a gereksinim vardır.",
        "Barsakta sentezlenen şilomikronlar diyet trigliseritlerinin taşınmasında rol oynar.",
    ], "D", 2)

add(21, "biyokimya",
    "Palmitoil CoA’nın (16:0) beta oksidasyonunda aşağıdaki ifadelerden hangisi yanlıştır?",
    [
        "Net 106 ATP üretilir.",
        "Yedi döngü sonucunda sekiz Asetil CoA üretilir.",
        "Yedi adet FADH₂ üretilir.",
        "17 karbonlu bir yağ asidinin oksidasyonuna oranla daha fazla ATP üretilir.",
        "Oksidasyon için gerekli NADPH’lar pentoz fosfat yolundan elde edilir.",
    ], "E", 2)

add(22, "biyokimya",
    "Keton cisimcikleri ile ilgili doğru ifade hangisidir?",
    [
        "Toklukta kan düzeyleri çok yükselir.",
        "Kas ve beyin hücreleri tarafından üretilir.",
        "Sitoplazmada HMG CoA redüktaz tarafından üretilir.",
        "Karaciğer tarafından enerji yakıtı olarak kullanılırlar.",
        "Kanda en yüksek konsantrasyonda beta hidroksibütirat bulunur.",
    ], "E", 2)

add(23, "biyokimya",
    "Aşağıdakilerden hangisi Asetil CoA’dan oluşmaz?",
    ["Gliserol 3-fosfat", "Kolesterol", "Araşidonik asit", "Hidroksi metil glutaril CoA (HMG CoA)", "Asetoasetat"],
    "A", 2)

add(24, "biyokimya",
    "Prostoglandinler ile ilgili ifadelerden hangi(leri) doğrudur?\nI. Prostoglandinlerin öncü maddesi araşidonik asittir.\nII. Araşidonik asit esansiyel bir yağ asididir.\nIII. Prostoglandin sentezi için siklooksijenaz enzimine gereksinim vardır.",
    ["Sadece II", "I ve III", "Sadece I", "I, II ve III", "II ve III"],
    "B", 3)

add(25, "biyokimya",
    "Yağ asidi sentezinde yer alan Asetil CoA karboksilaz enzimi için yanlış ifade hangisidir?",
    [
        "Malonil CoA üretimini sağlar.",
        "Substrat olarak Asetil CoA’yı kullanır.",
        "Yapısında prostetik grup olarak piridoksal fosfat bulunur.",
        "Reaksiyon sırasında 1 mol ATP kullanır.",
        "Sentez için HCO₃ gereksinimi vardır.",
    ], "C", 3)

add(26, "biyokimya",
    "Transaminasyon tepkimeleri hakkında verilenlerden hangi(leri) doğrudur?\nI. Hem sentez hem de yıkımda görev alırlar.\nII. Yıkım sırasında serbest amonyak açığa çıkar.\nIII. Sentez sırasında serbest amonyağı bir ketoaside bağlar.",
    ["Sadece I", "I ve II", "I, II ve III", "II ve III", "Sadece II"],
    "A", 3)

add(27, "biyokimya",
    "Glutamat dehidrogenaz tepkimesi için verilenlerden hangi(leri) doğrudur?\nI. Tepkime sonucunda alfa ketoglutarat oluşur.\nII. Bu enzim mitokondri matriksinde bulunur.\nIII. Kofaktör olarak NAD ve NADP’yi kullanır.",
    ["Sadece I", "I ve II", "I, II ve III", "II ve III", "Sadece II"],
    "C", 3)

add(28, "biyokimya",
    "Üre döngüsünün ilk tepkimesi olan Karbamoil fosfat sentetaz I reaksiyonu için hangi(leri) doğrudur?\nI. Tepkime için N-asetil glutamat’a gereksinimi vardır.\nII. Substrat olarak bikarbonat ve serbest amonyak kullanılır.\nIII. Reaksiyon sırasında 2 ATP’den 2 ADP oluşur.",
    ["Sadece I", "I ve II", "I, II ve III", "I ve III", "II ve III"],
    "C", 3)

add(29, "biyokimya",
    "Homosistein’den metionin sentezini gerçekleştiren metionin sentaz enzimi için aşağıdakilerden hangisi gereklidir?",
    ["B12 vitamini", "Biotin", "Niasin", "Folik asit", "Tiamin"],
    "D", 3)

add(30, "biyokimya",
    "Triptofandan aşırı miktarda serotonin üretildiği durumlarda hangi vitaminin eksikliği oluşabilir?",
    ["B12 vitamini", "Biotin", "Niasin", "Folik asit", "Tiamin"],
    "C", 3)

add(31, "biyokimya",
    "Aşağıda verilen maddelerden hangisi tirozin aminoasitinden sentezlenemez?",
    ["Triiyodotironin", "Epinefrin", "Melanin", "Kreatinin", "Dopamin"],
    "D", 3)

add(32, "biyokimya",
    "Aşağıdakilerden hangisi insülin’in etkileri arasında yer almaz?",
    [
        "Kas ve yağ doku hücrelerine glukoz girişinin sağlanması",
        "Hormon-duyarlı lipazın uyarılması",
        "Glikolizin uyarılması",
        "Glikojen sentezinin uyarılması",
        "Protein sentezinin uyarılması",
    ], "B", 3)

add(33, "biyokimya",
    "Aşağıdaki glikoliz enzimlerinden hangisi karbon-karbon bağını kırarak fruktoz 1,6-bifosfatın trioz şekerlere dönüşümünü sağlar?",
    ["Enolaz", "Trioz Fosfat İzomeraz", "Fosfogliserat Kinaz", "Gliseraldehit 3 Fosfat dehidrogenaz", "Aldolaz A"],
    "E", 3)

add(34, "biyokimya",
    "Pirüvattan tek bir reaksiyon ile hangi madde oluşamaz?",
    ["Fosfoenol piruvat", "Laktat", "Alanin", "Oksaloasetat", "Asetil CoA"],
    "A", 3)

add(35, "biyokimya",
    "Aşağıdaki dehidrogenaz enzimlerinin hangisinin aktivitesiyle, alternatif yolaklarla 1,5 ya da 2,5 ATP sentezi gerçekleşebilir?",
    ["Gliseraldehit 3 fosfat dehidrogenaz", "Pirüvat dehidrogenaz", "İzositrat dehidrogenaz", "Alfa ketoglutarat dehidrogenaz", "Malat dehidrogenaz"],
    "A", 3)

add(36, "biyokimya",
    "Krebs siklusunda aşağıdakilerden hangisi gerçekleşmez?",
    ["Asetil CoA’nın oksidasyonu", "alfa-ketoglutarat oluşumu", "CO₂ oluşumu", "NADH ve FADH₂ oluşumu", "Asetil CoA’nın piruvata dönüşümü"],
    "E", 3)

add(37, "biyokimya",
    "Krebs döngüsünden elde edilen FADH₂, ETZ’ye hangi basamaktan girer?",
    ["Kompleks I", "Kompleks II", "Koenzim Q", "Kompleks III", "Kompleks IV"],
    "B", 3)

add(38, "biyokimya",
    "Pentoz fosfat yolunun başlıca amacı aşağıdakilerden hangisidir?",
    ["Amino asitlerin karbon iskeletinin oksidasyonu", "ATP sentezlemek", "NADPH ve riboz-5-fosfat üretmek", "Açlıkta kan glukozunu artırmak", "Asidik şekerlerin üretilmesi"],
    "C", 4)

add(39, "biyokimya",
    "Aşağıdakilerden hangisi glukoneogenezde yer alan enzim veya metabolit değildir?",
    ["Fosfoglikoizomeraz", "Gliseraldehid 3-fosfat", "Aldolaz", "Piruvat dehidrogenaz", "Glukoz 6-fosfataz"],
    "D", 4)

add(40, "biyokimya",
    "Glikojen sentezi için aşağıdakilerden hangisi yanlıştır?",
    [
        "Protein yapılı bir primere gereksinim vardır.",
        "Glikojenin yapısında 1,4 ve 1,6 glikozit bağları vardır.",
        "Glikojen sentezi insülin ile uyarılır.",
        "Glikojen sentazın fosforile hali aktiftir.",
        "Glukoz monomerleri senteze UDP-Glukoz olarak girer.",
    ], "D", 4)

add(41, "biyokimya",
    "Glikojenin yıkılmasını sağlayan enzimlerden biri olan glikojen fosforilazın ürünü aşağıdakilerden hangisidir?",
    ["Glikoz 1-fosfat", "Glikoz", "UDP-glikoz", "Glikoz 6-fosfat", "Glikoz 1,6-bifosfat"],
    "A", 4)

add(42, "biyokimya",
    "Fruktoz metabolizması ile ilgili aşağıdakilerden hangisi yanlıştır?",
    [
        "Fruktoz metabolizması karaciğerde çoğunlukla heksokinaz ile 6. karbondan fosforilasyon ile başlar.",
        "Fruktoz metabolizmasının glikoz metabolizmasına göre daha hızlı olmasının nedeni Fosfofruktokinaz kontrol basamağını atlamasıdır.",
        "Fazla fruktozlu diyet hiperürisemiye neden olur.",
        "Aldolaz-B eksikliğinde herediter fruktoz intoleransı gelişir.",
        "Diyabette görülen katarakt, lenste sorbitol birikiminden kaynaklanır.",
    ], "A", 4)

add(43, "biyokimya",
    "Pentoz fosfat yolunun inhibitörü aşağıdakilerden hangisidir?",
    ["NAD⁺", "FAD", "Asetil CoA", "NADH", "NADPH"],
    "E", 4)

add(44, "biyokimya",
    "Kan glukozu düşmüş bir kişide, aşağıdaki enzimlerden hangisinin karaciğerde inhibe olması gerekir?",
    ["Pirüvat karboksilaz", "Pirüvat kinaz", "PEP karboksikinaz", "Fruktoz-1,6-bifosfataz", "Glukoz-6-fosfataz"],
    "B", 4)

add(45, "biyokimya",
    "Aşağıdaki aminoasitlerden hangisi Koenzim olarak C Vitamininin kullanıldığı bir hidroksilasyon reaksiyonu sonucu oluşur ve kolajenin esas yapısının oluşmasında rol oynar?",
    ["Glisin", "Valin", "Lisin", "Glutamin", "Prolin"],
    "E", 4)

add(46, "biyokimya",
    "Aşağıdakilerden hangisi mitokondri membranında Elektron Taşıma Zincirinde (ETZ) NADH+H ve FADH₂’den aldığı elektronları Sitokromlara aktararak ATP sentezinde rol oynayan lipidik formattaki yapıdır?",
    ["Piruvat", "Alfa Lipoik Asit", "Alfa-keto glutarat", "Koenzim Q10", "Asetil-Coa"],
    "D", 4)

add(47, "biyokimya",
    "Aşağıdaki minerallerden hangisi insülinin glukozu hücre içerisine almasında rol oynayarak glukoz transportunu kolaylaştırıp insülinin etkisini potansiyalize eder?",
    ["Demir", "İyot", "Krom", "Manganez", "Molibden"],
    "C", 4)

add(48, "biyokimya",
    "Aşağıdaki eser elementlerden hangileri tiroid dokusunda T3 ve T4 hormonlarının sentezi için gereklidir?",
    [
        "Mb (Molibden), Fe",
        "Se (Selenyum), I (İyot)",
        "Zn (Çinko), Ca (Kalsiyum)",
        "Cr (Krom), Cu (Bakır)",
        "Mn (Mangan), Mg",
    ], "B", 4)

add(49, "biyokimya",
    "Aşağıdakilerden hangisi mortalitesi en yüksek hastalıklar grubunda olan ve beslenme ile ilişkisi bilimsel olarak kanıtlanmış hastalıklardan değildir?\nI. Kardiyovasküler Hastalıklar\nII. Diabetes Mellitus\nIII. Stroke (İnme)",
    ["Yalnız I", "Yalnız II", "I ve II", "II ve III", "I, II ve III"],
    "E", 4)

add(50, "biyokimya",
    "Alveolleri kollabe olmasını önleyen apoproteinler, karbonhidratlar ve esas olarak içerdiği lipid ile solunumu kolaylaştıran akciğer sürfaktanı içeriğindeki lipid hangi seçenekte doğru verilmiştir?",
    ["Fosfatidilinozitol", "Fosfatidilkolin", "Fosfatidiletanolamin", "Glikosfingolipid", "Sfingomiyelin"],
    "B", 4)

add(51, "biyokimya",
    "Hiperkolesterolomiyi düzenlemek için kullanılan statin grubu ilaçlar plazma kolesterol düzeylerini düşürmede hangi mekanizma üzerinden etkilerini gösterirler?",
    [
        "Kolesterolün ince bağırsaktan emilimini azaltırlar.",
        "Kolesterolü safra asidine dönüştürerek atılımını artırırlar.",
        "Mevalonat yıkımını artırırlar.",
        "Kolesterol sentezinde HMG-KoA redüktazı inhibe ederler.",
        "Karaciğerde LDL reseptörünü uyarırlar.",
    ], "D", 4)

add(52, "biyokimya",
    "Metabolizmada kolesterolün hücre içi düzenlenmesinde aşağıdaki durumlardan hangisi etkili değildir?",
    [
        "ACAT ile esterifikasyon",
        "LDL reseptörü ile hücreye alım",
        "Hücredeki Apo C-II ifadesi",
        "HMG-KoA redüktaz transkripsiyonu düzenlenmesi",
        "Kolesterolün Apo A-I aracılı HDL üzerine aktarımı",
    ], "C", 4)

add(53, "biyokimya",
    "Karaciğerde HMG-KoA redüktaz enzim aktivitesinin düzenlenmesinde etkisi olmayan seçenek hangisidir?",
    ["SREB proteini", "İnsülin", "Diyetle alınan lipid", "Glukagon", "Kinaz enzimleri"],
    "C", 4)

add(54, "biyokimya",
    "Sentezinde kolesterolden köken almayan bileşik aşağıdaki seçeneklerden hangisinde yer almaktadır?",
    ["Progesteron", "Vitamin C", "Kortizol", "Safra tuzu", "Aldosteron"],
    "B", 4)

add(55, "biyokimya",
    "Sodyum-potasyum ATPaz pompası hangi prensibe göre çalışır?",
    ["Basit difüzyon", "Kolaylaştırılmış difüzyon", "Ozmotik transport", "Aktif transport", "İyonik transport"],
    "D", 4)

add(56, "biyokimya",
    "Aktif taşınmada sodyum elektrokimyasal gradyenti kullanan taşıyıcı seçeneklerden hangisidir?",
    ["SGLT1", "Kalsiyum-ATPaz", "GLUT 2", "Na⁺/K⁺-ATPaz", "Na⁺/Ca²⁺"],
    "A", 4)

add(57, "biyokimya",
    "Aşağıdaki seçeneklerden hangisinde verilen bilgi doğru değildir?",
    [
        "Plazmalojenler ve PAF dihidroksiaseton fosfattan yapılan eter lipidlerdir.",
        "Sfingolipitler lesitinden sentezlenir.",
        "Triaçilgliseroller ve bazı fosfogliseroller, gliserol-3-P’nin ardışık açilasyonuyla sentezlenir.",
        "Sfingomiyelin ve glikosfingolipitler hücre zarında yapısal eleman olarak işlev görürler.",
        "Gangliozidler, plazma zarı dış yüzeyinde yer alan hücre reseptörleri ve antijen olarak önemlidir.",
    ], "B", 5)

add(58, "biyokimya",
    "Proteinlerin lipid membrana bağlanmasını sağlayan tepkimeye ne ad verilir?",
    ["Denatürasyon", "Metilasyon", "Prenilasyon", "Renatürasyon", "Açılasyon"],
    "C", 5)

# ------------------------- BİYOFİZİK (59-72) -------------------------
add(59, "biyofizik",
    "Bir mol glukozun potansiyel enerjisi 686 kcal/mol’dür. Hücresel solunumda glukozdan 277 kcal/mol elde ediliyorsa, hücre solunumunun net verimi yüzde kaçtır? Fazla enerji hücrede nasıl kullanılır?",
    [
        "%27, fazla enerji hücresel işlerde kullanılır.",
        "%40, fazla enerji ısıya dönüşür.",
        "Enerjinin korunumu yasasına göre tüm enerji işe dönüşür.",
        "%27, fazla enerji biyolojik reaksiyonlarda kullanılır.",
        "%40, fazla enerji depolanır.",
    ], "B", 5)

add(60, "biyofizik",
    "Fosfolipid çift tabakasının oluşumunda temel sürdürücü kuvvet aşağıdakilerden hangisidir?",
    ["Hidrojen bağı oluşumu", "Hidrofobik etkileşimler", "Kovalent etkileşimler", "ATP hidrolizi", "Mekanik kuvvetler"],
    "B", 5)

add(61, "biyofizik",
    "Eşit konsantrasyonlardaki (gram/litre) glukoz (180 g/mol) ve sükroz (342 g/mol) solüsyonları birbirinden, sadece su geçişine izin veren, başlangıçta kapalı bir zar ile ayrılmıştır. Yarı geçirgen zar açıldığında suyun net geçişi hangi tarafa olacaktır?",
    [
        "Net geçiş sıfırdır.",
        "Sükroz tarafına.",
        "Glukoz tarafına.",
        "Başlangıçta sükroza, ardından glukoza.",
        "Geçiş olmaz.",
    ], "C", 5)

add(62, "biyofizik",
    "Fick difüzyon yasasına göre, aşağıdakilerden hangisi hücre zarından geçebilen bir maddenin zar boyunca net difüzyon hızını azaltır?",
    [
        "Zarın geçirgenliğinin artması",
        "Maddenin konsantrasyon gradyanında artış",
        "Zarın yüzey alanının büyümesi",
        "Maddenin ağırlığında azalma",
        "Zar kalınlığında artış",
    ], "E", 5)

add(63, "biyofizik",
    "Hücre zarından madde taşınımı ile ilgili aşağıdakilerden hangisi yanlıştır?",
    [
        "Pasif taşınımda metabolik enerji harcanması gerekmez.",
        "İyon kanallarının seçiciliğinde iyonun yükü önemlidir.",
        "Kanallardan iyon geçişi ATP’nin hidrolizi ile gerçekleşir.",
        "Kolaylaştırılmış difüzyonda akı bir doygunluk değerine ulaşır.",
        "Na⁺ ile ortaklaşa ve karşıt taşınım için ana enerji kaynağı ATP’dir.",
    ], "C", 5)

add(64, "biyofizik",
    "Hücre zarının elektriksel özellikleri ile ilgili hangi ifade yanlıştır?",
    [
        "Zar direnci, iyonların zardan geçiş kolaylığının tersinin ölçüsüdür.",
        "Zarda açık kanal sayısı ile zar direnci doğru orantılıdır.",
        "Zarın kapasitansı yüzey alanının büyüklüğü ile doğru orantılıdır.",
        "Zar kapasitansı zarın depolayacağı yük miktarını gösterir.",
        "Zaman sabiti (τ=RC) nöronun iletim hızının hesaplanmasında kullanılır.",
    ], "B", 5)

add(65, "biyofizik",
    "Hücre içi Ca²⁺ konsantrasyonu 0.0001 mM, hücre dışı konsantrasyonu 1 mM ise, Ca²⁺ denge (Nernst) potansiyelini hesaplayınız?",
    ["+122 mV", "+61 mV", "0 mV", "+244 mV", "-80 mV"],
    "A", 6)

add(66, "biyofizik",
    "Hücre zarından geçişinde metabolik enerjinin gerekli olmadığı yönde hareket eden bir iyon için aşağıdakilerden hangisi doğrudur?",
    [
        "İyon geçişi birincil aktif taşıma ile gerçekleşiyordur.",
        "İyon zardan doğrudan geçer.",
        "İyona sadece elektriksel kuvvet etki ediyordur.",
        "İyonun zardan geçişi için ATP kullanılır.",
        "İyonun elektrokimyasal kuvvetleri sıfırdan farklıdır.",
    ], "E", 6)

add(67, "biyofizik",
    "Na⁺ ve Cl⁻ geçiren, ancak büyük anyonlar (A⁻) için geçirgen olmayan bir zar iki kompartmanı birbirinden ayırıyor. Sistem dengededir. Birinci tarafta [Na⁺]₁ = 0,326 mol/l, [A⁻]₁ = 0,266 mol/l ve ikinci tarafta [Cl⁻]₂ = 0,14 mol/l, [A⁻]₂ = 0. Donnan dengesine göre ikinci taraftaki [Na⁺]₂ konsantrasyonu ne kadardır?",
    ["0,326 mol/l", "0,14 mol/l", "0,06 mol/l", "0,266 mol/l", "0,466 mol/l"],
    "B", 6)

add(68, "biyofizik",
    "Aşağıdakilerden hangisi hücrenin dinlenim zar potansiyel değerine potasyumun (K⁺) etkisinin daha fazla olmasını açıklar?",
    [
        "Zarda sızıntı K⁺ iyon kanallarının kapalı halde durması.",
        "Zarın geçirgenliğinin K⁺ iyonlarına daha fazla olması.",
        "K⁺ iyonlarının pozitif yük içermesi.",
        "Na⁺ sızıntı kanallarının fazla sayıda olması.",
        "Na⁺ konsantrasyonunun hücre dışında fazla olması.",
    ], "B", 6)

add(69, "biyofizik",
    "I. Tepkimeyi başlatırlar\nII. Tepkimenin hızını değiştirirler\nIII. Tepkimenin yönünü değiştirirler\nIV. Tepkime sonunda yapısal değişikliğe uğrarlar\nV. Kademeli tepkimelerde en hızlı adımda etkilidirler\nYukarıdaki verilen bilgilerden hangisi/leri katalizörlerin özelliklerindendir?",
    ["Yalnız I", "III-V", "II-III-IV", "I-II", "Yalnız II"],
    "E", 6)

add(70, "biyofizik",
    "Aşağıda verilen ısı aktarımı ile ilgili bilgilerden hangisi doğrudur?",
    [
        "Konveksiyon ile ısı aktarımı, yavaş moleküllerden hızlı moleküllere doğrudur.",
        "Kondüksiyon ile ısı aktarımı, enerjinin sıvı veya gaz içindeki transferidir.",
        "Evaporasyon, ısı enerjisi ile maddelerin katı halden sıvı hale geçişidir.",
        "Bütün cisimler radyasyon yaymaktadır.",
        "Güneş, konveksiyon ile ısı aktarımı yapmaktadır.",
    ], "D", 6)

add(71, "biyofizik",
    "I. Vazodilatasyon\nII. Piloreeksiyon\nIII. Solunumda artış\nIV. Titreme\nV. Terleme ve buharlaşma\nYukarıdakilerden hangisi/leri sıcaklığı yükselten mekanizmalardandır?",
    ["I-II", "IV-V", "II-III-V", "II-IV", "I-III-IV"],
    "D", 6)

add(72, "biyofizik",
    "Vücudun içi ve dışı arasındaki dokunun kalınlığı 3 cm, iletkenliğin olduğu alan 1.5 m², vücudun içi ile dışı arasındaki sıcaklık farkı 3 °C ise ısı akışı ne kadardır? (Kdoku = 18 cal.cm/m².saat.°C)",
    ["81 cal/saat", "27 cal/saat", "13,5 cal/saat", "54 cal/saat", "18 cal/saat"],
    "B", 6)

# ------------------------- MİKROBİYOLOJİ (73-84) -------------------------
add(73, "mikrobiyoloji",
    "Virüslerin yapısı ile ilgili yanlış hangisidir?",
    [
        "DNA virüslerinde helikal kapsid bulunmaz.",
        "Bazı virüsler sadece genom ve ikosahedral kapsidden oluşur.",
        "Pozitif RNA virüsleri mRNA gibi davranır.",
        "RNA virüslerinin çoğu çift sarmallıdır.",
        "Helikal kapsidi olan virüslerin hepsi zarflıdır.",
    ], "D", 6)

add(74, "mikrobiyoloji",
    "Virüslerin replikasyonu ile ilgili yanlış hangisidir?",
    [
        "Zarfsız virüsler hücreyi lizise uğratarak salınır.",
        "RNA virüslerinin çoğu sitoplazmada çoğalır.",
        "DNA virüsleri RNA polimeraz taşır.",
        "DNA virüslerinin çoğu nükleusta çoğalır.",
        "Zarflı virüsler hücreden tomurcuklanarak salınır.",
    ], "C", 6)

add(75, "mikrobiyoloji",
    "Aşağıdaki virüslerden hangisi kısmen çift sarmallı sirküler DNA genomuna sahiptir?",
    ["Herpesvirus", "Parvovirus", "Poxvirus", "Adenovirus", "Hepatit B virus"],
    "E", 6)

add(76, "mikrobiyoloji",
    "Virüslerin tanı testlerinden hangisinde eritrositler kullanılır?",
    ["Lateks aglütinasyon", "Direk IFA testi", "ELISA", "İmmünokromotografik kart testi", "Hemaglütinasyon inhibisyon testi"],
    "E", 6)

add(77, "mikrobiyoloji",
    "Aşağıdakilerden hangisi tekrarlayan virus infeksiyonunu gösterir?",
    [
        "IgG yüksek avidite(+), IgM(-)",
        "IgG düşük avidite(+), IgM(+)",
        "IgG yüksek avidite(+), IgM(+)",
        "IgG düşük avidite(+), IgM(-)",
        "IgG (+), IgM(-)",
    ], "C", 6)

add(78, "mikrobiyoloji",
    "Herpes simplex virusun sebep olduğu veziküler lezyonlarından kazıntı örneği alınarak yapılan “Tzanck” testinde görülen sitopatik etki hangisidir?",
    ["Piknozis", "Agregasyon", "Çok nükleuslu hücreler", "Minimal sitopatik etki", "Sitomegali"],
    "C", 7)

add(79, "mikrobiyoloji",
    "İnsan sağlığı için önemli olan bakterilerin büyük bir kısmı en iyi 20-45°C’de ürer. Bu grupta yer alan bakteriler hangileridir?",
    ["Psikrofil", "Termofil", "Mezofil", "Halofil", "Hemofil"],
    "C", 7)

add(80, "mikrobiyoloji",
    "Aşağıdaki bakterilerden hangisi zorunlu aeroptur?",
    ["Bordetella pertussis", "Bacteroides fragilis", "Clostridium perfringens", "Peptostreptococcus", "Veillonella"],
    "A", 7)

add(81, "mikrobiyoloji",
    "Bakterinin “hemoliz” özelliği ile ilgili olarak hangisi/hangileri doğrudur?\nI) MacConkey Agarda beta hemoliz özelliği görülebilir.\nII) Buyyon besiyerinde beta hemoliz özelliği görülebilir.\nIII) Koyun Kanlı Agarda alfa hemolitik koloniler görülebilir.",
    ["sadece I", "sadece II", "sadece III", "I ve II", "II ve III"],
    "C", 7)

add(82, "mikrobiyoloji",
    "Çikolata besiyeri ile ilgili olarak hangisi/hangileri doğrudur?\nI- Zengin bir besiyeridir.\nII- Neisseria ve Haemophilus türü bakterilerin üretilmesi kullanılır.\nIII- Besiyeri kan içerir.",
    ["I ve II", "II ve III", "I ve III", "Hepsi", "Hiçbiri"],
    "D", 7)

add(83, "mikrobiyoloji",
    "Gram pozitif bakteri hücre duvarı yapısında hangisi/hangileri bulunmaz?\nI) Peptidoglikan\nII) Teikoik asit\nIII) Lipopolisakkarit (LPS)",
    ["I, II", "II, III", "sadece I", "sadece II", "sadece III"],
    "E", 7)

add(84, "mikrobiyoloji",
    "Bakteri hücre duvarı ile ilgili bilgilerden hangisi yanlıştır?",
    [
        "Bakteriyi basınç değişikliklerine karşı korur.",
        "Bakterinin şeklini korur.",
        "Gram boyanma özelliğinden sorumlu yapıdır.",
        "Hücre duvarında peptidoglikan tabaka bulunmaz.",
        "Bazı bakteriler beslenme koşulları, penisilin veya lizozim etkisi ile değişikliğe uğrayarak hücre duvarını kaybeder “Lister form-L form” haline dönebilirler.",
    ], "D", 7)

# ------------------------- DAVRANIŞ BİLİMLERİ (85-94) -------------------------
add(85, "davranis-bilimleri",
    "Duygular ve bellekle ilişkili beyin bölgesi aşağıdakilerden hangisidir?",
    ["Oksipital lob", "Frontal lob", "Pons", "Temporal lob", "Parietal lob"],
    "D", 7)

add(86, "davranis-bilimleri",
    "Aşağıdakilerden hangisi Deskriptif (Tanımlayıcı) Psikiyatri ile ilgili uygulama alanlarından değildir?",
    [
        "Hastalıkların tanılarını belirler",
        "Ayırıcı tanı yapar",
        "Hastalıkları sınıflandırır",
        "Normal ve anormal davranışların altında yatan nedensel etkenleri araştırır",
        "Tedavi planı oluşturur",
    ], "D", 7)

add(87, "davranis-bilimleri",
    "Hangisi benlik (ego) görevleri arasında yer almaz?",
    [
        "Bireyin ruhsal dünyası içinde ve dışında olanların birbirinden ayırt edilmesi, gerçeği değerlendirme",
        "Dürtülerin birbirleriyle ve dış dünyayla ilişkilerinin düzenlenmesi uygun zaman ve koşullarda eyleme dönüştürülmesi",
        "Dürtüleri bekletebilme, erteleyebilme",
        "İyi-kötü, doğru-yanlış gibi değer yargıları ile dürtülerin doyurulmasında yargılayıcı mekanizma işlevi",
        "Ruhsal yapı üzerinde düzenleyici, dengeleyici ve uyum sağlayıcı işlevi",
    ], "D", 7)

add(88, "davranis-bilimleri",
    "Erikson’un psikoseksüel gelişim evrelerinden fallik döneme denk gelen Erikson’un kişilik gelişimi evresi hangisidir?",
    [
        "Temel güvene karşı güvensizlik",
        "Özerkliğe karşı utanç",
        "Girişime karşı suçluluk",
        "Çalışkanlığa karşı aşağılık duygusu",
        "Kimlik kazanmaya karşı kimlik karmaşası",
    ], "C", 7)

add(89, "davranis-bilimleri",
    "Erikson’un psikoseksüel gelişim evrelerinden oral döneme denk gelen Erikson’un kişilik gelişimi evresi hangisidir?",
    [
        "Temel güvene karşı güvensizlik",
        "Özerkliğe karşı utanç",
        "Girişime karşı suçluluk",
        "Çalışkanlığa karşı aşağılık duygusu",
        "Kimlik kazanmaya karşı kimlik karmaşası",
    ], "A", 8, conf=0.9,
    note="Soru kökünün bir kısmı taranan sayfada su damgası altında kaldı; cevap anahtarı okunabilir durumdadır.")

add(90, "davranis-bilimleri",
    "Stresle başa çıkma mekanizmaları ile ilgili hangisi yanlıştır?",
    [
        "Gerçekçi olmayan hedeflerden uzak durulmalıdır.",
        "Düzenli olarak fiziksel egzersiz yapılmalıdır.",
        "Sebze ve meyvelerden zengin bir beslenme biçimi uygulanmalıdır.",
        "Stresi azaltmak için kafeinli içecekler tüketilmelidir.",
        "Yeterli ve dengeli uyunmalıdır.",
    ], "D", 8)

add(91, "davranis-bilimleri",
    "Aşağıdakilerden hangisi “alışkanlık” kavramını tanımlar?",
    [
        "Doğuştan gelen otomatik tepkilerdir.",
        "Zamanla otomatik bir tepki haline dönüşen, sonradan edinilmiş davranışlardır.",
        "Genetik faktörlerle belirlenen davranışlardır.",
        "Fiziksel bir rahatsızlığa bağlı olarak ortaya çıkar.",
        "Doğuştan gelen bir yetenek olarak karşımıza çıkar.",
    ], "B", 8, status="derived", conf=0.9,
    note="Bu sorunun basılı cevabı sayfa kenarında kesilmiş; AI tarafından çözüldü.")

add(92, "davranis-bilimleri",
    "Bağımlılık ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
    [
        "Bağımlılık doğuştan gelen bir özelliktir.",
        "Bağımlılık davranışı zamanla rutin ve aşırı ölçüde tekrarlanır.",
        "Bağımlılık yalnızca fiziksel sağlığı etkiler.",
        "Bağımlılık iyileşir ancak düzelmez.",
        "Bağımlı bireyler madde kullanmayı kolaylıkla bırakabilir.",
    ], "B", 8)

add(93, "davranis-bilimleri",
    "Aşağıdakilerden hangisi çocuklarda görülen istismar türlerinden değildir?",
    ["Cinsel istismar", "Fiziksel istismar", "Duygusal istismar", "ihmal", "Çocuğun kaza yolu ile yaralanması"],
    "E", 8)

add(94, "davranis-bilimleri",
    "Çocukların yaşadıkları ihmal veya istismarı neden söylemedikleri ile ilgili aşağıdakilerden hangisi yanlıştır?",
    [
        "Kendilerine inanılmayacağından korkarlar.",
        "Başlarının belaya gireceğinden korkarlar.",
        "İstismarcının tehditlerinden korkarlar.",
        "Ailenin parçalanmasını isteyebilirler.",
        "Nasıl anlatılacağını bilmeyebilirler.",
    ], "D", 8)

# ------------------------- TIP TARİHİ VE ETİK (95-96) -------------------------
add(95, "tip-tarihi-etik",
    "Türk tıp tarihinin özellikle modern cerrahi ve tıp eğitimi başlıkları altında önemli yere sahip siması aşağıdakilerden hangisidir?",
    ["Gazi Osman Paşa", "Kazım Karabekir Paşa", "Operatör Cemil Topuzlu Paşa", "Sokullu Mehmet Paşa", "Tiryaki Hasan Paşa"],
    "C", 8)

add(96, "tip-tarihi-etik",
    "Aşağıdakilerden hangisi eski Çin tıbbının günümüzde evrensel ölçekte benimsenen bir uygulamasıdır?",
    ["Ayur veda", "Radyolojik görüntüleme", "Akupunktur", "Damar yoluyla sıvı verme", "Yoga"],
    "C", 8)

# ------------------------- SBET (97-100) -------------------------
add(97, "sbet",
    "Hangi gruplar “en az” ayrımcılığa maruz kalan gruplardır?",
    [
        "Farklı cinsel yönelime sahip olanlar",
        "Rehabilitasyon desteği alan engelliler",
        "Maddi destek alan göçmenler",
        "Örgütlü muhalifler",
        "Çoğunluğa sahip dini inanç veya mezhep grupları",
    ], "E", 8)

add(98, "sbet",
    "Toplumsal cinsiyete dayalı ayrımcılık için hangisi yanlıştır?",
    [
        "Toplumsal cinsiyet eşitliği kadınlar için talep edilir.",
        "Günümüzde özellikle sağlık alanında açık cinsiyetçilik yapılmaktadır.",
        "Toplumsal olarak kurulan toplumsal cinsiyet rolleri ve normlarından kaynaklanır.",
        "Kişinin insan haklarını ihlal eden her türlü ayrımcılık, dışlama ve engelleme durumudur.",
        "Açık cinsiyetçilik yerini örtük cinsiyetçiliğe bırakmıştır.",
    ], "B", 8, status="derived", conf=0.9,
    note="Bu sorunun basılı cevabı sayfada yer almıyor; AI tarafından çözüldü.")

add(99, "sbet",
    "“Milgram Deneyi” en temelde hangi kavramı açıklamak için yapılmış bir çalışmadır?",
    ["Kalıp yargı", "Otoriteye uyum", "Öznel inançlar", "Görev bilinci", "İşkenceci kişilik"],
    "B", 8)

add(100, "sbet",
    "Aşağıdaki ifadelerden hangisi “Ayrımcılık” tanımı içinde yer almaz?",
    [
        "Sadece kendi grubunun avantajını düşünen",
        "Diğer grubun dezavantajını görmezden gelen",
        "Diğer grubun dezavantajını pekiştiren",
        "İtaatli davranan",
        "Diğerine acı verici bir tutum ve davranış içinde olan",
    ], "D", 8)

# ------------------------- ENTEGRE (101-105) -------------------------
add(101, "entegre",
    "Hangisi bağımlılık için en önemli mekanizma olan dopaminerjik sistem ile ilişkili beyin alanıdır?",
    ["Nucleus Caudatus", "Nucleus Accumbens", "Globus Pallidus", "Corpus Striatum", "Putamen"],
    "B", 8)

add(102, "entegre",
    "Hangisi Opioid grubu maddeler içerisinde yer almaz?",
    ["Esrar", "Eroin", "Morfin", "Kodein", "Metadon"],
    "A", 8)

add(103, "entegre",
    "Bağımlılık tanısal ölçütleri arasında yer almayan hangisidir?",
    [
        "İstenen etkiyi sağlamak için belirgin olarak artmış miktarlarda madde kullanma gereksinimi",
        "Çoğu kez tasarlandığından daha yüksek dozlarda ve daha uzun dönem kullanılır",
        "Bırakmak ya da denetim altına almak için sürekli bir istek ya da boşa çıkan çabalar vardır.",
        "Maddenin neden olduğu fizik ya da psikolojik bir sorunun olduğunun farkında olmama",
        "Maddeyi sağlamak, kullanmak ya da etkilerinden kurtulmak için çok fazla zaman harcama",
    ], "D", 8)

add(104, "entegre",
    "Fensiklidin bağımlılık yapıcı maddeler arasında hangi grupta yer alır?",
    ["Opioidler", "Uyarıcılar", "Sedatifler", "Hipnotikler", "Hallüsinojenler"],
    "E", 8)

add(105, "entegre",
    "Aşağıdaki bağımlılık çeşitlerinden hangisinin kuvvetli psişik bağımlılık yapma özelliği vardır?",
    ["Kokain", "Alkol", "Esrar", "Nikotin", "Amfetamin"],
    "A", 8)

# ------------------------- DOĞRULAMA + ÇIKTI -------------------------
nums = [q["number"] for q in QUESTIONS]
assert len(QUESTIONS) == 105, f"Beklenen 105 soru, bulunan {len(QUESTIONS)}"
assert nums == list(range(1, 106)), f"Soru numaraları hatalı: eksik={set(range(1,106))-set(nums)}"
for q in QUESTIONS:
    assert len(q["options"]) == 5
    assert all(o for o in q["options"])

exam = {
    "id": EXAM_ID,
    "label": "2024-2025 Dönem 1 TEM 2",
    "shortLabel": "2024-25",
    "year": "2024-2025",
    "period": 1,
    "term": "TEM 2",
    "questionCount": 105,
    "date": "2025-06",
    "sourceFile": "DÖNEM 1 TEM 2 24-25.pdf",
    "sourcePages": [1, 2, 3, 4, 5, 6, 7, 8],
    "answerStatus": "official",
    "ocrQuality": "good",
    "notes": "1-100 arası sorulara ek olarak ENTEGRE başlığı altında 101-105 soruları vardır. 5, 91 ve 98. soruların basılı cevabı taranan sayfada yer almıyor; AI tarafından çözülüp 'derived' olarak işaretlenmiştir.",
    "disciplines": [
        {"id": "histoloji", "name": "Histoloji", "questionCount": 9, "first": 1, "last": 9},
        {"id": "fizyoloji", "name": "Fizyoloji", "questionCount": 10, "first": 10, "last": 19},
        {"id": "biyokimya", "name": "Biyokimya", "questionCount": 39, "first": 20, "last": 58},
        {"id": "biyofizik", "name": "Biyofizik", "questionCount": 14, "first": 59, "last": 72},
        {"id": "mikrobiyoloji", "name": "Mikrobiyoloji", "questionCount": 12, "first": 73, "last": 84},
        {"id": "davranis-bilimleri", "name": "Davranış Bilimleri", "questionCount": 10, "first": 85, "last": 94},
        {"id": "tip-tarihi-etik", "name": "Tıp Tarihi ve Etik", "questionCount": 2, "first": 95, "last": 96},
        {"id": "sbet", "name": "SBET", "questionCount": 4, "first": 97, "last": 100},
        {"id": "entegre", "name": "Entegre", "questionCount": 5, "first": 101, "last": 105},
    ],
}

exam_out = {"exam": exam, "questions": QUESTIONS}
exam_path = os.path.join(EXAM_DIR, f"{EXAM_ID}.json")
with open(exam_path, "w", encoding="utf-8") as f:
    json.dump(exam_out, f, ensure_ascii=False, indent=2)

index = {
    "version": 1,
    "generatedAt": "2026-11-06",
    "site": "Sınav Platformu",
    "scope": "Dönem 1 / TEM 2",
    "exams": [
        {
            "id": exam["id"],
            "label": exam["label"],
            "shortLabel": exam["shortLabel"],
            "year": exam["year"],
            "period": exam["period"],
            "term": exam["term"],
            "questionCount": exam["questionCount"],
            "answerStatus": exam["answerStatus"],
            "disciplines": exam["disciplines"],
        }
    ],
}
with open(os.path.join(OUT_DIR, "index.json"), "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print(f"OK: {len(QUESTIONS)} soru -> {exam_path}")
print("Cevap dağılımı:")
from collections import Counter
print(dict(Counter(q["correctAnswer"] for q in QUESTIONS)))
print("Ders dağılımı:")
print(dict(Counter(q["discipline"] for q in QUESTIONS)))
