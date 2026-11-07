# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))
for q in d["questions"]:
    if q["number"] == 108:
        q["explanation"] = "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA). Kafein (1,3,7-trimetilksantin) bir metilksantindir ve kahve, çay, enerji içeceklerinde bulunur. Esrar (cannabis), morfin (opiyat), metamfetamin (stimulan) ve MDMA (halüsinojen/stimulan) yasadışı maddelerdir."
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done")
