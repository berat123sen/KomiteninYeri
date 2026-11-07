# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\z-anatomy\Z-Anatomy-Layer1-3.obj"

verts = []
objs = []
cur = None
obj_verts = defaultdict(set)
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("v "):
            a = line.split()
            verts.append((float(a[1]), float(a[2]), float(a[3])))
        elif line.startswith("o "):
            cur = line[2:].strip()
            objs.append(cur)
        elif line.startswith("f ") and cur:
            for t in line.split()[1:]:
                obj_verts[cur].add(int(t.split("/")[0]) - 1)

print("global bounds:")
xs = [q[0] for q in verts]
ys = [q[1] for q in verts]
zs = [q[2] for q in verts]
print(" x", round(min(xs), 3), round(max(xs), 3))
print(" y", round(min(ys), 3), round(max(ys), 3))
print(" z", round(min(zs), 3), round(max(zs), 3))

want = [
    "Femur.l", "Femur.r", "Humerus.l", "Humerus.r", "Scapula.l", "Scapula.r",
    "Sphenoid_bone.l", "Parietal_bone.r", "Left_parietal_bone",
    "C3", "C5", "C6", "C7", "Cervical_vertebra-Labels_Cone.046",
    "Cervical_vertebra-Labels.001_Cone.011", "Vertebra_Cone.004",
    "Atlas-Labels_Cone.049", "Axis_Cone.048",
    "L1", "L2", "L4", "L5", "T8_Cone.015", "Sacrum_Cone.016",
    "Sternum.r_Cone.021", "Manubrium_of_sternum.r_Cone.020", "Xiphoid_process",
    "Hip_bone.l", "Hip_bone.r", "Tibia.l", "Tibia.r", "Fibula.l", "Fibula.r",
    "Radius.l", "Radius.r", "Ulna.l", "Ulna.r", "Clavicle.l", "Clavicle.r",
]

def find(sub):
    return [o for o in objs if o.startswith(sub)]

print("\nselected bboxes:")
for w in want:
    matches = find(w)
    if not matches:
        print(f"{w:42s} NOT FOUND")
        continue
    for m in matches:
        idxs = obj_verts[m]
        if not idxs:
            print(f"{m:42s} (no faces)")
            continue
        pts = [verts[i] for i in idxs]
        bb = (
            min(q[0] for q in pts), max(q[0] for q in pts),
            min(q[1] for q in pts), max(q[1] for q in pts),
            min(q[2] for q in pts), max(q[2] for q in pts),
        )
        print(
            f"{m:42s} x[{bb[0]:7.3f},{bb[1]:7.3f}] "
            f"y[{bb[2]:7.3f},{bb[3]:7.3f}] z[{bb[4]:7.3f},{bb[5]:7.3f}] nv={len(idxs)}"
        )
