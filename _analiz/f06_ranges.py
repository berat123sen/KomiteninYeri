# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\ocr_pages"
qre = re.compile(r"^\s*(\d{1,3})\s*[\.\),]\s*", re.M)
for p in range(1, 9):
    t = open(os.path.join(d, f"f06_p{p:03d}.txt"), encoding="utf-8").read()
    nums = [int(x) for x in qre.findall(t)]
    # keep plausible sequence 1..105
    seq = []
    for n in nums:
        if 1 <= n <= 105:
            seq.append(n)
    print(f"p{p}: count={len(seq)} first={seq[:12]} last={seq[-12:]}")
