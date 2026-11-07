# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
107: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu 191. madde). Kullanmak, bulundurmak, nakletmek ve satmak suçtur. Sadece satmak suçtur (B) yanlıştır; kullanım da suçtur. Hayır suç değildir (C) yanlıştır. Kullanılan maddeye göre değişir (D) yanlıştır; tüm uyuşturucu maddeler için kullanım suçtur. Esrar kullanmak suç değildir (E) yanlıştır; esrar da uyuşturucu madde kapsamındadır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
