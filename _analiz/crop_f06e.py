# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf
F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
O = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages\crops"
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))
page = doc[0]; r = page.rect
clip = pymupdf.Rect(r.x0+0.03*r.width, r.y0+0.68*r.height, r.x0+0.98*r.width, r.y0+0.80*r.height)
pix = page.get_pixmap(matrix=pymupdf.Matrix(4,4), clip=clip)
out = os.path.join(O, "p1_answers.png"); pix.save(out); print(out, pix.width, pix.height)
doc.close()
