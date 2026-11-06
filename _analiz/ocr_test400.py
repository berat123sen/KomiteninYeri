# -*- coding: utf-8 -*-
import sys, os, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf

F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
TMP = r"C:\Users\Berat\AppData\Local\Temp\opencode\ocr_test"
os.makedirs(TMP, exist_ok=True)
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))
page = doc[0]
pix = page.get_pixmap(matrix=pymupdf.Matrix(400/72, 400/72))
img = os.path.join(TMP, "p01_400.png")
pix.save(img)
print("rendered", pix.width, pix.height)
env = dict(os.environ)
env["TESSDATA_PREFIX"] = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\tessdata"
for psm in ["3", "4", "6"]:
    out = os.path.join(TMP, f"p01_400_psm{psm}")
    r = subprocess.run([r"C:\Program Files\Tesseract-OCR\tesseract.exe", img, out,
                        "-l", "tur", "--psm", psm, "--dpi", "400"],
                       capture_output=True, text=True, encoding="utf-8", env=env)
    txt = open(out + ".txt", encoding="utf-8").read()
    print("=" * 30, "psm", psm, "chars", len(txt), "=" * 30)
    print(txt[:1500])
doc.close()
