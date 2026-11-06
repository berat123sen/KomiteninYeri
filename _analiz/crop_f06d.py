# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf
F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
O = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages\crops"
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))
regions = [
    (1, "p1_low_left", 0.03, 0.56, 0.52, 0.76),
    (1, "p1_low_right", 0.48, 0.56, 0.98, 0.76),
]
for pno, name, x0, y0, x1, y1 in regions:
    page = doc[pno - 1]; r = page.rect
    clip = pymupdf.Rect(r.x0+x0*r.width, r.y0+y0*r.height, r.x0+x1*r.width, r.y0+y1*r.height)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(4,4), clip=clip)
    out = os.path.join(O, name+".png"); pix.save(out); print(name, pix.width, pix.height)
doc.close()
