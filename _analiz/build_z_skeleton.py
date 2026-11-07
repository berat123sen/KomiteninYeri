# -*- coding: utf-8 -*-
"""
Z-Anatomy (CC BY-SA 4.0) kaynak OBJ'sinden:
  - public/models/skeleton-bones.obj : 56 katalog kaydı, gerçek kemik geometrileri
  - public/models/skeleton-soft.obj  : ligament / kıkırdak / diş / diğer (opsiyonel katman)

Kaynak: _analiz/z-anatomy/Z-Anatomy-Layer1-3.obj
"""
import re
import sys
from collections import defaultdict

import numpy as np
import fast_simplification

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SRC = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz\z-anatomy\Z-Anatomy-Layer1-3.obj"
OUT_BONES = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-bones.obj"
OUT_SOFT = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\models\skeleton-soft.obj"

BONE_RATIO = 0.30
BONE_MAX = 10000
BONE_MIN = 60
SOFT_RATIO = 0.15
SOFT_MAX = 2500
SOFT_MIN = 20

# --------------------------------------------------------------------------
# 1) OBJ oku
# --------------------------------------------------------------------------
vertices = []
objects = []
cur = None
cur_faces = None
with open(SRC, encoding="utf-8", errors="ignore") as fh:
    for line in fh:
        if line.startswith("v "):
            a = line.split()
            vertices.append((float(a[1]), float(a[2]), float(a[3])))
        elif line.startswith("o "):
            cur = line[2:].strip()
            cur_faces = []
            objects.append((cur, cur_faces))
        elif line.startswith("f ") and cur_faces is not None:
            parts = line.split()
            fi = [int(t.split("/")[0]) - 1 for t in parts[1:]]
            for j in range(1, len(fi) - 1):
                cur_faces.append((fi[0], fi[j], fi[j + 1]))

print(f"kaynak: {len(vertices)} vertex, {len(objects)} obje", flush=True)
verts_np = np.asarray(vertices, dtype=np.float32)

# --------------------------------------------------------------------------
# 2) Sınıflandırma
# --------------------------------------------------------------------------
SOFT_KEYS = (
    "ligament", "capsul", "cartilage", "membrane", "fat_pad", "symphysis",
    "nucleus", "zona", "cord", "meniscus", "labrum", "bursa", "skin",
    "sesamoid", "tooth", "teeth", "disc",
)

def is_soft(name: str) -> bool:
    low = name.lower()
    if re.match(r"^\d\d-", low):
        return True
    return any(k in low for k in SOFT_KEYS)

