import { useEffect, useMemo, useRef, useState } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { Html, OrbitControls } from "@react-three/drei";
import { OBJLoader } from "three/examples/jsm/loaders/OBJLoader.js";
import * as THREE from "three";

/* ------------------------------------------------------------------ */
/* Model transform (measured from the OBJ bounding box)                */
/* ------------------------------------------------------------------ */

const SCALE = 0.0448;
const CENTER: [number, number, number] = [-0.0893, -9.5145, -0.0886];
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
  /** Bu kemiğin çizildiği model grupları */
  meshes: string[];
  /**
   * Kemiğin model üzerindeki işaret noktası; ilgili mesh'in sınır kutusuna
   * göre 0..1 arası oran. Verilmezse mesh'in sınır kutusu merkezi kullanılır.
   */
  anchor?: [number, number, number];
};

const BONES: BoneMeta[] = [
  /* ---------------------------- Kafa ve boyun ---------------------------- */
  { id: "os-frontale", tr: "Alın kemiği", la: "Os frontale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.75, 0.82] },
  { id: "os-parietale", tr: "Duvar kemiği", la: "Os parietale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.88, 0.3] },
  { id: "os-temporale", tr: "Şakak kemiği", la: "Os temporale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.27, 0.55, 0.42] },
  { id: "os-occipitale", tr: "Art kafa kemiği", la: "Os occipitale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.35, 0.1] },
  { id: "os-sphenoidale", tr: "Temel kemik", la: "Os sphenoidale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.56, 0.6] },
  { id: "os-ethmoidale", tr: "Kalbur kemiği", la: "Os ethmoidale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.62, 0.72] },
  { id: "mandibula", tr: "Alt çene kemiği", la: "Mandibula", region: "Kafa ve boyun", meshes: ["Mandible"], anchor: [0.5, 0.45, 0.75] },
  { id: "maxilla", tr: "Üst çene kemiği", la: "Maxilla", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.3, 0.88] },
  { id: "os-palatinum", tr: "Damak kemiği", la: "Os palatinum", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.25, 0.55] },
  { id: "os-zygomaticum", tr: "Elmacık kemiği", la: "Os zygomaticum", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.3, 0.45, 0.8] },
  { id: "os-nasale", tr: "Burun kemiği", la: "Os nasale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.46, 0.93] },
  { id: "os-lacrimale", tr: "Gözyaşı kemiği", la: "Os lacrimale", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.42, 0.52, 0.85] },
  { id: "vomer", tr: "Saban kemiği", la: "Vomer", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.5, 0.34, 0.8] },
  { id: "concha-nasalis-inferior", tr: "Alt burun konkası", la: "Concha nasalis inferior", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.42, 0.31, 0.86] },
  { id: "malleus", tr: "Çekiç kemikçiği", la: "Malleus", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.3, 0.52, 0.4] },
  { id: "incus", tr: "Örs kemikçiği", la: "Incus", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.31, 0.49, 0.38] },
  { id: "stapes", tr: "Üzengi kemikçiği", la: "Stapes", region: "Kafa ve boyun", meshes: ["Cranium"], anchor: [0.32, 0.46, 0.36] },
  { id: "os-hyoideum", tr: "Dil kemiği", la: "Os hyoideum", region: "Kafa ve boyun", meshes: ["Cervical_Spine"], anchor: [0.5, 1.03, 1.15] },
  { id: "atlas", tr: "Birinci boyun omuru", la: "Atlas (C1)", region: "Kafa ve boyun", meshes: ["Cervical_Spine"], anchor: [0.5, 0.94, 0.4] },
  { id: "axis", tr: "İkinci boyun omuru", la: "Axis (C2)", region: "Kafa ve boyun", meshes: ["Cervical_Spine"], anchor: [0.5, 0.86, 0.4] },
  { id: "vertebrae-cervicales", tr: "Boyun omurları", la: "Vertebrae cervicales", region: "Kafa ve boyun", meshes: ["Cervical_Spine"], anchor: [0.5, 0.5, 0.45] },

  /* ----------------------- Göğüs kafesi ve omurga ----------------------- */
  { id: "vertebrae-thoracicae", tr: "Göğüs omurları", la: "Vertebrae thoracicae", region: "Göğüs kafesi ve omurga", meshes: ["Thoracic_Spine"], anchor: [0.5, 0.5, 0.4] },
  { id: "vertebrae-lumbales", tr: "Bel omurları", la: "Vertebrae lumbales", region: "Göğüs kafesi ve omurga", meshes: ["Lumbar_Spine"], anchor: [0.5, 0.5, 0.45] },
  { id: "os-sacrum", tr: "Sağrı kemiği", la: "Os sacrum", region: "Göğüs kafesi ve omurga", meshes: ["Sacrum"], anchor: [0.5, 0.5, 0.5] },
  { id: "os-coccygis", tr: "Kuyruk sokumu", la: "Os coccygis", region: "Göğüs kafesi ve omurga", meshes: ["Coccyx"], anchor: [0.5, 0.4, 0.5] },
  { id: "sternum", tr: "Göğüs kemiği", la: "Sternum", region: "Göğüs kafesi ve omurga", meshes: ["Sternum"], anchor: [0.45, 0.55, 0.75] },
  { id: "costae", tr: "Kaburgalar", la: "Costae", region: "Göğüs kafesi ve omurga", meshes: ["Ribs_Left", "Ribs_Right"], anchor: [0.55, 0.55, 0.9] },

  /* ----------------------------- Omuz ve kol ---------------------------- */
  { id: "clavicula", tr: "Köprücük kemiği", la: "Clavicula", region: "Omuz ve kol", meshes: ["Clavicle_Left", "Clavicle_Right"], anchor: [0.5, 0.55, 0.65] },
  { id: "scapula", tr: "Kürek kemiği", la: "Scapula", region: "Omuz ve kol", meshes: ["Scapula_Left", "Scapula_Right"], anchor: [0.5, 0.55, 0.2] },
  { id: "humerus", tr: "Üst kol kemiği", la: "Humerus", region: "Omuz ve kol", meshes: ["Humerus_Left", "Humerus_Right"], anchor: [0.5, 0.6, 0.5] },
  { id: "radius", tr: "Ön kol kemiği (radius)", la: "Radius", region: "Omuz ve kol", meshes: ["Radius_Left", "Radius_Right"], anchor: [0.5, 0.55, 0.55] },
  { id: "ulna", tr: "Dirsek kemiği (ulna)", la: "Ulna", region: "Omuz ve kol", meshes: ["Ulna_Left", "Ulna_Right"], anchor: [0.5, 0.65, 0.35] },
  { id: "os-scaphoideum", tr: "Skafoid kemik", la: "Os scaphoideum", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.4, 0.93, 0.55] },
  { id: "os-lunatum", tr: "Ayçık kemiği", la: "Os lunatum", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.5, 0.94, 0.5] },
  { id: "os-triquetrum", tr: "Üç köşeli kemik", la: "Os triquetrum", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.62, 0.93, 0.42] },
  { id: "os-pisiforme", tr: "Bezelye kemiği", la: "Os pisiforme", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.66, 0.9, 0.35] },
  { id: "os-trapezium", tr: "Yamuk kemik (trapezium)", la: "Os trapezium", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.38, 0.88, 0.62] },
  { id: "os-trapezoideum", tr: "Trapezoid kemik", la: "Os trapezoideum", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.46, 0.87, 0.58] },
  { id: "os-capitatum", tr: "Başlı kemik", la: "Os capitatum", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.54, 0.86, 0.52] },
  { id: "os-hamatum", tr: "Çengelli kemik", la: "Os hamatum", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.62, 0.87, 0.46] },
  { id: "ossa-metacarpi", tr: "El tarak kemikleri", la: "Ossa metacarpi", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.5, 0.65, 0.5] },
  { id: "phalanges-manus", tr: "El parmak kemikleri", la: "Phalanges manus", region: "Omuz ve kol", meshes: ["Hand_Left", "Hand_Right"], anchor: [0.5, 0.25, 0.5] },

  /* --------------------------- Kalça ve bacak --------------------------- */
  { id: "os-coxae", tr: "Kalça kemiği", la: "Os coxae", region: "Kalça ve bacak", meshes: ["Pelvis_Left", "Pelvis_Right"], anchor: [0.5, 0.55, 0.5] },
  { id: "femur", tr: "Uyluk kemiği", la: "Femur", region: "Kalça ve bacak", meshes: ["Femur_Left", "Femur_Right"], anchor: [0.5, 0.6, 0.5] },
  { id: "patella", tr: "Diz kapağı", la: "Patella", region: "Kalça ve bacak", meshes: ["Patella_Left", "Patella_Right"], anchor: [0.5, 0.5, 0.8] },
  { id: "tibia", tr: "Kaval kemiği", la: "Tibia", region: "Kalça ve bacak", meshes: ["Tibia_Left", "Tibia_Right"], anchor: [0.5, 0.6, 0.5] },
  { id: "fibula", tr: "Baldır kemiği", la: "Fibula", region: "Kalça ve bacak", meshes: ["Fibula_Left", "Fibula_Right"], anchor: [0.5, 0.6, 0.4] },
  { id: "talus", tr: "Aşık kemiği", la: "Talus", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.5, 0.85, 0.35] },
  { id: "calcaneus", tr: "Topuk kemiği", la: "Calcaneus", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.5, 0.55, 0.15] },
  { id: "os-naviculare", tr: "Kayık kemiği", la: "Os naviculare", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.5, 0.8, 0.45] },
  { id: "os-cuboideum", tr: "Küp kemiği", la: "Os cuboideum", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.42, 0.62, 0.35] },
  { id: "os-cuneiforme-mediale", tr: "İç kamamsı kemik", la: "Os cuneiforme mediale", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.4, 0.78, 0.58] },
  { id: "os-cuneiforme-intermedium", tr: "Orta kamamsı kemik", la: "Os cuneiforme intermedium", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.5, 0.78, 0.6] },
  { id: "os-cuneiforme-laterale", tr: "Dış kamamsı kemik", la: "Os cuneiforme laterale", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.6, 0.78, 0.55] },
  { id: "ossa-metatarsi", tr: "Ayak tarak kemikleri", la: "Ossa metatarsi", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.5, 0.4, 0.7] },
  { id: "phalanges-pedis", tr: "Ayak parmak kemikleri", la: "Phalanges pedis", region: "Kalça ve bacak", meshes: ["Foot_Left", "Foot_Right"], anchor: [0.5, 0.15, 0.85] },
];

