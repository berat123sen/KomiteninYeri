# -*- coding: utf-8 -*-
"""Her sayfanın ilk satırlarını ve sınav belirteçlerini özetle."""
import os, re, sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\ocr_pages"
rep = json.load(open(r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\ocr_report.json", encoding="utf-8"))

# key -> dosya adı
keymap = {}
for p in rep["pages"]:
    keymap[p["key"]] = p["file"]

year_re = re.compile(r"(19|20)\d{2}")
exam_re = re.compile(r"(TEM\s*I{1,3}|DÖNEM|DONEM|SINIF|YARIYIL|YY)", re.I)
sec_re = re.compile(r"\(\s*1\s*[-–]\s*\d+\s*\.?\s*SORULAR", re.I)

for key in sorted(keymap):
    fname = keymap[key]
    files = sorted([f for f in os.listdir(d) if f.startswith(key + "_") and f.endswith(".txt")])
    print("\n" + "=" * 100)
    print(f"{key}  {fname}")
    print("=" * 100)
    for f in files:
        pno = int(re.search(r"_p(\d+)\.txt", f).group(1))
        text = open(os.path.join(d, f), encoding="utf-8").read()
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        head = " | ".join(lines[:5])[:180]
        flags = []
        if sec_re.search(text):
            flags.append("SEC1")           # (1-x SORULAR) var → sınav başı olabilir
        if year_re.search(text):
            flags.append("YIL:" + ",".join(sorted(set(year_re.findall(text) and []) or [])))
        # yıl tam eşleşmeleri
        years = sorted(set(re.findall(r"20\d{2}|19\d{2}", text)))
        if years:
            flags.append("YIL:" + ",".join(years))
        if exam_re.search(text):
            flags.append("EXAM")
        print(f"  p{pno:03d} [{' '.join(flags):22s}] {head}")
