# -*- coding: utf-8 -*-
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EXAM_ID = "2023-2024-tem-2"
SOURCE_PDF = "2023-2024-tem-2.pdf"

QS = []
def Q(num, disc_id, disc, stem, opts, ans, page, status="official", conf=0.97, note=None):
    QS.append({
        "id": f"{EXAM_ID}-q{num:03d}",
        "examId": EXAM_ID,
        "number": num,
        "disciplineId": disc_id,
        "discipline": disc,
        "type": "multiple_choice",
        "stem": stem,
        "options": opts,
        "correctAnswer": ans,
        "sourcePage": page,
        "answerStatus": status,
        "confidence": conf,
        "reviewStatus": "approved",
        "note": note,
    })
# --- Sayfa 1: TIBBI BIYOKIMYA Q1-14 ---
Q(1, "biyokimya", "Tıbbi Biyokimya", "Aşağıdakilerden hangisi Pentoz Fosfat yolunun görevlerindendir?", [
 "Glikoz metabolizmasında alternatif bir yolaktır",
 "Pentoz Fosfat yolunda ATP üretimi ve tüketimi görülür",
 "Nükleotid sentezi için Riboz-5-fosfat üretilir",
 "Sitozoldeki biyosentetik reaksiyonlar için NADPH üretilir",
 "3-7 karbonlu şekerlerin birbirine dönüşümünü ve glikolize bağlantısını sağlar",
], "B", 1)
Q(2, "biyokimya", "Tıbbi Biyokimya", "Pentoz fosfat yolunun inhibitörü aşağıdakilerden hangisidir?", [
 "NAD", "FAD", "Asetil KoA", "NADH", "NADPH",
], "E", 1)
Q(3, "biyokimya", "Tıbbi Biyokimya", "Karbonhidrat, protein ve yağların metabolizması sonucu oluşan ortak ürün hangisidir?", [
 "Yağ asitleri", "Glukoz", "Gliserol", "Asetil KoA", "Üre",
], "D", 1)
Q(4, "biyokimya", "Tıbbi Biyokimya", "Glukoz sorbitol yolunda aşağıdaki ürünlerden hangisine dönüşür?", [
 "Galaktoz", "Fruktoz", "Glukronat", "Askorbat", "Mannoz",
], "B", 1)
Q(5, "biyokimya", "Tıbbi Biyokimya", "Kan glukozu düşük bir kişide, aşağıdaki enzimlerden hangisinin karaciğerde inhibe olması gerekir?", [
 "Pirüvat karboksilaz", "PEP karboksikinaz", "Fruktoz-1,6-bifosfataz", "Glukoz-6-fosfataz", "Fosfofruktokinaz-1",
], "E", 1)
Q(6, "biyokimya", "Tıbbi Biyokimya", "ATP sentazın (kompleks V) sap kısmına (Fo) bağlanarak hidrojen kanalını kapatan ve ATP sentezini durduran inhibitör hangisidir?", [
 "Oligomisin", "Rotenon", "Amital", "Antimisin A", "Dimerkaprol",
], "A", 1)
Q(7, "biyokimya", "Tıbbi Biyokimya", "Glikojen sentezinde başlangıç glikozil kalıntıları, glikojenin proteininde aşağıdaki aminoasitlerden hangisine eklenir?", [
 "Asparajin", "Triptofan", "Glisin", "Tirozin", "Alanin",
], "D", 1)
Q(8, "biyokimya", "Tıbbi Biyokimya", "Glikojen yıkımından sonra kana aktif glukoz salınımını sağlayan enzim aşağıdakilerden hangisidir?", [
 "Dallandıran enzim", "Fosfoglikomutaz", "Dalları yıkan enzim", "Glikojen fosforilaz", "Glukoz-6-fosfataz",
], "E", 1)
Q(9, "biyokimya", "Tıbbi Biyokimya", "Glikoneogenez reaksiyonunda enerji nereden sağlanır?", [
 "GTP", "CTP", "ATP", "UTP", "TTP",
], "D", 1)
Q(10, "biyokimya", "Tıbbi Biyokimya", "Krebs döngüsü ile ilgili aşağıdakilerden hangisi doğrudur?", [
 "TCA döngüsünün başlaması için Asetil-CoA tek başına yeterlidir",
 "TCA'nın kontrol basamakları sitrat sentaz, izositrat dehidrogenaz ve malat dehidrogenazdır",
 "TCA döngüsünde substrat düzeyinde fosforilasyonun olduğu tek yer sitrat sentazdır",
 "TCA döngüsünde Pirüvat dehidrogenaz gibi komplekse sahip olan enzim α-ketoglutarat dehidrogenazdır",
 "TCA sitozolde gerçekleşir",
], "D", 1)
Q(11, "biyokimya", "Tıbbi Biyokimya", "Glikolizde gliseraldehit-3-fosfat dehidrogenaz reaksiyonuyla elde edilen hidrojen ve elektronlar, mitokondriye malat-aspartat şantı ile girerse solunum zincirine aşağıdakilerden hangisi üzerinden katılır?", [
 "Sitokrom b", "Sitokrom c oksidaz", "NADH dehidrogenaz", "Kompleks 3", "Süksinat koenzim Q redüktaz",
], "C", 1)
Q(12, "biyokimya", "Tıbbi Biyokimya", "Krebs siklusunda aşağıdakilerden hangisi gerçekleşmez?", [
 "Asetil KoA'nın oksidasyonu", "Alfa-ketoglutarat oluşumu", "CO2 oluşumu", "NADH ve FADH2 oluşumu", "Asetil KoA'nın pirüvata dönüşümü",
], "E", 1)
Q(13, "biyokimya", "Tıbbi Biyokimya", "Bir karaciğer dokusu homojenize edilip santrifüj edilerek tüm membran komponentleri ve organelleri ortamdan uzaklaştırılıp sadece sitoplazma bırakılıyor. Bu sıvıda yapılan enzim deneylerinde aşağıdaki enzimlerden hangisinin aktivitesi saptanır?", [
 "Asetil CoA Karboksilaz", "Pirüvat Karboksilaz", "Glutamat dehidrogenaz", "Ornitin Transkarbamoilaz", "Asil CoA Dehidrogenaz",
], "A", 1)
Q(14, "biyokimya", "Tıbbi Biyokimya", "Bir deneysel ortamda işaretli karbon atomları (C14) kullanılarak CO2 gazı işaretlenmiş ve deney hayvanlarına solutulmuştur. Aşağıdaki maddelerin hangisinde bu işaretli karbon (C14) tespit edilebilir?", [
 "Palmitik asit", "Malonil CoA", "Asetil CoA", "Tek karbon sayılı yağ asitleri", "Araşidonik asit",
], "B", 1)
# --- Sayfa 2: TIBBI BIYOKIMYA Q15-28 ---
Q(15, "biyokimya", "Tıbbi Biyokimya", "Prostaglandinlerin sentezinde aşağıdakilerden hangisi siklooksijenaz yolağı üzerinden sentezlenmez?", [
 "Prostasiklin", "Tromboksan", "Prostaglandin E2", "Lökotrien", "Prostaglandin H2",
], "D", 2)
Q(16, "biyokimya", "Tıbbi Biyokimya", "Karbon sayısı 17 olan bir yağ asidinin beta oksidasyona uğraması ile ilgili ifadelerden hangisi yanlıştır?", [
 "Tek karbonlu yağ asitlerinin beta oksidasyonu sonucunda glukoneojenik molekül oluşur",
 "Tek karbonlu yağ asitlerinin beta oksidasyonunda aynı kofaktörler kullanılır",
 "Son oksidasyondan sonra bir mol Asetil CoA ve bir mol Propiyonil CoA üretilir",
 "Karbon sayısı 16 olan bir yağ asidinin oksidasyonuna göre daha az Asetil CoA üretilir",
 "Tek karbonlu yağ asitlerinin beta oksidasyonu peroksizomlarda gerçekleşir",
], "E", 2)
Q(17, "biyokimya", "Tıbbi Biyokimya", "Yağ asitlerinin okside olmak üzere mitokondriye geçişinde rol oynayan 'Karnitin Palmitoil Transferaz I' enzimi aşağıdakilerden hangisi tarafından inhibe edilir?", [
 "Asetil CoA", "Sitrat", "Oksaloasetat", "Malonil CoA", "Palmitoil CoA",
], "D", 2)
Q(18, "biyokimya", "Tıbbi Biyokimya", "Yağların sindirimi sırasında 'Fosfatidil kolin' Fosfolipaz A2 ile karşılaştığında hangi molekül oluşur?", [
 "Fosfokolin", "Fosfatidik asit", "Lizolesitin", "Kolin", "Diasilgliserol",
], "C", 2)
Q(19, "biyokimya", "Tıbbi Biyokimya", "Bir çocukta yapılan ölçümlerde kandaki amonyak düzeyinin çok fazla yükseldiği gözlenmiştir. Bu çocukta hangi enzimin eksikliği bu tabloya yol açmaz?", [
 "N-asetilglutamat sentaz", "Glutamat dehidrogenaz", "Karbamoil fosfat sentetaz", "Argininosüksinat sentetaz", "Ornitin transkarbamoilaz",
], "B", 2)
Q(20, "biyokimya", "Tıbbi Biyokimya", "Aşağıdaki tepkimelerden hangisi 'metiltetrahidrofolat' kullanarak folat tuzağından kurtarır?", [
 "Norepinefrin-Epinefrin dönüşümü", "Homosistein-Sistatyonin dönüşümü", "Homosistein-Metionin dönüşümü", "Spermin-Spermidin dönüşümü", "Arginin-Ornitin dönüşümü",
], "C", 2)
Q(21, "biyokimya", "Tıbbi Biyokimya", "Triptofandan aşırı miktarlarda serotonin üretimi gerçekleştiği durumlarda hangi vitaminin eksikliği görülebilir?", [
 "Piridoksal fosfat", "Biotin", "B12", "Tiamin", "Niasin",
], "E", 2)
Q(22, "biyokimya", "Tıbbi Biyokimya", "Aşağıdaki tepkimelerin hangisinin sonucunda hidrojen peroksitler (H2O2) oluşur?", [
 "Aminoasit oksidaz", "Glutamat dehidrogenaz", "Transaminasyon", "Glutaminaz", "Glutamin sentetaz",
], "A", 2)
Q(23, "biyokimya", "Tıbbi Biyokimya", "Aşağıda verilen enzimlerden hangisinin eksikliği kanda ve idrarda fenilketon cisimciklerinin artmasına yol açar?", [
 "Katalaz", "Fenilalanin aminotransferaz", "Fenilalanin dekarboksilaz", "Fenilalanin oksidaz", "Dihidrobiyopterin redüktaz",
], "E", 2)
Q(24, "biyokimya", "Tıbbi Biyokimya", "Vücudumuzdaki basıncın ayarlanmasında ve pıhtılaşmada rol oynayan Nitrik Oksit (NO) aşağıdaki aminoasitlerin hangisinden sentezlenir?", [
 "Glutamik asit", "Glisin", "Tirozin", "Arginin", "Histidin",
], "D", 2)
Q(25, "biyokimya", "Tıbbi Biyokimya", "Tokluk durumunda (insülin/glukagon oranı arttığında) aşağıdakilerden hangisi yanlıştır?", [
 "Glikojen fosforilaz aktive olur", "Sitrat liyaz enzimi aktive olur", "Asetil CoA karboksilaz aktive olur", "Pirüvat dehidrogenaz aktive olur", "Glikokinaz aktive olur",
], "A", 2)
Q(26, "biyokimya", "Tıbbi Biyokimya", "Doktorunun önerdiği şekilde yağdan fakir diyet ile beslenen bir kadın, yağ alımını azaltıp karbonhidrat alımını artırarak aynı miktarda kalori almaktadır. Bu diyet sonucu kadının kan lipoproteinlerinden hangisinde bir düşme beklenir?", [
 "VLDL", "LDL", "Şilomikron", "HDL", "IDL",
], "C", 2)
Q(27, "biyokimya", "Tıbbi Biyokimya", "Akciğerlerde eksikliğinde solunum zorluğu, alveollerde kapanma ile seyreden respiratuvar distres sendromuna neden olan surfaktan yapısında aşağıdaki lipitlerden hangisi bulunur?", [
 "Fosfatidilinozitol", "Fosfatidiletanolamin", "Glikosfingolipid", "Fosfatidilkolin", "Sfingomiyelin",
], "D", 2)
Q(28, "biyokimya", "Tıbbi Biyokimya", "Kalp damar hastalıkları riski oluşturan hiperkolesterolemiyi düzenlemek için kullanılan ilaçlar plazma kolesterol düzeylerini düşürmede hangi mekanizma üzerinden etkilerini gösterirler?", [
 "Kolesterolün ince bağırsaktan emilimini inhibe ederler",
 "Kolesterolü safra asidine dönüştürerek atılımını artırırlar",
 "Mevalonat yıkımını artırırlar",
 "Karaciğerde LDL reseptörünü uyarırlar",
 "Kolesterol sentezinde HMG-KoA redüktazı inhibe ederler",
], "E", 2)
# --- Sayfa 3: TIBBI BIYOKIMYA Q29-40 ---
Q(29, "biyokimya", "Tıbbi Biyokimya", "Metabolizmada kolesterolün hücre içi düzenlenmesinde aşağıdakilerden hangisi etkilidir?", [
 "Esterifikasyon", "Hücredeki Apo C-II ekspresyonu", "LDL reseptörü ile hücreye alım", "HMG-KoA redüktaz transkripsiyonunun düzenlenmesi", "Kolesterolün Apo A-I aracılı HDL üzerine aktarımı",
], "B", 3)
Q(30, "biyokimya", "Tıbbi Biyokimya", "Plazmadaki derişimleri ateroskleroz ve koroner kalp hastalığı insidansı ile en çok ilişkili olan lipid ikilisi hangi seçenekte doğru verilmiştir?", [
 "LDL-Şilomikron", "HDL-IDL", "LDL-HDL", "VLDL-LDL", "Şilomikron-VLDL",
], "C", 3)
Q(31, "biyokimya", "Tıbbi Biyokimya", "Karaciğerde HMG-KoA redüktaz enzim aktivitesinin düzenlenmesinde etkisi olmayan seçenek hangisidir?", [
 "Diyetle alınan lipid", "SREB proteini", "İnsülin", "Glukagon", "Kinaz enzimleri",
], "A", 3)
Q(32, "biyokimya", "Tıbbi Biyokimya", "Aşağıdakilerden hangisinin sentezinde kolesterol başlangıç maddesi olarak görev alır?", [
 "Progesteron", "Kortizol", "Safra tuzu", "Aldosteron", "Vitamin C",
], "E", 3)
Q(33, "biyokimya", "Tıbbi Biyokimya", "Sodyum-potasyum pompası hangi taşıma sistemine girer?", [
 "Aktif transport", "Basit difüzyon", "Kolaylaştırılmış difüzyon", "Osmotik transport", "İyonik transport",
], "A", 3)
Q(34, "biyokimya", "Tıbbi Biyokimya", "Aşağıdaki proteinlerden hangisi, bir çözücüde aktif olarak hücreye taşımak için sodyum elektrokimyasal gradiyentini kullanır?", [
 "Kalsiyum-ATPaz", "GLUT2", "SGLT1", "Na-K ATPaz", "Na-Ca değiş-tokuş",
], "C", 3)
Q(35, "biyokimya", "Tıbbi Biyokimya", "Aşağıdakilerden hangisi kas ve karaciğer dokuları arasındaki glikojen yıkımı/glukoz alımı metabolik yolunu açıklar?", [
 "Glukoneogenezis", "Glikojenez", "Glikojenoliz", "Cori Döngüsü", "Miyoinositol Döngüsü",
], "D", 3)
Q(36, "biyokimya", "Tıbbi Biyokimya", "Aşağıdakilerden hangisi mitokondride pirüvatın dekarboksilasyonu ile asetil-koenzim A oluşumunu katalizleyen ve tiamin pirofosfat, niasin ve pantotenik asit gibi kofaktörlerin kullanıldığı enzimdir?", [
 "Hekzokinaz", "Pirüvat Dehidrogenaz", "Alfa-keto glutarat dehidrogenaz", "Pirüvat karboksilaz", "Asetil-CoA karboksilaz",
], "B", 3)
Q(37, "biyokimya", "Tıbbi Biyokimya", "Aşağıdaki eser elementlerden hangisi hemoglobin ve sitokromların yapısında bulunur ve eksikliği eritrositlerin hacminin normalden daha düşük olması ile kendini gösteren ve en yaygın anemi türü olan mikrositer anemiye yol açar?", [
 "Fe (Demir)", "Mn (Mangan)", "Zn (Çinko)", "Cr (Krom)", "Co (Kobalt)",
], "A", 3)
Q(38, "biyokimya", "Tıbbi Biyokimya", "Aşağıdaki eser elementlerden hangisinin tiroid fonksiyonları açısından önemli görevleri vardır?", [
 "Mo (Molibden)", "Mn (Mangan)", "Zn (Çinko)", "Cr (Krom)", "Se (Selenyum)",
], "E", 3)
Q(39, "biyokimya", "Tıbbi Biyokimya", "Aşağıdakilerden hangisi mortalitesi en yüksek (insanları en fazla öldüren) hastalıklar grubunda olan ve beslenme ile ilişkisi bilimsel olarak kanıtlanmış hastalıklardandır? I. Kardiyovasküler Hastalıklar II. Diabetes Mellitus III. Kronik Obstrüktif Akciğer Hastalıkları", [
 "Yalnız I", "Yalnız II", "I ve III", "II ve III", "I, II ve III",
], "C", 3)
Q(40, "histoloji", "Histoloji ve Embriyoloji", "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.", [
 "Histoloji terimi, doku anlamına gelen histos ve bilim/çalışma anlamına gelen logia kelimelerinin birleşmesiyle oluşmuştur.",
 "Histoloji insanın çıplak gözle görülebilen vücut kısımlarını inceleyen bilim alanıdır.",
 "Normal yapı ve gelişim yanında, hücre ve doku hasarının mikroskobik düzeyde araştırılması, kök hücre biyolojisi, rejeneratif tıp araştırmaları ile in vitro fertilizasyon da Histoloji ve Embriyolojinin çalışma alanları içerisinde yer alır.",
 "Embriyoloji fertilizasyondan doğuma kadar insanın normal gelişimini inceleyen bilim alanıdır.",
 "İnsan vücudunu oluşturan esas yapısal bileşenler; hücreler, hücrelerarası maddeler ve vücut sıvılarıdır.",
], "B", 3)
# --- Sayfa 4: HISTOLOJI Q41-49 + MIKROBIYOLOJI Q50-52 ---
Q(41, "histoloji", "Histoloji ve Embriyoloji", "Aşağıda verilen tanımlamalardan yanlış olanı işaretleyiniz.", [
 "Histoloji ve Embriyoloji bilim alanının gelişiminde; hücrenin tanımlanması, hücre teorisinin ortaya konulması ve elektron mikroskobunun keşfi çok önemli aşamalardır.",
 "Bilim alanının gelişim sürecinde; Robert Hooke ilk defa hücreyi tanımlarken, hücrelerde bir çekirdeğin varlığı Robert Brown tarafından keşfedilmiştir.",
 "Mikroskobik incelemelerde en önemli olan iki faktör, büyütme ve ayırma gücüdür.",
 "İnsan gözünün ayırma gücü, hücrelerin ayırt edilmesi için yeterlidir.",
 "Canlıların temel yapısal biriminin hücre olduğu gerçeği hücre teorisi ile ortaya konulmuştur.",
], "D", 4)
Q(42, "histoloji", "Histoloji ve Embriyoloji", "Işık mikroskobik incelemeler için dokunun anestezi altındaki canlıdan alınmasından sonra formalin solüsyonu içerisinde koyulmasındaki amaç aşağıdakilerden hangisidir?", [
 "Yıkama", "Şeffaflandırma", "Dehidratasyon", "Otolitik ve bakteriyolitik reaksiyonların önlenmesi", "Gömme",
], "D", 4)
Q(43, "histoloji", "Histoloji ve Embriyoloji", "Hangisi ışık mikroskobik ve elektron mikroskobik inceleme yöntemleri arasındaki benzerliklerden birisidir?", [
 "İkisinde de gözle görülebilen ışık kaynağı kullanılır.", "İkisinde de dokuları canlı olarak incelemek mümkündür.", "İkisinde de inceleme için alınan dokular önce fikse (tespit) edilir.", "Her iki yöntemde de renkli görüntü elde edebiliriz.", "Mikroskopların büyütme ve çözümlleme güçleri yakın değerlerdedir.",
], "C", 4)
Q(44, "histoloji", "Histoloji ve Embriyoloji", "Aşağıdakilerden hangisi sitoplazmayı boyayan asidik boyadır?", [
 "Eosin", "Toluidin mavisi", "Hematoksilen", "Carmine", "Ksilol",
], "A", 4)
Q(45, "histoloji", "Histoloji ve Embriyoloji", "Peroksizomlarla ilgili olarak verilen seçeneklerden hangisi yanlıştır?", [
 "Bol miktarda hidrolitik enzimler içeren membransız organellerdir", "İçeriklerinde katalaz enzimi sayesinde toksik olan hidrojen peroksiti yıkarak hücreyi korurlar", "Karaciğer ve böbrek hücrelerinde gelişmiş olup bol miktarda bulunurlar", "Yağ asitlerinin beta-oksidasyonunda ve toksik moleküllerin detoksifikasyonunda rol oynarlar", "Sinir sisteminde aksonların etrafındaki miyelin kılıfın lipid komponentinin sentezinde görev alırlar",
], "A", 4)
Q(46, "histoloji", "Histoloji ve Embriyoloji", "Hücrede veziküler transportla ilgili olarak verilen seçeneklerden hangisi yanlıştır?", [
 "Maddelerin hücre içine girdiği veziküler transport süreci endositoz, maddelerin hücreyi terkettiği süreç ise ekzositoz olarak adlandırılır", "Sıvı maddelerin ve 150 nm'den küçük çaplı moleküllerin hücre içerisine alındığı pinositoz sürecinde klatrin kaplı veziküller oluşur", "Reseptör aracılı endositozda hücreye alınacak uygun moleküllerin seçiminde adaptin molekülleri görev alır ve klatrinle kaplı vezikül oluşumu gerçekleşir", "Ekzositozun konstitütif yolunda salgı ürünü hücrede depolanmadan transport vezikülleri içinde direk olarak plazma membranına iletilerek hücreyi terkeder", "Ekzositozun düzenlenen salgı yolunda salgı ürünü veziküller içinde geçici olarak depolanır ve nöral ya da hormonal uyarıyla birlikte plazma membranına iletilerek hücreden dışarıya verilir",
], "B", 4)
Q(47, "histoloji", "Histoloji ve Embriyoloji", "Hücrede plazma membranına yakın (periferde) yer alan, hücreye alınan reseptör-protein kompleksinin geri dönüşüme ya da yıkıma gideceğini belirleyen yapı hangisidir?", [
 "Lizozom", "Peroksizom", "Golgi Kompleksi", "Erken endozom", "Geç endozom",
], "D", 4)
Q(48, "histoloji", "Histoloji ve Embriyoloji", "Hücreler arası bağlantıların ve mikrovillusların yapısına katılan, hücre hareketi ve bölünmesinde önemli rollere sahip membransız hücre iskeleti elemanı aşağıdakilerden hangisidir?", [
 "Mikrotübüller", "Ara filamanlar", "Sentrioller", "Aktin filamanları", "Serbest ribozomlar",
], "D", 4)
Q(49, "histoloji", "Histoloji ve Embriyoloji", "Golgi kompleksi ile ilgili yanlış seçeneği işaretleyiniz.", [
 "Membranla çevrili sisterna veya keselerden oluşur.", "Steroid sentezleyen hücrelerde en fazla bulunan organeldir.", "Salgı proteinlerinin yoğunlaştırılmasından sorumludur.", "Cis, trans ve medial golgi ağından oluşur.", "Koatomer molekülleri golgi ve endoplazmik retikulum arasında iki yönlü transportu sağlar.",
], "B", 4)
Q(50, "mikrobiyoloji", "Mikrobiyoloji", "Aşağıdakilerden hangisi bakterilerin ve mantarların metabolizmalarında gereksinim duydukları demiri karşılamak için dış ortamdan demir yakalayarak hücre içerisine taşıyan demiri bağlayıcı (Fe3+) küçük moleküllerdir?", [
 "Siderofor", "Aksiyal filaman", "Flajella", "Porin", "Mezozom",
], "A", 4)
Q(51, "mikrobiyoloji", "Mikrobiyoloji", "Hastalıklarda mikrop teorisini kanıtlayan ve Kuduz aşısını geliştiren hangi bilim adamıdır?", [
 "Antonie van Leeuwenhoek", "Robert Koch", "Louis Pasteur", "Alexander Fleming", "Joseph Lister",
], "C", 4)
Q(52, "mikrobiyoloji", "Mikrobiyoloji", "Keşfedilen ilk virus hangisidir?", [
 "İnfluenza (grip) virusu", "Tütün mozaik virusu", "Çiçek (variola) virusu", "Çocuk felci (polio) virusu", "Kuduz (rabies) virusu",
], "B", 4)
# --- Sayfa 5: MIKROBIYOLOJI Q53-60 + BIYOFIZIK Q61-66 ---
Q(53, "mikrobiyoloji", "Mikrobiyoloji", "Virusların genomu ile ilgili aşağıdakilerden hangisi doğrudur?", [
 "Rotavirus dışındaki RNA virusları çift sarmallıdır", "Direkt mRNA görevi gören RNA negatif polaritelidir", "DNA virusları lineer, segmentli ya da sirküler olabilir", "Parvovirus tek sarmallı DNA virusudur", "İnfluenza virus tek sarmallı segmentsiz RNA genomuna sahiptir",
], "D", 5)
Q(54, "mikrobiyoloji", "Mikrobiyoloji", "Virusların replikasyonu ile ilgili yanlış hangisidir?", [
 "Viral bağlanma proteinleri zarfsız viruslarda kapsid proteinleridir", "Zarfsız viruslar hücrelerin lizisi sonucu dışarı çıkarlar", "Zarflı virusların penetrasyonu endositozis veya füzyon ile olur", "Zarfsız virusların çoğu viropeksis ile hücreye girer", "Endositozis nötral pH'da gerçekleşir",
], "E", 5)
Q(55, "mikrobiyoloji", "Mikrobiyoloji", "Serumda bir virusa karşı antikor aranmasında ELISA testinde hangi aşama yanlıştır?", [
 "Mikroplaktaki kuyular virus antijeni ile kaplıdır", "Hasta serumu ilave edilir. Sonra yıkama yapılır", "Enzim bağlı antiviral antikor konur. Sonra yıkama yapılır", "Substrat eklendikten sonra yıkama yapılmaz", "Renkli ürün elde edilen kuyular antikor varlığını gösterir",
], "C", 5)
Q(56, "mikrobiyoloji", "Mikrobiyoloji", "Polimeraz zincir reaksiyonu (PCR) ile ilgili yanlış hangisidir?", [
 "Denaturasyon 94°C'de yapılır", "Annealing'de 55°C'de Taq polimeraz aktivite yapar", "Primer hedef bölgenin 3' ucuna bağlanır", "Elongasyon 72°C'de gerçekleşir", "dNTP'ler ekstensiyonda DNA zincirinin yapısına girer",
], "B", 5)
Q(57, "mikrobiyoloji", "Mikrobiyoloji", "Temel (basit) besiyerlerinde (buyyon/jeloz) hangisi asla bulunmaz?", [
 "Et suyu", "Kan", "Tuz", "Agar", "Pepton",
], "B", 5)
Q(58, "mikrobiyoloji", "Mikrobiyoloji", "Oksijen varlığında üreyemeyen ve 'süperoksit dismutaz (SOD) ve katalaz enzimi' bulunmayan bakteri grubu hangisidir?", [
 "Zorunlu aerob", "Fakültatif anaerob", "Aerotolerant", "Zorunlu anaerob", "Mikroaerofil",
], "D", 5)
Q(59, "mikrobiyoloji", "Mikrobiyoloji", "Bütün bakterilerde bulunan yapı hangisidir?", [
 "Kapsül", "Flajella", "Nukleus (Nukleotid)", "Golgi aparatı", "Spor",
], "C", 5)
Q(60, "mikrobiyoloji", "Mikrobiyoloji", "Gram boyanma özelliği, bakterinin hangi yapısı ile ilişkilidir?", [
 "Mezozom", "Nukleus", "Ribozom", "Kapsül", "Hücre duvarı",
], "E", 5)
Q(61, "biyofizik", "Biyofizik", "Elektromanyetik spektrum için aşağıda verilen ifadelerden hangileri doğrudur? I) Dalga boyu azalıp, frekans arttıkça enerji artar. II) Dalga boyu artıp, frekans azaldıkça enerji artar. III) Gamma ve X-ışınlarının enerjisi en yüksektir. IV) Yüksek enerjili ışınlar atom ve hücre çekirdeği düzeyinde etkili olurlar. V) Mikrodalga ve radyo dalgalarının enerjisi görünür ışın altındadır.", [
 "I, II, IV", "I, III, V", "I, III, IV", "I, II, IV, V", "I, II, V",
], "B", 5)
Q(62, "biyofizik", "Biyofizik", "Aşağıdaki vücut sıcaklığı ile ilgili verilen bilgilerden hangisi yanlıştır?", [
 "Deri damarlarında vazokonstriksiyon vücutta ısı kaybını azaltır", "Piloereksiyon vücutta ısı kaybını azaltır", "Solunumun hızlanması durumunda vücutta ısı kaybı artar", "İştahsızlık sonucu vücutta ısı üretimi artar", "TSH salgılanmasında azalma vücutta ısı üretimini azaltır",
], "D", 5)
Q(63, "biyofizik", "Biyofizik", "Vücudun içi ve dışı arasındaki dokunun kalınlığı 3 cm, iletkenliği 18 cal.cm/m.saat.°C, alan 1.5 m2, vücut içi ile dışı arasındaki sıcaklık farkı 3°C ise ısı akışı ne kadardır?", [
 "81 cal/saat", "27 cal/saat", "13,5 cal/saat", "54 cal/saat", "18 cal/saat",
], "B", 5)
Q(64, "biyofizik", "Biyofizik", "80 kg'lık bir insan orta derecede 260 kcal/saat enerji harcar. Bunun 200 kcal/saat kısmı ısıya dönüşür. Bu ısı vücuttan atılmazsa vücut sıcaklığı kaç derece artar? (1 cal=4 J, Cp=2000 J/kg°C)", [
 "3", "4", "5", "8", "13",
], "C", 5)
Q(65, "biyofizik", "Biyofizik", "Aşağıdaki reaksiyon türlerinden hangisi hücre içinde entropiyi azaltır?", [
 "Hidroliz", "Sindirim", "Katabolik reaksiyonlar", "Anabolik reaksiyonlar", "Entropi sabittir",
], "D", 5)
Q(66, "biyofizik", "Biyofizik", "Sabit sıcaklık ve basınç altındaki bir sistemde gerçekleşen bir difüzyon sürecinin Gibbs-Serbest enerjisi (AG) aşağıdakilerden hangisidir?", [
 "AG<0", "AG=0", "Hesaplanamaz", "AG>0", "AG=[]",
], "A", 5)
# --- Sayfa 6: BIYOFIZIK Q67-78 ---
Q(67, "biyofizik", "Biyofizik", "Aşağıdakilerden hangisinde hidrofobik etkileşimler bulunmaz?", [
 "Zar lipid çift tabaka oluşumunda", "Misel oluşumunda", "Proteinlerin kendilerine özgü 3 boyutlu yapılarında", "NaCl'nin suda çözünmesinde", "DNA çift sarmal yapının stabil olmasında",
], "D", 6)
Q(68, "biyofizik", "Biyofizik", "ATP hidrolizi ile enerji salınımı, hücrede içe dönüşür. Buna göre canlı bir hücrede ATP hidrolizinin enerjetiği hangisi belirler?", [
 "ATP'nin elektronegatif niteliği", "Sıcaklık farkı", "Hidrofobik etkileşimler", "Yakınsız moleküller", "Hücre zarı",
], "A", 6)
Q(69, "biyofizik", "Biyofizik", "Hücre zarının elektriksel özellikleri ile ilgili hangi ifade yanlıştır?", [
 "Zaman sabiti (τ=RC), zarın yük depolama (kapasitans) ve zar direnci üzerinden yük aktarma yeteneğini gösterir", "Zarın yüksek kapasitansı vardır", "Zar kapasitansı yüzey alanının büyüklüğü ile doğru orantılıdır", "Zar kapasitansı küçüldükçe hücre zarı zaman sabiti artar", "Zaman sabiti nöronun iletim hızının hesaplanmasında kullanılır",
], "D", 6)
Q(70, "biyofizik", "Biyofizik", "Hücre zarında gerçekleşen osmozun hareket yönünün belirlenmesinde, aşağıdakilerden hangileri temel faktörlerden değildir? I: Hücre içinde çözünen maddelerin konsantrasyonu. II: Hücre dışında çözünen maddelerin konsantrasyonu. III: Çözünenlerin polaritesi. IV: Çözünenlerin moleküler ağırlığı. V: Aquaporinlerin varlığı", [
 "I, II, IV", "I, II, V", "I, II, IV, V", "II, III, IV", "IV, V",
], "A", 6)
Q(71, "biyofizik", "Biyofizik", "Sinir hücresinde yer alan Na+/K+ pompası zar boyunca 3 Na+/2 K+ değişimi yapar. Bu pompasal temel görevi aşağıdakilerden hangisidir?", [
 "Donnan denge kurmak", "Hücre içi Na konsantrasyonunu arttırmak", "Hücre içi K konsantrasyonunu arttırmak", "Sistolik durumuna getirmek", "Hücrede iyonik ve kimyasal potansiyel enerjiyi depolamak",
], "E", 6)
Q(72, "biyofizik", "Biyofizik", "Fick difüzyon yasasına göre, aşağıdakilerden hangisi zar boyunca geçebilecek bir maddenin difüzyon hızını arttırmaz?", [
 "Zar kalınlığının azalması", "Maddenin konsantrasyon farkının artması", "Zar yüzey alanının büyümesi", "Zar geçirgenliğinin artması", "Maddenin boyutunun azalması",
], "D", 6)
Q(73, "biyofizik", "Biyofizik", "Membran potansiyeli -70 mV olan dinlenim durumunda bir hücrede, Cl- için Nernst denge potansiyeli -90 mV'tur. Cl- un zardan pasif geçişi hangi yöne ve ne kadarlık elektrokimyasal potansiyel farkla olur?", [
 "-160 mV, hücre dışına", "-90 mV, hücre dışına", "0 mV, dengededir", "+20 mV, hücre içine", "+70 mV, hücre içine",
], "D", 6)
Q(74, "biyofizik", "Biyofizik", "Bir sinir hücresi membranının her iki tarafında yer alan iyonların Nernst-Denge potansiyelleri ile ilgili hangisi doğrudur?", [
 "Tüm iyonların Nernst potansiyelleri kullanılarak zar potansiyeli hesaplanır", "Hücre içi ve dışı arasındaki bütün iyonların toplam konsantrasyonunu gösterir", "Bir cins iyon için iyonun konsantrasyon farkını dengeleyen elektrokimyasal potansiyeldir", "Nernst-Denge potansiyelleri ile hücre zarının iyon geçirgenliği hesaplanır", "Na+ iyonu için hücre dışı konsantrasyonunun hücre içi konsantrasyona oranının logaritması alındığında değer negatif bulunur",
], "C", 6)
Q(75, "biyofizik", "Biyofizik", "Aşağıdakilerden hangisi Gibbs-Donnan potansiyelinin özelliği değildir?", [
 "Yalnızca pasif mekanizmalarla bir zarın iki tarafı arasında kurulan potansiyel farktır", "Zarı geçemeyen anyonlar, zarı geçebilen iyonların yeni bir dağılıma uğramasına neden olur", "Gibbs-Donnan potansiyeli bir denge durumudur", "Gibbs-Donnan dengesinin kurulması, osmoz nedeniyle hücrelerin şişmesine neden olur", "Gibbs-Donnan potansiyeli için Na/K pompası aktivasyonu gereklidir",
], "E", 6)
Q(76, "biyofizik", "Biyofizik", "Aşağıdakilerden hangisi hücrenin dinlenim membran potansiyel değerine potasyumun (K+) etkisinin daha fazla olmasının açıklar?", [
 "Zarda az sayıda K+ iyon kanallarının kapalı halde durması", "Zarın geçirgenliğinin K+ iyonlarına daha fazla olması", "K+ iyonlarının pozitif yük içermesi", "Na+ seçici kanalların fazla sayıda olması", "Na+ konsantrasyonunun hücre dışında az olması",
], "B", 6)
Q(77, "fizyoloji", "Fizyoloji", "Vücut dış ortam sıcaklığı 0°C olduğu durumda, sağlıklı bir insanda vücut sıcaklığının düzenlenmesi için merkez efektör organlar üzerindeki etkilerle aşağıdaki olayların başlangıcına yol açar?", [
 "Deri damarlarında vazokonstriksiyon", "Tiroid hormon salgısında artma", "Adrenalin salgısının artması", "Derideki kılların deri yüzeyine yapışması",
], "A", 6)
Q(78, "fizyoloji", "Fizyoloji", "Lökositlerdeki hidrolazların sentezi sırasında kullanılan başlıca organeller aşağıdakilerden hangisinde başlıca olarak verilmiştir?", [
 "Düz endoplazmik retikulum-Golgi aygıtı", "Granüllü endoplazmik retikulum-Golgi aygıtı", "Düz endoplazmik retikulum-Peroksizom", "Sitozoldeki serbest ribozomlar-Salgı granülü", "Peroksizom",
], "A", 6)
# --- Sayfa 7: FIZYOLOJI Q79-87 + DAVRANIS Q88-89 ---
Q(79, "fizyoloji", "Fizyoloji", "Uzun zincirli yağ asitlerinin metabolizması sırasında, yağ asitlerinde gelişen kimyasal olay ile bu olayın gerçekleştiği organel aşağıdakilerden hangisinde doğru olarak verilmiştir?", [
 "Hidroksilasyon-Lizozom", "Oksidasyon-Lizozom", "Hidroksilasyon-Peroksizom", "Oksidasyon-Peroksizom", "Glikozillenme-Golgi aygıtı",
], "D", 7)
Q(80, "fizyoloji", "Fizyoloji", "Translasyon sürecinde gelişen aşağıdaki olayların zamansal olarak oluş sırası seçeneklerin hangisinde doğru olarak verilmiştir? I) Kodonun antikodon ile bağlanması, II) Amino asidin aktifleşmesi, III) Peptid bağının oluşumu, IV) tRNA-amino asit kompleksinin oluşması", [
 "I, II, III, IV", "II, IV, I, III", "III, IV, I, II", "IV, II, I, III", "II, I, II, IV",
], "B", 7)
Q(81, "fizyoloji", "Fizyoloji", "Aşağıdakilerden hangilerinin reseptörü hücre zarında bulunur? I) D vitamini, II) Glisin, III) Noradrenalin, IV) Prostaglandinler", [
 "I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV",
], "B", 7)
Q(82, "fizyoloji", "Fizyoloji", "Hücre zarının Na+'a geçirgen ve diğer tüm iyonlara geçirimsiz olması durumunda, Na+'un hücre zarından olan net difüzyon hızı 0 mEq/dakika, hücre dışındaki Na konsantrasyonu 300 mEq/L ve hücre içinin hücre dışına göre elektriksel potansiyel farkı +120 mV ise, Na'un hücre içindeki konsantrasyonunun kaç mEq/L olması gerekir (Nernst denklemindeki katsayı=60 olarak alınınız)?", [
 "3", "30", "60", "300", "600",
], "A", 7)
Q(83, "fizyoloji", "Fizyoloji", "Koleralı hastalara verilen oral rehidratasyon tozu çözeltisindeki solütlerin barsaklardan emilimi aşağıdakilerden hangisi aracılığıyla sağlanır?", [
 "Na+-H+ taşıyıcısı", "Na+-Glikoz taşıyıcısı", "Na+-Ca2+ taşıyıcısı", "HCO3--Cl- taşıyıcısı", "Na+-K+-2Cl- taşıyıcısı",
], "B", 7)
Q(84, "fizyoloji", "Fizyoloji", "İnsülin eksikliğinin olduğu diabetes mellituslu bir hastadaki ana sorun glukozun hücre zarından olan taşıma mekanizmalarından birindeki yetersizliktir. Bu taşıma mekanizması aşağıdakilerden hangisi ile adlandırılır?", [
 "Endositoz", "Basit difüzyon", "Primer aktif taşıma", "Sekonder aktif taşıma", "Kolaylaştırılmış difüzyon",
], "E", 7)
Q(85, "fizyoloji", "Fizyoloji", "Aktif hale gelen heterotrimerik G proteininin adenilat siklazı aktifleştirmesi sonucunda aşağıdakilerden hangilerinin oluşumuna yol açar? I) cAMP, II) cGMP, III) Diasilgliserol, IV) IP3", [
 "I ve II", "II ve III", "I ve III", "III ve IV", "II ve IV",
], "D", 7)
Q(86, "fizyoloji", "Fizyoloji", "Düşük doz aspirinin antitrombotik etki oluşturmasının ana nedeni aşağıdakilerden hangisinde verilmiştir?", [
 "Tromboksan A2-Prostasiklin dengesini tromboksan lehine bozması", "Tromboksan A2-Prostasiklin dengesini prostasiklin lehine bozması", "Lökotrien-Prostaglandin dengesini prostaglandin lehine bozması", "Lökotrien-Prostaglandin dengesini lökotrien lehine bozması", "Plazminojenin etkinliğini artırması",
], "B", 7)
Q(87, "fizyoloji", "Fizyoloji", "Nitrik oksitin aktive ettiği sıklık guanilat siklaz enzimi aşağıdakilerden hangi düz kasında etkili olur?", [
 "Proteinkinaz A", "Proteinkinaz C", "Proteinkinaz G", "Tirozinkinaz", "Fosfolipaz A2",
], "C", 7)
Q(88, "davranis-bilimleri", "Davranış Bilimleri", "Aşağıdakilerden hangisi güdüler için doğrudur?", [
 "Güdü ve dürtü benzer kavramlardır", "Bir eksiklik ile dengesi bozulan organizmada itici güçtür", "Değişmeyen ve türe özgü güçlerdir", "Organizmanın uyarılmış bir durumudur", "Organizmadaki gereksinimleri başlatan güçlerdir",
], "C", 7)
Q(89, "davranis-bilimleri", "Davranış Bilimleri", "Benlik için bunaltıcı görünen ama sıkıntı vermeyecek bir neden açıklama bulmak ne tür bir benlik savunma düzenektir?", [
 "Karşıt tepki kurma", "Düşünselleştirme", "Yalıtma", "Akla uygunlaştırma", "Yüceleştirme",
], "D", 7)
# --- Sayfa 8: DAVRANIS Q90-96 + AYRIMCILIK Q97-99 + TIP TARİHİ Q100 + ENTEGRE Q101-102 ---
Q(90, "davranis-bilimleri", "Davranış Bilimleri", "Günlük yaşamda dil sürçmeleri, kasıtsız unutkanlıklar, ertelemeler, dalgınlıklar ne tür benlik savunma düzenegine örnektir?", [
 "Yadsıma", "Yansıtma", "Çözülme", "Karşıt tepki kurma", "Bastırma",
], "E", 8)
Q(91, "davranis-bilimleri", "Davranış Bilimleri", "Alkol bağımlılığı tanısı konulabilmesi için, yeterli tanısal ölçütlerin ne kadar süredir kişi tarafından karşılanıyor olması gereklidir?", [
 "1 ay", "3 ay", "6 ay", "12 ay", "24 ay",
], "D", 8)
Q(92, "davranis-bilimleri", "Davranış Bilimleri", "Hangi ifade biyopsikososyal model için doğru değildir?", [
 "Hastalıkların çoğu sadece biyolojik etkenler tarafından belirlenir, ancak psikolojik ve sosyal olaylar hastalıkların gidişatı üzerinde etkilidir",
 "İnsana sadece biyolojik açıdan bakmak, toplumsal ve psikolojik yönünü ele almamak büyük bir eksikliktir",
 "Bütün ruhsal bozukluklarda olayların nedenlerine, belirtilerine, biçimlerine, gidiş, sonlanış ve tedavisine çok boyutlu, çok etkenli bir bakış açısı yaratmak zorunludur",
 "İnsan normal ve anormal davranışlarıyla biyopsikososyal bir varlıktır",
 "Bu model insanın tüm yönleriyle değerlendirilmesine imkan sağlamaktadır",
], "A", 8)
Q(93, "davranis-bilimleri", "Davranış Bilimleri", "Nörotransmitterler ile ilgili aşağıdakilerden hangisi ya da hangileri doğrudur? I. Nöronda sentez edilir. II. Dopamin ve serotonin nörotransmitter örnekleridir. III. Postsinaptik uçtan sinaps aralığına salınır. IV. Davranışın düzenlenmesinde rol alırlar.", [
 "I ve II", "II ve III", "I ve III", "I ve IV", "II ve IV",
], "B", 8)
Q(94, "davranis-bilimleri", "Davranış Bilimleri", "Stresle başa çıkma mekanizmaları ile ilgili hangisi yanlıştır?", [
 "Düzenli olarak fiziksel egzersiz yapılmalıdır", "Sebze ve meyvelerden zengin bir beslenme biçimi uygulanmalıdır", "Stresi azaltmak için kafeinli içecekler tüketilmelidir", "Yeterli ve dengeli uyunmalıdır", "Gerçekçi olmayan hedeflerden uzak durulmalıdır",
], "D", 8)
Q(95, "davranis-bilimleri", "Davranış Bilimleri", "Hangisi stres için en uygun tanımdır?", [
 "Bir nesneye karşı duyulan yoğun korku", "Kişinin zihninden atamadığı tekrarlayıcı düşünceler", "Başına kötü bir şey geleceğine yönelik sürekli bir beklenti hali", "İnsan ilişkilerindeki baskının sonucu hissedilen zorlanma durumu", "Ölüm ya da öldürme düşünceleri",
], "D", 8)
Q(96, "davranis-bilimleri", "Davranış Bilimleri", "Hangisi ayrımcılık kavramlarından biri değildir?", [
 "Toplumsal yargılar", "Önyargı", "Kalıpyargı", "Negatif stereotipler", "Cinsiyetçilik",
], "A", 8)
Q(97, "davranis-bilimleri", "Davranış Bilimleri", "Aşağıdaki ifadelerden hangisi 'Ayrımcılık' tanımı içinde yer almaz?", [
 "Sadece kendi grubunun avantajını düşünen", "Diğer grubun dezavantajını görmezden gelen", "Diğer grubun dezavantajını pekiştiren", "Diğerine acı verici bir tutum ve davranış sergileyen", "Adil davranan",
], "D", 8)
Q(98, "davranis-bilimleri", "Davranış Bilimleri", "Aşağıdakilerden hangisi çocuk istismarı türlerinden değildir?", [
 "Cinsel istismar", "Fiziksel istismar", "Duygusal istismar", "İhmal", "Çocuğun kaza yoluyla yaralanması",
], "E", 8)
Q(99, "davranis-bilimleri", "Davranış Bilimleri", "Çocuklar yaşadıkları ihmal ve istismarı söylememelerinin nedenleri ile ilgili aşağıdakilerden hangisi doğrudur?", [
 "Kendilerine inanılmayacağını düşünürler", "Başlarının belaya gireceğinden istismarcının tehditlerinden korkarlar", "Ailenin parçalanacağını düşünürler", "Nasıl anlatacaklarını bilemeyebilirler", "Tümü",
], "D", 8)
Q(100, "tip-tarihi-etik", "Tıp Tarihi ve Etik", "Kadim Hint tıbbı konusunda aşağıdakilerden hangisi doğru değildir?", [
 "Bütün hastalıkların tedavisi Hindistan'da üretilen ilaçlarla yapılmıştır", "'Samhita' tıp kitabı anlamına gelmektedir", "Cerrahi uygulamalarda başarı belirli düzeydedir", "Sağlık ve sağlık koruma 'Ayurveda' olarak adlandırılmaktadır", "Zihin ve beden sağlığını korumak 'yoga'dır",
], "A", 8)
Q(101, "entegre", "Entegre Oturum", "Hangisi alkol ve madde bağımlılıkları için tanısal ölçütler arasında yer almaz?", [
 "Tolerans", "Alkol ve maddenin yarattığı bedensel sorunların farkında olmama", "Bırakınca yoksunluk belirtilerinin olması", "Bırakmak için boşa giden çabalar", "Sosyal ve mesleki işlevsellikte bozulma",
], "B", 8)
Q(102, "entegre", "Entegre Oturum", "Hangisi madde bağımlılığında ilk kullanımdaki pekiştiriciler arasında sayılmaz?", [
 "Keyif verici etkisinin olması", "Anksiyolitik etkisinin olması", "Bırakınca oluşan yan etkilerden kurtulma", "Analjezik etkisinin olması", "Öfori yapıcı etkisinin olması",
], "B", 8)

