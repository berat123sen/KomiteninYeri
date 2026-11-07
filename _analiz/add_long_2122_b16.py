# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
100: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur. TCK 191: uyuşturucu madde kullanma ve bulundurma suçu. Uyuşturucu madde ticareti (TCK 188) daha ağır cezayı gerektirir. Kullanım suçu (TCK 191) tedavi ve denetimli serbestlik ile sonuçlanabilir.",
101: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Kafein (1,3,7-trimetilksantin) bir metilksantindir ve kahve, çay, enerji içeceklerinde bulunur. Esrar, morfin, metamfetamin, MDMA yasadışı maddelerdir. Kafein adenosin reseptörlerini bloke ederek uyanıklığı artırır.",
102: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir. Farmakovijilans WHO tarafından 'ilaçların advers etkilerinin ve diğer ilaçla ilgili problemlerin saptanması, değerlendirilmesi, anlaşılması ve önlenmesi' olarak tanımlanır. Farmakovijilans sistemi spontan bildirim, aktif gözetim ve risk yönetimi içerir.",
103: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim diğer savunma düzenekleridir. Yadsıma, tehdit edici gerçekleri bilinç dışına itme mekanizmasıdır. Bağımlı bireyler genellikle bağımlılıklarını inkar eder (yadsıma).",
104: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur. TCK 191: uyuşturucu madde kullanma ve bulundurma suçu.",
105: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Kafein (1,3,7-trimetilksantin) bir metilksantindir ve kahve, çay, enerji içeceklerinde bulunur.",
106: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur.",
108: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Kafein (1,3,7-trimetilksantin) bir metilksantindir ve kahve, çay, enerji içeceklerinde bulunur.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
