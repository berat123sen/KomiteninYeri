import { useMemo, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";
import {
  ArrowLeft,
  Dices,
  GraduationCap,
  Layers,
  RefreshCw,
  Shuffle,
  Sparkles,
} from "lucide-react";
import type { Question } from "../types";
import { useAllExams } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { PageLoader, ErrorState } from "../components/Loading";
import { QuizSession } from "../components/QuizSession";
import { cn, shuffle } from "../lib/utils";

export function RandomPage() {
  usePageTitle("Rastgele Soru");
  const { data, loading, error } = useAllExams();
  const [params] = useSearchParams();

  const [examId, setExamId] = useState("all");
  const [discipline, setDiscipline] = useState(params.get("ders") ?? "all");
  const [count, setCount] = useState(10);
  const [session, setSession] = useState<Question[] | null>(null);
  const [sessionLabel, setSessionLabel] = useState("");

  const disciplineOptions = useMemo(() => {
    if (!data) return [];
    const map = new Map<string, { id: string; name: string; count: number }>();
    for (const exam of data) {
      if (examId !== "all" && exam.exam.id !== examId) continue;
      for (const q of exam.questions) {
        const current = map.get(q.disciplineId);
        if (current) current.count += 1;
        else map.set(q.disciplineId, { id: q.disciplineId, name: q.discipline, count: 1 });
      }
    }
    return [...map.values()].sort((a, b) => b.count - a.count);
  }, [data, examId]);

  const examPool = useMemo(() => {
    if (!data) return [];
    return data
      .filter((exam) => examId === "all" || exam.exam.id === examId)
      .flatMap((exam) => exam.questions);
  }, [data, examId]);

  const pool = useMemo(
    () => examPool.filter((q) => discipline === "all" || q.disciplineId === discipline),
    [examPool, discipline],
  );

  if (loading) return <PageLoader label="Soru havuzu hazırlanıyor…" />;
  if (error) return <ErrorState message={error} />;

  const exams = data ?? [];

  function start() {
    if (pool.length === 0) return;
    const picked = shuffle(pool).slice(0, Math.min(count, pool.length));
    const examLabel =
      examId === "all"
        ? "Tüm sınavlar"
        : exams.find((e) => e.exam.id === examId)?.exam.shortLabel ?? "";
    const discLabel =
      discipline === "all"
        ? "Tüm dersler"
        : disciplineOptions.find((d) => d.id === discipline)?.name ?? "";
    setSessionLabel(`${examLabel} · ${discLabel}`);
    setSession(picked);
  }

  if (session) {
    return (
      <QuizSession
        title="Rastgele Soru"
        subtitle={`${sessionLabel} · ${session.length} soru`}
        questions={session}
        revealMode="immediate"
        onRestart={start}
        backTo="/rastgele"
        backLabel="Rastgele kurulum"
      />
    );
  }

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <Link to="/" className="inline-flex items-center gap-1 transition hover:text-indigo-600 dark:hover:text-indigo-300">
          <ArrowLeft className="h-3.5 w-3.5" />
          Ana sayfa
        </Link>
      </div>

      <div className="mt-4">
        <span className="chip border-amber-200 bg-amber-50 text-amber-700 dark:border-amber-500/30 dark:bg-amber-500/10 dark:text-amber-300">
          <Shuffle className="h-3.5 w-3.5" />
          Rastgele soru
        </span>
        <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
          Kısa bir pratik seansı
        </h1>
        <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          Sınav ve ders filtrelerini seç, arşivden rastgele sorular çek. Her cevaptan sonra doğru
          cevabı ve kaynağını görürsün.
        </p>
      </div>

      <div className="mt-6 grid gap-4 lg:grid-cols-[minmax(0,1fr)_300px]">
        <div className="space-y-4">
          <section className="card p-5 sm:p-6">
            <h2 className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
              <GraduationCap className="h-4 w-4 text-indigo-500" />
              1 · Sınav / yıl
            </h2>
            <div className="mt-3 flex flex-wrap gap-2">
              <Chip active={examId === "all"} onClick={() => setExamId("all")} label="Tüm sınavlar" />
              {exams.map((exam) => (
                <Chip
                  key={exam.exam.id}
                  active={examId === exam.exam.id}
                  onClick={() => setExamId(exam.exam.id)}
                  label={`${exam.exam.shortLabel} · ${exam.exam.questionCount} soru`}
                />
              ))}
            </div>
          </section>

          <section className="card p-5 sm:p-6">
            <h2 className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
              <Layers className="h-4 w-4 text-indigo-500" />
              2 · Ders
            </h2>
            <div className="mt-3 flex flex-wrap gap-2">
              <Chip
                active={discipline === "all"}
                onClick={() => setDiscipline("all")}
                label={`Tüm dersler · ${examPool.length}`}
              />
              {disciplineOptions.map((d) => (
                <Chip
                  key={d.id}
                  active={discipline === d.id}
                  onClick={() => setDiscipline(d.id)}
                  label={`${d.name} · ${d.count}`}
                />
              ))}
            </div>
            {disciplineOptions.length === 0 && (
              <p className="mt-3 text-xs text-slate-400">Bu sınav için ders verisi bulunamadı.</p>
            )}
          </section>

          <section className="card p-5 sm:p-6">
            <h2 className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
              <Dices className="h-4 w-4 text-indigo-500" />
              3 · Kaç soru?
            </h2>
            <div className="mt-3 flex flex-wrap gap-2">
              {[5, 10, 20, 50].map((n) => (
                <Chip key={n} active={count === n} onClick={() => setCount(n)} label={`${n} soru`} />
              ))}
            </div>
            <p className="mt-3 text-xs text-slate-400">
              Havuzda bu filtreyle {pool.length} soru var. Seçtiğin sayı havuzdan büyükse tümü
              kullanılır.
            </p>
          </section>
        </div>

        <aside>
          <div className="card p-5 lg:sticky lg:top-20">
            <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-amber-500 to-orange-500 text-white shadow-sm">
              <Dices className="h-5 w-5" />
            </span>
            <h2 className="mt-3 text-sm font-bold text-slate-900 dark:text-white">Seans özeti</h2>
            <dl className="mt-4 space-y-2.5 text-sm">
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Sınav</dt>
                <dd className="max-w-[60%] truncate text-right font-semibold text-slate-900 dark:text-white">
                  {examId === "all"
                    ? "Tüm sınavlar"
                    : exams.find((e) => e.exam.id === examId)?.exam.shortLabel}
                </dd>
              </div>
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Ders</dt>
                <dd className="max-w-[60%] truncate text-right font-semibold text-slate-900 dark:text-white">
                  {discipline === "all"
                    ? "Tüm dersler"
                    : disciplineOptions.find((d) => d.id === discipline)?.name}
                </dd>
              </div>
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Soru</dt>
                <dd className="font-semibold text-slate-900 dark:text-white">
                  {Math.min(count, pool.length)}
                </dd>
              </div>
            </dl>

            <button
              type="button"
              className="btn-primary mt-5 w-full"
              onClick={start}
              disabled={pool.length === 0}
            >
              <RefreshCw className="h-4 w-4" />
              Soruları getir
            </button>

            <div className="mt-4 flex items-start gap-2 rounded-xl bg-slate-50 px-3 py-2.5 text-[11px] leading-relaxed text-slate-500 dark:bg-slate-800/60 dark:text-slate-400">
              <Sparkles className="mt-0.5 h-3.5 w-3.5 shrink-0 text-amber-500" />
              <p>
                Rastgele seanslarda cevaplar anında gösterilir ve ilerlemene kaydedilir. “Yeniden
                başla” yeni bir rastgele seçim yapar.
              </p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}

function Chip({
  active,
  onClick,
  label,
}: {
  active: boolean;
  onClick: () => void;
  label: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "rounded-xl border px-3 py-2 text-xs font-semibold transition",
        active
          ? "border-indigo-500 bg-indigo-50 text-indigo-700 ring-1 ring-indigo-500 dark:border-indigo-400 dark:bg-indigo-500/10 dark:text-indigo-300 dark:ring-indigo-400"
          : "border-slate-200 bg-white text-slate-600 hover:border-indigo-300 hover:text-indigo-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300 dark:hover:border-indigo-500/60 dark:hover:text-indigo-300",
      )}
    >
      {label}
    </button>
  );
}
