# -*- coding: utf-8 -*-
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\yeni-model\Human skeleton HD.obj"

v = 0
f = 0
objects = []
groups = []
materials = set()
mtllib = []
names = Counter()
cur_obj = None
cur_groups = []
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("v "):
            v += 1
        elif line.startswith("f "):
            f += 1
            names[cur_obj or "(none)"] += 1
        elif line.startswith("o "):
            cur_obj = line[2:].strip()
            objects.append(cur_obj)
        elif line.startswith("g "):
            g = line[2:].strip()
            cur_groups.append(g)
            groups.append(g)
        elif line.startswith("usemtl "):
            materials.add(line[7:].strip())
        elif line.startswith("mtllib "):
            mtllib.append(line[7:].strip())

print("vertex:", v, "face:", f)
print("objects:", len(objects))
print("groups:", len(groups))
print("materials:", len(materials), sorted(materials)[:20])
print("mtllib:", mtllib)
print("\n-- objects (first 120) --")
for o in objects[:120]:
    print(repr(o))
print("\n-- objects with face counts --")
for name, n in names.most_common(120):
    print(f"{n:8d}  {name!r}")
