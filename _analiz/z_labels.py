# -*- coding: utf-8 -*-
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\z-anatomy\Z-Anatomy-Layer1-3.obj"
cur = None
faces = Counter()
objs = []
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("o "):
            cur = line[2:].strip()
            objs.append(cur)
            faces[cur] = 0
        elif line.startswith("f ") and cur:
            faces[cur] += 1

print("LABEL/CONE objects:")
for o in objs:
    if "cone" in o.lower() or "label" in o.lower():
        print(f"{faces[o]:6d}  {o}")
