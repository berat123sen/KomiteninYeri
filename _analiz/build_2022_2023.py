# -*- coding: utf-8 -*-
"""2022-2023 Dönem 1 TEM 2 (A kitapçığı) -> JSON.
Kaynak: WhatsApp Image 2026-11-16 ... (1).pdf (fotoğraf taraması).
Sayfa sırası (orijinal PDF sayfaları): 9,10,11,17,13,14,15,16,18 -> kaynak PDF sayfa 1..9
"""
from lib_build_new import Builder

EID = "2022-2023-tem-2"
b = Builder(EID)
add = b.add

# ===== TIBBİ BİYOKİMYA (1-36) =====
add(1, "biyokimya", "Glikoneojenez sırasında karaciğerde glikolizin inhibisyonu için ana mekanizma nedir?",
    ["Glukokinaz, yüksek Glukoz-6-P derişimi tarafından inhibe edilir.",
     "Fosfofruktokinaz-2/Fruktoz-2,6-bisfosfatazın fosforilasyonu, Fosfofruktokinaz-1'in allosterik bir aktivatörü olan Fruktoz-2,6-bisfosfat düzeylerinin düşmesine yol açar.",
     "Artan hepatik asetil-KoA, pirüvat dehidrojenazın aktivitesini inhibe eder.",
     "Glukoz-6-P'nin glukoza hidrolizi, Glukoz-6-P'nin glikoliz için varlığını azaltır.",
     "İnsülinin bir glukoz taşıyıcısı olan GLUT-2'yi aktive ederek glukozun karaciğer alımını etkinleştirerek glukoneogeneze yönelmesini sağlar."], "B", 1)
add(2, "biyokimya", "Hangisi 2,3-bifosfogliseratı tanımlayan bir özelliktir?",
    ["Substrat düzeyinde fosforilasyon için kullanılan yüksek enerjili bir substrattır.",
     "Pentoz fosfat yolunun ara çevrim aşamasındaki bir üründür.",
     "Fosfogliserat kinaz tepkimesinin bir ürünüdür.",
     "Hemoglobinin O₂'ye eğilimini azaltan allosterik bir efektördür.",
     "Gliseraldehit-3-fosfat dehidrogenaz tepkimesinin ürünüdür."], "D", 1)
add(3, "biyokimya", "Okside hali makrofajlar tarafından alınarak köpük hücrelerinin oluşmasını sağlayan lipoprotein molekülü aşağıdakilerden hangisidir?",
    ["Şilomikron", "Çok düşük dansiteli lipoprotein (VLDL)", "Ara yoğunluklu lipoprotein (IDL)", "Düşük dansiteli lipoprotein (LDL)", "Yüksek dansiteli lipoprotein (HDL)"], "D", 1)
add(4, "biyokimya", "Yüksek dansiteli lipoprotein (HDL) metabolizmasında görev yapan lesitin kolesterol asil transferaz enziminin (LCAT) aktivatörü aşağıdaki apoproteinlerden hangisidir?",
    ["Apo AI", "Apo CII", "Apo B-48", "Apo B-100", "Apo E"], "A", 1)
add(5, "biyokimya", "Elektron transport zincirinde yer alan komplekslerden hangisi aynı zamanda TCA döngüsünün enzimlerinden biridir?",
    ["Kompleks I", "Kompleks II", "Kompleks III", "Kompleks IV", "Kompleks V"], "B", 1)
add(6, "biyokimya", "Aşağıdaki enzimlerden hangisi hem TCA döngüsünün hız kısıtlayıcı enzimlerinden biri hem de pirüvat dehidrogenaz enzimiyle fonksiyonel benzerlik gösteren enzimdir?",
    ["Malat dehidrogenaz", "Süksinat dehidrogenaz", "Sitrat liyaz", "İzositrat dehidrogenaz", "Alfa ketoglutarat dehidrogenaz"], "E", 1)
add(7, "biyokimya", "Pentoz fosfat yolunun inhibitörü aşağıdakilerden hangisidir?",
    ["NAD⁺", "FAD", "Asetil KoA", "NADH", "NADPH"], "E", 1)
add(8, "biyokimya", "Karbonhidrat, protein ve yağların metabolizması sonucu oluşan ortak ürün hangisidir?",
    ["Yağ asitleri", "Glukoz", "Gliserol", "Asetil KoA", "Üre"], "D", 1)
add(9, "biyokimya", "Pentoz fosfat yolu ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
    ["Eritrosit membran bütünlüğü için önemlidir", "Lipid sentezi için gereklidir", "Nükleotid sentezi için üç karbonlu monosakkarit kaynağıdır", "ATP harcanmaz", "Glutatyon redüktaz enzimi için kofaktör sağlar"], "C", 1)
add(10, "biyokimya", "Glikojenin yıkılmasını sağlayan enzimlerden biri olan glikojen fosforilazın ürünü ve ürünün dönüştüğü molekül aşağıdakilerden hangisidir?",
    ["Glikoz 1-fosfat ve Glikoz 6-fosfat", "Glikoz 1,6 bifosfat ve Glikoz 6-fosfat", "UDP glikoz ve glikoz", "Glikoz 6-fosfat ve glikoz", "Glikoz 2,6 bifosfat ve Glikoz 6-fosfat"], "A", 1)
add(11, "biyokimya", "Glukoz sorbitol yolunda aşağıdaki ürünlerden hangisine dönüşür?",
    ["Galaktoz", "Fruktoz", "Glukronat", "Askorbat", "Mannoz"], "B", 1)
add(12, "biyokimya", "Kan glukozu düşmüş bir kişide, aşağıdaki enzimlerden hangisinin karaciğerde inhibe olması gerekir?",
    ["Pirüvat karboksilaz", "PEP karboksikinaz", "Fruktoz-1,6-bifosfataz", "Glukoz-6-fosfataz", "Fosfofruktokinaz-1"], "E", 1)
add(13, "biyokimya", "Sitrik asit döngüsünde görev alan enzimler, aşağıdaki vitaminlerden hangisini ko-enzim olarak kullanmaz?",
    ["Pantotenik asit", "Askorbik asit", "Riboflavin", "Niasin", "Tiamin"], "B", 1)
add(14, "biyokimya", "Glikojen sentezinde başlangıç glikozil kalıntıları, glikojenin proteininde aşağıdaki aminoasitlerden hangisine eklenir?",
    ["Asparajin", "Triptofan", "Glisin", "Tirozin", "Alanin"], "D", 1)
