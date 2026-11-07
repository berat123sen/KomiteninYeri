# -*- coding: utf-8 -*-
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\z-anatomy\Z-Anatomy-Layer1-3.obj"

objects = []
cur = None
faces = Counter()
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("o "):
            cur = line[2:].strip()
            objects.append(cur)
        elif line.startswith("f ") and cur:
            faces[cur] += 1

print("objects:", len(objects), "total faces:", sum(faces.values()))
print("\n-- all object names --")
for name in objects:
    print(name)

print("\n-- keywords --")
kw = ["bone", "cartilage", "ligament", "muscle", "tendon", "artery", "vein", "nerve", "organ", "skin", "disc"]
for k in kw:
    n = sum(1 for o in objects if k in o.lower())
    if n:
        print(k, n)
