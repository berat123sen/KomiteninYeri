# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
21: "Üre döngüsünde glutamat yer almaz; aspartat, ornitin, arginin, sitrullin yer alır. Glutamat üre döngüsünde yer almaz (glutamat dehidrogenaz ile amonyak üretir ama döngüye girmez). Aspartat amino grubu verici olarak, ornitin taşıyıcı olarak, arginin üre üretimi için, sitrullin ara ürün olarak görev alır.",
23: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder (aerobik glikoliz). Yağ asidi/kolesterol (A), laktoz/seramid (C), üre/amonyak (D), aseton/resolvin (E) kanser hücrelerinin birincil enerji kaynağı değildir. Warburg etkisi: kanser hücreleri oksijen varlığında bile glikolizi tercih eder.",
25: "Trigliserit sentezi yağ dokusunda gliserol-3-fosfattan (glikolizden) başlar, gliserolden değil. Yağ dokusunda gliserol kinaz enzimi yoktur; gliserol-3-fosfat glikolizden (DHAP'tan) elde edilir. Karaciğerde gliserol kinaz vardır ve gliserolden gliserol-3-fosfat sentezleyebilir.",
30: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9 (negatif geri bildirim). -3, -6, -10, -11 yanlıştır. Negatif geri bildirim homeostazı korur; pozitif geri bildirim süreci amplifiye eder.",
31: "Üre döngüsünde glutamat yer almaz; aspartat (amino grup verici olarak), ornitin (taşıyıcı), arginin (üre üretimi), sitrullin (ara ürün) yer alır. Glutamat üre döngüsünde yer almaz (glutamat dehidrogenaz ile amonyak üretir ama döngüye girmez).",
36: "Dihidrobiyopterin redüktaz eksikliğinde fenilalanin hidroksilaz çalışamaz (BH4 kofaktörü gerekli); fenilalanin birikir. Fenilalanin hidroksilaz tirozin sentezi için BH4 gerektirir. Eksiklikte fenilalanin konsantrasyonu artar (fenilketonüri). BH4 eksikliği de fenilketonüriye yol açar.",
37: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder (aerobik glikoliz). Yağ asidi/kolesterol, laktoz/seramid, üre/amonyak, aseton/resolvin kanser hücrelerinin birincil enerji kaynağı değildir. Warburg etkisi: oksijen varlığında bile glikoliz tercih edilir.",
45: "Düşük HDL-kolesterol Apo A-1 eksikliği ile ilişkilidir (Apo A-1 HDL'nin ana apoproteindir). Apo B-48 (şilomikron), Apo B-100 (VLDL/LDL), Apo (a) (Lp(a)), Apo E (remnant) HDL ile ilişkili değildir. Apo A-1 LCAT aktivatörüdür.",
48: "Glikojen sentezinde glikozil kalıntıları tirozin'e bağlanır (glikojenin). Asparajin, triptofan, glisin, alanin glikojen çekirdeği değildir. Glikojen sentezi glikojenin (protein) + UDP-glukoz ile başlar.",
53: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder (aerobik glikoliz). Yağ asidi/kolesterol, laktoz/seramid, üre/amonyak, aseton/resolvin kanser hücrelerinin birincil enerji kaynağı değildir.",
60: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9 (negatif geri bildirim). -3, -6, -10, -11 yanlıştır. Negatif geri bildirim homeostazı korur.",
64: "Nernst denklemi: E = -60·log([iç]/[dış]) = -60·log(1000/1) = -180 mV. Pozitif iyonun iç konsantrasyonu dışından fazla olduğunda denge potansiyeli negatif olur.",
66: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi (metabolik enerji gerektirmez). Na+ ile ortaklaşa/karşıt taşıma, kanallardan iyon geçişi aktif/pasif olabilir.",
68: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz). Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur.",
74: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür. 28°C kaslar çalışmaz, 33°C vücut sıcaklık kontrolünü kaybeder, 37°C normal, 42°C MSS çöker.",
75: "Ekstra enerji = 300 kcal; yürüme gücü 250 W = 60 kcal/dk? Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır.",
78: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür.",
79: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
80: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
83: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz).",
85: "V = E·d = 9×10⁶ V/m × 6×10⁻⁹ m = 54 mV. Hesap: 9×6 = 54, 10⁶×10⁻⁹ = 10⁻³, 54×10⁻³ V = 54 mV.",
86: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür.",
88: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır. Bir nesneye karşı duyulan yoğun korku (fobi), tekrarlayıcı düşünceler (OKB), sürekli beklenti (anksiyete) ve ölüm düşünceleri (depresyon) stres tanımı değildir.",
89: "'Erkeklerin cerrahi branşlara alınmasına karşıyım' ifadesi açık (aşikar) cinsiyetçilik türüdür. Örtük cinsiyetçilik (örtülü), korumacı (paternalistik), modern (gizli), sembolik (kültürel) farklı türlerdir.",
90: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim, yansıtma diğer savunma düzenekleridir.",
91: "Farmakovijilans ilaç güvenliği (advers etki izlemi, ilaç güvenlilik izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
98: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Esrar, morfin, metamfetamin, MDMA yasadışı maddelerdir.",
99: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur.",
101: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir.",
103: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır.",
105: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde).",
108: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
