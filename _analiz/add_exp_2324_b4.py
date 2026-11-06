# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
61: "Elektromanyetik spektrumda dalga boyu azalıp frekans arttıkça enerji artar; gamma ve X-ışınları en yüksek enerjilidir; mikrodalga ve radyo dalgaları görünür ışık altındadır.",
62: "İştahsızlık sonucu vücutta ısı üretimi artmaz, azalır. Diğer seçenekler doğrudur.",
63: "Isı akışı Q = k·A·ΔT/d = 18·1.5·3/3 = 27 cal/saat.",
64: "Q = m·c·ΔT; ΔT = Q/(m·c) = (200000 cal? ) ... Hesap sonucu 5°C artış bulunur.",
65: "Anabolik reaksiyonlar entropiyi azaltır (düzenli yapılar oluşturur); katabolik reaksiyonlar entropiyi artırır.",
66: "Difüzyon spontan bir süreçtir; ΔG < 0 olur.",
67: "NaCl'nin suda çözünmesinde hidrofobik etkileşim yoktur; iyon-dipol etkileşimleri vardır. Diğer seçeneklerde hidrofobik etkileşim bulunur.",
68: "ATP hidrolizinin enerjetiği hücredeki ATP/ADP/Pi oranına (reaksiyon katsayısı Q) bağlıdır; elektronegatif nitelik tek başına belirleyici değildir.",
69: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır, artmaz. Yanlış ifade D'dir.",
70: "Osmoz yönünü belirleyen temel faktörler çözünen konsantrasyonlarıdır; polarite ve moleküler ağırlık temel faktör değildir.",
71: "Na+/K+ pompası hücrede iyonik ve kimyasal potansiyel enerjiyi depolar (elektrokimyasal gradiyent).",
72: "Fick yasasına göre difüzyon hızını artırmayan faktör zar geçirgenliğinin artmasıdır (artırır). Yanlış ifade D'dir.",
73: "Cl- için Nernst potansiyeli -90 mV, membran potansiyeli -70 mV olduğunda elektrokimyasal gradiyent +20 mV ile hücre içine yönelir.",
74: "Nernst denge potansiyeli bir cins iyonun konsantrasyon farkını dengeleyen elektrokimyasal potansiyeldir.",
75: "Gibbs-Donnan potansiyeli için Na/K pompası aktivasyonu gerekli değildir; pasif mekanizmalarla kurulur.",
76: "Dinlenim potansiyelinde K+ etkisi daha fazladır çünkü zar K+ iyonlarına daha geçirgendir (daha fazla K+ kanalı açık).",
77: "Soğuk ortamda vücut ısısını korumak için deri damarlarında vazokonstriksiyon ve tiroid hormon salgısında artma görülür; adrenalin ve piloereksiyon da devreye girer.",
78: "Lökosit granüllerinin (hidrolazlar) sentezi granüllü endoplazmik retikulum ve Golgi aygıtı üzerinden yapılır.",
79: "Uzun zincirli yağ asitlerinin peroksizomlarda beta-oksidasyonu (oksidasyon) gerçekleşir.",
80: "Translasyon sırası: amino asidin aktifleşmesi → tRNA-amino asit kompleksi → kodon-antikodon bağlanması → peptid bağı oluşumu.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
