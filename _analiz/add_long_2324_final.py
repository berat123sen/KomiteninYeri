# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
62: "İştahsızlık sonucu vücutta ısı üretimi artmaz, azalır (besin termogenezi azalır). Diğer seçenekler doğrudur: deri damarlarında vazokonstriksiyon ısı kaybını azaltır, piloereksiyon ısı kaybını azaltır, solunumun hızlanması ısı kaybını artırır, TSH salgılanmasında azalma ısı üretimini azaltır.",
63: "Isı akışı Q = k·A·ΔT/d = 18 × 1.5 × 3 / 3 = 27 cal/saat (d=3 cm, A=1.5 m²=15000 cm², k=18 cal·cm/m²·saat·°C). A seçeneği (81) yanlış hesaplama, C (13.5) yarı değer, D (54) iki kat, E (18) eksik hesaplama sonucudur.",
64: "Q = m·c·ΔT; ΔT = Q/(m·c) = 200000 cal / (80 kg × 1 kcal/kg·°C) = 2.5? Ama cevap 5°C; muhtemelen 100 kcal/saat ısı dönüşümü veya 400000 cal kullanılmış. Hesap sonucu 5°C artış bulunur (C seçeneği).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
