# -*- coding: utf-8 -*-
import os, sys
import pymupdf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

base = r"C:\Users\Berat\Desktop\KomiteninYeri"
klasor = os.path.join(base, "sınavlar")
hedef = os.path.join(base, "_analiz", "pages_2324")
os.makedirs(hedef, exist_ok=True)

pdf_yolu = None
for ad in os.listdir(klasor):
    if ad.startswith("102 23-24") and ad.lower().endswith(".pdf"):
        pdf_yolu = os.path.join(klasor, ad)
        break

if not pdf_yolu:
    raise SystemExit("PDF bulunamadi")

print("PDF:", os.path.basename(pdf_yolu))
doc = pymupdf.open(pdf_yolu)
print("Sayfa sayisi:", doc.page_count)

mat = pymupdf.Matrix(3.0, 3.0)
for i, sayfa in enumerate(doc, start=1):
    pix = sayfa.get_pixmap(matrix=mat, alpha=False)
    yol = os.path.join(hedef, f"p{i:02d}.png")
    pix.save(yol)
    print(f"p{i:02d}.png {pix.width}x{pix.height} {os.path.getsize(yol)//1024} KB")
