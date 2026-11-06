# -*- coding: utf-8 -*-
"""Klasördeki PDF'ler için sınav manifestosu (sayfa aralıkları + cevap sayısı)."""
import os, re, sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\ocr_pages"

ans_re = re.compile(r"(?:CEVAP|YANIT|Cevap|Yanıt|CEVAP|YANIT)\s*[;:.]?\s*([A-E])", re.I)

def page_text(key, p):
    f = os.path.join(d, f"{key}_p{p:03d}.txt")
    return open(f, encoding="utf-8").read() if os.path.exists(f) else ""

def scan(key, start, end, label):
    total = 0
    per_page = {}
    for p in range(start, end + 1):
        t = page_text(key, p)
        n = len(ans_re.findall(t))
        per_page[p] = n
        total += n
    print(f"  {label:38s} p{start:02d}-{end:02d}  cevap~{total:3d}  sayfa:{list(per_page.values())}")

print("F01 2023-24")
scan("f01", 1, 8, "2023-2024")
print("\nF02 2017-18")
scan("f02", 1, 10, "2017-2018")
print("\nF03 2021")
scan("f03", 1, 9, "2020-2021? (2021)")
print("\nF04 (f03 ters)")
scan("f04", 1, 9, "duplicate")
print("\nF05 karma")
scan("f05", 1, 12, "2019 Dönem1 Tem2")
scan("f05", 13, 23, "2017-2018 (dup)")
scan("f05", 24, 33, "Dönem I Tem 2 (yıl?)")
scan("f05", 34, 41, "TEM II (yıl?)")
scan("f05", 42, 48, "TEM II HAM 2014")
scan("f05", 49, 56, "1.Sınıf 2.YY 2014")
scan("f05", 57, 68, "1.SINIF TEM2 2013")
scan("f05", 69, 76, "2.TEM 2011-2012")
scan("f05", 77, 83, "2010-2011")
scan("f05", 84, 90, "2009-2010")
print("\nF06 2024-25")
scan("f06", 1, 8, "2024-2025")
