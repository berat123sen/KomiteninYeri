import { useEffect, useMemo, useRef, useState } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { Html, OrbitControls } from "@react-three/drei";
import { OBJLoader } from "three/examples/jsm/loaders/OBJLoader.js";
import { mergeVertices } from "three/examples/jsm/utils/BufferGeometryUtils.js";
import * as THREE from "three";

/* ------------------------------------------------------------------ */
/* Model transform (measured from the Z-Anatomy OBJ bounding box)      */
/* ------------------------------------------------------------------ */

/** Kaynak modelin boyu (metre). 3 dünya birimine ölçeklenir. */
const MODEL_HEIGHT = 1.696404;
const SCALE = 3 / MODEL_HEIGHT; // ≈ 1.76845
/** Kaynak modelin sınır kutusu merkezi (metre). */
const CENTER: [number, number, number] = [0.0001765, 0.857308, 0.0122085];
const GROUP_POS: [number, number, number] = [
  -CENTER[0] * SCALE,
  -CENTER[1] * SCALE,
  -CENTER[2] * SCALE,
];

const HOME_POSITION: [number, number, number] = [0, 0.03, 3.95];
const HOME_TARGET: [number, number, number] = [0, 0, 0];

/* ------------------------------------------------------------------ */
/* Bone catalogue (206 bones -> 56 named groups)                       */
/* ------------------------------------------------------------------ */

type Region = "Kafa ve boyun" | "Göğüs kafesi ve omurga" | "Omuz ve kol" | "Kalça ve bacak";

type BoneMeta = {
  id: string;
  /** Türkçe ad */
  tr: string;
  /** Latince ad */
  la: string;
  region: Region;
  /** Bu kaydın çizildiği OBJ grupları (gerçek kemik geometrileri). */
  meshes: string[];
};

/** Tek parçalı (merkez) kemik grubu. */
const ONE = (id: string): string[] => [id];
/** Sağ-sol çifti tek kayıt altında toplanan kemik grubu. */
const PAIR = (id: string): string[] => [`${id}__l`, `${id}__r`];

