# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for p in [
    r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-bones.obj",
    r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-soft.obj",
]:
    xs, ys, zs = [], [], []
    with open(p, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            if line.startswith("v "):
                a = line.split()
                xs.append(float(a[1])); ys.append(float(a[2])); zs.append(float(a[3]))
    print(p.split("\\")[-1], "n=", len(xs))
    print(" x", min(xs), max(xs))
    print(" y", min(ys), max(ys))
    print(" z", min(zs), max(zs))
