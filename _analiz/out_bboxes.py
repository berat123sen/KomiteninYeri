# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-bones.obj"
verts = []
faces = defaultdict(list)
cur = None
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("v "):
            a = line.split()
            verts.append((float(a[1]), float(a[2]), float(a[3])))
        elif line.startswith("g "):
            cur = line[2:].strip()
        elif line.startswith("f ") and cur:
            for t in line.split()[1:]:
                faces[cur].append(int(t.split("/")[0]) - 1)

want = [
    "os-frontale", "os-parietale__l", "os-parietale__r",
    "os-temporale__l", "os-temporale__r", "os-occipitale",
    "mandibula", "costae__l", "costae__r", "femur__l", "femur__r",
    "humerus__l", "humerus__r", "scapula__l", "scapula__r",
    "vertebrae-thoracicae", "os-sacrum", "patella__l", "tibia__l",
    "sternum", "clavicula__l", "talus__l", "calcaneus__l",
]
for name in want:
    idxs = set(faces[name])
    pts = [verts[i] for i in idxs]
    xs = [q[0] for q in pts]; ys = [q[1] for q in pts]; zs = [q[2] for q in pts]
    cx = (min(xs) + max(xs)) / 2
    cy = (min(ys) + max(ys)) / 2
    cz = (min(zs) + max(zs)) / 2
    print(f"{name:26s} center=({cx:.4f},{cy:.4f},{cz:.4f})  "
          f"size=({max(xs)-min(xs):.3f},{max(ys)-min(ys):.3f},{max(zs)-min(zs):.3f})")
