# -*- coding: utf-8 -*-
"""Sayfa bazlı soru numarası aralığı ve bölüm başlığı çıkar."""
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\ocr_pages"

qre = re.compile(r"^\s*(\d{1,3})\s*[\.\)]\s*", re.M)
secre = re.compile(r"([A-ZÇĞİÖŞÜa-zçğıöşü ]{4,40})\s*\(\s*(\d{1,3})\s*[-–]\s*(\d{1,3})\s*\.?\s*SORULAR", re.I)

for key in ["f01", "f02", "f03", "f04", "f05", "f06"]:
    files = sorted([f for f in os.listdir(d) if f.startswith(key + "_") and f.endswith(".txt")])
    print("\n" + "=" * 90)
    print(key)
    print("=" * 90)
    for f in files:
        pno = int(re.search(r"_p(\d+)\.txt", f).group(1))
        text = open(os.path.join(d, f), encoding="utf-8").read()
        nums = [int(x) for x in qre.findall(text)]
        # monotonik artan benzersiz ilk 60
        secs = secre.findall(text)
        seclist = "; ".join(f"{a.strip()}({b}-{c})" for a, b, c in secs)
        first10 = nums[:10]
        print(f"  p{pno:03d} q:{str(first10):40s} sec:[{seclist}]")
