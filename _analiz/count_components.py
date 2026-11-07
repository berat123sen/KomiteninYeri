# -*- coding: utf-8 -*-
import sys
from collections import defaultdict, deque

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-bones.obj"

verts = []
groups = {}
cur = None
for line in open(p, encoding="utf-8", errors="ignore"):
    if line.startswith("v "):
        a = line.split()
        verts.append((float(a[1]), float(a[2]), float(a[3])))
    elif line.startswith("g "):
        cur = line[2:].strip()
        groups[cur] = []
    elif line.startswith("f ") and cur is not None:
        idx = [int(t.split("/")[0]) for t in line.split()[1:]]
        groups[cur].append(idx)

for name in ("Cranium", "Mandible", "Ribs_Left", "Hand_Left", "Foot_Left"):
    faces = groups.get(name, [])
    if not faces:
        continue
    # union-find over vertices
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for f in faces:
        for i in range(1, len(f)):
            union(f[0], f[i])
    comps = defaultdict(int)
    for f in faces:
        comps[find(f[0])] += 1
    sizes = sorted(comps.values(), reverse=True)
    print(f"{name:14s} yuz={len(faces):6d} bagli_bilesen={len(sizes):3d} en_buyuk={sizes[:5]}")
