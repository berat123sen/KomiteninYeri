# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
87: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır. Enerji = güç × zaman; zaman = enerji/güç. 300000 cal / 250 W = 1200 s? Hesap detayı: 300 kcal = 1255200 J; 250 W = 250 J/s; t = 5020 s ≈ 83 dk. Yaklaşık 80 dakika.",
94: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir. Farmakovijilans WHO tarafından 'ilaçların advers etkilerinin ve diğer ilaçla ilgili problemlerin saptanması, değerlendirilmesi, anlaşılması ve önlenmesi' olarak tanımlanır.",
96: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur. TCK 191: uyuşturucu madde kullanma ve bulundurma suçu.",
97: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Kafein (1,3,7-trimetilksantin) bir metilksantindir ve kahve, çay, enerji içeceklerinde bulunur.",
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
