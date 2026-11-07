# -*- coding: utf-8 -*-
import sys
from array import array

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\yeni-model\Human skeleton HD.obj"

xs = array("f")
ys = array("f")
zs = array("f")
faces = array("i")
face_sizes = {}
nface = 0
bad = 0
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("v "):
            a = line.split()
            xs.append(float(a[1]))
            ys.append(float(a[2]))
            zs.append(float(a[3]))
        elif line.startswith("f "):
            parts = line.split()
            idx = [int(t.split("/")[0]) for t in parts[1:]]
            k = len(idx)
            face_sizes[k] = face_sizes.get(k, 0) + 1
            if k < 3:
                bad += 1
                continue
            # fan-triangulate
            a0 = idx[0]
            for j in range(1, k - 1):
                faces.append(a0)
                faces.append(idx[j])
                faces.append(idx[j + 1])
            nface += 1

n = len(xs)
print("verts:", n, "faces(raw):", nface, "tris:", len(faces)//3, "sizes:", face_sizes, "bad:", bad)
print("bounds x:", min(xs), max(xs), "y:", min(ys), max(ys), "z:", min(zs), max(zs))