const BONES: BoneMeta[] = [
  /* ---------------------------- Kafa ve boyun ---------------------------- */
  { id: "os-frontale", tr: "Alın kemiği", la: "Os frontale", region: "Kafa ve boyun", meshes: ONE("os-frontale") },
  { id: "os-parietale", tr: "Duvar kemiği", la: "Os parietale", region: "Kafa ve boyun", meshes: PAIR("os-parietale") },
  { id: "os-temporale", tr: "Şakak kemiği", la: "Os temporale", region: "Kafa ve boyun", meshes: PAIR("os-temporale") },
  { id: "os-occipitale", tr: "Art kafa kemiği", la: "Os occipitale", region: "Kafa ve boyun", meshes: ONE("os-occipitale") },
  { id: "os-sphenoidale", tr: "Temel kemik", la: "Os sphenoidale", region: "Kafa ve boyun", meshes: ONE("os-sphenoidale") },
  { id: "os-ethmoidale", tr: "Kalbur kemiği", la: "Os ethmoidale", region: "Kafa ve boyun", meshes: ONE("os-ethmoidale") },
  { id: "mandibula", tr: "Alt çene kemiği", la: "Mandibula", region: "Kafa ve boyun", meshes: ONE("mandibula") },
  { id: "maxilla", tr: "Üst çene kemiği", la: "Maxilla", region: "Kafa ve boyun", meshes: PAIR("maxilla") },
  { id: "os-palatinum", tr: "Damak kemiği", la: "Os palatinum", region: "Kafa ve boyun", meshes: PAIR("os-palatinum") },
  { id: "os-zygomaticum", tr: "Elmacık kemiği", la: "Os zygomaticum", region: "Kafa ve boyun", meshes: PAIR("os-zygomaticum") },
  { id: "os-nasale", tr: "Burun kemiği", la: "Os nasale", region: "Kafa ve boyun", meshes: PAIR("os-nasale") },
  { id: "os-lacrimale", tr: "Gözyaşı kemiği", la: "Os lacrimale", region: "Kafa ve boyun", meshes: PAIR("os-lacrimale") },
  { id: "vomer", tr: "Saban kemiği", la: "Vomer", region: "Kafa ve boyun", meshes: ONE("vomer") },
  { id: "concha-nasalis-inferior", tr: "Alt burun konkası", la: "Concha nasalis inferior", region: "Kafa ve boyun", meshes: PAIR("concha-nasalis-inferior") },
  { id: "malleus", tr: "Çekiç kemikçiği", la: "Malleus", region: "Kafa ve boyun", meshes: PAIR("malleus") },
  { id: "incus", tr: "Örs kemikçiği", la: "Incus", region: "Kafa ve boyun", meshes: PAIR("incus") },
  { id: "stapes", tr: "Üzengi kemikçiği", la: "Stapes", region: "Kafa ve boyun", meshes: PAIR("stapes") },
  { id: "os-hyoideum", tr: "Dil kemiği", la: "Os hyoideum", region: "Kafa ve boyun", meshes: ONE("os-hyoideum") },
  { id: "atlas", tr: "Birinci boyun omuru", la: "Atlas (C1)", region: "Kafa ve boyun", meshes: ONE("atlas") },
  { id: "axis", tr: "İkinci boyun omuru", la: "Axis (C2)", region: "Kafa ve boyun", meshes: ONE("axis") },
  { id: "vertebrae-cervicales", tr: "Boyun omurları", la: "Vertebrae cervicales", region: "Kafa ve boyun", meshes: ONE("vertebrae-cervicales") },

  /* ----------------------- Göğüs kafesi ve omurga ----------------------- */
  { id: "vertebrae-thoracicae", tr: "Göğüs omurları", la: "Vertebrae thoracicae", region: "Göğüs kafesi ve omurga", meshes: ONE("vertebrae-thoracicae") },
  { id: "vertebrae-lumbales", tr: "Bel omurları", la: "Vertebrae lumbales", region: "Göğüs kafesi ve omurga", meshes: ONE("vertebrae-lumbales") },
  { id: "os-sacrum", tr: "Sağrı kemiği", la: "Os sacrum", region: "Göğüs kafesi ve omurga", meshes: ONE("os-sacrum") },
  { id: "os-coccygis", tr: "Kuyruk sokumu", la: "Os coccygis", region: "Göğüs kafesi ve omurga", meshes: ONE("os-coccygis") },
  { id: "sternum", tr: "Göğüs kemiği", la: "Sternum", region: "Göğüs kafesi ve omurga", meshes: ONE("sternum") },
  { id: "costae", tr: "Kaburgalar", la: "Costae", region: "Göğüs kafesi ve omurga", meshes: PAIR("costae") },

  /* ----------------------------- Omuz ve kol ---------------------------- */
  { id: "clavicula", tr: "Köprücük kemiği", la: "Clavicula", region: "Omuz ve kol", meshes: PAIR("clavicula") },
  { id: "scapula", tr: "Kürek kemiği", la: "Scapula", region: "Omuz ve kol", meshes: PAIR("scapula") },
  { id: "humerus", tr: "Üst kol kemiği", la: "Humerus", region: "Omuz ve kol", meshes: PAIR("humerus") },
  { id: "radius", tr: "Ön kol kemiği (radius)", la: "Radius", region: "Omuz ve kol", meshes: PAIR("radius") },
  { id: "ulna", tr: "Dirsek kemiği (ulna)", la: "Ulna", region: "Omuz ve kol", meshes: PAIR("ulna") },
  { id: "os-scaphoideum", tr: "Skafoid kemik", la: "Os scaphoideum", region: "Omuz ve kol", meshes: PAIR("os-scaphoideum") },
  { id: "os-lunatum", tr: "Ayçık kemiği", la: "Os lunatum", region: "Omuz ve kol", meshes: PAIR("os-lunatum") },
  { id: "os-triquetrum", tr: "Üç köşeli kemik", la: "Os triquetrum", region: "Omuz ve kol", meshes: PAIR("os-triquetrum") },
  { id: "os-pisiforme", tr: "Bezelye kemiği", la: "Os pisiforme", region: "Omuz ve kol", meshes: PAIR("os-pisiforme") },
  { id: "os-trapezium", tr: "Yamuk kemik (trapezium)", la: "Os trapezium", region: "Omuz ve kol", meshes: PAIR("os-trapezium") },
  { id: "os-trapezoideum", tr: "Trapezoid kemik", la: "Os trapezoideum", region: "Omuz ve kol", meshes: PAIR("os-trapezoideum") },
  { id: "os-capitatum", tr: "Başlı kemik", la: "Os capitatum", region: "Omuz ve kol", meshes: PAIR("os-capitatum") },
  { id: "os-hamatum", tr: "Çengelli kemik", la: "Os hamatum", region: "Omuz ve kol", meshes: PAIR("os-hamatum") },
  { id: "ossa-metacarpi", tr: "El tarak kemikleri", la: "Ossa metacarpi", region: "Omuz ve kol", meshes: PAIR("ossa-metacarpi") },
  { id: "phalanges-manus", tr: "El parmak kemikleri", la: "Phalanges manus", region: "Omuz ve kol", meshes: PAIR("phalanges-manus") },

  /* --------------------------- Kalça ve bacak --------------------------- */
  { id: "os-coxae", tr: "Kalça kemiği", la: "Os coxae", region: "Kalça ve bacak", meshes: PAIR("os-coxae") },
  { id: "femur", tr: "Uyluk kemiği", la: "Femur", region: "Kalça ve bacak", meshes: PAIR("femur") },
  { id: "patella", tr: "Diz kapağı", la: "Patella", region: "Kalça ve bacak", meshes: PAIR("patella") },
  { id: "tibia", tr: "Kaval kemiği", la: "Tibia", region: "Kalça ve bacak", meshes: PAIR("tibia") },
  { id: "fibula", tr: "Baldır kemiği", la: "Fibula", region: "Kalça ve bacak", meshes: PAIR("fibula") },
  { id: "talus", tr: "Aşık kemiği", la: "Talus", region: "Kalça ve bacak", meshes: PAIR("talus") },
  { id: "calcaneus", tr: "Topuk kemiği", la: "Calcaneus", region: "Kalça ve bacak", meshes: PAIR("calcaneus") },
  { id: "os-naviculare", tr: "Kayık kemiği", la: "Os naviculare", region: "Kalça ve bacak", meshes: PAIR("os-naviculare") },
  { id: "os-cuboideum", tr: "Küp kemiği", la: "Os cuboideum", region: "Kalça ve bacak", meshes: PAIR("os-cuboideum") },
  { id: "os-cuneiforme-mediale", tr: "İç kamamsı kemik", la: "Os cuneiforme mediale", region: "Kalça ve bacak", meshes: PAIR("os-cuneiforme-mediale") },
  { id: "os-cuneiforme-intermedium", tr: "Orta kamamsı kemik", la: "Os cuneiforme intermedium", region: "Kalça ve bacak", meshes: PAIR("os-cuneiforme-intermedium") },
  { id: "os-cuneiforme-laterale", tr: "Dış kamamsı kemik", la: "Os cuneiforme laterale", region: "Kalça ve bacak", meshes: PAIR("os-cuneiforme-laterale") },
  { id: "ossa-metatarsi", tr: "Ayak tarak kemikleri", la: "Ossa metatarsi", region: "Kalça ve bacak", meshes: PAIR("ossa-metatarsi") },
  { id: "phalanges-pedis", tr: "Ayak parmak kemikleri", la: "Phalanges pedis", region: "Kalça ve bacak", meshes: PAIR("phalanges-pedis") },
];

