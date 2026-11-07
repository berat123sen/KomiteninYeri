# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-bones.obj"

groups = []
cur = None
for line in open(p, encoding="utf-8", errors="ignore"):
    if line.startswith("g "):
        cur = {"name": line[2:].strip(), "v": set()}
        groups.append(cur)
    elif line.startswith("f ") and cur is not None:
        for t in line.split()[1:]:
            cur["v"].add(int(t.split("/")[0]))

V = []
for line in open(p, encoding="utf-8", errors="ignore"):
    if line.startswith("v "):
        a = line.split()
        V.append((float(a[1]), float(a[2]), float(a[3])))

for g in groups:
    pts = [V[i - 1] for i in g["v"]]
    xs = [q[0] for q in pts]
    ys = [q[1] for q in pts]
    zs = [q[2] for q in pts]
    print(
        f'{g["name"]:16s} x[{min(xs):7.2f},{max(xs):7.2f}] '
        f'y[{min(ys):7.2f},{max(ys):7.2f}] z[{min(zs):7.2f},{max(zs):7.2f}]'
    )
