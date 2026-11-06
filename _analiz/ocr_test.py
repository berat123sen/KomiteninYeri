# -*- coding: utf-8 -*-
"""Tek sayfa OCR testi."""
import os, sys, subprocess, pymupdf
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FOLDER = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz"
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = os.path.join(OUT, "tessdata")
os.makedirs(os.path.join(OUT, "ocr"), exist_ok=True)

files = os.listdir(FOLDER)
fname = [f for f in files if "2017-2018" in f][0]
doc = pymupdf.open(os.path.join(FOLDER, fname))
page = doc[0]
pix = page.get_pixmap(matrix=pymupdf.Matrix(300/72, 300/72))
img = os.path.join(OUT, "ocr", "test.png")
pix.save(img)
doc.close()

env = os.environ.copy()
env["TESSDATA_PREFIX"] = TESSDATA
out_base = os.path.join(OUT, "ocr", "test")
r = subprocess.run([TESS, img, out_base, "-l", "tur+eng", "--psm", "3"], env=env,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print("STDERR:", r.stderr[:500])
with open(out_base + ".txt", encoding="utf-8") as f:
    print(f.read()[:2500])
