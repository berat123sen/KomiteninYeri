# -*- coding: utf-8 -*-
import os, sys, pymupdf
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
base = r"C:\Users\Berat\Desktop\KomiteninYeri"
klasor = os.path.join(base, "sınavlar")
hedef = os.path.join(base, "_analiz", "pages_2122")
os.makedirs(hedef, exist_ok=True)

for ad in ["2021 tem 2.pdf", "2022_TEM2_241126_201709 (1).pdf"]:
    pdf_yolu = os.path.join(klasor, ad)
    doc = pymupdf.open(pdf_yolu)
    key = "2021" if ad.startswith("2021") else "2022"
    mat = pymupdf.Matrix(3.0, 3.0)
    for i, sayfa in enumerate(doc, start=1):
        pix = sayfa.get_pixmap(matrix=mat, alpha=False)
        yol = os.path.join(hedef, f"{key}_p{i:02d}.png")
        pix.save(yol)
    print(ad, "rendered", doc.page_count, "pages")
print("done")