const META = new Map(BONES.map((b) => [b.id, b]));
const BY_MESH = new Map<string, BoneMeta>();
for (const bone of BONES) {
  for (const mesh of bone.meshes) {
    BY_MESH.set(mesh, bone);
  }
}

const REGIONS: Region[] = [
  "Kafa ve boyun",
  "Göğüs kafesi ve omurga",
  "Omuz ve kol",
  "Kalça ve bacak",
];

/* ------------------------------------------------------------------ */
/* Optional soft-tissue layer (ligaments / cartilage / teeth)          */
/* ------------------------------------------------------------------ */

const SOFT_STYLE: Record<string, { color: string; opacity: number }> = {
  "soft-ligaments": { color: "#d8c9a8", opacity: 0.42 },
  "soft-cartilage": { color: "#8fc4de", opacity: 0.5 },
  "soft-teeth": { color: "#f4f1e8", opacity: 0.92 },
  "soft-other": { color: "#c7b9a6", opacity: 0.32 },
};

/* ------------------------------------------------------------------ */
/* Types                                                              */
/* ------------------------------------------------------------------ */

type Focus = {
  position: [number, number, number];
  target: [number, number, number];
};

type BoneEntry = {
  key: string;
  geometry: THREE.BufferGeometry;
  bbox: THREE.Box3;
  /** bbox centre, in OBJ local coordinates (metres) */
  center: [number, number, number];
  /** largest bbox edge, in world units */
  size: number;
  /** default label anchor, in OBJ local coordinates (metres) */
  label: [number, number, number];
};

const HOME_FOCUS: Focus = { position: HOME_POSITION, target: HOME_TARGET };

function toWorld(p: [number, number, number]): [number, number, number] {
  return [
    (p[0] - CENTER[0]) * SCALE,
    (p[1] - CENTER[1]) * SCALE,
    (p[2] - CENTER[2]) * SCALE,
  ];
}

