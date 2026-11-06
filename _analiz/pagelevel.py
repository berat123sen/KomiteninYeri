# -*- coding: utf-8 -*-
"""Sayfa bazlı metin analizi: hangi sayfa metinli, hangi sayfa taranmış."""
import os
import sys
import json
import pymupdf
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FOLDER = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz"

pdfs = sorted([f for f in os.listdir(FOLDER) if f.lower().endswith(".pdf")])
all_info = {}

for name in pdfs:
    doc = pymupdf.open(os.path.join(FOLDER, name))
    pages = []
    for i, page in enumerate(doc):
        t = page.get_text().strip()
        pages.append({
            "page": i + 1,
            "chars": len(t),
            "imgs": len(page.get_images(full=True)),
            "has_text": len(t) > 60,
            "preview": t[:120].replace("\n", " "),
        })
    doc.close()
    text_pages = [p["page"] for p in pages if p["has_text"]]
    scan_pages = [p["page"] for p in pages if not p["has_text"]]
    all_info[name] = {
        "total": len(pages),
        "text_pages": text_pages,
        "scan_pages": scan_pages,
        "pages": pages,
    }
    print(f"\n### {name}")
    print(f"    Toplam {len(pages)} sayfa | Metinli: {len(text_pages)} {text_pages[:20]} | Taranmış: {len(scan_pages)} {scan_pages[:20]}")

with open(os.path.join(OUT, "page_level.json"), "w", encoding="utf-8") as f:
    json.dump(all_info, f, ensure_ascii=False, indent=1)
print("\nKaydedildi: page_level.json")
