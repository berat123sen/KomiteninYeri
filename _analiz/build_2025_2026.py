# -*- coding: utf-8 -*-
"""2025-2026 Dönem 1 TEM 2 (A kitapçığı) -> JSON.
Kaynak: WhatsApp Image 2026-11-16 ... (1).pdf (CamScanner fotoğrafları).
Sayfa sırası (orijinal PDF sayfaları): 3,1,2,7,4,5,6,8,12 -> kaynak PDF sayfa 1..9
"""
from lib_build_new import Builder

EID = "2025-2026-tem-2"
b = Builder(EID)
add = b.add

I_II = "I ve II"
S = ["I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV"]
S2 = ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"]

# ===== FİZYOLOJİ (1-12) — sayfa 1 =====
add(1, "fizyoloji", "Claude Bernard'ın \"milieu\" kavramı ile ifade edilen ortamlarla bu ortamların karşılık geldiği vücut sıvı bölümleri arasında yapılan aşağıdaki eşleştirmelerden hangisi doğrudur?",
    ["Milieu interior — Toplam vücut sıvı bölümü", "Milieu exterior — İnterstisyel sıvı bölümü", "Milieu interior — Hücre dışı sıvı bölümü", "Milieu exterior — Hücre içi sıvı bölümü", "Milieu interior — Hücre içi sıvı bölümü"], "C", 1)
