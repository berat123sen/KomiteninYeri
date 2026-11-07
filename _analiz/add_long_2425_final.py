# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
43: "Pentoz fosfat yolunu NADPH (ürün) inhibe eder (geri bildirim inhibisyonu). NAD+, FAD, asetil-CoA ve NADH inhibitör değildir. NADPH üretimi arttıkça glukoz-6-fosfat dehidrogenaz (G6PD, hız sınırlayıcı enzim) inhibe olur. G6PD eksikliğinde hemolitik anemi gelişir (favizm, primaquin duyarlılığı). NADPH ayrıca yağ asidi sentezi, kolesterol sentezi ve nükleotid sentezi için gereklidir. Pentoz fosfat yolu oksidatif (G6PD) ve non-oksidatif (transketolaz/transaldolaz) fazlardan oluşur.",
65: "Nernst denklemi: E = (61/z)·log([dış]/[iç]) mV (25°C). Ca2+ için z=2: E = (61/2)·log(1/0.0001) = 30.5·log(10000) = 30.5·4 = 122 mV. Nernst denklemi bir iyonun denge potansiyelini hesaplar. +61 mV (B) z=1 için, 0 mV (C) denge durumu, +244 mV (D) z=0.5 için, -80 mV (E) ters işaret için yanlıştır.",
72: "Isı akışı Q = k·A·ΔT/d = 18 × 1.5 × 3 / 3 = 27 cal/saat (d=3 cm, A=1.5 m²=15000 cm², k=18 cal·cm/m²·saat·°C). 81 cal/saat (A) yanlış hesaplama, 13.5 (C) yarı değer, 54 (D) iki kat, 18 (E) eksik hesaplama sonucudur.",
80: "Bordetella pertussis zorunlu aerob (oksijen gerektirir). Bacteroides fragilis, Clostridium perfringens, Peptostreptococcus, Veillonella anaerob bakterilerdir. Zorunlu aeroblar oksijen gerektirir ve SOD/katalaz enzimleri içerir.",
89: "Oral dönem (0-18 ay, Freud) Erikson'un 'temel güvene karşı güvensizlik' (trust vs mistrust) evresine denk gelir. Anal dönem 'özerkliğe karşı utanç' evresine, fallik dönem 'girişime karşı suçluluk' evresine denk gelir.",
90: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir. Kafein sempatik aktiviteyi artırır ve stresi artırabilir. A, B, C, E doğru önerilerdir.",
102: "Esrar (cannabis) cannabinoid grubunda yer alır (THC, CBD). Opioid grubu: eroin, morfin, kodein, metadon, fentanil. A seçeneği (esrar) opioid grubunda yer almaz.",
104: "Fensiklidin (PCP, 'angel dust') halüsinojenler (dissosiatif anestezikler) grubunda yer alır. Opioidler, uyarıcılar, sedatifler, hipnotikler farklı gruplardır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
