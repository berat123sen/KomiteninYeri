# -*- coding: utf-8 -*-
import sys
from array import array

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\yeni-model\Human skeleton HD.obj"

xs = array("f")
ys = array("f")
zs = array("f")
faces = array("i")
with open(p, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("v "):
            a = line.split()
            xs.append(float(a[1]))
            ys.append(float(a[2]))
            zs.append(float(a[3]))
        elif line.startswith("f "):
            parts = line.split()
            idx = [int(t.split("/")[0]) - 1 for t in parts[1:]]
            for j in range(1, len(idx) - 1):
                faces.append(idx[0])
                faces.append(idx[j])
                faces.append(idx[j + 1])

n = len(xs)
print("verts", n, "tris", len(faces) // 3, flush=True)

parent = array("i", range(n))
rank = array("b", [0]) * n


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


tri = len(faces) // 3
for t in range(tri):
    a = faces[t * 3]
    b = faces[t * 3 + 1]
    c = faces[t * 3 + 2]
    ra = find(a)
    rb = find(b)
    if ra != rb:
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    rc = find(c)
    ra = find(a)
    if ra != rc:
        if rank[ra] < rank[rc]:
            ra, rc = rc, ra
        parent[rc] = ra
        if rank[ra] == rank[rc]:
            rank[ra] += 1
    if t % 500000 == 0:
        print("union", t, flush=True)

roots = np.array([find(i) for i in range(n)], dtype=np.int64)
unique, compact = np.unique(roots, return_inverse=True)
k = len(unique)
print("components:", k, flush=True)

vx = np.frombuffer(xs, dtype=np.float32)
vy = np.frombuffer(ys, dtype=np.float32)
vz = np.frombuffer(zs, dtype=np.float32)

counts = np.bincount(compact, minlength=k)

# triangle counts per component
face_comp = compact[np.frombuffer(faces, dtype=np.int32).reshape(-1, 3)[:, 0]]
tri_counts = np.bincount(face_comp, minlength=k)


def comp_bounds(values):
    mn = np.full(k, np.inf, dtype=np.float64)
    mx = np.full(k, -np.inf, dtype=np.float64)
    np.minimum.at(mn, compact, values)
    np.maximum.at(mx, compact, values)
    return mn, mx


minx, maxx = comp_bounds(vx)
miny, maxy = comp_bounds(vy)
minz, maxz = comp_bounds(vz)

order = np.argsort(tri_counts)[::-1]
print("\nTop components (tri, verts, bbox):")
for ci in order[:50]:
    print(
        f"{tri_counts[ci]:7d} tris {counts[ci]:7d} v  "
        f"x[{minx[ci]:8.1f},{maxx[ci]:8.1f}] "
        f"y[{miny[ci]:8.1f},{maxy[ci]:8.1f}] "
        f"z[{minz[ci]:8.1f},{maxz[ci]:8.1f}]"
    )

# Save compact labels for later use
np.save(r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\yeni-model\vertex_labels.npy", compact)
print("\nlabel file written")
