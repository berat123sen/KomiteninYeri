# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
26: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi (metabolik enerji gerektirmez). Na+ ile ortaklaşa/karşıt taşıma, kanallardan iyon geçişi aktif/pasif olabilir. Basit difüzyon, kolaylaştırılmış difüzyon ve osmoz pasif taşıma mekanizmalarıdır.",
75: "Ekstra enerji = 300 kcal; yürüme gücü 250 W = 60 kcal/dk? Hesap sonucu 80 dakika. 100, 90, 60, 40 dakika yanlıştır. Enerji = güç × zaman; zaman = enerji/güç = 300000 cal / 250 W (60 kcal/dk) = 5 dk? Hesap detayı: 300 kcal = 1255200 J; 250 W = 250 J/s; t = 1255200/250 = 5020 s ≈ 83 dk. Yaklaşık 80 dakika.",
79: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür. Fosfolipitler amfipatik moleküllerdir; hidrofilik baş ve hidrofobik kuyruk.",
80: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez. Misel oluşumu deterjanlar ve safra tuzlarında görülür.",
83: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz). Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur.",
85: "V = E·d = 9×10⁶ V/m × 6×10⁻⁹ m = 54 mV. Hesap: 9×6 = 54, 10⁶×10⁻⁹ = 10⁻³, 54×10⁻³ V = 54 mV. Hücresel zar potansiyeli tipik olarak -70 mV civarındadır.",
86: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür. 28°C kaslar çalışmaz, 33°C vücut sıcaklık kontrolünü kaybeder, 37°C normal, 42°C MSS çöker.",
101: "Farmakovijilans ilaç güvenliği (advers etki izlemi, ilaç güvenlilik izlemi) ile ilgilidir. İlaç satışı, sektörü, deposu ve kutusu farmakovijilans ile ilgili değildir.",
103: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır. Yansıtma, akla uygunlaştırma, özdeşim, yansıtma diğer savunma düzenekleridir.",
105: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Esrar, morfin, metamfetamin, MDMA yasadışı maddelerdir.",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur.",
108: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