add(15, "biyokimya", "Glikoliz, glukoneogenez ve glikojenolize katılan ortak metabolit aşağıdakilerden hangisidir?",
    ["Fruktoz 1-fosfat", "Riboz 5-fosfat", "UDP-glukoz", "Galaktoz 1-fosfat", "Glukoz 6-fosfat"], "E", 2)
add(16, "biyokimya", "Aşağıdakilerden hangisi glukoneogenezde yer alan enzim veya metabolit değildir?",
    ["Fosfoenolpiruvat", "Gliseraldehid 3-fosfat", "Piruvat karboksilaz", "Piruvat dehidrogenaz", "Glukoz 6-fosfataz"], "D", 2)
add(17, "biyokimya", "Diyabetli hastalarda kan glukoz düzeyinin uygun şekilde sürdürülmesi için yiyeceklerin glisemik indekslerinin göz önünde tutulması gerekir. Aşağıdakilerden hangisi glisemik indeksi en iyi tanımlar?",
    ["Gıda alımı sonrası glukagonun kan derişimindeki artış",
     "Gıda alımı sonrası glukagonun kan derişimindeki artış ile aynı miktarda beyaz ekmeğinkinin kıyaslanması",
     "Gıda alımı sonrası kan insülin derişimindeki artış",
     "Gıda alımı sonrası glukagonun kan derişimindeki düşüş ile aynı miktarda beyaz ekmeğinkinin kıyaslanması",
     "Gıda alımı sonrası kan insülin derişimindeki artış ile aynı miktarda beyaz ekmeğinkinin kıyaslanması"], "B", 2,
    note="Taranan sayfadaki basılı cevap B olarak görünüyor; şık metinleri taramada net okunamadı ve glisemik indeksin klasik tanımıyla (kan glukoz yanıtı) örtüşmüyor. Kaynakla karşılaştırarak kontrol edin.",
    review="needs_review", conf=0.6)
add(18, "biyokimya", "Yağ asidi sentezi ve Yağ asidi yıkımı (beta oksidasyon) arasındaki farklar açısından aşağıdakilerden hangisi doğrudur?",
    ["Sentez mitokondride, oksidasyon sitozolde gerçekleşir", "Sentezde NADH, oksidasyonda FAD kullanılır", "İnsülin yokluğunda sentez hızlanır, oksidasyon baskılanır", "Oksidasyonda ara bileşik olarak malonil CoA oluşur, sentezde oluşmaz", "Sentezde Asil Taşıyıcı Protein (ACP) kullanılır, oksidasyonda almaz"], "E", 2)
add(19, "biyokimya", "Yağ asidi sentezi için aşağıdakilerden hangisi gerekli değildir?",
    ["Asetil CoA", "FADH₂", "ATP", "Biotin", "HCO₃⁻"], "B", 2)
add(20, "biyokimya", "Yağ asitlerinin beta oksidasyonu sırasında ilk döngü sonucunda aşağıdakilerden hangisi açığa çıkmaz?",
    ["H₂O", "Asetil CoA", "NADH + H⁺", "FADH₂", "Yağ asil CoA (n-2)"], "A", 2)
add(21, "biyokimya", "Keton cisimcikleri hakkında aşağıda verilen ifadelerden hangisi yanlıştır?",
    ["Uzun süren açlıkta sentezleri artar", "İnsülin yokluğunda sentezleri artar", "Karaciğer enerji kaynağı olarak keton cisimciklerini kullanır", "Kanda en yüksek konsantrasyonda beta hidroksibütirat görülür", "Keton cisimcikleri kanda yükseldiğinde idrarda da saptanırlar"], "C", 2)
add(22, "biyokimya", "Bir karışımda bulunan gliserofosfolipitler Fosfolipaz D ile muamele edilirse aşağıdakilerden hangisi açığa çıkmaz?",
    ["Serin", "İnositol", "Kolin", "Etanolamin", "Lizolesitin"], "E", 2)
add(23, "biyokimya", "Hem gliserofosfolipit hem de trigliserit sentezine gidebilen ara madde hangisidir?",
    ["CDP-kolin", "Fosfatidik asit", "Fosfatidil serin", "Sfingomiyelin", "Plazmalojen"], "B", 2)
add(24, "biyokimya", "Doğumdan itibaren tamamen yağsız bir diyetle beslenen sıçanlarda aşağıdakilerden hangisinin oluşumu gerçekleşemez?",
    ["Kolesterol", "Triasilgliserol", "Prostaglandinler", "Sfingofosfolipitler", "Gliserofosfolipitler"], "C", 2)
add(25, "biyokimya", "Aşağıdakilerden hangisi primer safra asitlerinin konjugasyonunda yer alan temel bileşiktir?",
    ["Karnitin", "Serin", "Glutamik asit", "Glisin", "Koenzim A"], "D", 2)
add(26, "biyokimya", "Sitrat, aşağıda verilen enzimlerin hangisinin üzerinde pozitif allosterik etki gösterir?",
    ["Piruvat kinaz", "Asetil CoA karboksilaz", "Fosfofruktokinaz", "Karnitin asil transferaz I", "Sitrat liyaz"], "B", 2)
add(27, "biyokimya", "Aşağıda verilen maddelerden hangisinin öncü maddesi kolesterol değildir?",
    ["Adrenalin", "Kortizol", "Kolik asit", "Vitamin D", "Testosteron"], "A", 2)
add(28, "biyokimya", "Aşağıdaki aminoasitlerden hangisi Sitrik Asit Döngüsünde (Kreb's) yer alan bir maddenin transaminasyonu sonucunda oluşur?",
    ["Metionin", "Valin", "İzolösin", "Aspartik asit", "Alanin"], "D", 2)
add(29, "biyokimya", "Üre döngüsünün ilk enzimi olan \"Karbamoil fosfat sentetaz I\" enziminin reaksiyonu gerçekleştirebilmesi için aşağıdakilerden hangisine gereksinimi yoktur?",
    ["HCO₃⁻", "ATP", "NAD", "NH₄⁺", "N-asetil glutamat"], "C", 3)
add(30, "biyokimya", "Aşağıdaki Sitrik Asit Döngüsü elemanlarından hangisi aminoasitlerin karbon iskeletinin yıkımı sonucu oluşmaz?",
    ["Süksinil CoA", "Fumarat", "Alfa ketoglutarat", "Oksaloasetat", "Sitrat"], "E", 3)
