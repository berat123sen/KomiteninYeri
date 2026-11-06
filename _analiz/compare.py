# -*- coding: utf-8 -*-
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\ocr_pages"

def rd(k, p):
    f = os.path.join(d, f"{k}_p{p:03d}.txt")
    return open(f, encoding="utf-8").read() if os.path.exists(f) else ""

def toks(t):
    return set(w.lower() for w in re.findall(r"\w{5,}", t, re.UNICODE))

def jac(a, b):
    A, B = toks(a), toks(b)
    return len(A & B) / max(1, len(A | B))

for k1, p1, k2, p2 in [("f03",1,"f04",9), ("f03",1,"f06",1), ("f03",2,"f06",2), ("f03",3,"f06",3)]:
    print(k1, p1, "vs", k2, p2, "jaccard=%.2f" % jac(rd(k1,p1), rd(k2,p2)))

print("\n2021 (f03) -> 2022 (f04) en iyi eşleşmeler:")
for i in range(1, 10):
    scores = [(jac(rd("f03", i), rd("f04", j)), j) for j in range(1, 10)]
    s, j = max(scores)
    print(f"  p{i} -> p{j} (jac={s:.2f})")

print("\n2021 (f03) -> 2024-25 (f06) en iyi eşleşmeler:")
for i in range(1, 10):
    scores = [(jac(rd("f03", i), rd("f06", j)), j) for j in range(1, 9)]
    s, j = max(scores)
    print(f"  p{i} -> p{j} (jac={s:.2f})")