# --- Cikti ---
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(base)
out_dir = os.path.join(root, "sinav-platformu", "public", "data", "exams")
os.makedirs(out_dir, exist_ok=True)

exam = {
    "exam": {
        "id": EXAM_ID,
        "label": "2023-2024 Dönem 1 TEM 2",
        "shortLabel": "2023-24",
        "year": "2023-2024",
        "period": 1,
        "term": "TEM 2",
        "questionCount": len(QS),
        "answerStatus": "official",
        "sourcePdf": f"/kaynak/{SOURCE_PDF}",
        "disciplines": [],
    },
    "questions": QS,
}

# discipline summary
from collections import OrderedDict
disc = OrderedDict()
for q in QS:
    d = disc.setdefault(q["disciplineId"], {"id": q["disciplineId"], "name": q["discipline"], "questionCount": 0, "first": q["number"], "last": q["number"]})
    d["questionCount"] += 1
    d["first"] = min(d["first"], q["number"])
    d["last"] = max(d["last"], q["number"])
exam["exam"]["disciplines"] = list(disc.values())

out_path = os.path.join(out_dir, f"{EXAM_ID}.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(exam, f, ensure_ascii=False, indent=2)
print("Yazildi:", out_path, "soru:", len(QS))

# index.json guncelle
index_path = os.path.join(root, "sinav-platformu", "public", "data", "index.json")
with open(index_path, "r", encoding="utf-8") as f:
    idx = json.load(f)
ids = [e["id"] for e in idx["exams"]]
if EXAM_ID not in ids:
    idx["exams"].insert(0, {
        "id": EXAM_ID,
        "label": exam["exam"]["label"],
        "shortLabel": exam["exam"]["shortLabel"],
        "year": exam["exam"]["year"],
        "period": exam["exam"]["period"],
        "term": exam["exam"]["term"],
        "questionCount": exam["exam"]["questionCount"],
        "answerStatus": exam["exam"]["answerStatus"],
        "disciplines": exam["exam"]["disciplines"],
    })
with open(index_path, "w", encoding="utf-8") as f:
    json.dump(idx, f, ensure_ascii=False, indent=2)
print("index.json guncellendi")