add(31, "biyokimya", "NAD ve NADP öncü maddesi olan nikotinat (niasin) hangi aminoasitten sentezlenebilir?",
    ["Triptofan", "Tirozin", "Treonin", "Fenilalanin", "Histidin"], "A", 3)
add(32, "biyokimya", "Glisin, aşağıdaki maddelerden hangisinin sentezinde rol oynamaz?",
    ["Glutatyon", "Taurin", "Kolik asit konjugasyonu", "Serin", "HEME"], "B", 3)
add(33, "biyokimya", "Sistatyonin beta sentaz enzim eksikliğinde aşağıdaki maddelerin hangisinin konsantrasyonu kanda yükselir?",
    ["Arginin", "Sitrullin", "Homosistein", "Ornitin", "Sistein"], "C", 3)
add(34, "biyokimya", "Aşağıdakilerden hangisi kas ve karaciğer dokuları arasındaki glikojen-laktat-glukoz dönüşümünü anlatan metabolik yolağın karşılığıdır?",
    ["Cori Döngüsü", "Glikojenez", "Üre Döngüsü", "Glukoneogenez", "Miyoinositol Döngüsü"], "A", 3)
add(35, "biyokimya", "Aşağıdakilerden hangisi mitokondride piruvatın dekarboksilasyonu ile asetilkoenzim oluşumunu katalizleyen ve tiamin pirofosfat, niasin ve pantotenik asit gibi koenzimlerin kullandığı enzimdir?",
    ["Heksokinaz", "Piruvat Dehidrogenaz", "Alfa-keto glutarat dehidrogenaz", "Piruvat karboksilaz", "Asetil-CoA karboksilaz"], "B", 3,
    conf=0.9)
add(36, "biyokimya", "Lipitlerin sindirimi sırasında triaçilgliserolleri parçalayarak 2 adet serbest yağ asidi ve bir adet 2-monogliserol oluşumunu sağlayan enzim aşağıdakilerden hangisidir?",
    ["Lipoprotein Lipaz", "Pankreatin", "Pankreatik Lipaz", "Fosfo Lipaz", "Pankreatik Sekretaz"], "C", 3)

# ===== HİSTOLOJİ VE EMBRİYOLOJİ (37-45) =====
add(37, "histoloji", "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.",
    ["Histoloji terimi, doku anlamına gelen histos ve bilim veya çalışma anlamına gelen logia kelimelerinin birleşmesiyle oluşmuştur.",
     "Histoloji insanda çıplak gözle görülebilen vücut kısımlarını inceleyen bilim alanıdır.",
     "Normal yapı ve gelişim yanında, hücre ve doku hasarının mikroskobik düzeyde araştırılması, kök hücre biyolojisi, rejeneratif tıp araştırmaları ile in vitro fertilizasyon da Histoloji ve Embriyolojinin çalışma alanları içerisinde yer alır.",
     "Embriyoloji fertilizasyondan doğuma kadar insanın normal gelişimini inceleyen bilim alanıdır.",
     "İnsan vücudunu oluşturan esas yapısal bileşenler; hücreler, hücrelerarası maddeler ve vücut sıvılarıdır."], "B", 3)
add(38, "histoloji", "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.",
    ["Histoloji ve Embriyoloji bilim alanının gelişiminde; hücrenin tanımlanması, hücre teorisinin ortaya konulması ve elektron mikroskobunun keşfi çok önemli aşamalardır.",
     "Bilim alanının gelişim sürecinde; Robert Hooke ilk defa hücreyi tanımlarken, hücrelerde bir çekirdeğin varlığı Robert Brown tarafından keşfedilmiştir.",
     "Canlıların temel yapısal biriminin hücre olduğu gerçeği hücre teorisi ile ortaya konulmuştur.",
     "Mikroskobik incelemelerde en önemli olan iki faktör, büyütme ve ayırma gücüdür.",
     "İnsan gözünün ayırma (rezolüsyon) gücü hücrelerin ayırt edilmesinde yeterlidir."], "E", 3)
add(39, "histoloji", "Hücrede veziküler transportla ilgili olarak verilen seçeneklerden hangisi yanlıştır?",
    ["Maddelerin hücre içine girdiği veziküler transport süreci endositoz, maddelerin hücreyi terkettiği süreç ise ekzositoz olarak adlandırılır.",
     "Sıvı maddelerin ve 150 nm'den küçük çaplı moleküllerin hücre içerisine alındığı pinositoz sürecinde klatrin kaplı veziküller oluşur.",
     "Reseptör aracılı endositozda hücreye alınacak uygun moleküllerin seçiminde adaptin molekülleri görev alır ve klatrinle kaplı vezikül oluşumu gerçekleşir.",
     "Ekzositozun konstitütif yolağında salgı ürünü hücrede depolanmadan transport veziküleri içinde direk olarak plazma membranına iletilerek hücreyi terkeder.",
     "Ekzositozun düzenlenmiş salgı yolağında salgı ürünü veziküller içinde geçici olarak depolanır ve nöral ya da hormonal uyarıyla birlikte plazma membranına iletilerek hücreden dışarıya verilir."], "B", 3)
add(40, "histoloji", "Endozomlarla ilgili olarak aşağıdakilerden hangisi yanlıştır?",
    ["Sitoplazmada endositotik yollarla ilişkili olarak bulunan membranla çevrili yapılardır.",
     "Erken endozomlar sitoplazmada periferal olarak yerleşirken, geç endozomlar Golgi ve çekirdeğe yakın yerleşimli olup daha asidik bir pH'ya sahiptir.",
     "Erken ve geç endozomlar arasında madde taşınımı multivezikuler cisimcikler yoluyla gerçekleşir.",
     "Lizozomal enzimler ve lizozomal membran proteinleri erken ve geç endozomlarda üretilir.",
     "Erken endozomlar endositozla hücreye alınan reseptör-protein komplekslerinin ayrılmasından ve geri dönüşümünden sorumlu yapılardır."], "D", 4)
add(41, "histoloji", "Lipid ve steroid metabolizmasında görev alan, detoksifikasyon ve zararlı maddelerin konjugasyonundan sorumlu organel hangisidir?",
    ["Granüler endoplazmik retikulum", "Golgi apparatus", "Agranüler endoplazmik retikulum", "Mitokondriyon", "Lizozom"], "C", 4)
