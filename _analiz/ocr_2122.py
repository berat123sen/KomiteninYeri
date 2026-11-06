# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from rapidocr_onnxruntime import RapidOCR

base = r"C:\Users\Berat\Desktop\KomiteninYeri"
inp = os.path.join(base, "_analiz", "pages_2122")
out = os.path.join(base, "_analiz", "ocr_2122")
os.makedirs(out, exist_ok=True)
ocr = RapidOCR()

for ad in sorted(os.listdir(inp)):
    if not ad.lower().endswith(".png"):
        continue
    p = os.path.join(inp, ad)
    res, _ = ocr(p)
    lines = [r[1] for r in (res or [])]
    outp = os.path.join(out, ad.replace(".png", ".txt"))
    with open(outp, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(ad, "->", len(lines), "lines")
print("done")
