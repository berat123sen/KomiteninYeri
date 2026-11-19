# -*- coding: utf-8 -*-
import fitz, re, json, sys, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = fitz.open(r"C:\Users\Berat\Downloads\2026-2027 Yılı 1.Sınıf Akademik Takvimi.pdf")
L = [l.strip() for p in d for l in p.get_text().split("\n") if l.strip()]
rows = []
starts = [i for i, l in enumerate(L) if re.fullmatch(r"MED\d{3}", l) or re.fullmatch(r"\d+ MED\d{3}", l)]
for k, s in enumerate(starts):
    e = starts[k + 1] if k + 1 < len(starts) else len(L)
    body = L[s + 1:e]
    # önceki satır numarası (ör. "12") sonraki kayda ait; sondan at
    if body and re.fullmatch(r"\d+", body[-1]) and k + 1 < len(starts):
        body = body[:-1]
    code = re.search(r"MED\d{3}", L[s]).group()
    rows.append({"code": code, "body": body})
out = []
for r in rows:
    b = r["body"]
    if len(b) < 2: continue
    date = b[0]
    rest = b[1:]
    time = rest[0] if re.match(r"\d{1,2}[:.]\d{2}", rest[0]) else ""
    rest = rest[1:] if time else rest
    typ = next((x for x in rest if x.lower() in ("teorik", "uygulama")), "")
    dept = ""
    if typ:
        idx = rest.index(typ)
        after = rest[idx + 1:]
        dept = after[0] if after else ""
        before = rest[:idx]
    else:
        before = rest
    out.append({"code": r["code"], "date": date, "time": time, "type": typ.lower(), "dept": dept.strip(),
                "topic": before[0] if before else "", "instr": before[1] if len(before) > 1 else "", "raw": rest})
json.dump(out, open(r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\takvim_rows.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
for code in sorted({o["code"] for o in out}):
    rs = [o for o in out if o["code"] == code]
    print("\n==", code, len(rs), rs[0]["date"], "->", rs[-1]["date"])
    c = collections.Counter(o["dept"] for o in rs if o["type"] == "teorik")
    print(dict(c))
    for o in rs:
        if re.search(r"kurul|SINAV|Sınav", o["topic"] + " ".join(o["raw"]), re.I):
            print("  *", o["date"], o["raw"][:3])