add(42, "histoloji", "Mitokondriyonlar ile ilgili aşağıdakilerden hangisi yanlıştır?",
    ["Sayıları, yapı ve şekilleri hücreden hücreye farklılık gösteren çift membranlı organellerdir.",
     "Bölünebilme ve şekil değiştirebilme özelliklerine sahiptir.",
     "İç ve dış mitokondriyal membranlar üzerinde proteinlerin mitokondriyona transportunda görevli translokaz kompleksleri bulunur.",
     "Mitokondriyal matrikste DNA, ribozom ve enzimler yer alır.",
     "Dış membran iyon ve moleküllere geçirimsiz olup ATP sentaz aktivitesine sahip elementar partikülleri içerir."], "E", 4)
add(43, "histoloji", "Mikrotübüllerle ilgili olarak verilen seçeneklerden hangisi yanlıştır?",
    ["Dairesel olarak düzenlenmiş 13 dimerik tübülin molekülünden oluşan 20-25 nm çapa sahip içi boş protein tüpleridir.",
     "Eksi uçları MTOC içinde nükleasyon bölgesi olarak görev yapan γ-tübülin halkası içinde olup artı uçları perifere bakar.",
     "Mikrovilluslarının yapısal merkezi kısımlarını oluştururlar.",
     "Hücre içerisinde organel ve veziküllerin transportundan ve mitoz sırasında mitotik iğin oluşmasında görev alırlar.",
     "Silya, flagella ve sentriolün yapısını oluştururlar."], "C", 4)
add(44, "histoloji", "Işık mikroskobik incelemeler için canlıdan alınan dokuyu otolitik ve bakteriyolitik reaksiyonlardan korumak için uygulanan doku takip işlemi hangisidir?",
    ["Tespit (fiksasyon)", "Yıkama", "Suyunu giderme (dehidratasyon)", "Gömme (bloklama)", "Kapatma"], "A", 4)
add(45, "histoloji", "Elektron mikroskobik inceleme yöntemi ile ilgili olarak aşağıdakilerden hangisi yanlıştır?",
    ["Gözle görülmeyen ışık kaynağı kullanır.", "Canlı hücre ve dokuların incelenmesine olanak sağlar.", "Renksiz (siyah-beyaz) görüntü elde edilir.", "Dokuların fiksasyonunda amaç için glutaraldehid ve osmik asit kullanılır.", "Gömme materyali olarak epoksi resin kullanılır."], "B", 4)

# ===== BİYOFİZİK (46-62) =====
add(46, "biyofizik", "Aşağıdakilerden hangisi vücut sıcaklığını düşüren bir mekanizma değildir?",
    ["Terleme ve buharlaşma", "Damarların genişlemesi", "Isı oluşumunun artması", "Azalmış istemli kas hareketleri", "Solunumda artış"], "C", 4)
add(47, "biyofizik", "Aşağıda ısı aktarımı ile verilen bilgilerden hangisi/hangileri doğrudur?\nI. Sıvı veya gaz içinde ısı aktarımına konveksiyon denir.\nII. Kısadalga radyasyon enerjetik radyasyondur.\nIII. Uzun dalgalar kısa dalgalara göre daha fazla zarar vericidir.",
    ["Yalnız I", "Yalnız II", "Yalnız III", "I-II", "II-III"], "D", 4)
add(48, "biyofizik", "Deri ısısı çevre ısısından yüksek olduğu zaman ısı kaybı aşağıdakilerden hangisi/hangileri ile gerçekleşir?\nI. Radyasyon\nII. Kondüksiyon\nIII. Kontraksiyon\nIV. Konveksiyon",
    ["I-III", "II-III", "I-III-IV", "II-III-IV", "I-II-IV"], "E", 4)
add(49, "biyofizik", "Aşağıdakilerden hangisi aktivasyon enerjisinin özelliklerinden biri değildir?",
    ["Değeri ancak katalizörle düşer.", "Sıcaklıkla değişir.", "Değeri her zaman pozitiftir.", "Reaksiyona giren maddelerin konsantrasyonunu arttırmakla da sağlanır.", "Reaktiflerin cinsine bağlı olarak değişir."], "B", 4)
add(50, "biyofizik", "Aşağıda reaksiyonlarla ilgili verilen ifadelerden hangisi/hangileri doğrudur?\nI. Ekzotermik reaksiyon sonucunda ısı enerjisi açığa çıkmaz.\nII. Endotermik reaksiyonlar ısı enerjisini kullanarak gerçekleşir.\nIII. Bütün kimyasal reaksiyonlar, reaksiyona başlayabilmeleri için bir giriş enerjisine yani aktivasyon enerjisine ihtiyaç duyarlar.",
    ["Yalnız I", "Yalnız II", "II ve III", "I ve III", "Yalnız III"], "C", 4)
add(51, "biyofizik", "İnsan vücut sıcaklığının biyolojik etkileri ile verilenlerden hangisi/hangileri doğrudur?\nI. 28 °C: Kaslar çalışmaz\nII. 30 °C: Vücut sıcaklık kontrolünü kaybeder.\nIII. 33 °C: Bilinç kaybı\nIV. 42 °C: MSS çöker.\nV. 44 °C: Ölüm",
    ["I ve II", "I, II ve III", "I, II, V", "Hepsi", "I, II, III ve IV"], "D", 4)
add(52, "biyofizik", "Aşağıdaki tepkime türlerinden hangisi hücre için entropisini azaltır?",
    ["Hidroliz.", "Sindirim.", "Anabolik reaksiyonlar.", "Katabolik reaksiyonlar.", "Hiçbiri"], "C", 4)
add(53, "biyofizik", "ATP'nin ADP'ye dönüşüm reaksiyonu için Gibbs serbest enerjisini hesaplayınız (T=293 Kelvin, ΔH: 19,07 Kcal, ΔS: 90 cal).",
    ["19070 cal.", "-90 cal", "-26,37 Kcal.", "-7,3 Kcal.", "7300 Kcal"], "D", 5)
add(54, "biyofizik", "Hücrelerde enerji dönüşümleri ile aşağıdakilerden hangisi yanlıştır?",
    ["Fotosentez sırasında serbest enerji (ΔG) artar.", "Hücresel solunumda serbest enerji (ΔG) azalır.", "ATP'nin elektronegatifliği, ATP hidrolizinin enerjetikliğini belirler.", "ATP'den fosfat grubunun salınması ile enerji açığa çıkar.", "ATP'nin serbest enerjisi ADP'den daha azdır."], "E", 5)