function focusForPoint(
  local: [number, number, number],
  size: number,
  centerX: number,
): Focus {
  const [wx, wy, wz] = toWorld(local);
  const dist = Math.min(1.6, Math.max(0.36, size * 2.2));
  const side = centerX > 0.02 ? 1 : centerX < -0.02 ? -1 : 0.12;
  return {
    target: [wx, wy, wz],
    position: [wx + side * dist * 0.18, wy + dist * 0.08, wz + dist],
  };
}

/* ------------------------------------------------------------------ */
/* OBJ loading (outside the Canvas so it starts immediately)          */
/* ------------------------------------------------------------------ */

let skeletonPromise: Promise<BoneEntry[]> | null = null;
let softPromise: Promise<BoneEntry[]> | null = null;

function buildEntries(object: THREE.Object3D): BoneEntry[] {
  const list: BoneEntry[] = [];
  object.traverse((child) => {
    const mesh = child as THREE.Mesh;
    if (!mesh.isMesh || !mesh.geometry) return;
    let geometry = mesh.geometry as THREE.BufferGeometry;

    // Kaynak OBJ normalsiz: düzgün gölgeleme için köşe normalleri üret.
    if (!geometry.getAttribute("normal")) {
      try {
        geometry = mergeVertices(geometry, 1e-4);
      } catch {
        /* birleştirme başarısız olursa düz gölgelemeye devam et */
      }
      geometry.computeVertexNormals();
    }

    geometry.computeBoundingBox();
    const bb = geometry.boundingBox;
    if (!bb) return;
    const center = new THREE.Vector3();
    bb.getCenter(center);
    const sizeLocal = Math.max(
      bb.max.x - bb.min.x,
      bb.max.y - bb.min.y,
      bb.max.z - bb.min.z,
    );
    const height = bb.max.y - bb.min.y;
    list.push({
      key: mesh.name,
      geometry,
      bbox: bb.clone(),
      center: [center.x, center.y, center.z],
      size: sizeLocal * SCALE,
      label: [
        center.x,
        center.y + height * 0.18,
        bb.max.z + 0.02,
      ],
    });
  });
  return list;
}

function fetchModel(url: string): Promise<BoneEntry[]> {
  return fetch(url)
    .then((res) => {
      if (!res.ok) throw new Error(`Model yüklenemedi (HTTP ${res.status})`);
      return res.text();
    })
    .then((text) => buildEntries(new OBJLoader().parse(text)));
}

function loadBoneEntries(): Promise<BoneEntry[]> {
  if (!skeletonPromise) {
    skeletonPromise = fetchModel(
      `${import.meta.env.BASE_URL}models/skeleton-bones.obj`,
    ).catch((error) => {
      skeletonPromise = null;
      throw error;
    });
  }
  return skeletonPromise;
}

function loadSoftEntries(): Promise<BoneEntry[]> {
  if (!softPromise) {
    softPromise = fetchModel(
      `${import.meta.env.BASE_URL}models/skeleton-soft.obj`,
    ).catch((error) => {
      softPromise = null;
      throw error;
    });
  }
  return softPromise;
}

/* ------------------------------------------------------------------ */
/* Camera animation                                                   */
/* ------------------------------------------------------------------ */

function CameraRig({
  focus,
  controlsRef,
}: {
  focus: Focus;
  controlsRef: React.MutableRefObject<any>;
}) {
  const { camera } = useThree();
  const anim = useRef<{
    startPos: THREE.Vector3;
    endPos: THREE.Vector3;
    startTarget: THREE.Vector3;
    endTarget: THREE.Vector3;
    t: number;
  } | null>(null);

  useEffect(() => {
    const controls = controlsRef.current;
    const startTarget: THREE.Vector3 = controls
      ? controls.target.clone()
      : new THREE.Vector3(0, 0, 0);
    anim.current = {
      startPos: camera.position.clone(),
      endPos: new THREE.Vector3(...focus.position),
      startTarget,
      endTarget: new THREE.Vector3(...focus.target),
      t: 0,
    };
  }, [focus, camera, controlsRef]);

  useFrame((_, delta) => {
    const a = anim.current;
    if (!a) return;
    a.t = Math.min(1, a.t + delta / 0.55);
    const e = 1 - Math.pow(1 - a.t, 3);
    camera.position.lerpVectors(a.startPos, a.endPos, e);
    const controls = controlsRef.current;
    if (controls) {
      controls.target.lerpVectors(a.startTarget, a.endTarget, e);
      controls.update();
    } else {
      camera.lookAt(a.endTarget);
    }
    if (a.t >= 1) anim.current = null;
  });

  return null;
}

