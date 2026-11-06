# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
31: "Metiltetrahidrofolat (metil-THF) homosistein→metionin dönüşümünde (metionin sentaz) metil verir; THF oluşur.",
32: "Üre döngüsünde glutamat yer almaz; aspartat, ornitin, arginin, sitrullin yer alır.",
33: "Glukoz-alanin döngüsü (Cahill döngüsü) kas amino gruplarını alanin ile karaciğere taşır; hepatik glukoneogeneze katkıda bulunur.",
34: "Homosistein artışı sistatyonin beta sentaz eksikliğinde (homosistinüri) görülür.",
35: "Dihidrobiyopterin redüktaz eksikliğinde fenilalanin hidroksilaz çalışamaz; fenilalanin birikir.",
36: "Arginaz sitozolik (karaciğer) enzimdir; glutamat dehidrogenaz, OTC, glutaminaz, CPS1 mitokondriyaldır.",
37: "İnsan kemioheterotroftur: organik bileşikleri (kemio-) enerji ve karbon kaynağı (heterotrof) olarak kullanır.",
38: "Pürin katabolizmasının son ürünü ürik asittir (insanda ürikaz yoktur).",
39: "ETZ'de elektron kaynağı olarak NADH (glikoliz/TCA'dan) kullanılır; NADPH pentoz fosfat yolundan gelir ve biyosentezde kullanılır.",
40: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder (aerobik glikoliz).",
41: "Çizgili kasta acil enerji kaynağı kreatin fosfat (fosfokreatin) olup kreatinden sentezlenir.",
42: "Prenilasyon Ras/Rho proteinlerinin membrana bağlanması için gereklidir; statinler prenilasyonu azaltır (artırmaz). A, B, C, E doğru ifadelerdir.",
43: "Safra asitleri FXR (farnesoid X reseptörü) üzerinden gen düzeyinde etki gösterir.",
44: "Tromboksan A2 (TXA2) trombosit agregasyonunu ve vazokonstriksiyonu tetikler.",
45: "Lipoprotein lipaz endotelde GPIHBP1 (GPI bağlantılı HDL-bağlı protein 1) ile tutunur ve aktive olur.",
46: "Düşük HDL-kolesterol Apo A-1 eksikliği ile ilişkilidir (Apo A-1 HDL'nin ana apoproteindir).",
47: "Fosfogliserat kinaz reaksiyonu substrat düzeyinde fosforilasyon yapar (1,3-BPG → 3-PG, ATP üretir).",
48: "Hipoglisemide glukokinaz inhibe olmalıdır (glukoz fosforilasyonu azalır); PFK-1 ve glukoz-6-fosfataz aktif olmalıdır.",
49: "Karbonhidrat, protein ve yağ metabolizmasının ortak ürünü Asetil-CoA'dır.",
50: "Glikojen fosforilaz glikojeni glikoz-1-fosfat'a çevirir (fosforoliz).",
51: "Eritrosit oksidatif direnci pentoz fosfat yoluna (NADPH üretimi) bağlıdır.",
52: "Koenzim Q (ubikinon) lipid yapıdadır, protein içermez; ETZ'de elektron taşıyıcıdır.",
53: "TCA döngüsünün allosterik kontrol enzimleri sitrat sentaz, izositrat dehidrogenaz ve α-ketoglutarat dehidrogenazdır.",
54: "Glikojen sentezinde glikozil kalıntıları tirozin'e bağlanır (glikojenin protein çekirdeği).",
55: "α-ketoglutarat dehidrogenaz pirüvat dehidrogenaza fonksiyonel olarak benzer (her ikisi de α-ketoasit dehidrogenaz kompleksidir).",
56: "Pirüvat kinaz reaksiyonu (PEP → pirüvat) substrat düzeyinde fosforilasyon örneğidir.",
57: "Aldoz redüktaz glukozu sorbitole çevirir (poliol yolu); diyabetik katarakt patogenezinde rol oynar.",
58: "Süksinat dehidrogenaz hem TCA döngüsü hem de ETZ (kompleks II) enzimidir.",
59: "Glikoliz stoplazmadan ETZ'ye elektron (NADH) sağlar (malat-aspartat/gliserofofosfat şantı ile).",
60: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9 (negatif geri bildirim).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