add(55, "biyofizik", "Bir hücrenin zar kalınlığı iki katına çıkar ancak hücre aynı boyutta kalırsa, hücre zarının direnci ve kapasitansı nasıl değişir?",
    ["Direnç ve kapasitans artar.", "Direnç artar, kapasitans azalır.", "Direnç azalır, kapasitans artar.", "Direnç ve kapasitans azalır.", "Hesaplanamaz."], "B", 5)
add(56, "biyofizik", "Hücre zarı ile ilgili aşağıdakilerden hangisi yanlıştır?",
    ["Lipit çift tabaka elektriksel bakımdan yalıtkan özelliklere sahiptir.", "Zar işlevsel olarak bir kapasitöre eşdeğerdir.", "Hücre zarının kapasitansı, zar potansiyelinin akımdaki değişikliğe ne kadar hızlı tepki verebileceğini belirler.", "Açık iyon kanal sayısı zar direncini değiştirir.", "İyon kanallarının açılması iletkenliği arttırır."], "D", 5)
add(57, "biyofizik", "Hücre zarından basit difüzyon ile doğrudan geçen bir molekülün difüzyon hızının (difüzyon akısının) büyüklüğünü aşağıdakilerden hangisi etkilemez?",
    ["ATP konsantrasyonu.", "Molekülün konsantrasyon farkı.", "Molekülün difüzyon katsayısı.", "Zarın yüzey alanı.", "Zar kalınlığı."], "A", 5)
add(58, "biyofizik", "Eşit konsantrasyonlardaki (gram/litre) glikoz ve sükroz solüsyonları, sadece su geçişine izin veren, başlangıçta kapalı bir zar ile ayrılmıştır. Yarı geçirgen zar açıldığında suyun net geçişi hangi tarafa olacaktır?",
    ["Glikoz tarafına.", "Sükroz tarafına.", "Geçiş olmaz.", "Başlangıçta sükroz, ardından glikoz tarafına.", "Hesaplanamaz."], "A", 5)
add(59, "biyofizik", "Hücre zarından madde taşınımı ile ilgili aşağıdakilerden hangisi yanlıştır?",
    ["Pasif taşınımda metabolik enerji harcanması gerekmez.", "İyon kanalının seçiciliğinde iyonun yükü önemlidir.", "Kanallardan iyon geçişi ATP'nin hidrolizi ile gerçekleşir.", "Kolaylaştırılmış difüzyonda akı bir doygunluk değerine ulaşır.", "Na⁺ ile ortaklaşa ve karşıt taşınım için ana enerji kaynağı ATP'dir."], "C", 5)
add(60, "biyofizik", "Aşağıdakilerden hangisi Donnan potansiyelinin özelliği değildir?",
    ["Yalnızca pasif mekanizmalarla bir zarın iki tarafı arasında kurulan potansiyel farktır.", "Zarı geçemeyen anyonlar, zarı geçebilen iyonların yeni bir dağılıma uğramasına neden olur.", "Donnan potansiyeli bir denge durumudur.", "Donnan dengesinin kurulması, ozmoz nedeniyle hücrelerin şişmesine neden olur.", "Donnan potansiyeli Na⁺/K⁺ pompası ile kurulur."], "E", 5)
add(61, "biyofizik", "Aşağıdakilerden hangisi bir cins iyonun konsantrasyon farkından doğan göçü dengelemek için zarın iki tarafı arasındaki olması gereken potansiyel farkı ifade eder?",
    ["Konsantrasyon gradiyenti.", "Elektriksel gradiyent.", "Fick Yasası.", "Nernst potansiyeli.", "Dinlenim zar potansiyeli"], "D", 5)
add(62, "biyofizik", "Bir nöronun dinlenim zar potansiyeli -70 mV, sodyum (Na⁺) denge potansiyeli (ENa)=+60 mV ise zarda Na⁺ için elektrokimyasal potansiyel farkın değeri ve Na⁺'ı göçe zorlayan pasif kuvvetin yönü nedir?",
    ["+130 mV, hücre dışına.", "-130 mV, hücre içine.", "0 mV", "-10 mV, hücre içine.", "+10 mV, hücre dışına."], "B", 5)

# ===== TIBBİ FİZYOLOJİ (63-74) =====
add(63, "fizyoloji", "Kandaki glükoz düzeyini düzenleyen bir negatif geri bildirim devresi, glükoz düzeyi 100 mg/dL'den 60 mg/dL'e düştüğünde, glükoz düzeyini en çok 90 mg/dL'ye çıkarabildiğine göre bu devrenin kazancı ne kadardır?",
    ["-1", "-2", "-3", "-4", "-5"], "C", 5)
add(64, "fizyoloji", "Mitokondrilerdeki oksidatif fosforilasyon sırasında, ATP sentezini sağlayan enzim aşağıdaki iyon gradyanlarının hangisinden yararlanarak ADP'yi ATP'ye dönüştürür?",
    ["H⁺", "Na⁺", "Ca⁺⁺", "Cl⁻", "HCO₃⁻"], "A", 5)
add(65, "fizyoloji", "Silyum hareketi için kullanılan ATP'nin parçalanmasını sağlayan ATP'az etkinliğine sahip molekül ile hareket sırasında rol oynayan iyon aşağıdaki seçeneklerin hangisinde doğru olarak verilmiştir?",
    ["Neksin: K⁺", "Neksin: Ca⁺⁺", "Dinein: K⁺", "Dinein: Ca⁺⁺", "Adaptin: Na⁺"], "D", 5)
add(66, "fizyoloji", "Pri-miRNA'dan RISC-miRNA kompleksi oluşum sürecinde rol oynayan proteinler aşağıdaki seçeneklerden hangisinde doğru olarak verilmiştir?\nI) Peptidil transferaz\nII) Mikroişlemci kompleks\nIII) Hidrolaz\nIV) Kesici",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "III ve IV"], "D", 6)
add(67, "fizyoloji", "DNA eşlenmesi sırasında birbirini izleyen nükleotidlerin birbirine bağlanmasını sağlayan enzim aşağıdakilerden hangisidir?",
    ["Ligaz", "Helikaz", "Primaz", "Polimeraz", "Topoizomeraz"], "D", 6)
add(68, "fizyoloji", "Su molekülleri arasındaki hidrojen bağları şebekesi suya fizyolojik açıdan önemli olan aşağıdaki özelliklerden hangilerini kazandırır?\nI) Yüzey geriliminin yüksek olması\nII) Buharlaşma ısısının düşük olması\nIII) Dielektrik sabitinin yüksek olması\nIV) Isı kapasitesinin düşük olması",
    ["I ve II", "I ve III", "II ve III", "II ve IV", "I ve IV"], "B", 6)
