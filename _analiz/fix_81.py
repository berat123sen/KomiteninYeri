# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))
for q in d["questions"]:
    if q["number"] == 81:
        q["explanation"] = "Nernst denklemi: E = 60·log([dış]/[iç]) = 60·log(300/x) = 120 → log(300/x)=2 → 300/x=100 → x=3 mEq/L. 30, 60, 300, 600 mEq/L yanlıştır. Nernst denklemi bir iyonun denge potansiyelini hesaplar. Na+ için z=+1, E = 60·log([dış]/[iç]) formülü kullanılır."
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done")
