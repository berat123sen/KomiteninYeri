# -*- coding: utf-8 -*-
import os, sys, pymupdf
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
FOLDER = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages"
files = os.listdir(FOLDER)
fname = [f for f in files if f.lower().startswith("2_241126")][0]
print("Dosya:", fname)
doc = pymupdf.open(os.path.join(FOLDER, fname))
print("Sayfa sayısı:", doc.page_count)
for pno in [1, 2, 40, 41, 42, 43, 44, 48, 49, 50, 60, 89, 90]:
    if 1 <= pno <= doc.page_count:
        pix = doc[pno - 1].get_pixmap(matrix=pymupdf.Matrix(2.0, 2.0))
        out = os.path.join(OUT, f"mixed90_p{pno:02d}.png")
        pix.save(out)
        print(out)
doc.close()
