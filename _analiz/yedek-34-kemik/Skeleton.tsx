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
/* Bone metadata                                                      */
/* ------------------------------------------------------------------ */

type Region = "Kafa ve boyun" | "Omurga ve gövde" | "Omuz ve kol" | "Kalça ve bacak";

type BoneMeta = {
  key: string;
  tr: string;
  la: string;
  region: Region;
};

const BONES: BoneMeta[] = [
  { key: "Cranium", tr: "Kafatası", la: "Cranium", region: "Kafa ve boyun" },
  { key: "Mandible", tr: "Alt çene", la: "Mandibula", region: "Kafa ve boyun" },
  { key: "Cervical_Spine", tr: "Boyun omurları", la: "Vertebrae cervicales", region: "Kafa ve boyun" },

  { key: "Thoracic_Spine", tr: "Göğüs omurları", la: "Vertebrae thoracicae", region: "Omurga ve gövde" },
  { key: "Lumbar_Spine", tr: "Bel omurları", la: "Vertebrae lumbales", region: "Omurga ve gövde" },
  { key: "Sacrum", tr: "Sağrı kemiği", la: "Os sacrum", region: "Omurga ve gövde" },
  { key: "Coccyx", tr: "Kuyruk sokumu", la: "Os coccygis", region: "Omurga ve gövde" },
  { key: "Sternum", tr: "Göğüs kemiği", la: "Sternum", region: "Omurga ve gövde" },
  { key: "Ribs_Left", tr: "Sol kaburgalar", la: "Costae sinistrae", region: "Omurga ve gövde" },
  { key: "Ribs_Right", tr: "Sağ kaburgalar", la: "Costae dextrae", region: "Omurga ve gövde" },

  { key: "Clavicle_Left", tr: "Sol köprücük kemiği", la: "Clavicula sinistra", region: "Omuz ve kol" },
  { key: "Clavicle_Right", tr: "Sağ köprücük kemiği", la: "Clavicula dextra", region: "Omuz ve kol" },
  { key: "Scapula_Left", tr: "Sol kürek kemiği", la: "Scapula sinistra", region: "Omuz ve kol" },
  { key: "Scapula_Right", tr: "Sağ kürek kemiği", la: "Scapula dextra", region: "Omuz ve kol" },
  { key: "Humerus_Left", tr: "Sol üst kol kemiği", la: "Humerus sinister", region: "Omuz ve kol" },
  { key: "Humerus_Right", tr: "Sağ üst kol kemiği", la: "Humerus dexter", region: "Omuz ve kol" },
  { key: "Radius_Left", tr: "Sol ön kol kemiği", la: "Radius sinister", region: "Omuz ve kol" },
  { key: "Ulna_Left", tr: "Sol dirsek kemiği", la: "Ulna sinistra", region: "Omuz ve kol" },
  { key: "Radius_Right", tr: "Sağ ön kol kemiği", la: "Radius dexter", region: "Omuz ve kol" },
  { key: "Ulna_Right", tr: "Sağ dirsek kemiği", la: "Ulna dextra", region: "Omuz ve kol" },
  { key: "Hand_Left", tr: "Sol el kemikleri", la: "Ossa manus sinistrae", region: "Omuz ve kol" },
  { key: "Hand_Right", tr: "Sağ el kemikleri", la: "Ossa manus dextrae", region: "Omuz ve kol" },

  { key: "Pelvis_Left", tr: "Sol kalça kemiği", la: "Os coxae sinistrum", region: "Kalça ve bacak" },
  { key: "Pelvis_Right", tr: "Sağ kalça kemiği", la: "Os coxae dextrum", region: "Kalça ve bacak" },
  { key: "Femur_Left", tr: "Sol uyluk kemiği", la: "Femur sinistrum", region: "Kalça ve bacak" },
  { key: "Femur_Right", tr: "Sağ uyluk kemiği", la: "Femur dextrum", region: "Kalça ve bacak" },
  { key: "Patella_Left", tr: "Sol diz kapağı", la: "Patella sinistra", region: "Kalça ve bacak" },
  { key: "Patella_Right", tr: "Sağ diz kapağı", la: "Patella dextra", region: "Kalça ve bacak" },
  { key: "Tibia_Left", tr: "Sol kaval kemiği", la: "Tibia sinistra", region: "Kalça ve bacak" },
  { key: "Tibia_Right", tr: "Sağ kaval kemiği", la: "Tibia dextra", region: "Kalça ve bacak" },
  { key: "Fibula_Left", tr: "Sol baldır kemiği", la: "Fibula sinistra", region: "Kalça ve bacak" },
  { key: "Fibula_Right", tr: "Sağ baldır kemiği", la: "Fibula dextra", region: "Kalça ve bacak" },
  { key: "Foot_Left", tr: "Sol ayak kemikleri", la: "Ossa pedis sinistri", region: "Kalça ve bacak" },
  { key: "Foot_Right", tr: "Sağ ayak kemikleri", la: "Ossa pedis dextri", region: "Kalça ve bacak" },
];

