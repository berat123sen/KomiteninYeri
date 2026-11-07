# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
90: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir. Kafein sempatik aktiviteyi artırır ve stresi artırabilir. A, B, C, E doğru önerilerdir. Kafein adenosin reseptörlerini bloke ederek uyanıklığı artırır ve stres yanıtını güçlendirir.",
102: "Esrar (cannabis) cannabinoid grubunda yer alır (THC, CBD). Opioid grubu: eroin, morfin, kodein, metadon, fentanil. A seçeneği (esrar) opioid grubunda yer almaz. Esrarın aktif bileşeni THC (tetrahidrokanabinol) CB1/CB2 reseptörlerine bağlanır.",
104: "Fensiklidin (PCP, 'angel dust') halüsinojenler (dissosiatif anestezikler) grubunda yer alır. Opioidler, uyarıcılar, sedatifler, hipnotikler farklı gruplardır. PCP NMDA reseptör antagonisti olup dissosiatif anestezi yapar.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
