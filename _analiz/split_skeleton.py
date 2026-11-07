# -*- coding: utf-8 -*-
"""
Split skeleton.obj into per-bone OBJ groups so the 3D viewer can:
- select the exact bone under the cursor (real meshes, no fake hit spheres),
- highlight it,
- isolate it,
- put a label on it.

Run from repo root: python _analiz/split_skeleton.py
"""
import os
import sys
import shutil
import collections

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = r"C:\Users\Berat\Desktop\KomiteninYeri"
SRC = os.path.join(BASE, "_analiz", "skeleton_original.obj")
BACKUP = SRC
OUT = os.path.join(BASE, "sinav-platformu", "public", "models", "skeleton-bones.obj")

if not os.path.exists(BACKUP):
    shutil.copyfile(SRC, BACKUP)
    print("backup ->", BACKUP)

vertices = []      # (x,y,z)
normals = []       # raw text after vn
face_lines = []    # (indices tuple, raw face line)
other_headers = [] # vt? none, keep any v/vn
v_lines = []
vn_lines = []

with open(SRC, "r", encoding="utf-8", errors="ignore") as f:
    for line in f:
        if line.startswith("v "):
            v_lines.append(line)
            a = line.split()
            vertices.append((float(a[1]), float(a[2]), float(a[3])))
        elif line.startswith("vn "):
            vn_lines.append(line)
        elif line.startswith("f "):
            idx = tuple(int(t.split("/")[0]) - 1 for t in line.split()[1:])
            face_lines.append((idx, line))

print("v:", len(vertices), "vn:", len(vn_lines), "f:", len(face_lines))

# ---- connected components over shared vertex indices -----------------------
parent = list(range(len(vertices)))

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra

for idx, _ in face_lines:
    for i in range(1, len(idx)):
        union(idx[0], idx[i])

comps = collections.defaultdict(list)  # root -> list of (idx, line)
for idx, line in face_lines:
    comps[find(idx[0])].append((idx, line))

print("components:", len(comps))

# ---- classify components into bones ---------------------------------------
def classify(fc, cx, cy, cz, xmin, xmax, ymin, ymax, zmin, zmax):
    # The model faces +Z, so the subject's left side is +X
    # (their left hand appears on the viewer's right).
    side = "Left" if cx > 0 else "Right"
    w = xmax - xmin

    if fc >= 8000:
        return "Sacrum"
    if fc >= 6600 and cy > 15:
        return "Cranium"
    if 2800 <= fc < 3200 and cy > 14:
        return "Mandible"
    if 2300 <= fc < 2500 and cy < -8:
        return "Coccyx"
    if 2600 <= fc < 2800 and abs(cx) > 1:
        return "Pelvis_" + side
    if 1500 <= fc < 1600 and abs(cx) > 2:
        return "Scapula_" + side
    if 480 <= fc < 520 and cy < -10:
        return "Femur_" + side
    if 340 <= fc < 360 and abs(cx) < 1:
        return "Sternum"
    if 280 <= fc < 300 and cy < -22:
        return "Tibia_" + side
    if 165 <= fc < 180 and cy < -22:
        return "Fibula_" + side
    if 260 <= fc < 270 and abs(cx) > 6:
        return "Humerus_" + side
    if 230 <= fc < 240 and abs(cx) > 8:
        return ("Radius_" if cz > -2.6 else "Ulna_") + side
    if 205 <= fc < 225 and abs(cx) > 8:
        return ("Radius_" if cz > -2.6 else "Ulna_") + side
    if 390 <= fc < 400 and abs(cx) > 2:
        return "Clavicle_" + side

    if cy < -39:
        return "Foot_" + side
    if cy < -22 and abs(cx) > 2 and fc < 60:
        return "Patella_" + side
    if abs(cx) > 8 and cy < -8:
        return "Hand_" + side

    # spine: everything on the midline
    if abs(cx) < 0.9:
        if cy > 12.5:
            return "Cervical_Spine"
        if cy > 4.5:
            return "Thoracic_Spine"
        return "Lumbar_Spine"

    # ribs / costal cartilage: lateral, above the pelvis, not limb bones
    if cy > 0.3:
        return "Ribs_" + side
    return None


buckets = collections.defaultdict(list)
unknown = []

for root, faces in comps.items():
    vs = sorted({i for idx, _ in faces for i in idx})
    pts = [vertices[i] for i in vs]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; zs = [p[2] for p in pts]
    n = len(faces)
    cx, cy, cz = sum(xs)/len(xs), sum(ys)/len(ys), sum(zs)/len(zs)
    key = classify(n, cx, cy, cz, min(xs), max(xs), min(ys), max(ys), min(zs), max(zs))
    if key is None:
        unknown.append((n, cx, cy, cz))
        # fallback: nearest side / spine
        key = ("Lumbar_Spine" if cy < 5 else "Thoracic_Spine")
    buckets[key].append((n, faces))

if unknown:
    print("UNKNOWN (fallback):", unknown)

# ---- report ---------------------------------------------------------------
print("\nAssignment:")
for key in sorted(buckets):
    fs = buckets[key]
    total = sum(n for n, _ in fs)
    print(f"  {key:18s} comps={len(fs):3d} faces={total:6d}")

expected = [
    "Cranium", "Mandible", "Cervical_Spine", "Thoracic_Spine", "Lumbar_Spine",
    "Sacrum", "Coccyx", "Sternum", "Ribs_Left", "Ribs_Right",
    "Clavicle_Left", "Clavicle_Right", "Scapula_Left", "Scapula_Right",
    "Humerus_Left", "Humerus_Right", "Radius_Left", "Ulna_Left",
    "Radius_Right", "Ulna_Right", "Hand_Left", "Hand_Right",
    "Pelvis_Left", "Pelvis_Right", "Femur_Left", "Femur_Right",
    "Patella_Left", "Patella_Right", "Tibia_Left", "Tibia_Right",
    "Fibula_Left", "Fibula_Right", "Foot_Left", "Foot_Right",
]
missing = [k for k in expected if k not in buckets]
extra = [k for k in buckets if k not in expected]
if missing:
    print("MISSING BONES:", missing)
if extra:
    print("EXTRA KEYS:", extra)

# ---- write grouped obj ----------------------------------------------------
written_faces = 0
with open(OUT, "w", encoding="utf-8", newline="\n") as out:
    out.writelines(v_lines)
    out.writelines(vn_lines)
    for key in expected:
        if key not in buckets:
            continue
        out.write(f"g {key}\n")
        out.write("usemtl Bones___Vray\n")
        for _, faces in buckets[key]:
            for _, line in faces:
                out.write(line)
                written_faces += 1
    out.write("\n")

print("\nwrote", OUT)
print("size MB:", round(os.path.getsize(OUT) / 1024 / 1024, 2))
print("faces written:", written_faces, "of", len(face_lines))
