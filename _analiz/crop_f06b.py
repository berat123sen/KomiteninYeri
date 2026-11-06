# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf

F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
O = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages\crops"
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))

regions = []
for pno in [2, 3, 6]:
    for col, (x0, x1) in {"L": (0.03, 0.52), "R": (0.48, 0.98)}.items():
        regions.append((pno, f"p{pno}_{col}1", x0, 0.02, x1, 0.52))
        regions.append((pno, f"p{pno}_{col}2", x0, 0.50, x1, 0.99))
for pno, name, x0, y0, x1, y1 in regions:
    page = doc[pno - 1]
    r = page.rect
    clip = pymupdf.Rect(r.x0 + x0 * r.width, r.y0 + y0 * r.height,
                        r.x0 + x1 * r.width, r.y0 + y1 * r.height)
    pix = page.get_pixmap(matrix=pymupdf.Matrix(3.2, 3.2), clip=clip)
    out = os.path.join(O, name + ".png")
    pix.save(out)
    print(name, pix.width, pix.height)
doc.close()
