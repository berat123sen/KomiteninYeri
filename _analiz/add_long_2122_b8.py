# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
30: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9 (negatif geri bildirim). -3, -6, -10, -11 yanlıştır. Negatif geri bildirim homeostazı korur; pozitif geri bildirim süreci amplifiye eder. Geri bildirim kazancı (gain) = düzeltilen miktar / kalan miktar.",
47: "Fosfogliserat kinaz reaksiyonu substrat düzeyinde fosforilasyon yapar (1,3-BPG → 3-PG, ATP üretir). Heksokinaz, fosfofruktokinaz-1, gliseraldehid-3-fosfat dehidrogenaz, enolaz bu reaksiyonu yapmaz. Substrat düzeyinde fosforilasyon: ATP doğrudan substratın fosfat grubu transferi ile üretilir.",
49: "Karbonhidrat, protein ve yağ metabolizmasının ortak ürünü Asetil-CoA'dır (mitokondride). Yağ asitleri, glukoz, gliserol ve üre bu ortak ürün değildir. Asetil-CoA Krebs döngüsüne girer ve enerji (ATP) üretir. Asetil-CoA ayrıca ketogenez, kolesterol sentezi ve yağ asidi sentezi için öncü moleküldür.",
52: "Koenzim Q (ubikinon) lipid yapıdadır, protein içermez; ETZ'de elektron taşıyıcıdır (kompleks I/II → III). NADH redüktaz, süksinat DH, sitokrom c, sitokrom aa3 protein içerir. Koenzim Q mobil elektron taşıyıcıdır (membranda difüze olur).",
59: "Glikoliz stoplazmadan ETZ'ye elektron (NADH) sağlar (malat-aspartat/gliserofofosfat şantı ile). Üre siklusu, pentoz fosfat yolu, heksozmonofosfat şantı, orotik asit siklusu elektron kaynağı değildir. Glikoliz 2 NADH üretir (G3P DH reaksiyonunda).",
60: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9 (negatif geri bildirim). -3, -6, -10, -11 yanlıştır. Negatif geri bildirim homeostazı korur; pozitif geri bildirim süreci amplifiye eder.",
64: "Nernst denklemi: E = -60·log([iç]/[dış]) = -60·log(1000/1) = -180 mV. Pozitif iyonun iç konsantrasyonu dışından fazla olduğunda denge potansiyeli negatif olur. Nernst denklemi bir iyonun denge potansiyelini hesaplar.",
65: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz). Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur. τ = R×C; R ve C'nin çarpımıdır. Zar kapasitansı C = ε·A/d formülü ile hesaplanır.",
66: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi (metabolik enerji gerektirmez). Na+ ile ortaklaşa/karşıt taşıma, kanallardan iyon geçişi aktif/pasif olabilir. Basit difüzyon, kolaylaştırılmış difüzyon ve osmoz pasif taşıma mekanizmalarıdır.",
67: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür. 28°C kaslar çalışmaz, 33°C vücut sıcaklık kontrolünü kaybeder, 37°C normal, 42°C MSS çöker. Hipotermi sınıflandırması: hafif (32-35°C), orta (28-32°C), ağır (<28°C).",
68: "Ekstra enerji = 300 kcal; yürüme gücü 250 W = 60 kcal/dk? Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır. Enerji = güç × zaman; zaman = enerji/güç. 300000 cal / 250 W = 1200 s? Hesap detayı: 300 kcal = 1255200 J; 250 W = 250 J/s; t = 5020 s ≈ 83 dk. Yaklaşık 80 dakika.",
69: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür. Fosfolipitler amfipatik moleküllerdir; hidrofilik baş ve hidrofobik kuyruk. Çift tabaka oluşumu entropi artışı ile termodinamik olarak elverişlidir.",
70: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür.",
71: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür.",
72: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz). Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur. τ = R×C.",
73: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür. 28°C kaslar çalışmaz, 33°C vücut sıcaklık kontrolünü kaybeder, 37°C normal, 42°C MSS çöker.",
74: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır.",
76: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür.",
77: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır.",
78: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür.",
79: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
80: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
81: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz).",
82: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür.",
83: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika.",
84: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
85: "V = E·d = 9×10⁶ V/m × 6×10⁻⁹ m = 54 mV. Hesap: 9×6 = 54, 10⁶×10⁻⁹ = 10⁻³, 54×10⁻³ V = 54 mV.",
86: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür.",
87: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika.",
88: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır. Bir nesneye karşı duyulan yoğun korku (fobi), tekrarlayıcı düşünceler (OKB), sürekli beklenti (anksiyete) ve ölüm düşünceleri (depresyon) stres tanımı değildir.",
89: "'Erkeklerin cerrahi branşlara alınmasına karşıyım' ifadesi açık (aşikar) cinsiyetçilik türüdür. Örtük cinsiyetçilik (örtülü), korumacı (paternalistik), modern (gizli), sembolik (kültürel) farklı türlerdir.",
90: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim, yansıtma diğer savunma düzenekleridir.",
91: "Farmakovijilans ilaç güvenliği (advers etki izlemi, ilaç güvenlilik izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
92: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim diğer savunma düzenekleridir.",
93: "Çocuğun kaza yoluyla yaralanması çocuk istismarı türü değildir (cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir). Kaza ile yaralanma istismar değildir.",
94: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
95: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Esrar, morfin, metamfetamin, MDMA yasadışı maddelerdir.",
96: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur.",
97: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
98: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir.",
99: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır.",
100: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde).",
101: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
102: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir.",
103: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır.",
104: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde).",
105: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
106: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir.",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde).",
108: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