add(69, "fizyoloji", "500 mL saf suda 0.5 M CaCl₂ çözündüğünde, bu çözeltinin osmolaritesi kaç mOsm olur?",
    ["1000", "2000", "3000", "4000", "5000"], "C", 6,
    note="Taranan sayfadaki basılı cevap C (3000) olarak görünüyor; stemdeki değerlerle yapılan hesap (0,5 M × 3 = 1500 mOsm/L) bununla örtüşmüyor. Kaynakla karşılaştırarak kontrol edin.",
    review="needs_review", conf=0.6)
add(70, "fizyoloji", "Bir parçacığa ait difüzyon katsayısı aşağıdaki parametrelerden hangileri ile ters orantılıdır?\nI) Mutlak sıcaklık\nII) Parçacığın yarıçapı\nIII) Ortam viskozitesi\nIV) Boltzmann sabiti",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "III ve IV"], "B", 6)
add(71, "fizyoloji", "Aşağıdakiler hücre zarından olan difüzyon hızlarına göre sıralandığında, en hızlı difüzyona uğrayan ilk 2 tanesi hangisidir?\nI) Alkol\nII) Na⁺\nIII) CO₂\nIV) Glükoz\nV) Ca⁺⁺",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "IV ve V"], "C", 6)
add(72, "fizyoloji", "Aşağıdakilerden hangilerinin reseptörü hücre içindedir?\nI) Tiroid hormonları\nII) Asetilkolin\nIII) İnsülin hormonu\nIV) Steroid hormonlar",
    ["I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV"], "D", 6)
add(73, "fizyoloji", "Araşidonik asit üzerine etki yapan siklooksijenaz enzimleri aşağıdakilerden hangilerinin üretimini sağlarlar?\nI) Prostasiklin\nII) Tromboksan A₂\nIII) Lökotrienler\nIV) 5-Hidroksieykozatetraenoik asit",
    ["I ve II", "II ve III", "I ve III", "II ve IV", "III ve IV"], "A", 6)
add(74, "fizyoloji", "Atriyal natriüretik peptid (ANP) reseptörünün dahil olduğu reseptör grubu ve bu reseptörün aktivasyonunun oluşumunu sağladığı ikinci haberci aşağıdaki seçeneklerden hangisinde doğru olarak verilmiştir?",
    ["G proteinlerine eşlenik: cAMP", "G proteinlerine eşlenik: cGMP", "Katalitik: cAMP", "Katalitik: cGMP", "İyonotropik: IP₃"], "D", 6)

# ===== TIBBİ MİKROBİYOLOJİ (75-84) =====
add(75, "mikrobiyoloji", "Hangisi mikroorganizmaların fizyolojik gereksinimleri arasında yer almaz?",
    ["Oksijen", "pH", "Isı", "Tuz", "Karbondioksit"], "D", 6)
add(76, "mikrobiyoloji", "Ellerin dezenfeksiyonu ile anne ve bebek ölümlerinin düştüğünü bilimsel gözlemlere dayalı olarak ilk defa iddia eden Kadın Doğum uzmanının adını işaretleyiniz.",
    ["L. Pasteur", "J. Lister", "I. Semmelweis", "Ibn-i Sina", "R. Koch"], "C", 6)
add(77, "mikrobiyoloji", "Gram negatif bakterilerde hücre duvarı somatik antijeni hangisidir?",
    ["LPS", "Teikoik asit", "Lipoteikoik asit", "Omps", "Glycocalix"], "A", 6)
add(78, "mikrobiyoloji", "Bakterilerde hücre duvarı bölünmesi ve yeniden sentezinde görev alan enzimlerin genel ismi nedir?",
    ["Transpeptidaz", "Otolizinler", "β-laktamazlar", "Hyalorinidaz", "Lipaz"], "A", 7,
    note="Taranan sayfadaki basılı cevap A olarak görünüyor; hücre duvarı yeniden şekillenmesinde görev alan enzimler genel olarak otolizinlerdir (B). Kaynakla karşılaştırarak kontrol edin.",
    review="needs_review", conf=0.6)
add(79, "mikrobiyoloji", "Virüslerin yapısı ile ilgili hangisi yanlıştır?",
    ["Parvovirus en küçük DNA virüsüdür", "Segmentli DNA genomu henüz gösterilmemiştir.", "Rotavirus çift sarmallı DNA virüsüdür", "İnfluenza virus tek sarmallı segmentli RNA virüsüdür.", "Hepatit B virus kısmen çift sarmallı, sirküler DNA virüsüdür"], "C", 7)
add(80, "mikrobiyoloji", "Virüslerin replikasyonu ile ilgili yanlış hangisidir?",
    ["Zarfsız virüsler hücreyi lizise uğratarak hücreden çıkar", "Zarflı virüslerde viral bağlanma proteinleri glikoproteinlerdir", "Virüslerin hücrelere bağlanmasında ilk evrede elektrostatik kuvvetler rol oynar.", "Zarfsız virüsler füzyon mekanizması ile hücreye girer.", "Viral genomun replikasyonu kapsidin ayrılmasından sonra gerçekleşir."], "D", 7)
add(81, "mikrobiyoloji", "PCR (polimeraz zincir reaksiyonu) testi ile ilgili doğru hangisidir?",
    ["RNA amplifikasyon yöntemidir.", "PCR ürünleri elektroforezde anot tarafındaki kuyucuklara yüklenir.", "Denatürasyon 55°C'de gerçekleşir.", "Ekstensiyon'da primer genoma bağlanır.", "Taq polimeraz elongasyonda çalışır"], "E", 7)
add(82, "mikrobiyoloji", "Virüslerde kapsid ile ilgili yanlış olanı işaretleyiniz.",
    ["İkosahedral, helikal veya kompleks yapıda olabilir.", "Antijenik özellik gösterir.", "Virüsün hücreye adsorbsiyonunda rol oynar", "Kapsomer glikoprotein yapısındadır", "Nükleik asiti çevresel etkilerden korur"], "D", 7)
add(83, "mikrobiyoloji", "Virüslerin tanısında hangi testi uygularken hücre kültürü kullanılır?",
    ["Nötralizasyon", "Lateks agglütinasyon", "Line prop assay (LiPA)", "ELISA", "Western Blot"], "A", 7)
