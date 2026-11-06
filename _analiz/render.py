# -*- coding: utf-8 -*-
"""Seçili PDF sayfalarını PNG olarak render et (dosya adı eşleşmesi toleranslı)."""
import os
import sys
import pymupdf
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FOLDER = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages"
os.makedirs(OUT, exist_ok=True)

files = os.listdir(FOLDER)
def pick(*needles):
    for f in files:
        low = f.lower()
        if all(n.lower() in low for n in needles):
            return f
    raise FileNotFoundError(needles)

targets = [
    ("2017-2018", pick("2017-2018"), [1, 2, 9, 10]),
    ("2021", pick("2021", "tem"), [1, 2, 8, 9]),
    ("2022", pick("2022"), [1, 2, 8, 9]),
    ("2024-25", pick("24-25"), [1, 2, 7, 8]),
    ("mixed90", pick("2_241126"), [1, 2, 41, 42, 43, 48, 49, 50, 90]),
    ("2023-24", pick("102", "23-24"), [1, 2]),
]

for key, fname, pages in targets:
    path = os.path.join(FOLDER, fname)
    doc = pymupdf.open(path)
    for pno in pages:
        if pno < 1 or pno > doc.page_count:
            continue
        page = doc[pno - 1]
        pix = page.get_pixmap(matrix=pymupdf.Matrix(2.0, 2.0))
        out = os.path.join(OUT, f"{key}_p{pno:02d}.png")
        pix.save(out)
        print(f"{out}  ({pix.width}x{pix.height})")
    doc.close()