const META = new Map(BONES.map((b) => [b.id, b]));
const BY_MESH = new Map<string, BoneMeta[]>();
for (const bone of BONES) {
  for (const mesh of bone.meshes) {
    const list = BY_MESH.get(mesh) ?? [];
    list.push(bone);
    BY_MESH.set(mesh, list);
  }
}

const REGIONS: Region[] = [
  "Kafa ve boyun",
  "Göğüs kafesi ve omurga",
  "Omuz ve kol",
  "Kalça ve bacak",
];

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
  /** bbox centre, in OBJ local coordinates */
  center: [number, number, number];
  /** largest bbox edge, in world units */
  size: number;
  /** default label anchor, in OBJ local coordinates */
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

function anchorLocal(meta: BoneMeta, entry: BoneEntry): [number, number, number] {
  if (!meta.anchor) return entry.label;
  const { min, max } = entry.bbox;
  const [fx, fy, fz] = meta.anchor;
  return [
    min.x + fx * (max.x - min.x),
    min.y + fy * (max.y - min.y),
    min.z + fz * (max.z - min.z),
  ];
}

function focusForPoint(
  local: [number, number, number],
  size: number,
  centerX: number,
): Focus {
  const [wx, wy, wz] = toWorld(local);
  const dist = Math.min(1.9, Math.max(0.45, size * 2.6));
  const side = centerX > 0.4 ? 1 : centerX < -0.4 ? -1 : 0.18;
  return {
    target: [wx, wy, wz],
    position: [wx + side * dist * 0.22, wy + dist * 0.1, wz + dist],
  };
}

