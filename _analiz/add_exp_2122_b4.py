# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
86: "K+ için elektrokimyasal itici kuvvet = Em - Ek = -70 - (-90) = +20 mV; pozitif değer K+'u hücre dışına zorlar.",
87: "Dinlenim zar potansiyeli yalnızca Donnan denge potansiyeline eşit değildir; Na/K pompası da katkıda bulunur (B yanlıştır).",
88: "Noradrenalin (locus coeruleus) arousal, vijilans ve stres yanıtının düzenlenmesinde ana nörotransmitterdir.",
89: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir.",
90: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır.",
91: "Dissosiasyon: yoğun bunaltıyla karşılaşılan kişinin bunu bedeninde bir işlev bozukluğuna dönüştürmesidir.",
92: "Rasyonalizasyon (ussallaştırma) yasak dürtü ve yaşantıları entelektüel yetilerle açıklamadır; eğitim düzeyi yüksek kişilerde sık görülür.",
93: "Olgunlaşmamış (ilkel) savunma düzenekleri: yansıtma, içe atım, yadsıma, bölünme, somatizasyon. Düşünselleştirme olgun savunmadır.",
94: "Von Bertalanffy-Weiss sistemler kuramında alt sistemler dinamik ve bağımsız birimlerdir; üst sistemler alt sistemlerin basit toplamı değildir (B yanlıştır).",
95: "Bağımlılıkların ortak özellikleri: yoksunluk, işlevsellik bozukluğu, denetim çabaları, farkında olma. 'Bağımlılıklar düzelir ancak iyileşmez' ortak özellik değildir.",
96: "Madde bağımlılığında uzun süre kullanımda rol oynayan pekiştiriciler arasında genetik ve sosyoekonomik durum sayılmaz (negatif pekiştirme: yoksunluk belirtilerinden kurtulma).",
97: "Cinsel istismara uğramış çocuklarda fiziksel belirti mutlaka olmayabilir; zedelenmiş cinsellik, ihanet, çaresizlik ve damgalanma duyguları görülür.",
98: "Çocukları cinsel istismar ve ihmalinden korumada en etkili yöntem çocuğa cinsel eğitim verilmesidir.",
99: "Toplumsal cinsiyet stereotiplerine göre erkeklerden beklenen davranışlar: kendine güvenli, maceracı, lider.",
100: "'Erkeklerin cerrahi branşlara alınmasına karşıyım' ifadesi açık (aşikar) cinsiyetçilik türüdür.",
101: "Eroin opiyatlar (opioidler) grubunda yer alır.",
102: "Alışkanlıklar düzelir ve iyileşebilir; 'iyileşmez' ifadesi yanlıştır.",
103: "Bağımlılıklarda kişi fizik ya da psikolojik bir sorun olduğunu genellikle farkındadır; farkında olmama yanlıştır.",
104: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır.",
105: "İlaç kullanma amaçları: profilaksi, tedavi, teşhis, cerrahi girişimlerde; tanıtım ilaç kullanma amacı değildir.",
106: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir.",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur.",
108: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