BONE_MAP = [
    ("os-frontale", r"^Frontal_bone", "c"),
    ("os-parietale", r"^Parietal_bone\.r", "r"),
    ("os-parietale", r"^Left_parietal_bone", "l"),
    ("os-temporale", r"^Temporal_bone\.[lr]", None),
    ("os-occipitale", r"^Occipital_bone", "c"),
    ("os-sphenoidale", r"^Sphenoid_bone\.[lr]", "c"),
    ("os-ethmoidale", r"^Ethmoid_bone", "c"),
    ("mandibula", r"^Mandible", "c"),
    ("maxilla", r"^Maxilla\.[lr]", None),
    ("os-palatinum", r"^Palatine_bone\.[lr]", None),
    ("os-zygomaticum", r"^Zygomatic_bone\.[lr]", None),
    ("os-nasale", r"^Nasal_bone\.[lr]", None),
    ("os-lacrimale", r"^LAcrimal_bone\.[lr]", None),
    ("vomer", r"^Vomer", "c"),
    ("concha-nasalis-inferior", r"^Inferior_nasal_concha_bone\.[lr]", None),
    ("malleus", r"^Malleus\.[lr]", None),
    ("incus", r"^Incus\.[lr]", None),
    ("stapes", r"^Stapes\.[lr]", None),
    ("os-hyoideum", r"^Hyoid_bone", "c"),
    ("atlas", r"^Atlas-Labels", "c"),
    ("axis", r"^Axis_", "c"),
    ("vertebrae-cervicales", r"^(C3|C5|C6|C7)_", "c"),
    ("vertebrae-cervicales", r"^Cervical_vertebra-Labels_Cone", "c"),
    ("vertebrae-thoracicae", r"^T(\d+)(_|$)", "c"),
    ("vertebrae-lumbales", r"^(L1|L2|L4|L5)_", "c"),
    ("vertebrae-lumbales", r"^Vertebra_Cone", "c"),
    ("os-sacrum", r"^Sacrum_", "c"),
    ("os-coccygis", r"^Coccyx_", "c"),
    ("sternum", r"^(Manubrium_of_sternum|Sternum\.r_Cone|Xiphoid_process)", "c"),
    ("costae", r"^\d+(?:st|nd|rd|th|d)_rib\.[lr]", None),
    ("clavicula", r"^Clavicle\.[lr]", None),
    ("scapula", r"^Scapula\.[lr]", None),
    ("humerus", r"^Humerus\.[lr]", None),
    ("radius", r"^Radius\.[lr]", None),
    ("ulna", r"^Ulna\.[lr]", None),
    ("os-scaphoideum", r"^Scaphoid_bone\.[lr]", None),
    ("os-lunatum", r"^Lunate_bone\.[lr]", None),
    ("os-triquetrum", r"^Triquetrum_bone\.[lr]", None),
    ("os-pisiforme", r"^Pisiform_bone\.[lr]", None),
    ("os-trapezium", r"^Trapezium_bone\.[lr]", None),
    ("os-trapezoideum", r"^Trapezoid_bone\.[lr]", None),
    ("os-capitatum", r"^Capitate_bone\.[lr]", None),
    ("os-hamatum", r"^Hamate_bone\.[lr]", None),
    ("ossa-metacarpi", r"^\d+(?:st|nd|rd|th|d)_metacarpal_bone\.[lr]", None),
    ("phalanges-manus", r"^(Proximal|Middle|Distal)_phalanx_of_.*finger\.[lr]", None),
    ("os-coxae", r"^Hip_bone\.[lr]", None),
    ("femur", r"^Femur\.[lr]", None),
    ("patella", r"^Patella\.[lr]", None),
    ("tibia", r"^Tibia\.[lr]", None),
    ("fibula", r"^Fibula\.[lr]", None),
    ("talus", r"^Talus\.[lr]", None),
    ("calcaneus", r"^Calcaneus\.[lr]", None),
    ("os-naviculare", r"^Navicular_bone\.[lr]", None),
    ("os-cuboideum", r"^Cuboid_bone\.[lr]", None),
    ("os-cuneiforme-mediale", r"^Medial_cuneiform_bone\.[lr]", None),
    ("os-cuneiforme-intermedium", r"^Intermediate_cuneiform_bone\.[lr]", None),
    ("os-cuneiforme-laterale", r"^Lateral_cuneiform_bone\.[lr]", None),
    ("ossa-metatarsi", r"^\d+(?:st|nd|rd|th|d)_metatarsal_bone\.[lr]", None),
    ("phalanges-pedis", r"^(Proximal|Middle|Distal)_phalanx_of_.*finger_of_foot\.[lr]", None),
]

def side_of(name: str, forced):
    if forced:
        return forced
    low = name.lower()
    if re.search(r"\.l(?:_|\.|$)", low):
        return "l"
    if re.search(r"\.r(?:_|\.|$)", low):
        return "r"
    return "c"

def match_bone(name: str):
    for entry, pattern, forced in BONE_MAP:
        if re.search(pattern, name):
            return entry, side_of(name, forced)
    return None

bones = defaultdict(list)
soft = defaultdict(list)
unmatched = []

for i, (name, faces) in enumerate(objects):
    if not faces:
        continue
    if name.startswith("Cervical_vertebra-Labels.001"):
        continue
    if is_soft(name):
        low = name.lower()
        if re.match(r"^\d\d-", low) or "tooth" in low:
            cat = "soft-teeth"
        elif "cartilage" in low:
            cat = "soft-cartilage"
        elif "ligament" in low or "capsul" in low or "membrane" in low or "frenula" in low:
            cat = "soft-ligaments"
        else:
            cat = "soft-other"
        soft[cat].append(i)
        continue
    m = match_bone(name)
    if m:
        bones[m].append(i)
    else:
        unmatched.append((name, len(faces)))

print(f"kemik grubu: {len(bones)}, eşleşmeyen: {len(unmatched)}", flush=True)
for name, nf in unmatched:
    print(f"  EŞLEŞMEDİ {nf:7d}  {name}")

