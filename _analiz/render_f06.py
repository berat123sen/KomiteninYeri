# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf

F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
O = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages"
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))
for p in [1, 2, 8]:
    page = doc[p - 1]
    print("page", p, "rect", page.rect)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(2.0, 2.0))
    out = os.path.join(O, f"f06_p{p:02d}.png")
    pix.save(out)
    print(" ->", out, pix.width, pix.height)
doc.close()