/* ------------------------------------------------------------------ */
/* OBJ loading (outside the Canvas so it starts immediately)          */
/* ------------------------------------------------------------------ */

let skeletonPromise: Promise<BoneEntry[]> | null = null;

function buildEntries(object: THREE.Object3D): BoneEntry[] {
  const list: BoneEntry[] = [];
  object.traverse((child) => {
    const mesh = child as THREE.Mesh;
    if (!mesh.isMesh || !mesh.geometry) return;
    const geometry = mesh.geometry as THREE.BufferGeometry;
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
        (bb.min.x + bb.max.x) / 2,
        (bb.min.y + bb.max.y) / 2 + height * 0.18,
        bb.max.z + 0.3,
      ],
    });
  });
  return list;
}

function loadBoneEntries(): Promise<BoneEntry[]> {
  if (!skeletonPromise) {
    skeletonPromise = fetch(`${import.meta.env.BASE_URL}models/skeleton-bones.obj`)
      .then((res) => {
        if (!res.ok) throw new Error(`Model yüklenemedi (HTTP ${res.status})`);
        return res.text();
      })
      .then((text) => buildEntries(new OBJLoader().parse(text)))
      .catch((error) => {
        skeletonPromise = null;
        throw error;
      });
  }
  return skeletonPromise;
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
  selectedMeta,
  labelMeshes,
  isolated,
  onSelectMesh,
}: {
  entries: BoneEntry[];
  selectedMeta: BoneMeta | null;
  labelMeshes: string[];
  isolated: boolean;
  onSelectMesh: (meshKey: string, point: THREE.Vector3) => void;
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
        position: anchorLocal(selectedMeta, entry),
      }));
  }, [entries, labelMeshes, selectedMeta]);

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
              onSelectMesh(entry.key, e.point);
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