add(2, "fizyoloji", "Hücrelerin glikokaliksi başlıca aşağıdaki bileşenlerin hangilerini içerir?\nI) Protein\nII) Trigliserid\nIII) Kolesterol\nIV) Karbonhidrat",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "I ve IV"], "E", 1)
add(3, "fizyoloji", "Aşağıdaki moleküllerden hangileri reseptör aracılı endositozda rol oynar?\nI) Klatrin\nII) Dinamin\nIII) Okludin\nIV) Konneksin",
    ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"], "A", 1)
add(4, "fizyoloji", "Aşağıdaki organellerden hangileri mitokondrilerin iç ortamında bulunur?\nI) Lizozom\nII) Ribozom\nIII) Peroksizom\nIV) DNA",
    ["I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV"], "E", 1)
add(5, "fizyoloji", "Mitokondrilerdeki oksidatif fosforilasyon sırasında ATP sentezinde rol oynayan enzim aşağıdakilerden hangisidir?",
    ["H⁺-ATPaz", "F₀F₁-ATPaz", "Ca⁺⁺-ATPaz", "Na⁺-K⁺-ATPaz", "K⁺-H⁺-ATPaz"], "B", 1)
add(6, "fizyoloji", "Aşağıdaki hücre iskelet elemanlarından hangileri ara filament sınıfına girer?\nI) Desmin\nII) Vimentin\nIII) Aktin\nIV) Miyozin",
    ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"], "A", 1)
add(7, "fizyoloji", "Kalp kası hücre zarındaki Na⁺-K⁺-ATPazın çalışması aşağıdaki sonuçlardan hangilerine yol açar?\nI) Hücre içindeki pozitif yüke katkıda bulunur\nII) Na⁺ ve K⁺ iyonlarına ait difüzyon potansiyellerinin gelişmesini sağlar\nIII) Hücre içine doğru ozmoz gelişmesini önler\nIV) Hücre içindeki Ca⁺⁺ konsantrasyonunun artması yönünde etki yapar",
    ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"], "B", 1)
add(8, "fizyoloji", "DNA'nın eşlenmesinin son aşamasında primer RNA'ları kaldırarak yerine DNA bazlarının dizilmesine olanak sağlayan enzim aşağıdakilerden hangisidir?",
    ["Ligaz", "Helikaz", "Primaz", "Polimeraz", "Ekzonükleaz"], "E", 1)
add(9, "fizyoloji", "İnsanda aşağıdaki hücreler arasında telomeraz etkinliği en yüksek olanları hangileridir?\nI) Çizgili kas\nII) Kemik iliği\nIII) Karaciğer\nIV) Testisteki germ hücreleri",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "I ve IV"], "D", 1)
add(10, "fizyoloji", "Kolera hastalığında gelişen ağır ishalin gelişmesi sırasında, bağırsak epitel hücrelerinde aşağıdaki değişikliklerden hangileri meydana gelir?\nI) Proteinkinaz A aktivitesi artmıştır\nII) Bağırsak lümenine Cl⁻ sekresyonu azalmıştır\nIII) G proteininin alfa birimine ADP-riboz bağlanmıştır\nIV) Kistik fibroz transmembran kondüktans (iletim) regülatörünün etkinliği azalmıştır",
    ["I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV"], "C", 1)
add(11, "fizyoloji", "Işık ışınlarının retina üzerine düşmesi ile birlikte, fotoreseptör basillerde aşağıdaki değişikliklerden hangileri gelişir?\nI) G proteinine eşlenik olan reseptör uyarılır\nII) Fosfodiesterazın etkinliği artırılır\nIII) Adenilil siklaz inhibe edilir\nIV) cGMP'nin etkinliği artırılır",
    ["I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV"], "A", 1)
add(12, "fizyoloji", "Nitrik oksit aşağıdakilerden hangilerinin etkinliğini artırarak etkisini gösterir?\nI) STAT\nII) Tirozinkinaz\nIII) Guanilil siklaz\nIV) cGMP",
    ["I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV"], "D", 1)

# ===== MİKROBİYOLOJİ (13-28) — sayfa 2-3 =====
add(13, "mikrobiyoloji", "Aşağıdakilerden hangisi kuduz aşısını bulan bilim adamıdır?",
    ["Robert Koch", "Louis Pasteur", "Edward Jenner", "Paul Ehrlich", "Alexander Fleming"], "B", 2)
add(14, "mikrobiyoloji", "Aşağıdakilerden hangisi DNA virüslerinin genel yapısal özellikleri için doğru bir ifadedir?",
    ["Zarfsız DNA virüsü yoktur.", "DNA virüslerinin çoğu helikal kapsid yapısına sahiptir.", "Poxvirüsler dışında DNA virüsleri sitoplazmada replike olur.", "DNA virüslerinde segmentli genom henüz gösterilmemiştir.", "DNA virüslerinde sirküler genom görülmez."], "D", 2)
add(15, "mikrobiyoloji", "Aşağıdaki virüslerden hangisi segmentli RNA genomuna sahiptir?",
    ["Rhabdovirus", "Retrovirus", "Picornavirus", "Rotavirus", "Poliovirus"], "D", 2)
add(16, "mikrobiyoloji", "Aşağıdaki virüslerden hangisi hem sitoplazma hem de nukleusda replike olur?",
    ["Adenovirus (ADV)", "Herpesvirus (HSV)", "Human immundeficiency virus (HIV)", "Coronavirus", "Poliovirus"], "C", 2)
add(17, "mikrobiyoloji", "Viral replikasyon sırasında erken proteinler için aşağıdakilerden hangisi doğrudur?",
    ["Yapısal proteinlerdir.", "Zarflı virüslerde bulunmaz.", "Kapsid proteinlerinin tümünü oluşturur.", "Genellikle enzimdir, genom replikasyonu için gereklidir.", "Montaj safhasında sentezlenir."], "D", 2)
add(18, "mikrobiyoloji", "Virüslerin hücrelerde oluşturdukları inklüzyon cisimcikleri ile ilgili aşağıdakilerden hangisi yanlıştır?",
    ["CMV, \"baykuş gözü hücreler\" denilen bazofilik intranükleer cisimcikler oluşur.", "Tzanck testinde HSV ve VZV'nin çok nukleuslu hücrelerde intranükleer inklüzyonları görülür.", "Kuduz virüsü bazofilik intrastoplazmik oval veya yuvarlak Negri cisimcikleri oluşturur.", "Eozinofil (asidofil) inklüzyonlar pembe ve bazofilik olanlar mavi-mor boyanır.", "İnklüzyon cisimcikleri hücrelerin nukleus, stoplazma veya her ikisinde oluşan viral ürünlerin topluluğudur."], "C", 2)
add(19, "mikrobiyoloji", "İnsan sağlığı için önemli olan bakterilerin büyük bir kısmı en iyi 20-45 °C sıcaklıkta ürer. Bu grupta yer alan bakteriler hangileridir?",
    ["Psikrofil", "Termofil", "Mezofil", "Halofil", "Hemofil"], "C", 2)
add(20, "mikrobiyoloji", "Aşağıdakilerden hangisi bakterilerin ve mantarların metabolizmalarında gereksinim duydukları demiri karşılamak için dış ortamdan demir yakalayarak hücre içerisine taşıyan demiri bağlayıcı (Fe3) küçük moleküllerdir?",
    ["Siderofor", "Aksiyal filaman", "Flajella", "Porin", "Mezozom"], "A", 2)
add(21, "mikrobiyoloji", "Aşağıdakilerden hangisi eşeysiz mantar sporu değildir?",
    ["Artrospor", "Blastospor", "Klamidospor", "Konidyospor", "Zigospor"], "E", 2)
add(22, "mikrobiyoloji", "Hangisi nemli ısı ile yapılan sterilizasyon yöntemi değildir?",
    ["Otoklav", "Koch kazanı", "UHT", "Pastörizasyon", "Tindalizasyon"], "D", 2)
add(23, "mikrobiyoloji", "Hangisi canlı dokularda patojen mikroorganizmaların üreyerek yayılması sonucu oluşur?",
    ["Asepsi", "Antisepsi", "Sepsis", "Dezenfeksiyon", "Dezenfektan"], "C", 2)
add(24, "mikrobiyoloji", "Bakteri hücresinin hareketi ile ilişkili yapılar hangileridir?\nI-Flagella\nII-Aksiyel filament\nIII-Fimbria-Pilus\nIV-Mezozom",
    ["I ve II", "II ve III", "III ve IV", "I ve IV", "I, II ve III"], "A", 2)
add(25, "mikrobiyoloji", "Bakteri hücre duvarı ile ilişkili bilgilerden hangisi yanlıştır?",
    ["Bakteriyi basınç değişikliklerine karşı korur", "Bakteriye şekil verir", "Gram boyanma özelliğinden sorumlu yapıdır", "Hücre duvarında peptidoglikan tabaka bulunmaz", "Bazı bakteriler, beslenme koşulları, penisilin veya lizozim etkisi ile hücre duvarını kaybederek \"L form\" haline dönebilirler"], "D", 2)
add(26, "mikrobiyoloji", "Bakteriler arasında genetik madde aktarımı ile hangisi en az ilişkilidir?",
    ["Plazmidler", "Fertilite (F) faktörü", "Transpozonlar", "Bakteriyofajlar", "İnklüzyon cisimcikleri"], "E", 2)
add(27, "mikrobiyoloji", "Temel (basit) besiyerlerinde hangileri asla bulunmaz?\nI) Tuz\nII) Agar\nIII) At kanı\nIV) Koyun kanı",
    ["I ve II", "II ve III", "III ve IV", "I, II ve IV", "I, II, III"], "C", 3)
add(28, "mikrobiyoloji", "Çikolata besiyeri ile ilgili olarak hangisi/hangileri yanlıştır?\nI- Zengin bir besiyeridir.\nII- Bu besiyerinde sadece Gram negatif bakteriler üretilebilir.\nIII- Bu besiyerinde sadece Gram pozitif bakteriler üretilebilir.",
    ["I ve II", "II ve III", "I ve III", "Sadece I", "Sadece II"], "B", 3)

# ===== BİYOKİMYA (29-76) — sayfa 3-6 =====
add(29, "biyokimya", "Aşağıdakilerden hangisi GLUT1 taşıyıcısının özelliğidir?",
    ["Glukozu ATP kullanarak hücre içine taşır", "Sodyum ile birlikte çalışan bir simport sistemidir", "Bir uniport taşıyıcıdır ve kolaylaştırılmış difüzyon yapar", "Yalnızca bağırsak epitel hücrelerinde bulunur", "Glukozu gradiyentine karşı taşır"], "C", 3)
add(30, "biyokimya", "6 yaşındaki bir çocuk açlık dönemlerinde nöbet geçiriyor. Kan glukozu normal, fakat BOS glukozu düşüktür. Bu tablo en olası olarak hangi taşıyıcı bozukluğunu düşündürür?",
    ["SGLT1", "GLUT1", "GLUT4", "Na⁺/K⁺-ATPaz", "AE1 anyon değiştirici"], "B", 3)
add(31, "biyokimya", "Aşağıdaki karbonhidratlardan hangisinin glisemik indeksi en yüksektir?",
    ["Fruktoz", "Laktoz", "Sakkaroz", "Glukoz", "Trehaloz"], "D", 3)
add(32, "biyokimya", "Süt içtikten sonra gaz, karın ağrısı ve ishal şikâyetleri yaşayan bir hastada aşağıdaki enzimlerden hangisinin eksikliği en olasıdır?",
    ["Maltaz", "İsomaltaz", "Glukoamilaz", "Sükraz", "Laktaz"], "E", 3)
add(33, "biyokimya", "Aşağıdaki durumlardan hangisi trigliserit sentezini artırır?",
    ["Glukagon artışı", "Açlık süresinin uzaması", "cAMP artışı", "İnsülin düzeyinin artması", "Hormona duyarlı lipaz aktivasyonu"], "D", 3)
add(34, "biyokimya", "Yağ dokusunun trigliserit sentezi sırasında gliserol-3-fosfat oluşturabilmesi için hangi süreç gereklidir?",
    ["Ketoliz", "Glukoneogenez", "Glikoliz", "Beta oksidasyon", "Üre döngüsü"], "C", 3)
add(35, "biyokimya", "Kolesterol molekülündeki tüm karbon atomlarının kaynağı aşağıdakilerden hangisidir?",
    ["Laktat", "Asetil-CoA", "Piruvat", "Oksaloasetat", "Serin"], "B", 3)
add(36, "biyokimya", "Hücresel kolesterol düzeyi arttığında HMG-CoA redüktaz aktivitesi nasıl etkilenir?",
    ["Artar, çünkü daha fazla kolesterol yapılmalı", "Artar, çünkü SREBP aktive olur", "Azalır, çünkü enzim sentezi artar", "Azalır, çünkü enzim fosforile edilir", "Hiçbir değişiklik olmaz"], "D", 3)
add(37, "biyokimya", "Safra asitlerinin lipid sindirimindeki temel görevi aşağıdakilerden hangisidir?",
    ["Aminoasit emilimini artırmak", "Lipitleri oksitlemek", "Lipitlerin misel oluşturmasını sağlamak", "Safra kesesinin kasılmasını uyarmak", "Şilomikron sentezini başlatmak"], "C", 3)
add(38, "biyokimya", "Aşağıdakilerden hangisi primer safra asitlerinden biridir?",
    ["Litokolik asit", "Deoksikolik asit", "Kolestanone", "Koprostanol", "Kolik asit"], "E", 3)
add(39, "biyokimya", "Karaciğerden salınan VLDL'nin başlıca görevi aşağıdakilerden hangisidir?",
    ["Diyet kolesterolünü taşımak", "Serbest yağ asitlerini kas hücrelerine vermek", "Endojen trigliseritleri dokulara taşımak", "Aminoasit transportu yapmak", "Safra asitlerini geri döngüye sokmak"], "C", 3)
add(40, "biyokimya", "Lipoprotein lipaz (LPL) aktivasyonu için gerekli olan apolipoprotein aşağıdakilerden hangisidir?",
    ["Apo B-100", "Apo E", "Apo A-I", "Apo C-II", "Apo(a)"], "D", 3)
add(41, "biyokimya", "Protoporfirin halkasına demir eklenmesi ile oluşan, hemoglobin ve miyoglobinin yapısında oksijen bağlama/bırakma görevini üstlenen halkasal yapı aşağıdakilerden hangisidir?",
    ["Globin", "Porfirin", "HEM", "Bilirubin", "Klorofil"], "C", 3)
add(42, "biyokimya", "Aşağıdakilerden hangisi mitokondri membranında Elektron Taşıma Zincirinde (ETZ) NADH+H ve FADH2'den aldığı elektronları Sitokromlara aktararak ATP sentezinde rol oynayan lipidik formattaki yapıdır?",
    ["Piruvat", "Alfa Lipoik Asit", "Alfa-keto glutarat", "Koenzim Q10", "Asetil-CoA"], "D", 4)
add(43, "biyokimya", "Hemoglobin sentezi, mitokondride Süksinil Koenzim A ve Glisin moleküllerinin kondensasyonu sonucunda ALA (Delta-Aminolevülinik Asit) oluşması ile başlar. Aşağıdaki vitaminlerden hangisi bu basamağın koenzimi (kofaktörü) olarak görev alır ve eksikliği mikrositer anemiye yol açar?",
    ["B1", "B6", "B12", "D Vitamini", "Folik Asit"], "B", 4)
add(44, "biyokimya", "Aşağıdaki eser elementlerden hangileri tiroit dokusunda T3 ve T4 hormonlarının sentezi için gereklidir?",
    ["Mb (Molibden), Fe (Demir)", "Se (Selenyum), I (İyot)", "Zn (Çinko), Ca (Kalsiyum)", "Cr (Krom), Cu (Bakır)", "Mn (Mangan), Mg (Magnezyum)"], "B", 4)
add(45, "biyokimya", "Aşağıdakilerden hangisi mortalitesi yüksek hastalıklar grubunda olan ve beslenme ile ilişkisi bilimsel olarak kanıtlanmış hastalıklardandır?\nI. Kardiyovasküler Hastalıklar\nII. Diabetes Mellitus\nIII. Stroke (İnme)",
    ["Yalnız I", "Yalnız II", "I ve II", "II ve III", "I, II ve III"], "E", 4)
add(46, "biyokimya", "Aşağıdakilerden hangisi serbest radikal süpürücü etkileri olan süperoksit gibi radikalleri detoksifiye etmede kullanılan enzimlerde kofaktör olarak rol oynayan eser elementtir?",
    ["Molibden", "Manganez", "Kobalt", "Selenyum", "Krom"], "B", 4)
add(47, "biyokimya", "Karbonhidrat içeren bir besinin, tüketim sonrası oluşturduğu kan glukoz artış hızını ve miktarını, standart glukoz referansına göre karşılaştırmalı olarak ifade eden biyokimyasal ölçüt aşağıdakilerden hangisidir?",
    ["Glisemik indeks", "Bazal metabolizma hızı", "Vücut kitle indeksi", "Enerji yoğunluğu", "Besin piramidi"], "A", 4)
add(48, "biyokimya", "Aşağıdaki glikoliz enzimlerinden hangisinin aktivitesi sonucu ATP oluşur?",
    ["Heksokinaz", "Fosfofruktokinaz-1", "Gliseraldehit 3 fosfat dehidrogenaz", "Fosfogliserat kinaz", "Enolaz"], "D", 4)
add(49, "biyokimya", "Kan glukozu düşmüş bir kişide, aşağıdaki enzimlerden hangisinin karaciğerde inhibe olması gerekir?",
    ["Pirüvat karboksilaz", "PEP karboksikinaz", "Glukokinaz", "Fruktoz-1,6-bifosfataz", "Glukoz-6-fosfataz"], "C", 4)
add(50, "biyokimya", "Glikojenin yıkılmasını sağlayan enzimlerden biri olan glikojen fosforilazın ürünü aşağıdakilerden hangisidir?",
    ["Glikoz 1-fosfat", "Glikoz 1,6 bifosfat", "UDP glikoz", "Glikoz 6-fosfat", "Glikoz 2,6 bifosfat"], "A", 4)
add(51, "biyokimya", "Pirüvattan tek bir reaksiyon ile hangi madde oluşamaz?",
    ["Fosfoenol piruvat", "Laktat", "Alanin", "Oksaloasetat", "Asetil CoA"], "A", 4)
add(52, "biyokimya", "Aşağıdaki dehidrogenaz enzimlerinin hangisinin aktivitesiyle ortaya çıkan NADH'tan, alternatif yolaklarla 1,5 ya da 2,5 ATP sentezi gerçekleşebilir?",
    ["Pirüvat dehidrogenaz", "Gliseraldehit 3 fosfat dehidrogenaz", "İzositrat dehidrogenaz", "Alfa ketoglutarat dehidrogenaz", "Malat dehidrogenaz"], "B", 4)
add(53, "biyokimya", "Aşağıdakilerden hangisi Krebs siklusu basamaklarından değildir?",
    ["Asetil CoA'nın oksidasyonu", "Alfa-ketoglutarat oluşumu", "CO2 oluşumu", "Asetil CoA'nın piruvata dönüşümü", "NADH ve FADH2 oluşumu"], "D", 4)
add(54, "biyokimya", "Krebs döngüsünden elde edilen NADH, ETZ'ye hangi basamaktan girer?",
    ["Kompleks I", "Kompleks II", "Koenzim Q", "Kompleks III", "Kompleks IV"], "A", 4)
add(55, "biyokimya", "Pentoz fosfat yolunun başlıca amacı aşağıdakilerden hangisidir?",
    ["Amino asitlerin karbon iskeletinin oksidasyonu", "ATP sentezlemek", "NADPH ve riboz-5-fosfat üretmek", "Açlıkta kan glukozunu artırmak", "Asidik şekerlerin üretilmesi"], "C", 5)
add(56, "biyokimya", "Aşağıdakilerden hangisi glukoneogenezde yer alan enzim veya metabolit değildir?",
    ["Fosfoglikoizomeraz", "Gliseraldehid 3-fosfat", "Aldolaz", "Piruvat dehidrogenaz", "Glukoz 6-fosfataz"], "D", 5)
add(57, "biyokimya", "Glikojen sentezi için aşağıdakilerden hangisi yanlıştır?",
    ["Protein yapılı bir primere gereksinim vardır", "Glikojen sentezi glukagon ile uyarılır", "Glikojenin yapısında 1,4 ve 1,6 glikozit bağları vardır", "Glikojen sentazın defosforile hali aktiftir", "Glukoz monomerleri senteze UDP-Glukoz olarak girer"], "B", 5)
add(58, "biyokimya", "Glukoz sorbitol yolunda aşağıdaki ürünlerden hangisine dönüşür?",
    ["Galaktoz", "Fruktoz", "Glukronat", "Askorbat", "Mannoz"], "B", 5)
add(59, "biyokimya", "Fruktoz metabolizması ile ilgili aşağıdakilerden hangisi yanlıştır?",
    ["Fruktoz metabolizması karaciğerde çoğunlukla heksokinaz ile 6. karbondan fosforilasyon ile başlar", "Fruktoz metabolizmasının glikoz metabolizmasına göre daha hızlı olmasının nedeni fosfofruktokinaz kontrol basamağını atlamasıdır.", "Fazla fruktozlu diyet hiperürisemiye neden olur.", "Aldolaz-B eksikliğinde herediter fruktoz intoleransı gelişir.", "Diyabette görülen katarakt, lenste sorbitol birikiminden kaynaklanır"], "A", 5)
add(60, "biyokimya", "Kan glukozu düşmüş bir kişide, aşağıdaki enzimlerden hangisinin karaciğerde inhibe olması gerekir?",
    ["Pirüvat karboksilaz", "Pirüvat kinaz", "PEP karboksikinaz", "Fruktoz-1,6-bifosfataz", "Glukoz-6-fosfataz"], "B", 5)
add(61, "biyokimya", "Bir deneysel ortamda işaretli karbon atomları (C14) kullanılarak CO2 gazı işaretlenmiş ve deney hayvanlarına solutulmuştur. İşaretli karbon (C14) tespit edilebilmesiyle ilgili olarak aşağıdaki maddelerin hangisi(leri) doğrudur?\nI. Asetil CoA'nın yarısında tespit edilebilir\nII. Malonil CoA'nın karbonlarının üçte birinde tespit edilebilir\nIII. Palmitik asit (16C) karbonlarının hiçbirinde tespit edilemez\nIV. Propionil CoA tüm karbonlarında tespit edilebilir",
    ["Sadece IV", "I, III ve IV", "I, II ve III", "II ve III", "I, II, III ve IV"], "D", 5)
add(62, "biyokimya", "Bir karaciğer dokusu homojenize edilip arkasından santrifüj edilerek tüm membran komponentleri ve organelleri ortamdan uzaklaştırılıp sadece mitokondri bırakılıyor. Bu sıvıda yapılan enzim deneylerinde aşağıdaki enzimlerden hangisi(leri)nin aktivitesi saptanır?\nI. Glutaminaz\nII. Glutamat dehidrogenaz\nIII. Ornitin Transkarbamoilaz",
    ["Sadece I", "I ve II", "Sadece II", "II ve III", "I, II ve III"], "E", 5)
add(63, "biyokimya", "Gastrik Lipaz ve Lingual Lipaz etkisiyle trigliseritlerden koparılan yağ asitleri kanda nasıl taşınır?",
    ["Şilomikron", "Albumin", "VLDL", "Kolesterol esteri", "LDL"], "B", 5)
add(64, "biyokimya", "Yağların sindirimi sırasında \"Fosfatidil kolin\" Fosfolipaz A2 ile karşılaştığında hangi molekül(ler) oluşur?\nI. Diasilgliserol\nII. Fosfatidik asit\nIII. Lizolesitin\nIV. Serbest yağ asidi",
    ["II ve III", "II, III ve IV", "III ve IV", "I ve II", "I, II ve IV"], "C", 5)
add(65, "biyokimya", "Yağ asidi biyosentezinde Asetil CoA'dan Malonil CoA dönüşümünü sağlayan ve yağ asidi sentezinde hız kısıtlayıcı basamak olan Asetil CoA Karboksilaz enziminin aktivitesinin kontrolü ile ilgili doğru ifade(ler) hangisi(leri)dir?\nI. Sitrat tarafından uyarılır\nII. Palmitat tarafından inhibe edilir\nIII. Glukagon ve Epinefrin tarafından uyarılır",
    ["Sadece I", "I ve II", "I, II ve III", "II ve III", "I ve III"], "B", 5)
add(66, "biyokimya", "Araşidonik asitten Prostaglandinlerin sentezinde aşağıdakilerden hangisi(leri) siklooksijenaz yolağı üzerinden sentezlenir?\nI. Prostasiklin\nII. Tromboksan A₂\nIII. Prostaglandin G₂\nIV. Lökotrien A₄",
    ["I, II ve III", "I ve III", "II ve IV", "Sadece IV", "I, II, III ve IV"], "A", 5)
add(67, "biyokimya", "Palmitoik asidin beta oksidasyonunda aşağıdakilerden hangisi oluşmaz?",
    ["8 adet Asetil CoA", "7 adet NADH + H⁺", "Net 106 ATP", "7 adet H₂O", "7 adet FADH₂"], "D", 6)
add(68, "biyokimya", "Aşağıdakilerden hangisi(leri) Asetil CoA'dan oluşur?\nI. Gliserol 3-fosfat\nII. Araşidonik asit\nIII. Hidroksi metil glutaril CoA (HMG CoA)\nIV. Asetoasetat",
    ["I, II, III ve IV", "I, II ve III", "III ve IV", "II, III ve IV", "I ve IV"], "D", 6)
add(69, "biyokimya", "On aminoasitten oluşan C-Gly-Lys-Glu-Arg-Phe-Gly-Tyr-Glu-Pro-Arg-N peptidi, önce tripsin ile daha sonra pepsin ile muamele ediliyor. Peptid zinciri kaç parçaya bölünür?",
    ["2", "3", "4", "5", "6"], "E", 6)
add(70, "biyokimya", "Bir çocukta yapılan ölçümlerde kandaki amonyak düzeyinin çok fazla yükseldiği gözlenmiştir. Bu çocukta hangi enzim(ler)in eksikliği bu tabloya yol açabilir?\nI. N-asetilglutamat sentaz\nII. Glutamat dehidrogenaz\nIII. Karbamoil fosfat sentetaz\nIV. Glutaminaz",
    ["Sadece III", "I ve III", "I, III ve IV", "II ve IV", "II ve III"], "B", 6)
add(71, "biyokimya", "Hangisi Tirozin aminoasidinden sentezlenebilir?",
    ["Spermin", "Niasin", "DOPA", "Nitrik oksit (NO)", "Histamin"], "C", 6)
add(72, "biyokimya", "Tokluk durumunda, (insülin/glukagon oranı arttığında), aşağıdakilerden hangisi(leri) doğrudur?\nI. Glikojen fosforilaz aktive olur\nII. Sitrat liyaz enzimi aktive olur\nIII. Asetil CoA karboksilaz aktive olur",
    ["II ve III", "I ve III", "Sadece II", "I ve II", "Sadece III"], "A", 6)
add(73, "biyokimya", "İnsülin eksikliğinde ya da uzun süren açlık durumunda belirtilenlerden hangisi yanlıştır?",
    ["Glukoneogenez artar", "Glikojenolizis artar", "Ketogenez artar", "Proteolizis artar", "Lipogenez artar"], "E", 6)
add(74, "biyokimya", "Noradrenalinin adrenaline dönüşebilmesi için aşağıdaki mekanizmaların hangisi doğrudur?",
    ["Dehidrogenaz enzimi ile hidroksillenme", "S-Adenozilmetioninden metil aktarımı", "Tetrahidrofolattan metil aktarımı", "Ortamda Vitamin B12 varlığı", "NADH varlığında indirgenme"], "B", 6)
add(75, "biyokimya", "Hastanın idrarında çıkan ve havayla temas ettiği zaman oksitlenerek siyah pigmentler oluşturan madde hangisidir?",
    ["Tirozin", "5-hidroksiindol asetik asit", "Nitrik oksit", "Homojentisik asit", "Melanin"], "D", 6)
add(76, "biyokimya", "Tetrahidrobiyopterin tekrar oluşamadığında hangi enzimin aktivitesinde bozulma meydana gelir?",
    ["N-asetil glutamat sentaz", "Tirozinaz", "Sistatyonin beta sentaz", "Karbamoil fosfat sentetaz I", "Fenilalanin hidroksilaz"], "E", 6)

# ===== BİYOFİZİK (77-91) — sayfa 6-8 =====
add(77, "biyofizik", "Aşağıda verilen bilgilerden hangisi/leri katalizörlerin özelliklerindendir?\nI. Tepkimeyi başlatırlar\nII. Tepkimenin hızını değiştirirler\nIII. Tepkimenin yönünü değiştirirler\nIV. Tepkime sonunda yapısal değişikliğe uğrarlar\nV. Kademeli tepkimelerde en hızlı adımda etkilidirler",
    ["Yalnız I", "Yalnız II", "I-III-IV", "I-II", "III-V"], "B", 6)
add(78, "biyofizik", "Aşağıda verilen ısı aktarımı ile ilgili bilgilerden hangisi doğrudur?",
    ["Oda sıcaklığındaki cisimler kızılötesi radyasyon, yüksek sıcaklıklarda UV ve görünür ışıma yaparlar.", "Kondüksiyon ile ısı aktarımı, enerjinin sıvı veya gaz içindeki transferidir.", "Evaporasyon, ısı enerjisi ile maddelerin katı halden sıvı hale geçişidir.", "Konveksiyon ile ısı aktarımı, yavaş moleküllerden hızlı moleküllere doğrudur.", "Güneş, konveksiyon ile ısı aktarımı yapmaktadır."], "A", 6)
add(79, "biyofizik", "Aşağıdakilerden hangileri sıcaklığı yükselten mekanizmalardandır?\nI. Vazodilatasyon\nII. Piloereksiyon\nIII. Solunumda artış\nIV. Titreme\nV. Terleme ve buharlaşma",
    ["I-II", "IV-V", "II-III-V", "II-IV", "I-III-IV"], "B", 6,
    note="Taranan sayfadaki basılı cevap B (IV-V) olarak görünüyor; ancak ısıyı yükselten mekanizmalar tıbbi olarak piloereksiyon ve titreme (II-IV, şık D) olur. Kaynakla karşılaştırarak kontrol edin.",
    review="needs_review", conf=0.6)
add(80, "biyofizik", "Aşağıdaki şıklardan hangisinde vücudun ısı yayma % miktarları büyükten küçüğe doğru olarak sıralanmıştır?\nI. Alın bölgesi\nII. Saç bölgesi\nIII. Yüz bölgesi\nIV. Ayak tabanı",
    ["I, II, IV, III", "I, II, III, IV", "I, III, IV, II", "II, III, IV, I", "IV, III, II, I"], "C", 7)
add(81, "biyofizik", "Aşağıdaki olaylardan hangisi hücrede entropi artışına örnek değildir?",
    ["Glikozun yıkımı sonucu CO₂ ve H₂O oluşması", "ATP'nin ADP + Pi'ye hidrolizi", "Proteinlerin amino asitlerine hidrolizi", "Polipeptit zincirinin, karakteristik üç boyutlu durumuna geçişi", "Difüzyon ile zardan madde geçişi"], "D", 7)
add(82, "biyofizik", "1 mol glikozun doğrudan yakılması ile hücre solunumunda parçalanması karşılaştırıldığında, aşağıdakilerden hangisi doğrudur?",
    ["Her iki durumda da açığa çıkan enerji tamamen ATP'ye dönüştürülür", "Doğrudan yanmada enerji kontrolsüz biçimde ısı olarak açığa çıkar; hücresel solunumda ise bir kısmı ATP sentezinde kullanılır", "Doğrudan yanmada Gibbs serbest enerjisi pozitif, hücresel solunumda ise negatiftir", "Hücresel solunumda enerji ısıya dönüşmez, enerji tamamen ATP'ye dönüştürülür", "Her iki süreçte de enerji aynı verimle kullanılır"], "B", 7)
add(83, "biyofizik", "Aşağıdakilerden hangisi zarın doğal elektriksel özelliklerinin oluşumunda rol oynamaz?",
    ["Misel yapılar", "Hidrofobik kuyruklar", "Fosfolipit çift tabaka yapı", "Fosfat ve kolin grupları", "Polar baş grubu"], "A", 7)
add(84, "biyofizik", "Bir molekülün zarda difüzyon hızı, zar boyunca konsantrasyon farkı 50 mM (mol/m³) olduğunda 10⁻¹⁰ mol·s⁻¹ olarak ölçülmüştür. Bu zarın yüzey alanı 10⁻¹⁰ m² ve difüzyon sabiti 10⁻¹⁰ m²/s ise zarın kalınlığını hesaplayınız (nanometre cinsinden).",
    ["1", "2", "5", "200", "500"], "C", 7)
add(85, "biyofizik", "Aşağıdakilerden hangisi difüzyon ile ilgili kavramlar arasında yer almaz?",
    ["Moleküllerin düzenli ve metabolik enerji ile yönlendirilmiş hareketleriyle gerçekleşir.", "1. Fick Yasasına göre, difüzyon akı yoğunluğu ile konsantrasyon gradiyenti orantılıdır.", "Difüzyon alanı büyüdükçe, birim zamanda geçen toplam madde miktarı artar.", "Molekül ağırlığı difüzyon katsayısının belirlenmesinde önemlidir.", "Konsantrasyon gradiyenti azalırsa, difüzyon hızı azalır."], "A", 7)
add(86, "biyofizik", "Bir kılcal damar duvar kalınlığı yaklaşık 2 mikrometredir (μm). Bu duvardan geçebilen küçük bir molekül için difüzyon katsayısı D=2×10⁻⁹ m²/s'dir. Bu molekülün kılcal duvarı difüzyonla kat etmesi için gerekli süre ne kadardır?",
    ["0.001 ms", "0.01 ms", "1 ms", "100 ms", "1000 ms"], "C", 7,
    note="Taramada D değerinin üssü filigran nedeniyle okunamıyor; basılı cevap (1 ms) ile tutarlı olan 2×10⁻⁹ m²/s alınmıştır.",
    conf=0.8)
add(87, "biyofizik", "Hücre zarındaki elektrik alanı iyonları zar boyunca hareket etmeye zorlar. Tipik bir zardaki elektrik alan şiddeti 1.0×10⁷ N/C'dir. Böyle bir elektrik alandaki bir K⁺ iyonuna etki eden kuvvetin büyüklüğü (N) nedir? (e = 1.6×10⁻¹⁹ C)",
    ["1.6 × 10⁻¹⁹", "1.6 × 10⁻¹²", "3.2 × 10⁻¹²", "1 × 10⁻⁷", "2 × 10⁻¹²"], "B", 7)
add(88, "biyofizik", "Bir nöron membranından iyon geçişlerinin zar potansiyeline etkisi elektrik devre modeli ile incelenebilir. Devre modelinde iyon kanalları ve denge potansiyelleri hangi devre elemanları ile temsil edilir?",
    ["Direnç ve kapasitör", "Direnç ve akım kaynağı", "Akım kaynağı ve kapasitör", "Kapasitör ve pil (elektromotor kuvvet)", "Direnç ve pil (elektromotor kuvvet)"], "E", 7)
add(89, "biyofizik", "Hücre içi K⁺ konsantrasyonu 100 mM, hücre dışı K⁺ konsantrasyonu 10 mM ise hücrede K⁺ denge potansiyeli değeri kaçtır? (log 0,1 = -1), (log 10 = 1), (RT/zF = 61).",
    ["61 mV", "-61 mV", "122 mV", "-122 mV", "0 mV"], "B", 7)
add(90, "biyofizik", "Dinlenim durumundaki bir nöronun zar potansiyeli -70 mV'tur. Zarda Na⁺ için denge potansiyeli +60 mV ise elektrokimyasal farkın işareti, büyüklüğü ve yönü aşağıdakilerden hangisidir?",
    ["+130 mV, hücre dışına", "-10 mV, hücre içine", "+10 mV, hücre dışına", "-130 mV, hücre içine", "Na⁺ dengededir"], "D", 7)
add(91, "biyofizik", "Hücrede dinlenim zar potansiyelinin kurulmasında aşağıdakilerden hangisinin önemli bir katkısı yoktur?",
    ["Zarın K⁺ geçirgenliği", "Zarın içi ve dışı arasında K⁺ konsantrasyon farkı", "Hücre içinde zarı geçemeyen negatif yüklü molekül ve proteinler", "Na/K pompası", "Zarda çözünen moleküllerin konsantrasyon farkları"], "E", 8)

# ===== HİSTOLOJİ (92-100) — sayfa 8-9 =====
add(92, "histoloji", "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.",
    ["Histoloji terimi, doku anlamına gelen histos ve bilim/çalışma anlamına gelen logia kelimelerinin birleşmesiyle oluşmuştur.", "Embriyoloji fertilizasyondan doğuma kadar insanın normal gelişimini inceleyen bilim alanıdır.", "Normal yapı ve gelişim yanında, hücre ve doku hasarının mikroskobik düzeyde araştırılması, kök hücre biyolojisi, rejeneratif tıp araştırmaları ile in vitro fertilizasyon da Histoloji ve Embriyolojinin çalışma alanları içerisinde yer alır.", "İnsan vücudunu oluşturan esas yapısal bileşenler; hücreler, hücrelerarası maddeler ve vücut sıvılarıdır.", "İnsan gözünün ayırma gücü hücrelerin ayırt edilmesi için yeterlidir."], "E", 8)
add(93, "histoloji", "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.",
    ["Histoloji ve Embriyoloji bilim alanının gelişiminde; hücrenin tanımlanması, hücre teorisinin ortaya konulması ve elektron mikroskobunun keşfi çok önemli aşamalardır", "Mikroskobik incelemelerde en önemli olan iki faktör, büyütme ve ayırma gücüdür", "Bilim alanının gelişim sürecinde; Robert Hooke ilk defa hücreyi tanımlarken, hücrelerde bir çekirdeğin varlığı Robert Brown tarafından keşfedilmiştir", "Canlıların temel yapısal biriminin hücre olduğu gerçeği ancak elektron mikroskobunun keşfi ile ortaya konulmuştur", "Genetik ve çevresel etkenlerden kaynaklanan doğumsal bozukluklar ve anormal prenatal gelişmeyi inceleyen Embriyolojinin alt dalına Teratoloji adı verilir"], "D", 8)
add(94, "histoloji", "Işık mikroskobik doku hazırlama süreciyle ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    ["En sık kullanılan fiksatif formalindir", "3-10 μm kalınlığında kesitler alınır", "Doku parçaları parafine gömülür", "En sık kullanılan boyama yöntemi Uranil asetat-Kurşun sitrat boyamasıdır", "Dokular dehidratasyon için artan derecelerde alkol serilerinden geçirilir"], "D", 8)
add(95, "histoloji", "Elektron mikroskobuna (TEM) yönelik doku hazırlama süreci ile ilgili aşağıdaki ifadelerden hangileri doğrudur?\nI. Primer fiksatif olarak genellikle Glutaraldehit kullanılır\nII. Doku parçaları rezine gömülür\nIII. Kesitler yaklaşık 50–100 nm kalınlığında alınır\nIV. Kontrast sağlamak için hematoksilen-eozin boyası kullanılır\nV. Formalin, lipoproteini boyayarak elektron yoğunluğunu artırır",
    ["I, II ve III", "I, II ve IV", "I, II, III ve IV", "I, II, III ve V", "II, III, IV ve V"], "A", 8)
add(96, "histoloji", "Hücrede endositoz süreci ile ilgili olarak aşağıda verilenlerden hangileri yanlıştır?\nI. Sıvıların ve 150 nm'den küçük çaplı moleküllerin hücre içerisine alınmasına pinositoz denir.\nII. Pinositoz sürecinde vezikül oluşumu için klatrin molekülleri kullanır.\nIII. Bakteriler, hücre kalıntıları ve biyolojik olarak parçalanan materyallerin hücre içerisine alınması fagositoz süreci ile gerçekleşir.\nIV. Fagositoz yapan hücrelerin en gelişmiş organelleri peroksizomlardır.\nV. Reseptör aracılı endositozda adaptin, dinamin gibi moleküller rol oynar ve klatrin bağımlı bir süreçtir.",
    ["I ve II", "II ve III", "II ve IV", "II, III, IV", "I ve V"], "C", 8,
    note="III. ifadenin taramadaki bazı sözcükleri filigran nedeniyle tam okunamadı; cevap etkilenmiyor.", conf=0.85)
add(97, "histoloji", "Endozomlarla ilgili olarak aşağıdakilerden hangisi yanlıştır?",
    ["Sitoplazmada endositotik yollarla ilişkili olarak bulunan membranla çevrili yapılardır.", "Erken endozomlar, hücrede Golgi ve çekirdeğe yakın yerleşimli olup daha asidik bir pH'ya sahiptir ve lizozomlara olgunlaşırlar.", "Erken ve geç endozomlar arasında madde taşınımı multivezikuler cisimcikler yoluyla gerçekleşir.", "Lizozomal enzimler ve lizozomal membran proteinleri GER ve Golgide üretildikten sonra endozomlar aracılığı ile lizozoma aktarılır.", "Erken endozomlar endositozla hücreye alınan reseptör-protein komplekslerinin ayrılmasından ve geri dönüşümünden sorumlu yapılardır."], "B", 8)
add(98, "histoloji", "Hücre çekirdeği ile ilgili olarak verilen seçeneklerden hangisi yanlıştır?",
    ["Çekirdek kromatininin en küçük yapısal birimleri nükleozomlar olup merkezi histon moleküllerini saran iki DNA halkasından oluşurlar.", "Ökromatin, gevşek olarak paketlenen kromatin formu olup nöronlar ve karaciğer hücreleri gibi metabolik yönden aktif hücrelerde görülür.", "Çekirdek kılıfının iç membranına tutunan fibröz lamina, lamin adı verilen ara filamanlardan oluşmaktadır.", "Nükleoporinleri içeren nüklear por kompleksi 70-80 nm çapında olup çekirdek ve sitoplazma arasında moleküllerin transportunu sağlar.", "Çekirdekçik, çift tabakalı bir membranla çevrili olup her hücrede yalnızca bir tanedir."], "E", 8)
add(99, "histoloji", "Hücre iskeleti ile ilgili olarak aşağıda verilenlerden hangisi yanlıştır?",
    ["Hücre iskeleti, mikrotübüller, aktin filamanları ve ara filamanlar tarafından oluşturulur.", "Mikrotübüller mikrovilluslarının yapısını oluşturur.", "Silya ve flagellada mikrotübüller stabil olup dinamik kararsızlık göstermez (uzayıp kısalmaz).", "Aktin filamanları mikrovilluslarının yapısını oluşturur, hücre bölünmesinde, fagositoz sürecinde fonksiyon görürler.", "Sentriyollerde yer alan mikrotübüller, periferde 9 adet üçlü (triplet) mikrotübül şeklinde organize olur."], "B", 8)
add(100, "histoloji", "Mitokondriyonla ilgili aşağıdakilerden hangisi yanlıştır?",
    ["Mitokondriyon dış membranı yüzey alanını genişletmek amacıyla kristalar şeklinde düzenlenmiştir.", "Mitokondriyal iç membranda ATP sentezi gerçekleşir.", "Mitokondriyon hücre yaşamının devamına ya da hücrenin ölüme gitmesine karar verebilen bir organeldir.", "İç ve dış mitokondriyal membranlar arasındaki intermembran aralıktan salınan sitokrom c, hücrenin apoptoz sürecine girmesini sağlar.", "Mitokondriyal matrikste DNA, ribozom ve enzimler yer alır."], "A", 9)

# ===== ENTEGRE (101-105) — sayfa 9 =====
add(101, "entegre", "Antibiyotiklerin yaygın kullanımının en fazla olduğu alan hangisidir?",
    ["Yoğun bakım üniteleri", "Evde kullanılan reçetesiz ilaçlar", "Tarım ve hayvancılık", "Uzay biyolojisi araştırmaları", "Aşı üretim tesisleri"], "C", 9)
add(102, "entegre", "Aşağıdakilerden hangisi küresel ısınma sonucunda vektör kaynaklı zoonoz riskinin artma mekanizmalarından biri değildir?",
    ["Vektör popülasyonunun büyümesi", "Aktif oldukları mevsimin uzaması", "Yeni coğrafyalara yayılmaları", "Reservuar hayvan çeşitliliğinin azalması", "Taşıdıkları patojenleri daha hızlı çoğaltmaları"], "D", 9)
add(103, "entegre", "Aşağıdaki zoonoz–kaynak eşleştirmelerinden hangisi yanlıştır?",
    ["Toxoplasma gondii — Çiğ/az pişmiş et", "Brucella spp. — Pastörize edilmemiş süt ürünleri", "Hepatit E — Yaban domuzu etleri", "Salmonella spp. — Çiğ yumurta", "Listeria monocytogenes — Taze sebzeler"], "E", 9)
add(104, "entegre", "Covid 19'un ilk vakaları nerede tespit edilmiştir?",
    ["Tokyo", "New York", "Wuhan'daki deniz ürünleri pazarı", "Seul", "Berlin"], "C", 9)
add(105, "entegre", "Aşağıdakilerden hangisi 'Tek Sağlık' temel çalışma alanlarından biri değildir?",
    ["Zoonotik hastalıklar", "Antimikrobiyal direnç / AMR", "Gıda güvenliği ve güvencesi", "Nüfus artışı ve sağlıksız kentleşme", "İklim değişikliği"], "D", 9)

exam = {
    "id": EID,
    "label": "2025-2026 Dönem 1 TEM 2",
    "shortLabel": "2025-26",
    "year": "2025-2026",
    "period": 1,
    "term": "TEM 2",
    "date": "2026-06",
    "sourceFile": "WhatsApp Image 2026-11-16 at 22.59.36 (1).pdf (sayfa 3,1,2,7,4,5,6,8,12)",
    "sourcePages": list(range(1, 10)),
    "answerStatus": "official",
    "ocrQuality": "medium",
    "notes": "A kitapçığı; telefonla taranmış (CamScanner) sayfalardan elle aktarılmıştır. 1-100 arası sorulara ek olarak ENTEGRE başlığı altında 101-105 soruları vardır. Basılı cevap anahtarı kullanılmıştır; şüpheli yerler 'kontrol gerekli' olarak işaretlenmiştir.",
}
b.finish(exam, 105)