const META = new Map(BONES.map((b) => [b.key, b]));
const REGIONS: Region[] = ["Kafa ve boyun", "Omurga ve gövde", "Omuz ve kol", "Kalça ve bacak"];

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
  /** bbox centre, in OBJ local coordinates */
  center: [number, number, number];
  /** largest bbox edge, in world units */
  size: number;
  /** label anchor, in OBJ local coordinates */
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

function focusFor(entry: BoneEntry): Focus {
  const [wx, wy, wz] = toWorld(entry.center);
  const dist = Math.min(2.0, Math.max(0.5, entry.size * 2.8));
  const side = entry.center[0] > 0.4 ? 1 : entry.center[0] < -0.4 ? -1 : 0.18;
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
  selected,
  isolated,
  onSelect,
}: {
  entries: BoneEntry[];
  selected: string | null;
  isolated: string | null;
  onSelect: (key: string) => void;
}) {
  const selectedEntry = entries.find((e) => e.key === selected);

  return (
    <group scale={SCALE} position={GROUP_POS}>
      {entries.map((entry) => {
        const hidden = isolated !== null && isolated !== entry.key;
        const isSelected = selected === entry.key;
        return (
          <mesh
            key={entry.key}
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
              onSelect(entry.key);
            }}
          >
            <meshStandardMaterial
              color={isSelected ? "#f2a33c" : "#ded7c6"}
              emissive={isSelected ? "#f59e0b" : "#000000"}
              emissiveIntensity={isSelected ? 0.35 : 0}
              roughness={0.72}
              metalness={0.06}
            />
          </mesh>
        );
      })}

      {selectedEntry && (
        <Html
          position={selectedEntry.label}
          center
          zIndexRange={[40, 10]}
          style={{ pointerEvents: "none" }}
        >
          <div className="pointer-events-none -translate-y-2 select-none whitespace-nowrap rounded-xl border border-slate-200/90 bg-white/95 px-3 py-1.5 text-center shadow-xl backdrop-blur dark:border-slate-700 dark:bg-slate-900/95">
            <div className="text-xs font-bold text-slate-900 dark:text-white">
              {META.get(selectedEntry.key)?.tr ?? selectedEntry.key}
            </div>
            <div className="text-[10px] font-medium text-slate-500 dark:text-slate-400">
              {META.get(selectedEntry.key)?.la ?? ""}
            </div>
          </div>
        </Html>
      )}
    </group>
  );
}

/* ------------------------------------------------------------------ */
/* Page                                                               */
/* ------------------------------------------------------------------ */

