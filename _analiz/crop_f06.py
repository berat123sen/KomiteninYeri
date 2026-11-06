# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf

F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
O = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\pages\crops"
os.makedirs(O, exist_ok=True)
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))

# fractional clip regions: (page, name, x0, y0, x1, y1)
regions = [
    (1, "p1_top_left", 0.03, 0.03, 0.52, 0.52),
    (1, "p1_top_right", 0.48, 0.03, 0.98, 0.52),
    (2, "p2_left", 0.03, 0.02, 0.52, 0.99),
    (2, "p2_right", 0.48, 0.02, 0.98, 0.99),
    (3, "p3_left", 0.03, 0.02, 0.52, 0.99),
    (3, "p3_right", 0.48, 0.02, 0.98, 0.99),
    (4, "p4_top_left", 0.03, 0.02, 0.52, 0.53),
    (4, "p4_top_right", 0.48, 0.02, 0.98, 0.53),
    (4, "p4_bot_left", 0.03, 0.52, 0.52, 0.99),
    (4, "p4_bot_right", 0.48, 0.52, 0.98, 0.99),
    (5, "p5_top_left", 0.03, 0.02, 0.52, 0.53),
    (5, "p5_top_right", 0.48, 0.02, 0.98, 0.53),
    (6, "p6_left", 0.03, 0.02, 0.52, 0.99),
    (6, "p6_right", 0.48, 0.02, 0.98, 0.99),
    (7, "p7_top_left", 0.03, 0.02, 0.52, 0.53),
    (7, "p7_top_right", 0.48, 0.02, 0.98, 0.53),
    (7, "p7_bot_left", 0.03, 0.52, 0.52, 0.99),
    (7, "p7_bot_right", 0.48, 0.52, 0.98, 0.99),
]
Z = 3.2 / 1.0
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
