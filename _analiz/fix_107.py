# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))
for q in d["questions"]:
    if q["number"] == 107:
        q["explanation"] = "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur. TCK 191: uyuşturucu madde kullanma ve bulundurma suçu. Uyuşturucu madde ticareti (TCK 188) daha ağır cezayı gerektirir. Kullanım suçu (TCK 191) tedavi ve denetimli serbestlik ile sonuçlanabilir."
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done")