expected = [
    "os-frontale", "os-parietale", "os-temporale", "os-occipitale",
    "os-sphenoidale", "os-ethmoidale", "mandibula", "maxilla", "os-palatinum",
    "os-zygomaticum", "os-nasale", "os-lacrimale", "vomer",
    "concha-nasalis-inferior", "malleus", "incus", "stapes", "os-hyoideum",
    "atlas", "axis", "vertebrae-cervicales", "vertebrae-thoracicae",
    "vertebrae-lumbales", "os-sacrum", "os-coccygis", "sternum", "costae",
    "clavicula", "scapula", "humerus", "radius", "ulna", "os-scaphoideum",
    "os-lunatum", "os-triquetrum", "os-pisiforme", "os-trapezium",
    "os-trapezoideum", "os-capitatum", "os-hamatum", "ossa-metacarpi",
    "phalanges-manus", "os-coxae", "femur", "patella", "tibia", "fibula",
    "talus", "calcaneus", "os-naviculare", "os-cuboideum",
    "os-cuneiforme-mediale", "os-cuneiforme-intermedium",
    "os-cuneiforme-laterale", "ossa-metatarsi", "phalanges-pedis",
]
found = {entry for entry, _ in bones}
missing = [e for e in expected if e not in found]
print(f"eksik katalog kaydı: {missing}", flush=True)

# --------------------------------------------------------------------------
# 3) Decimation + OBJ yazımı
# --------------------------------------------------------------------------
def process_object(obj_index: int, soft_layer: bool):
    faces = objects[obj_index][1]
    nf = len(faces)
    ratio, cap, minimum = (
        (SOFT_RATIO, SOFT_MAX, SOFT_MIN) if soft_layer
        else (BONE_RATIO, BONE_MAX, BONE_MIN)
    )
    target = max(minimum, min(cap, int(nf * ratio)))

    used = np.unique(np.asarray([v for tri in faces for v in tri], dtype=np.int64))
    remap = np.full(len(vertices), -1, dtype=np.int64)
    remap[used] = np.arange(len(used))
    v = verts_np[used]
    f = remap[np.asarray(faces, dtype=np.int64)].astype(np.int32)

    if target < nf:
        try:
            v, f = fast_simplification.simplify(v, f, target_count=target)
        except Exception as exc:
            print(f"  decimate hatası ({exc}); orijinal korunuyor", flush=True)
    return np.asarray(v, dtype=np.float32), np.asarray(f, dtype=np.int64)

def write_obj(path, groups, header, soft_layer=False):
    all_v = []
    group_faces = []
    total = 0
    for gname, obj_indices in groups:
        gv = []
        gf = []
        for oi in obj_indices:
            v, f = process_object(oi, soft_layer)
            off = len(gv)
            gv.extend(v.tolist())
            gf.extend((f + off).tolist())
        if not gf:
            continue
        offset = len(all_v)
        all_v.extend(gv)
        group_faces.append((gname, [(a + offset, b + offset, c + offset) for a, b, c in gf]))
        total += len(gf)

    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(header)
        for x, y, z in all_v:
            fh.write(f"v {x:.6f} {y:.6f} {z:.6f}\n")
        for gname, faces in group_faces:
            fh.write(f"g {gname}\n")
            for a, b, c in faces:
                fh.write(f"f {a + 1} {b + 1} {c + 1}\n")
    print(f"yazıldı: {path}  grup={len(group_faces)}  vertex={len(all_v)}  yüz={total}", flush=True)

bone_groups = []
for (entry, side) in sorted(bones):
    gname = entry if side == "c" else f"{entry}__{side}"
    bone_groups.append((gname, bones[(entry, side)]))

write_obj(
    OUT_BONES,
    bone_groups,
    "# Human skeleton (bones only) - derived from Z-Anatomy\n"
    "# Source: Z-Anatomy, https://github.com/LluisV/Z-Anatomy\n"
    "# License: CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/\n"
    "# Geometry decimated for web use. 56 named groups.\n",
)

write_obj(
    OUT_SOFT,
    sorted(soft.items()),
    "# Human skeleton soft tissues (optional layer) - derived from Z-Anatomy\n"
    "# Source: Z-Anatomy, https://github.com/LluisV/Z-Anatomy\n"
    "# License: CC BY-SA 4.0, https://creativecommons.org/licenses/by-sa/4.0/\n",
    soft_layer=True,
)
