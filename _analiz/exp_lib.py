# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DATA = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams"


def apply(exam_id, exp):
    p = f"{DATA}\\{exam_id}.json"
    d = json.load(open(p, encoding="utf-8"))
    n = 0
    for q in d["questions"]:
        if q["number"] in exp:
            q["explanation"] = exp[q["number"]].strip()
            n += 1
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    missing = [q["number"] for q in d["questions"] if not q.get("explanation")]
    print(f"{exam_id}: {n} açıklama yazıldı; açıklaması olmayan: {len(missing)}")
