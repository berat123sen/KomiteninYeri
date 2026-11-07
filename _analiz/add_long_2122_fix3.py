# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
10: "'Vaccination' kelime anlamı ineklemedir (Latince 'vacca' = inek). Jenner inek çiçek virusunu (cowpox) kullanarak çiçek hastalığını (smallpox) önleyen aşıyı geliştirmiştir (1796). Daha sonra 'vaccination' terimi genel anlamda aşılama için kullanılmaya başlanmıştır. 'Ariola' (A) çiçek hastalığı anlamına gelir; 'zayıflatılmış' (B) aşı türüdür; 'bağışıklama' (C) genel kavramdır; 'çiçek' (E) hastalığın adıdır.",
11: "Bakterilerde peptidoglikan sentezinde rol oynayan enzimler Penisilin Bağlayan Proteinler (PBP)'dir. PBP'ler transpeptidaz, karboksipeptidaz ve transglikozilaz aktivitesi gösterir. Penisilin ve diğer beta-laktam antibiyotikler PBP'leri inhibe ederek bakteri hücre duvarı sentezini bozar. Aminotransferazlar (B), glikosidazlar (C), beta-laktamazlar (D) ve peptidoglikan hidroksilazlar (E) bu işlevi görmez.",
12: "Gram (-) bakterilerde somatik antijen (O antijeni) LPS (lipopolisakkarit) yapısındadır. LPS dış membranın dış yaprağında bulunur ve endotoksin olarak adlandırılır. Teikoik asit (A) ve lipoteikoik asit (B) Gram (+) bakterilerde bulunur. OMP (D) ve glikokaliks proteinler (E) Gram (-)'de bulunur ama somatik antijen LPS'dir.",
24: "Yağlarla birlikte yağda eriyen vitaminler (A, D, E, K) emilir. Vitamin B12, C, folik asit, B6 suda eriyen vitaminlerdir ve yağ sindirimi ile birlikte emilmez. A, C, D, E seçenekleri yanlıştır.",
29: "Trigliserit sentezi yağ dokusunda gliserol-3-fosfattan (glikolizden) başlar, gliserolden değil. Yağ dokusunda gliserol kinaz enzimi yoktur; gliserol-3-fosfat glikolizden (DHAP'tan) elde edilir. Karaciğerde gliserol kinaz vardır ve gliserolden gliserol-3-fosfat sentezleyebilir.",
32: "Üre döngüsünde glutamat yer almaz; aspartat (amino grup verici), ornitin, arginin, sitrullin yer alır. Glutamat üre döngüsünde yer almaz (glutamat dehidrogenaz ile amonyak üretir ama döngüye girmez).",
35: "Dihidrobiyopterin redüktaz eksikliğinde fenilalanin hidroksilaz çalışamaz (BH4 kofaktörü gerekli); fenilalanin birikir. Fenilalanin hidroksilaz tirozin sentezi için BH4 gerektirir. Eksiklikte fenilalanin konsantrasyonu artar (fenilketonüri).",
40: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder (aerobik glikoliz). Yağ asidi/kolesterol, laktoz/seramid, üre/amonyak, aseton/resolvin kanser hücrelerinin birincil enerji kaynağı değildir.",
41: "Çizgili kasta acil enerji kaynağı kreatin fosfat (fosfokreatin) olup kreatinden sentezlenir. Kreatin kinaz ile ADP + kreatin fosfat → ATP + kreatin. Glukoz, glukoz-6-fosfat, kreatinin fosfat ve laktat acil enerji kaynağı değildir.",
43: "Safra asitleri FXR (farnesoid X reseptörü) üzerinden gen düzeyinde etki gösterir. FXR nükleer reseptördür; safra asidi metabolizması, lipid ve glukoz homeostazını düzenler. PY2, RXR, RAR, LXR farklı reseptörlerdir.",
46: "Düşük HDL-kolesterol Apo A-1 eksikliği ile ilişkilidir (Apo A-1 HDL'nin ana apoproteindir). Apo B-48 (şilomikron), Apo B-100 (VLDL/LDL), Apo (a) (Lp(a)), Apo E (remnant) HDL ile ilişkili değildir.",
47: "Fosfogliserat kinaz reaksiyonu substrat düzeyinde fosforilasyon yapar (1,3-BPG → 3-PG, ATP üretir). Heksokinaz, fosfofruktokinaz-1, gliseraldehid-3-fosfat dehidrogenaz, enolaz bu reaksiyonu yapmaz.",
52: "Koenzim Q (ubikinon) lipid yapıdadır, protein içermez; ETZ'de elektron taşıyıcıdır (kompleks I/II → III). NADH redüktaz, süksinat DH, sitokrom c, sitokrom aa3 protein içerir.",
54: "Glikojen sentezinde glikozil kalıntıları tirozin'e bağlanır (glikojenin). Asparajin, triptofan, glisin, alanin glikojen çekirdeği değildir.",
56: "Pirüvat kinaz reaksiyonu (PEP → pirüvat) substrat düzeyinde fosforilasyon örneğidir. Heksokinaz, fosfofruktokinaz-1, gliseraldehid-3-fosfat dehidrogenaz, enolaz bu reaksiyonu yapmaz.",
57: "Aldoz redüktaz glukozu sorbitole çevirir (poliol yolu); diyabetik katarakt patogenezinde rol oynar. Sorbitol dehidrogenaz, glukoz-6-fosfataz, epimeraz, enolaz bu dönüşümü yapmaz.",
59: "Glikoliz stoplazmadan ETZ'ye elektron (NADH) sağlar (malat-aspartat/gliserofofosfat şantı ile). Üre siklusu, pentoz fosfat yolu, heksozmonofosfat şantı, orotik asit siklusu elektron kaynağı değildir.",
60: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9 (negatif geri bildirim). -3, -6, -10, -11 yanlıştır.",
63: "Aktive edilmiş amino asit (aminoasil-tRNA) ATP harcayarak oluşur; AMP ve PPi açığa çıkar. GTP, GMP, GDP amino asit aktivasyonunda kullanılmaz.",
67: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi (metabolik enerji gerektirmez). Na+ ile ortaklaşa/karşıt taşıma, kanallardan iyon geçişi aktif/pasif olabilir.",
70: "Mikrotübüller hücre bölünmesi (mitoz mekiği) ve salgı veziküllerinin taşınmasında görevlidir. Sodyum taşıması, lizozomal hidrolazlar ve transkripsiyon mikrotübüllerle ilişkili değildir.",
76: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür. 28°C kaslar çalışmaz, 33°C vücut sıcaklık kontrolünü kaybeder, 37°C normal, 42°C MSS çöker.",
78: "Ekstra enerji = 300 kcal; yürüme gücü 250 W = 60 kcal/dk? Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır.",
80: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür.",
85: "V = E·d = 9×10⁶ V/m × 6×10⁻⁹ m = 54 mV. Hesap: 9×6 = 54, 10⁶×10⁻⁹ = 10⁻³, 54×10⁻³ V = 54 mV.",
90: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır. Bir nesneye karşı duyulan yoğun korku (fobi), tekrarlayıcı düşünceler (OKB), sürekli beklenti (anksiyete) ve ölüm düşünceleri (depresyon) stres tanımı değildir.",
100: "'Erkeklerin cerrahi branşlara alınmasına karşıyım' ifadesi açık (aşikar) cinsiyetçilik türüdür. Örtük cinsiyetçilik (örtülü), korumacı (paternalistik), modern (gizli), sembolik (kültürel) farklı türlerdir.",
104: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim, yansıtma diğer savunma düzenekleridir.",
106: "Farmakovijilans ilaç güvenliği (advers etki izlemi, ilaç güvenlilik izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
108: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Esrar, morfin, metamfetamin, MDMA yasadışı maddelerdir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
