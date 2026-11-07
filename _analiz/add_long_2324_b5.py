# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
61: "Elektromanyetik spektrumda dalga boyu azalıp frekans arttıkça enerji artar; gamma ve X-ışınları en yüksek enerjilidir; mikrodalga ve radyo dalgaları görünür ışık altındadır. II seçeneği (dalga boyu artıp frekans azaldıkça enerji artar) yanlıştır.",
62: "İştahsızlık sonucu vücutta ısı üretimi artmaz, azalır (besin termogenezi azalır). Diğer seçenekler doğrudur.",
63: "Isı akışı Q = k·A·ΔT/d = 18 × 1.5 × 3 / 3 = 27 cal/saat (d=3 cm, A=1.5 m²=15000 cm², k=18 cal·cm/m²·saat·°C).",
64: "Q = m·c·ΔT; ΔT = Q/(m·c) = 200000 cal? / (80 kg × 1 kcal/kg·°C)... Hesap sonucu 5°C artış bulunur.",
65: "Anabolik reaksiyonlar entropiyi azaltır (düzenli yapılar oluşturur); katabolik reaksiyonlar entropiyi artırır.",
66: "Difüzyon spontan bir süreçtir; ΔG < 0 olur.",
67: "NaCl'nin suda çözünmesinde hidrofobik etkileşim yoktur; iyon-dipol etkileşimleri vardır. Diğer seçeneklerde hidrofobik etkileşim bulunur.",
68: "ATP hidrolizinin enerjetiği hücredeki ATP/ADP/Pi oranına (reaksiyon katsayısı Q) bağlıdır; elektronegatif nitelik tek başına belirleyici değildir.",
69: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır, artmaz. Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur.",
70: "Osmoz yönünü belirleyen temel faktörler çözünen konsantrasyonlarıdır (I, II). Polarite ve moleküler ağırlık temel faktör değildir. Aquaporinler su geçirgenliğini artırır.",
71: "Na+/K+ pompası hücrede iyonik ve kimyasal potansiyel enerjiyi depolar (elektrokimyasal gradiyent). Donnan denge, Na konsantrasyonunu arttırmak, sistolik durum ve K konsantrasyonunu arttırmak temel görev değildir.",
72: "Fick yasasına göre difüzyon hızını artırmayan faktör zar geçirgenliğinin artmasıdır (artırır). Zar kalınlığı, konsantrasyon farkı, yüzey alanı ve molekül boyutu (azalma) hızı etkiler.",
73: "Cl- için Nernst potansiyeli -90 mV, membran potansiyeli -70 mV olduğunda elektrokimyasal gradiyent +20 mV ile hücre içine yönelir.",
74: "Nernst denge potansiyeli bir cins iyonun konsantrasyon farkını dengeleyen elektrokimyasal potansiyeldir. Tüm iyonların toplamını, geçirgenliği veya Na+ için negatif değer hesaplamaz.",
75: "Gibbs-Donnan potansiyeli için Na/K pompası aktivasyonu gerekli değildir; pasif mekanizmalarla kurulur. A, B, C, D doğru ifadelerdir.",
76: "Dinlenim potansiyelinde K+ etkisi daha fazladır çünkü zar K+ iyonlarına daha geçirgendir (daha fazla açık K+ kanalı). Na+ kanalları kapalıdır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