add(84, "mikrobiyoloji", "Mikroorganizmaları üretmek için kullanılan \"besiyerleri\" ile ilgili bilgilerden hangisi yanlıştır?",
    ["İnsan ve hayvanlarda çeşitli mikroorganizmalar hastalık oluştururlar. Bu mikroorganizmaların izolasyonu, tanımlanması ve üretilmesinde besiyerleri kullanılır.",
     "Agar, besiyeri hazırlanırken sıvı ortamları katılaştırmak amacı ile kullanılır.",
     "Agar, mikroorganizmaların büyük çoğunluğu tarafından ayrıştırılamaz, parçalanamaz.",
     "Bakteriler, Endo agar ve MacConkey agar besiyerindeki hemoliz durumlarına göre üçe ayrılırlar; alfa hemolitik, beta hemolitik, gamma hemolitik (non-hemolitik)",
     "Kanlı agar besiyeri, jeloz besiyeri ortamına %5-10 oranında kan ilavesi ile hazırlanır."], "D", 7)

# ===== DAVRANIŞ BİLİMLERİ (85-92) =====
add(85, "davranis-bilimleri", "Aşağıdakilerden hangisi davranışın düzenlenmesinde rol oynayan nörotransmitterlerden değildir?",
    ["Glutamat", "Oksitosin", "Serotonin", "Adrenalin", "Noradrenalin"], "B", 7)
add(86, "davranis-bilimleri", "Stresle başa çıkma mekanizmaları ile ilgili hangisi yanlıştır?",
    ["Gerçekçi olmayan hedeflerden uzak durulmalıdır.", "Düzenli olarak fiziksel egzersiz yapılmalıdır.", "Sebze ve meyvelerden zengin bir beslenme biçimi uygulanmalıdır.", "Stresi azaltmak için kafeinli içecekler tüketilmelidir.", "Yeterli ve dengeli uyunmalıdır."], "D", 7)
add(87, "davranis-bilimleri", "Hangisi stres için en uygun tanımdır?",
    ["Bir nesneye karşı duyulan özgül korku", "Kişinin zihninden atamadığı tekrarlayıcı düşünceler", "Başına kötü bir şey geleceğine yönelik sürekli bir beklenti hali", "İnsan ilişkilerindeki baskının sonucu hissedilen zorlanma durumu", "Ölüm ya da çıldırma düşünceleri"], "D", 7)
add(88, "davranis-bilimleri", "Aşağıdakilerden hangisi Freud'un \"Yapısal (Strüktürel)\" hipotezine göre Alt Benlik (Id) özelliklerinden değildir?",
    ["Kalıtımla geçen, doğuştan var olan, yerleşmiş bulunan her şey içerir", "Ruhsal aygıtın temel güç kaynağıdır", "Dış dünyayla bağlantısı yoktur", "Zaman ve yer kavramı tanımaz", "Korku ve utanç alt benlik gelişiminin öncüleridir"], "E", 7)
add(89, "davranis-bilimleri", "Hangisi Nevrotik (olgunlaşmamış) savunma düzenekleri arasında yer almaz?",
    ["Döndürme", "Karşıt tepki kurma", "Yansıtma", "Özdeşim", "Çözülme"], "C", 7)
add(90, "davranis-bilimleri", "Aşağıdaki cümlelerden hangisi \"Yalıtma\" savunma mekanizmasını en iyi şekilde açıklar?",
    ["Kişinin düşüncesinde yaptığı ya da yaptığını düşündüğü bir eylemi nötrleştirmek için, etkisizleştirmek için yaptığı eylemlerdir",
     "Gelişim sürecinde dürtülerin nesnelerini ya da amaçlarını değiştirip benlik için yapıcı, yaratıcı amaç ve nesne edinerek toplum tarafından beğenilen davranışlara döndürmesidir",
     "Yasak dürtü ve yaşantıların entelektüel yetiler ve bilgilerle açıklanmasıdır",
     "Bir anının bilişsel yanı tümü ile anımsanabilirken, duygusal yanının ayrılarak bastırılması ya da duyguların ilgisizmiş gibi görünen bir başka yaşantıya, başka nesneye aktarılmasıdır",
     "Zihindeki bir takım duygu ve düşünce kümelerinin bağlı oldukları yaşantılardan koparak özerkleşmeleri ve benliği etkilemeleri sürecidir"], "D", 7)
add(91, "davranis-bilimleri", "Biyolojik sistemler için von Bertalanfy ve Weiss tarafından geliştirilmiş olan \"Genel Sistemler Kuramına\" göre hangisi yanlıştır?",
    ["Daha basit ve küçük birimler daha karmaşık ve daha büyük birimlerle hiyerarşik bir düzen ve etkileşim içinde çalışırlar",
     "Her düzeydeki birim kendi içinde dinamik bir yapıdır, üst ya da alt birimlerden bağımsız olarak varlığını sürdürebilir.",
     "Üst sistemler alt sistemlerin basit bir toplamı değildir.",
     "Sistemler kendi aralarında süreklilik gösterirler.",
     "Her birim aynı zamanda hem bir bütün, hem de bir parçadır."], "B", 8)
add(92, "davranis-bilimleri", "Hangisi madde bağımlılarının ortak özelliklerinden değildir?",
    ["İstenen etkiyi sağlamak için belirgin olarak artmış miktarlarda madde kullanımının olması", "Maddenin çoğu kez tasarlandığından daha yüksek dozlarda ve daha uzun dönem süresince kullanılması.", "Maddeyi bırakmak ya da denetim altına almak için sürekli bir istek ve daha boşa çıkan çabaların bulunması.", "Bağımlılığa bağlı olarak toplumsal ve mesleki etkinliklerin bırakılması veya azaltılması.", "Fizik ya da psikolojik bir sorunun olduğunun farkında olmaması"], "E", 8)

# ===== AYRIMCILIK VE TOPLUMSAL CİNSİYET (93-98) =====
add(93, "ayrimcilik", "Bir bilimsel derleme veya poster sunumunda yer almayan ana başlık aşağıdakilerden hangisidir?",
    ["Giriş ve Amaç", "Yöntem", "Fotoğraflar", "Bulgular", "Kaynakça"], "C", 8)
