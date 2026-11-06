# -*- coding: utf-8 -*-
"""Tüm PDF'leri sayfa sayfa OCR et."""
import os, sys, subprocess, pymupdf, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

FOLDER = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz"
OCR = os.path.join(OUT, "ocr_pages")
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
TESSDATA = os.path.join(OUT, "tessdata")
os.makedirs(OCR, exist_ok=True)

env = os.environ.copy()
env["TESSDATA_PREFIX"] = TESSDATA

files = sorted([f for f in os.listdir(FOLDER) if f.lower().endswith(".pdf")])
report = []
for fi, fname in enumerate(files):
    key = f"f{fi+1:02d}"
    doc = pymupdf.open(os.path.join(FOLDER, fname))
    n = doc.page_count
    print(f"\n[{fi+1}/{len(files)}] {fname} ({n} sayfa)", flush=True)
    for pno in range(n):
        base = os.path.join(OCR, f"{key}_p{pno+1:03d}")
        txt_path = base + ".txt"
        if os.path.exists(txt_path):
            report.append({"file": fname, "key": key, "page": pno+1, "ocr": "cached"})
            continue
        # Önce gömülü metin varsa onu kullan
        page = doc[pno]
        embedded = page.get_text().strip()
        if len(embedded) > 200:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(embedded)
            report.append({"file": fname, "key": key, "page": pno+1, "ocr": "embedded"})
            continue
        pix = page.get_pixmap(matrix=pymupdf.Matrix(220/72, 220/72))
        img = base + ".png"
        pix.save(img)
        r = subprocess.run([TESS, img, base, "-l", "tur+eng", "--psm", "3"],
                           env=env, capture_output=True, text=True,
                           encoding="utf-8", errors="replace")
        ok = os.path.exists(txt_path)
        report.append({"file": fname, "key": key, "page": pno+1, "ocr": "ok" if ok else "fail"})
        print(f"   p{pno+1:03d} {'ok' if ok else 'FAIL'}", flush=True)
    doc.close()

with open(os.path.join(OUT, "ocr_report.json"), "w", encoding="utf-8") as f:
    json.dump({"files": files, "pages": report}, f, ensure_ascii=False, indent=1)
print("\nBitti.")
