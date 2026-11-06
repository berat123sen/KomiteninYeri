# -*- coding: utf-8 -*-
"""PDF metin çıkarma ve ön inceleme scripti (güvenli yazdırma)."""
import os
import sys
import json
import pymupdf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FOLDER = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz"

os.makedirs(OUT, exist_ok=True)

pdfs = sorted([f for f in os.listdir(FOLDER) if f.lower().endswith(".pdf")])
print(f"Toplam PDF: {len(pdfs)}\n")

summary = []
for name in pdfs:
    path = os.path.join(FOLDER, name)
    try:
        doc = pymupdf.open(path)
        page_count = doc.page_count
        total_text = []
        image_counts = []
        for page in doc:
            total_text.append(page.get_text())
            image_counts.append(len(page.get_images(full=True)))
        full = "\n".join(total_text)
        char_count = len(full)
        total_images = sum(image_counts)

        safe = name.replace(" ", "_").replace(".pdf", "")
        safe = "".join(c for c in safe if c.isalnum() or c in "_-")

        with open(os.path.join(OUT, safe + ".txt"), "w", encoding="utf-8") as f:
            f.write(full)

        item = {
            "file": name,
            "pages": page_count,
            "chars": char_count,
            "images": total_images,
            "avg_chars_per_page": round(char_count / page_count, 1) if page_count else 0,
            "likely_scanned": char_count < 100,
            "first_300": full[:300].replace("\n", " | "),
        }
        summary.append(item)
        doc.close()
        tag = "SCAN-OCR" if item["likely_scanned"] else "TEXT"
        print(f"[{tag}] {name} -> {page_count}s, {char_count}ch, {total_images} img")
    except Exception as e:
        print(f"[ERR] {name}: {e}")
        summary.append({"file": name, "error": str(e)})

with open(os.path.join(OUT, "summary.json"), "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"\nÇıktılar: {OUT}")