/* ------------------------------------------------------------------ */
/* Model                                                              */
/* ------------------------------------------------------------------ */

function SkeletonModel({
  entries,
  softEntries,
  selectedMeta,
  labelMeshes,
  isolated,
  onSelectMesh,
}: {
  entries: BoneEntry[];
  softEntries: BoneEntry[] | null;
  selectedMeta: BoneMeta | null;
  labelMeshes: string[];
  isolated: boolean;
  onSelectMesh: (meshKey: string) => void;
}) {
  const active = useMemo(
    () => new Set(selectedMeta ? selectedMeta.meshes : []),
    [selectedMeta],
  );

  const labels = useMemo(() => {
    if (!selectedMeta) return [];
    return labelMeshes
      .map((key) => entries.find((entry) => entry.key === key))
      .filter((entry): entry is BoneEntry => Boolean(entry))
      .map((entry) => ({
        key: entry.key,
        position: entry.label,
      }));
  }, [entries, labelMeshes, selectedMeta]);

  const softVisible = Boolean(softEntries && softEntries.length > 0 && !isolated);

  return (
    <group scale={SCALE} position={GROUP_POS}>
      {entries.map((entry) => {
        const isActive = active.has(entry.key);
        const hidden = isolated && !isActive;
        return (
          <mesh
            key={entry.key}
            name={entry.key}
            geometry={entry.geometry}
            visible={!hidden}
            onPointerOver={(e) => {
              e.stopPropagation();
              document.body.style.cursor = "pointer";
            }}
            onPointerOut={() => {
              document.body.style.cursor = "auto";
            }}
            onClick={(e) => {
              e.stopPropagation();
              onSelectMesh(entry.key);
            }}
          >
            <meshStandardMaterial
              color={isActive ? "#f2a33c" : "#ded7c6"}
              emissive={isActive ? "#f59e0b" : "#000000"}
              emissiveIntensity={isActive ? 0.35 : 0}
              roughness={0.72}
              metalness={0.06}
            />
          </mesh>
        );
      })}

      {softVisible &&
        softEntries!.map((entry) => {
          const style = SOFT_STYLE[entry.key] ?? {
            color: "#cfc4b0",
            opacity: 0.35,
          };
          return (
            <mesh
              key={`soft-${entry.key}`}
              name={entry.key}
              geometry={entry.geometry}
              renderOrder={2}
            >
              <meshStandardMaterial
                color={style.color}
                transparent
                opacity={style.opacity}
                depthWrite={false}
                roughness={0.55}
                metalness={0}
              />
            </mesh>
          );
        })}

      {selectedMeta &&
        labels.map((label) => (
          <Html
            key={label.key}
            position={label.position}
            center
            zIndexRange={[40, 10]}
            style={{ pointerEvents: "none" }}
          >
            <div className="pointer-events-none -translate-y-2 select-none whitespace-nowrap rounded-xl border border-slate-200/90 bg-white/95 px-3 py-1.5 text-center shadow-xl backdrop-blur dark:border-slate-700 dark:bg-slate-900/95">
              <div className="text-xs font-bold text-slate-900 dark:text-white">
                {selectedMeta.la}
              </div>
              <div className="text-[10px] font-medium text-slate-500 dark:text-slate-400">
                {selectedMeta.tr}
              </div>
            </div>
          </Html>
        ))}
    </group>
  );
}

/* ------------------------------------------------------------------ */
/* First-click matrix warm-up                                         */
/* ------------------------------------------------------------------ */

/**
 * R3F raycasting reads `matrixWorld` of every object with pointer handlers.
 * Meshes that were just mounted can still have an identity world matrix on
 * the very first pointer event (before the next render pass), which makes
 * the first click land on the wrong bone. Refreshing the interaction list
 * once on pointerdown (capture) makes the first click as reliable as the
 * rest.
 */
function MatrixWarmup() {
  const gl = useThree((state) => state.gl);
  const internal = useThree((state) => state.internal);

  useEffect(() => {
    const canvas = gl.domElement;
    const refresh = () => {
      for (const object of internal.interaction) {
        object.updateWorldMatrix(true, false);
      }
    };
    canvas.addEventListener("pointerdown", refresh, true);
    return () => canvas.removeEventListener("pointerdown", refresh, true);
  }, [gl, internal]);

  return null;
}