export default function SkeletonPage() {
  const [entries, setEntries] = useState<BoneEntry[]>([]);
  const [status, setStatus] = useState<"loading" | "ready" | "error">("loading");
  const [error, setError] = useState<string | null>(null);
  const [selected, setSelected] = useState<string | null>(null);
  const [isolated, setIsolated] = useState<string | null>(null);
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

        const known = new Set(BONES.map((b) => b.key));
        const unknown = list.filter((e) => !known.has(e.key));
        if (unknown.length > 0) {
          console.warn(
            "3D iskelet: tanınmayan kemik grupları:",
            unknown.map((e) => e.key || "(isimsiz)"),
          );
        }
        const loadedKeys = new Set(list.map((e) => e.key));
        const missing = BONES.filter((b) => !loadedKeys.has(b.key)).map((b) => b.key);
        if (missing.length > 0) {
          console.warn("3D iskelet: modelde bulunamayan kemikler:", missing);
        }
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

  const select = (key: string) => {
    setSelected(key);
    setIsolated((current) => (current === null ? null : key));
    const entry = bonesRef.current[key];
    if (entry) setFocus(focusFor(entry));
  };

  const reset = () => {
    setSelected(null);
    setIsolated(null);
    setFocus({ ...HOME_FOCUS });
  };

  const toggleIsolate = () => {
    if (isolated) {
      setIsolated(null);
    } else if (selected) {
      setIsolated(selected);
      const entry = bonesRef.current[selected];
      if (entry) setFocus(focusFor(entry));
    }
  };

  const filtered = useMemo(() => {
    if (!search) return BONES;
    const q = search.toLocaleLowerCase("tr");
    return BONES.filter(
      (b) =>
        b.tr.toLocaleLowerCase("tr").includes(q) ||
        b.la.toLocaleLowerCase("tr").includes(q) ||
        b.key.toLocaleLowerCase("tr").includes(q),
    );
  }, [search]);

  const selectedMeta = selected ? META.get(selected) : undefined;

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="mb-4 flex flex-wrap items-end justify-between gap-3">
        <div>
          <h1 className="text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
            3D İskelet Modeli
          </h1>
          <p className="mt-1 max-w-2xl text-sm text-slate-500 dark:text-slate-400">
            Bir kemiğe tıklayın: kemiğin üzerinde Türkçe ve Latince adı görünür, kamera o
            kemiğe yaklaşır. Omurga, kaburga gibi iç kemikler için sağdaki listeyi kullanın.
          </p>
        </div>
        {selectedMeta && (
          <div className="rounded-xl border border-amber-200 bg-amber-50 px-3 py-2 text-right dark:border-amber-500/30 dark:bg-amber-500/10">
            <div className="text-sm font-bold text-amber-900 dark:text-amber-200">
              {selectedMeta.tr}
            </div>
            <div className="text-[11px] font-medium text-amber-700/80 dark:text-amber-300/80">
              {selectedMeta.la}
            </div>
          </div>
        )}
      </div>

      <div className="grid gap-4 lg:grid-cols-[minmax(0,1fr)_320px]">
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
            <ambientLight intensity={0.85} />
            <hemisphereLight args={["#ffffff", "#c7c2b6", 0.5]} />
            <directionalLight position={[4, 7, 6]} intensity={2.1} />
            <directionalLight position={[-5, 3, -4]} intensity={0.9} />
            <directionalLight position={[0, -7, -3]} intensity={0.35} />

            {status === "ready" && (
              <SkeletonModel
                entries={entries}
                selected={selected}
                isolated={isolated}
                onSelect={select}
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
                {isolated ? "Tüm iskeleti göster" : "Yalnızca bu kemiği göster"}
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
                Türkçe · Latince
              </span>
            </h2>
            {isolated && (
              <button
                type="button"
                onClick={() => setIsolated(null)}
                className="text-[11px] font-semibold text-amber-600 hover:underline dark:text-amber-400"
              >
                İzolasyonu kapat
              </button>
            )}
          </div>
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Kemik ara…"
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
                      const isSelected = selected === b.key;
                      return (
                        <button
                          key={b.key}
                          type="button"
                          onClick={() => select(b.key)}
                          className={`flex w-full items-center justify-between gap-2 rounded-lg px-2.5 py-1.5 text-left text-xs transition ${
                            isSelected
                              ? "bg-amber-100 text-amber-900 dark:bg-amber-500/20 dark:text-amber-200"
                              : "text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800"
                          }`}
                        >
                          <span className="font-medium">{b.tr}</span>
                          <span
                            className={`text-[10px] ${
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
        </aside>
      </div>
    </div>
  );
}
