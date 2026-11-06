# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
m = json.load(open(r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\exam_manifest.json", encoding="utf-8"))
print("Sinav sayisi:", len(m["sinavlar"]))
print("Toplam soru:", sum(s["soru_sayisi"] for s in m["sinavlar"]))
for s in m["sinavlar"]:
    print(f" - {s['yil']:34s} {s['sayfa_araligi']:24s} {s['cevap_durumu']}")