/* ------------------------------------------------------------------ */
/* Page                                                               */
/* ------------------------------------------------------------------ */

type SoftStatus = "idle" | "loading" | "ready" | "error";

export default function SkeletonPage() {
  const [entries, setEntries] = useState<BoneEntry[]>([]);
  const [status, setStatus] = useState<"loading" | "ready" | "error">("loading");
  const [error, setError] = useState<string | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [labelMeshes, setLabelMeshes] = useState<string[]>([]);
  const [isolatedId, setIsolatedId] = useState<string | null>(null);
  const [focus, setFocus] = useState<Focus>(HOME_FOCUS);
  const [search, setSearch] = useState("");

  const [softEntries, setSoftEntries] = useState<BoneEntry[] | null>(null);
  const [softStatus, setSoftStatus] = useState<SoftStatus>("idle");
  const [softError, setSoftError] = useState<string | null>(null);
  const [showSoft, setShowSoft] = useState(false);

  const bonesRef = useRef<Record<string, BoneEntry>>({});
  const controlsRef = useRef<any>(null);

  useEffect(() => {
    let alive = true;
    loadBoneEntries()
      .then((list) => {
        if (!alive) return;
        const map: Record<string, BoneEntry> = {};
        for (const entry of list) map[entry.key] = entry;
        bonesRef.current = map;
        setEntries(list);
        setStatus("ready");
        console.info(`3D iskelet: ${list.length} kemik grubu yüklendi.`);
      })
      .catch((err) => {
        if (!alive) return;
        console.error("3D iskelet modeli yüklenemedi:", err);
        setError(err instanceof Error ? err.message : String(err));
        setStatus("error");
      });
    return () => {
      alive = false;
    };
  }, []);

  const entryBounds = (meta: BoneMeta): {
    center: [number, number, number];
    size: number;
  } | null => {
    const box = new THREE.Box3();
    for (const key of meta.meshes) {
      const entry = bonesRef.current[key];
      if (entry) box.union(entry.bbox);
    }
    if (box.isEmpty()) return null;
    const center = new THREE.Vector3();
    box.getCenter(center);
    const sizeLocal = Math.max(
      box.max.x - box.min.x,
      box.max.y - box.min.y,
      box.max.z - box.min.z,
    );
    return { center: [center.x, center.y, center.z], size: sizeLocal * SCALE };
  };

  const select = (id: string, meshKey?: string) => {
    const meta = META.get(id);
    if (!meta) return;
    setSelected(id);
    setLabelMeshes(
      meshKey && meta.meshes.includes(meshKey) ? [meshKey] : meta.meshes,
    );
    setIsolatedId((current) => (current === null ? null : id));

    if (meshKey) {
      const entry = bonesRef.current[meshKey];
      if (entry) {
        setFocus(focusForPoint(entry.center, entry.size, entry.center[0]));
      }
      return;
    }
    const bounds = entryBounds(meta);
    if (bounds) {
      setFocus(
        focusForPoint(bounds.center, bounds.size, bounds.center[0]),
      );
    }
  };

  const selectMesh = (meshKey: string) => {
    const owner = BY_MESH.get(meshKey);
    if (!owner) return;
    select(owner.id, meshKey);
  };

  const reset = () => {
    setSelected(null);
    setLabelMeshes([]);
    setIsolatedId(null);
    setFocus({ ...HOME_FOCUS });
  };

  const toggleIsolate = () => {
    if (!selected) return;
    if (isolatedId) {
      setIsolatedId(null);
      return;
    }
    const meta = META.get(selected);
    if (!meta) return;
    setIsolatedId(selected);
    const bounds = entryBounds(meta);
    if (bounds) {
      setFocus(
        focusForPoint(bounds.center, bounds.size, bounds.center[0]),
      );
    }
  };

  const toggleSoft = () => {
    if (showSoft) {
      setShowSoft(false);
      return;
    }
    setShowSoft(true);
    if (softEntries || softStatus === "loading") return;
    setSoftStatus("loading");
    setSoftError(null);
    loadSoftEntries()
      .then((list) => {
        setSoftEntries(list);
        setSoftStatus("ready");
        console.info(`Yumuşak doku katmanı: ${list.length} grup yüklendi.`);
      })
      .catch((err) => {
        console.error("Yumuşak doku katmanı yüklenemedi:", err);
        setSoftStatus("error");
        setSoftError(err instanceof Error ? err.message : String(err));
        setShowSoft(false);
      });
  };

  const filtered = useMemo(() => {
    if (!search) return BONES;
    const q = search.toLocaleLowerCase("tr");
    return BONES.filter(
      (b) =>
        b.tr.toLocaleLowerCase("tr").includes(q) ||
        b.la.toLocaleLowerCase("tr").includes(q) ||
        b.id.toLocaleLowerCase("tr").includes(q),
    );
  }, [search]);

  const selectedMeta = selected ? META.get(selected) ?? null : null;

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="mb-4 flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
            3D İskelet Modeli
          </h1>
          <p className="mt-1 max-w-2xl text-sm text-slate-500 dark:text-slate-400">
            206 kemiğin tamamı listelenmiştir. Bir kemiğe tıklayın veya sağdaki
            listeden seçin: adı kemiğin üzerinde görünür, kamera o bölgeye yaklaşır.
            Yumuşak doku katmanı isteğe bağlıdır.
          </p>
        </div>
        {selectedMeta && (
          <div className="rounded-xl border border-amber-200 bg-amber-50 px-3 py-2 text-right dark:border-amber-500/30 dark:bg-amber-500/10">
            <div className="text-sm font-bold text-amber-900 dark:text-amber-200">
              {selectedMeta.la}
            </div>
            <div className="text-[11px] font-medium text-amber-700/80 dark:text-amber-300/80">
              {selectedMeta.tr}
            </div>
          </div>
        )}
      </div>

      <div className="grid gap-4 lg:grid-cols-[minmax(0,1fr)_340px]">
        <div className="relative h-[62vh] min-h-[420px] overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-b from-slate-50 to-slate-200/70 dark:border-slate-800 dark:from-slate-900 dark:to-slate-950">
          {status === "loading" && (
            <div className="absolute inset-0 z-10 flex flex-col items-center justify-center gap-2 text-sm text-slate-500">
              <div className="h-6 w-6 animate-spin rounded-full border-2 border-slate-300 border-t-[var(--accent)]" />
              Model yükleniyor…
            </div>
          )}
          {status === "error" && (
            <div className="absolute inset-0 z-10 flex flex-col items-center justify-center gap-2 px-6 text-center text-sm text-red-600">
              <span className="font-semibold">3D model yüklenemedi.</span>
              <span className="text-xs text-slate-500">{error}</span>
            </div>
          )}

          <Canvas
            camera={{ position: HOME_POSITION, fov: 45 }}
            dpr={[1, 2]}
            gl={{ antialias: true, alpha: true }}
          >
            <MatrixWarmup />
            <ambientLight intensity={0.85} />
            <hemisphereLight args={["#ffffff", "#c7c2b6", 0.5]} />
            <directionalLight position={[4, 7, 6]} intensity={2.1} />
            <directionalLight position={[-5, 3, -4]} intensity={0.9} />
            <directionalLight position={[0, -7, -3]} intensity={0.35} />

            {status === "ready" && (
              <SkeletonModel
                entries={entries}
                softEntries={showSoft ? softEntries : null}
                selectedMeta={selectedMeta}
                labelMeshes={labelMeshes}
                isolated={isolatedId !== null}
                onSelectMesh={selectMesh}
              />
            )}

            <CameraRig focus={focus} controlsRef={controlsRef} />
            <OrbitControls
              ref={controlsRef}
              makeDefault
              enablePan
              enableZoom
              enableRotate
              enableDamping={false}
              minDistance={0.12}
              maxDistance={6.5}
              zoomSpeed={0.85}
              rotateSpeed={0.7}
              target={[0, 0, 0]}
            />
          </Canvas>

          <div className="pointer-events-none absolute bottom-3 left-3 rounded-lg bg-white/80 px-2.5 py-1 text-[11px] font-medium text-slate-500 backdrop-blur dark:bg-slate-900/70 dark:text-slate-400">
            Sürükle: döndür · Kaydır: yakınlaştır · Sağ tık: taşı
          </div>

          <div className="absolute bottom-3 right-3 flex flex-col items-end gap-2">
            {softStatus === "error" && (
              <div className="rounded-lg bg-red-50/90 px-2 py-1 text-[10px] font-medium text-red-600 backdrop-blur dark:bg-red-500/10 dark:text-red-300">
                Yumuşak doku yüklenemedi{softError ? `: ${softError}` : "."}
              </div>
            )}
            <div className="flex flex-wrap justify-end gap-2">
              <button
                type="button"
                onClick={toggleSoft}
                disabled={isolatedId !== null}
                title={
                  isolatedId !== null
                    ? "İzolasyon açıkken yumuşak doku gizlenir"
                    : undefined
                }
                className="btn-secondary text-xs disabled:cursor-not-allowed disabled:opacity-50"
              >
                {showSoft && softStatus === "loading"
                  ? "Yumuşak doku yükleniyor…"
                  : showSoft && softStatus === "ready"
                    ? "Yumuşak dokuyu gizle"
                    : "Yumuşak dokuyu göster"}
              </button>
              {selected && (
                <button type="button" onClick={toggleIsolate} className="btn-primary text-xs">
                  {isolatedId ? "Tüm iskeleti göster" : "Yalnızca bu bölgeyi göster"}
                </button>
              )}
              <button type="button" onClick={reset} className="btn-secondary text-xs">
                Görünümü sıfırla
              </button>
            </div>
          </div>
        </div>

        <aside className="card flex max-h-[62vh] min-h-[420px] flex-col p-4">
          <div className="flex items-baseline justify-between gap-2">
            <h2 className="text-sm font-bold text-slate-900 dark:text-white">
              Kemikler ({BONES.length}){" "}
              <span className="text-[10px] font-medium uppercase tracking-wider text-slate-400">
                206 kemik
              </span>
            </h2>
            {isolatedId && (
              <button
                type="button"
                onClick={() => setIsolatedId(null)}
                className="text-[11px] font-semibold text-amber-600 hover:underline dark:text-amber-400"
              >
                İzolasyonu kapat
              </button>
            )}
          </div>
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Kemik ara (Türkçe / Latince)…"
            className="mt-2 w-full rounded-lg border border-slate-200 bg-white px-2.5 py-1.5 text-xs text-slate-700 outline-none focus:border-[var(--accent)] dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200"
          />

          <div className="mt-2 flex-1 space-y-3 overflow-y-auto pr-1">
            {REGIONS.map((region) => {
              const items = filtered.filter((b) => b.region === region);
              if (items.length === 0) return null;
              return (
                <div key={region}>
                  <div className="mb-1 px-1 text-[10px] font-bold uppercase tracking-wider text-slate-400 dark:text-slate-500">
                    {region}
                  </div>
                  <div className="space-y-1">
                    {items.map((b) => {
                      const isSelected = selected === b.id;
                      return (
                        <button
                          key={b.id}
                          type="button"
                          onClick={() => select(b.id)}
                          className={`flex w-full items-center justify-between gap-2 rounded-lg px-2.5 py-1.5 text-left text-xs transition ${
                            isSelected
                              ? "bg-amber-100 text-amber-900 dark:bg-amber-500/20 dark:text-amber-200"
                              : "text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800"
                          }`}
                        >
                          <span className="font-medium">{b.tr}</span>
                          <span
                            className={`text-right text-[10px] ${
                              isSelected
                                ? "text-amber-700/80 dark:text-amber-300/80"
                                : "text-slate-400"
                            }`}
                          >
                            {b.la}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </div>
              );
            })}
            {filtered.length === 0 && (
              <p className="px-1 py-3 text-xs text-slate-400">Eşleşen kemik bulunamadı.</p>
            )}
          </div>

          <p className="mt-2 border-t border-slate-100 pt-2 text-[10px] leading-relaxed text-slate-400 dark:border-slate-800">
            Numaralı seriler (kaburga, omur, tarak ve parmak kemikleri) tek ad
            altında; sağ-sol çiftleri tek kayıtta toplanmıştır. Her kayıt gerçek
            kemik geometrisiyle ayrı ayrı tıklanabilir.
          </p>
        </aside>
      </div>

      <div className="mt-3 space-y-1 text-[10px] leading-relaxed text-slate-400 dark:text-slate-500">
        <p>
          3D model:{" "}
          <a
            href="https://github.com/LluisV/Z-Anatomy"
            target="_blank"
            rel="noreferrer"
            className="underline decoration-dotted hover:text-slate-600 dark:hover:text-slate-300"
          >
            Z-Anatomy
          </a>
          ,{" "}
          <a
            href="https://creativecommons.org/licenses/by-sa/4.0/"
            target="_blank"
            rel="noreferrer"
            className="underline decoration-dotted hover:text-slate-600 dark:hover:text-slate-300"
          >
            CC BY-SA 4.0
          </a>{" "}
          — web kullanımı için sadeleştirilmiştir.
        </p>
        <p>
          Yumuşak doku katmanı: bağlar, eklem kapsülleri, kıkırdaklar, dişler ve
          diskler. İsteğe bağlıdır; tıklanamaz ve izolasyon sırasında gizlenir.
        </p>
      </div>
    </div>
  );
}