export default function SkeletonPage() {
  const [entries, setEntries] = useState<BoneEntry[]>([]);
  const [status, setStatus] = useState<"loading" | "ready" | "error">("loading");
  const [error, setError] = useState<string | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [labelMeshes, setLabelMeshes] = useState<string[]>([]);
  const [isolatedId, setIsolatedId] = useState<string | null>(null);
  const [focus, setFocus] = useState<Focus>(HOME_FOCUS);
  const [search, setSearch] = useState("");
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
        console.info(`3D iskelet: ${list.length} geometri grubu yüklendi.`);
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

  const select = (id: string, meshKey?: string) => {
    const meta = META.get(id);
    if (!meta) return;
    const primaryKey =
      meshKey && meta.meshes.includes(meshKey) ? meshKey : meta.meshes[0];
    const primary = bonesRef.current[primaryKey];
    setSelected(id);
    setLabelMeshes(meshKey ? [meshKey] : meta.meshes);
    setIsolatedId((current) => (current === null ? null : id));
    if (primary) {
      setFocus(
        focusForPoint(
          anchorLocal(meta, primary),
          primary.size,
          primary.center[0],
        ),
      );
    }
  };

  const selectMesh = (meshKey: string, point: THREE.Vector3) => {
    const candidates = BY_MESH.get(meshKey);
    const entry = bonesRef.current[meshKey];
    if (!candidates || candidates.length === 0 || !entry) return;

    // Dünya koordinatındaki tıklama noktasını OBJ yerel koordinatına çevir.
    const local: [number, number, number] = [
      (point.x - GROUP_POS[0]) / SCALE,
      (point.y - GROUP_POS[1]) / SCALE,
      (point.z - GROUP_POS[2]) / SCALE,
    ];

    let best = candidates[0];
    let bestDistance = Infinity;
    for (const candidate of candidates) {
      const anchor = anchorLocal(candidate, entry);
      const dx = anchor[0] - local[0];
      const dy = anchor[1] - local[1];
      const dz = anchor[2] - local[2];
      const distance = dx * dx + dy * dy + dz * dz;
      if (distance < bestDistance) {
        bestDistance = distance;
        best = candidate;
      }
    }
    select(best.id, meshKey);
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
    } else {
      setIsolatedId(selected);
      const meta = META.get(selected);
      if (meta) {
        const entry = bonesRef.current[meta.meshes[0]];
        if (entry) {
          setFocus(
            focusForPoint(
              anchorLocal(meta, entry),
              entry.size,
              entry.center[0],
            ),
          );
        }
      }
    }
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
              minDistance={0.25}
              maxDistance={6.5}
              zoomSpeed={0.85}
              rotateSpeed={0.7}
              target={[0, 0, 0]}
            />
          </Canvas>

          <div className="pointer-events-none absolute bottom-3 left-3 rounded-lg bg-white/80 px-2.5 py-1 text-[11px] font-medium text-slate-500 backdrop-blur dark:bg-slate-900/70 dark:text-slate-400">
            Sürükle: döndür · Kaydır: yakınlaştır · Sağ tık: taşı
          </div>

          <div className="absolute bottom-3 right-3 flex flex-wrap justify-end gap-2">
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
            Numaralı kemikler (kaburga, omur, tarak ve parmak kemikleri) tek ad altında
            toplanmıştır. Modelde ayrı geometrisi olmayan kemikler ilgili bölge üzerinde
            işaretlenir.
          </p>
        </aside>
      </div>
    </div>
  );
}
