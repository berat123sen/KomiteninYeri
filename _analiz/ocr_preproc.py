# -*- coding: utf-8 -*-
import sys, os, subprocess
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf
import numpy as np
from PIL import Image

F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
TMP = r"C:\Users\Berat\AppData\Local\Temp\opencode\ocr_test"
os.makedirs(TMP, exist_ok=True)
f = [x for x in os.listdir(F) if "24-25" in x][0]
doc = pymupdf.open(os.path.join(F, f))
page = doc[1]  # page 2, clean 2-column
pix = page.get_pixmap(matrix=pymupdf.Matrix(400/72, 400/72), colorspace=pymupdf.csGRAY)
img = os.path.join(TMP, "p02_400_gray.png")
pix.save(img)
im = Image.open(img).convert("L")
arr = np.array(im)
for th in [150, 180, 200]:
    bw = (arr > th).astype(np.uint8) * 255
    outimg = os.path.join(TMP, f"p02_th{th}.png")
    Image.fromarray(bw).save(outimg)
    env = dict(os.environ)
    env["TESSDATA_PREFIX"] = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\tessdata"
    out = os.path.join(TMP, f"p02_th{th}")
    subprocess.run([r"C:\Program Files\Tesseract-OCR\tesseract.exe", outimg, out,
                    "-l", "tur", "--psm", "3", "--dpi", "400"],
                   capture_output=True, text=True, encoding="utf-8", env=env)
    txt = open(out + ".txt", encoding="utf-8").read()
    print("=" * 25, "threshold", th, "chars", len(txt), "=" * 25)
    print(txt[:1200])
doc.close()
