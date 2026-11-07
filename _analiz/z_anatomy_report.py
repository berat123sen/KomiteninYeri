# -*- coding: utf-8 -*-
import sys
import re
from collections import Counter, defaultdict

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
            faces[cur] = 0
        elif line.startswith("f ") and cur:
            faces[cur] += 1

def clean(n):
    n = re.sub(r"_Generated_Mesh_From_X3D(\.\d+)?$", "", n)
    n = re.sub(r"_(Cone|Sketchfab_upload_01)(\.\d+)?$", "", n)
    return n

print("objects:", len(objects), "faces:", sum(faces.values()))
print("label/cone objects:", sum(1 for o in objects if "cone" in o.lower() or "label" in o.lower()))
print()

groups = defaultdict(list)
def classify(n):
    l = n.lower()
    if "cone" in l or "label" in l:
        return "LABEL"
    if "cartilage" in l:
        return "CARTILAGE"
    if "tooth" in l or re.match(r"^\d\d-", l):
        return "TOOTH"
    if any(k in l for k in ["muscle", "tendon", "aponeurosis"]):
        return "MUSCLE"
    if any(k in l for k in ["artery", "vein", "nerve", "lymph"]):
        return "VESSEL"
    if any(k in l for k in ["brain", "lung", "heart", "liver", "kidney", "stomach", "intestine", "eye", "skin", "gland"]):
        return "ORGAN"
    if any(k in l for k in ["ligament", "capsule", "disc", "meniscus", "labrum", "bursa"]):
        return "LIGAMENT"
    return "BONE?"

for o in objects:
    groups[classify(o)].append((o, faces[o]))

for k in sorted(groups):
    lst = groups[k]
    print(f"{k:10s} objects={len(lst):4d} faces={sum(f for _, f in lst):8d}")

print("\n-- BONE? names --")
for o, f in sorted(groups["BONE?"]):
    print(f"{f:6d}  {clean(o)}")
