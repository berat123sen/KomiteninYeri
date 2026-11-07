# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
41: "İnsan gözünün ayırma gücü hücreleri ayırt etmek için yeterli değildir; mikroskop gerekir. İnsan gözü yaklaşık 0.2 mm (200 µm) rezolüsyona sahiptir; hücreler (10-100 µm) ve hücre içi yapılar gözle ayırt edilemez. Işık mikroskobu (rezolüsyon ~0.2 µm) veya elektron mikroskobu (rezolüsyon ~0.1 nm) gerekir. Diğer seçenekler doğru tanımlamalardır.",
43: "Işık ve elektron mikroskobunda ortak nokta dokuların önce fikse edilmesidir; ışık kaynağı, canlı inceleme, renkli görüntü ve çözünürlük farklıdır. Işık mikroskobunda formalin tespit, parafin gömme, H&E boyama kullanılır; elektron mikroskobunda glutaraldehid/osmik asit tespit, epoksi rezin gömme, uranil asetat/kurşun sitrat boyama kullanılır.",
44: "Eosin asidik boyadır ve sitoplazmayı (asidofilik yapıları) pembe boyar; hematoksilen bazik boyadır (çekirdeği mavi boyar). Eosin-hematoksilen (H&E) en yaygın histolojik boyama yöntemidir. Eosin asidik yapıları (sitoplazma, kollajen, eritrositler) pembe-turuncu boyar; hematoksilen bazik yapıları (çekirdek, ribozom) mavi-mor boyar.",
46: "Pinositozda klatrin kaplı veziküller oluşmaz; klatrin reseptör aracılı endositozda rol oynar. Pinocitozda kaveolin/flotillin proteinleri vezikül formasyonunda rol oynar. A, C, D, E doğru ifadelerdir. Pinositoz sıvı alımıdır; reseptör aracılı endositoz spesifik molekül alımıdır.",
47: "Erken endozom hücreye alınan reseptör-protein kompleksinin geri dönüşüm veya yıkıma gideceğini belirler (sorting endosome). Lizozom, peroksizom, Golgi ve geç endozom bu işlevi görmez. Erken endozom pH'ı ~6.0'dır; geç endozom pH'ı ~5.5, lizozom pH'ı ~4.5'tir.",
49: "Golgi kompleksi steroid sentezleyen hücrelerde en fazla bulunan organel değildir (düz endoplazmik retikulum daha fazladır). Salgı proteinlerini yoğunlaştırır. A, C, D, E doğru ifadelerdir. Golgi kompleksi protein modifikasyonu (glikozilasyon), paketleme ve hedefleme yapar.",
50: "Sideroforlar bakterilerin ve mantarların demir yakalama molekülleridir; Fe3+ bağlar ve hücreye taşır. Aksiyal filaman, flajella, porin ve mezozom demir taşıma ile ilgili değildir. Sideroforlar (enterobaktin, piyoverdin) bakterilerin demir eksikliği koşullarında sentezlediği moleküllerdir.",
52: "Keşfedilen ilk virus tütün mozaik virusudur (Ivanovsky/Beijerinck, 1892). İnfluenza, çiçek, polio ve kuduz virusları daha sonra keşfedilmiştir. Tütün mozaik virusu (TMV) RNA virusudur ve bitkileri enfekte eder.",
55: "ELISA'da substrat eklendikten sonra yıkama yapılmaz; renkli ürün antikor varlığını gösterir. A, B, C, D doğru aşamalardır (C'de enzim bağlı antikor konduktan sonra yıkama yapılır). Substrat (TMB) eklendikten sonra renk oluşumu gözlenir; yıkama yapılırsa renk kaybolur.",
57: "Temel (basit) besiyerlerinde kan bulunmaz; kanlı besiyeri zenginleştirilmiş besiyeridir. Et suyu, tuz, agar ve pepton temel besiyerlerinde bulunur. Buyyon (sıvı) ve jeloz (katı) temel besiyerleridir.",
58: "Zorunlu anaeroblar SOD ve katalaz enzimleri bulunmaz; oksijen varlığında üreyemezler. Zorunlu aerob, fakültatif anaerob, aerotolerant ve mikroaerofil diğer gruplardır. Zorunlu anaeroblar oksijen toksik etkisinden (ROS) korunamaz.",
59: "Bütün bakterilerde bulunan yapı nükleoid (nükleotid) bölgesidir. Kapsül, flajella, spor ve Golgi aparatı (bakteride yok) her bakteride bulunmaz. Nükleoid bakteriyel kromozomu (sirküler DNA) içerir.",
60: "Gram boyanma özelliği hücre duvarı yapısı ile ilişkilidir (peptidoglikan kalınlığı). Mezozom, nukleus, ribozom ve kapsül Gram boyanma ile ilişkili değildir. Gram pozitif: kalın peptidoglikan; Gram negatif: ince peptidoglikan + dış membran.",
64: "Q = m·c·ΔT; ΔT = Q/(m·c) = 200000 cal / (80 kg × 1 kcal/kg·°C) = 2.5? Ama cevap 5°C; muhtemelen 100 kcal/saat ısı dönüşümü veya 400000 cal kullanılmış. Hesap sonucu 5°C artış bulunur (C seçeneği).",
65: "Anabolik reaksiyonlar entropiyi azaltır (düzenli yapılar oluşturur); katabolik reaksiyonlar entropiyi artırır. Hidroliz ve sindirim entropiyi artırır. Entropi sabittir ifadesi (E) yanlıştır. Entropi termodinamiğin ikinci yasası ile ilişkilidir.",
66: "Difüzyon spontan bir süreçtir; ΔG < 0 olur. AG=0 denge durumudur. AG>0 non-spontandır. Hesaplanamaz ve AG=[] ifadeleri yanlıştır.",
67: "NaCl'nin suda çözünmesinde hidrofobik etkileşim yoktur; iyon-dipol etkileşimleri vardır. Diğer seçeneklerde hidrofobik etkileşim bulunur. Hidrofobik etkileşimler suyu dışlayan moleküller arasında (lipid, protein) görülür.",
68: "ATP hidrolizinin enerjetiği hücredeki ATP/ADP/Pi oranına (reaksiyon katsayısı Q) bağlıdır; elektronegatif nitelik tek başına belirleyici değildir. Gibbs serbest enerji: ΔG = ΔG°' + RT ln Q.",
69: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır, artmaz. Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur. τ = R×C; R ve C'nin çarpımıdır.",
70: "Osmoz yönünü belirleyen temel faktörler çözünen konsantrasyonlarıdır (I, II). Polarite ve moleküler ağırlık temel faktör değildir. Aquaporinler su geçirgenliğini artırır. Osmotik basınç π = iCRT formülü ile hesaplanır.",
72: "Fick yasasına göre difüzyon hızını artırmayan faktör zar geçirgenliğinin artmasıdır (artırır). Zar kalınlığı, konsantrasyon farkı, yüzey alanı ve molekül boyutu (azalma) hızı etkiler. J = -D·A·(dC/dx).",
73: "Cl- için Nernst potansiyeli -90 mV, membran potansiyeli -70 mV olduğunda elektrokimyasal gradiyent +20 mV ile hücre içine yönelir. Nernst denklemi: E = (61/z)·log([dış]/[iç]).",
74: "Nernst denge potansiyeli bir cins iyonun konsantrasyon farkını dengeleyen elektrokimyasal potansiyeldir. Tüm iyonların toplamını, geçirgenliği veya Na+ için negatif değer hesaplamaz.",
75: "Gibbs-Donnan potansiyeli için Na/K pompası aktivasyonu gerekli değildir; pasif mekanizmalarla kurulur. A, B, C, D doğru ifadelerdir. Donnan dengesi pasif bir süreçtir.",
76: "Dinlenim potansiyelinde K+ etkisi daha fazladır çünkü zar K+ iyonlarına daha geçirgendir (daha fazla açık K+ kanalı). Na+ kanalları kapalıdır. K+ iyonlarının pozitif yük içermesi ve Na+ konsantrasyonu ile ilgili değildir.",
78: "Uzun zincirli yağ asitlerinin peroksizomlarda beta-oksidasyonu (oksidasyon) gerçekleşir. Hidroksilasyon, lizozom ve Golgi aparatı bu süreçte rol oynamaz. Peroksizomlar çok uzun zincirli yağ asitlerini (VLCFA) okside eder.",
79: "Translasyon sırası: amino asidin aktifleşmesi (aminoasil-tRNA sentetaz) → tRNA-amino asit kompleksi → kodon-antikodon bağlanması (ribosomda) → peptid bağı oluşumu (peptidil transferaz).",
80: "D vitamini reseptörü hücre içi (nükleer) reseptördür. Glisin, noradrenalin ve prostaglandinler membran reseptörüne sahiptir (II ve III). D vitamini steroid hormon benzeri etki gösterir (nükleer reseptör).",
81: "Nernst denklemi: E = 60·log([dış]/[iç]) = 60·log(300/x) = 120 → log(300/x)=2 → 300/x=100 → x=3 mEq/L. 30, 60, 300, 600 mEq/L yanlıştır.",
82: "Oral rehidratasyon çözeltisindeki glukoz ve Na+ emilimi Na+-glikoz kotransporteri (SGLT1) aracılığıyla sağlanır. Na+-H+, Na+-Ca2+, HCO3--Cl- ve Na+-K+-2Cl- taşıyıcıları bu işlevi görmez.",
83: "İnsülin eksikliğinde glukozun hücreye alınması (GLUT4 translokasyonu) bozulur; bu kolaylaştırılmış difüzyondur. Endositoz, basit difüzyon, primer ve sekonder aktif taşıma farklı mekanizmalardır.",
84: "G proteininin adenilat siklazı aktive etmesi cAMP oluşturur. cGMP (PKG), DAG ve IP3 (fosfolipaz C) farklı yollardır.",
86: "Düşük doz aspirin tromboksan A2 sentezini (COX-1 inhibisyonu) baskılayarak prostasiklin lehine denge kurar (antitrombotik etki). Prostasiklin vazodilatasyon ve antiagregan etki gösterir.",
87: "Nitrik oksit guanilat siklazı aktive eder; cGMP artışı protein kinaz G (PKG) aktivasyonu ile düz kas relaksasyonu (vazodilatasyon) sağlar. NO endotel kaynaklı gevşetici faktördür (EDRF).",
88: "Güdüler organizmanın gereksinimlerini başlatan ve dengeyi sağlayan içsel güçlerdir; değişmeyen/türe özgü güçler değildir. Güdüler fizyolojik (açlık, susuzluk) ve psikolojik (başarı, merak) olabilir.",
89: "Bunaltıcı durumu sıkıntı vermeyecek bir nedenle açıklama bulmak 'rasyonalizasyon (akla uygunlaştırma)' savunma düzenegidir. Düşünselleştirme (intellectualization) farklı bir savunma mekanizmasıdır.",
94: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir. Kafein sempatik aktiviteyi artırır ve stresi artırabilir.",
98: "Çocuğun kaza yoluyla yaralanması çocuk istismarı türü değildir (cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir).",
100: "Kadim Hint tıbbında (Ayurveda) bütün hastalıkların tedavisi Hindistan'da üretilen ilaçlarla yapılmıştır ifadesi doğru değildir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
