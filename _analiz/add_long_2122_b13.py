# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
83: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır. Enerji = güç × zaman; zaman = enerji/güç. 300000 cal / 250 W = 1200 s? Hesap detayı: 300 kcal = 1255200 J; 250 W = 250 J/s; t = 5020 s ≈ 83 dk. Yaklaşık 80 dakika. Orta hızda yürüme ~4-5 kcal/dk harcar.",
85: "V = E·d = 9×10⁶ V/m × 6×10⁻⁹ m = 54 mV. Hesap: 9×6 = 54, 10⁶×10⁻⁹ = 10⁻³, 54×10⁻³ V = 54 mV. Hücre zarı potansiyeli tipik olarak -70 mV civarındadır. Hücresel zar potansiyeli tipik olarak -70 mV civarındadır.",
86: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür. 28°C kaslar çalışmaz, 33°C vücut sıcaklık kontrolünü kaybeder, 37°C normal, 42°C MSS çöker. Hipotermi sınıflandırması: hafif (32-35°C), orta (28-32°C), ağır (<28°C).",
87: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır. Enerji = güç × zaman; zaman = enerji/güç.",
91: "Farmakovijilans ilaç güvenliği (advers etki izlemi, ilaç güvenlilik izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir. Farmakovijilans WHO tarafından 'ilaçların advers etkilerinin ve diğer ilaçla ilgili problemlerin saptanması, değerlendirilmesi, anlaşılması ve önlenmesi' olarak tanımlanır.",
92: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim diğer savunma düzenekleridir. Yadsıma, tehdit edici gerçekleri bilinç dışına itme mekanizmasıdır.",
93: "Çocuğun kaza yoluyla yaralanması çocuk istismarı türü değildir (cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir). Kaza ile yaralanma istismar değildir. İstismar kasıtlı veya ihmalkar davranış sonucu oluşur.",
94: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
95: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Esrar, morfin, metamfetamin, MDMA yasadışı maddelerdir. Kafein (1,3,7-trimetilksantin) bir metilksantindir ve kahve, çay, enerji içeceklerinde bulunur.",
96: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur. TCK 191: uyuşturucu madde kullanma ve bulundurma suçu.",
97: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Kafein (1,3,7-trimetilksantin) bir metilksantindir.",
98: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
99: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim diğer savunma düzenekleridir.",
100: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur.",
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