add(94, "ayrimcilik", "Poster sunum için aşağıdaki ifadelerden hangisi yanlıştır?",
    ["Bilimsel toplantılarda asılan bildirilerdir.", "Posterler görsel bir iletişim aracıdır.", "İletmek istediğiniz düşünceyi etkili bir şekilde geniş kitlelere ulaştırabilen bilgi kaynağıdır.", "Çalışmalarınızın reklam niteliğinde hazırlanan afişlerdir", "Poster, bilimsel fikirlerin net ve kısa mesaj ile okuyucuya yansıtılmasıdır."], "D", 8)
add(95, "ayrimcilik", "Hangisi ayrımcılık kavramlarından biri değildir?",
    ["Önyargı", "Kalıpyargı", "Negatif Stereotipler", "Cinsiyetçilik", "Toplumsal olaylar"], "E", 8)
add(96, "ayrimcilik", "Aşağıdaki ifadelerden hangisi \"Ayrımcılık\" tanımı içinde yer almaz?",
    ["Sadece kendi grubunun avantajını düşünmek", "Diğer grubun dezavantajını görmezden gelen", "Diğer grubun dezavantajını pekiştiren", "Adil", "Diğerine acı verici bir tutum ve davranış"], "D", 8)
add(97, "ayrimcilik", "Hangi gruplar \"en az\" ayrımcılığa maruz kalan gruplardır?",
    ["Çoğunluğa sahip dini inanç veya mezhep grupları", "Farklı cinsel yönelime sahip olanlar", "Rehabilitasyon desteği alan engelliler", "Maddi destek alan göçmenler", "Örgütlü muhalifler"], "A", 8)
add(98, "ayrimcilik", "Sosyolojideki anlamı ile \"Önyargı\" kavramı için doğru ifade hangisidir?",
    ["Önyargı bir kolaylaştırıcı tutumdur", "Önyargı kötüdür", "Bir gruplar arası pozitif yönlendirmedir", "Bir gruplar içi olgu olarak negatif yönlendirmedir", "Gerçek deneyimlere dayalı genellemeye temellidir"], "B", 8)

# ===== TIPTA İNSAN BİLİMLERİ (99-100) =====
add(99, "tip-insan-bilimleri", "Aşağıdakilerden hangisi HIV gönüllü danışmanlık ve test merkezlerinin (GDTM) hizmetlerinden değildir?",
    ["HIV'e ilişkin danışmanlık hizmeti vermek", "Anonim ve ücretsiz HIV testi yapmak", "Test sonucu pozitif çıkan bireylere tedavi başlatmak", "Test sonucu pozitif çıkan bireyleri kesin tanı için hastaneye yönlendirmek", "HIV'le ilgili toplumsal farkındalık oluşturmak"], "C", 8)
add(100, "tip-insan-bilimleri", "Aşağıdakilerden hangisi HIV gönüllü danışmanlık ve test merkezlerinin (GDTM) kurulma gerekçelerinden biridir?",
    ["Toplumdaki LGBTI+ bireyleri tespit etmek", "Kamu otoritelerinin HIV pozitif bireylerle ilgili tedbirler almasını sağlamak", "HIV testi yaptırmak isteyenlerle ilgili istatistikleri topluma açıklamak", "HIV enfeksiyonuna dair toplumsal damgalama nedeniyle bireylerin HIV testi yaptırmaktan kaçınmasının önüne geçmek", "Toplumu HIV pozitif bireylerden korumak"], "D", 8)

# ===== ENTEGRE (101-108) =====
add(101, "entegre", "Hangisi madde bağımlıları için ilk kullanımdaki pekiştiriciler arasında sayılmaz?",
    ["Keyif verici etkisinin olması", "Anksiyolitik etkisinin olması", "Bırakılınca oluşan yan etkilerden kurtulma", "Analjezik etkisinin olması", "Öfori yapıcı etkisinin olması"], "C", 8)
add(102, "entegre", "Hangisi Opioid grubu maddeler içerisinde yer alır?",
    ["Esrar", "Eroin", "Extazy", "Kokain", "Tetrahidrokannabinol"], "B", 8)
add(103, "entegre", "Uyarıcı grubu madde bağımlılıklarında hangi nörotransmitter üzerinden psikoz gelişme riski vardır?",
    ["Seratonin", "GABA", "Dopamin", "Asetilkolin", "Glutamat"], "C", 8)
add(104, "entegre", "Madde bağımlılığında tanı koyulması için gereken asgari süre ölçütü aşağıdakilerden hangisidir?",
    ["1 ay", "3 ay", "6 ay", "12 ay", "24 ay"], "C", 9)
add(105, "entegre", "Aşağıdakilerden hangisi ilaçların yan etkilerini araştıran farmakolojinin dalıdır?",
    ["Farmakokinetik", "Farmakovijilans", "Farmakodinamik", "Farmakoekonomi", "Farmakogenetik"], "B", 9)
add(106, "entegre", "İlaçların ve madde bağımlılığında rol oynayan önemli farmakolojik mekanizma aşağıdakilerden hangisidir?",
    ["Kolinerjik", "Adrenerjik", "Histaminerjik", "Nitrik Oksit", "Dopaminerjik"], "E", 9)
add(107, "entegre", "Kuvvetli psişik bağımlılık yapan ilaç aşağıdakilerden hangisidir?",
    ["Nikotin", "Alkol", "Esrar", "Kokain", "Amfetamin"], "D", 9)
add(108, "entegre", "Güçlü fiziksel bağımlılık yapabilen ve ilacın kesilmesi bazen ölümle sonuçlanabilen yoksunluk sendromuna neden olan ilaç aşağıdakilerden hangisidir?",
    ["Morfin", "Metamfetamin", "Barbitürat", "Afyon", "Amfetamin"], "C", 9)

exam = {
    "id": EID,
    "label": "2022-2023 Dönem 1 TEM 2",
    "shortLabel": "2022-23",
    "year": "2022-2023",
    "period": 1,
    "term": "TEM 2",
    "date": "2023-06",
    "sourceFile": "WhatsApp Image 2026-11-16 at 22.59.36 (1).pdf (sayfa 9,10,11,17,13,14,15,16,18)",
    "sourcePages": list(range(1, 10)),
    "answerStatus": "official",
    "ocrQuality": "medium",
    "notes": "A kitapçığı; telefonla taranmış sayfalardan elle aktarılmıştır. Fotoğraf kalitesi nedeniyle bazı şıklar zor okunmuştur. Basılı cevap anahtarı kullanılmıştır; şüpheli yerler 'kontrol gerekli' olarak işaretlenmiştir.",
}
b.finish(exam, 108)
