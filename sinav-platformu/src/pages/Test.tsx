import { useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import {
  ArrowLeft,
  CheckCircle2,
  ChevronRight,
  Clock,
  ListChecks,
  Shuffle,
  Sparkles,
  Target,
  Zap,
} from "lucide-react";
import type { Question } from "../types";
import { useExam } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { PageLoader, ErrorState } from "../components/Loading";
import { QuizSession } from "../components/QuizSession";
import { cn, shuffle } from "../lib/utils";

type RevealMode = "immediate" | "end";
type CountOption = "all" | "10" | "20" | "50";

export function TestPage() {
  const { examId } = useParams<{ examId: string }>();
  const { data, loading, error } = useExam(examId);
  usePageTitle(data ? `${data.exam.shortLabel} · Test Modu` : "Test Modu");
  const [params] = useSearchParams();

  const [discipline, setDiscipline] = useState(params.get("ders") ?? "all");
  const [revealMode, setRevealMode] = useState<RevealMode>("immediate");
  const [count, setCount] = useState<CountOption>("all");
  const [mixOrder, setMixOrder] = useState(false);
  const [session, setSession] = useState<Question[] | null>(null);

  const pool = useMemo(() => {
    if (!data) return [];
    if (discipline === "all") return data.questions;
    return data.questions.filter((q) => q.disciplineId === discipline);
  }, [data, discipline]);

  if (loading) return <PageLoader label="Test hazırlanıyor…" />;
  if (error) return <ErrorState message={error} />;
  if (!data) return <ErrorState message="Sınav bulunamadı." />;

  const exam = data.exam;

  function start() {
    let list = [...pool];
    if (mixOrder) list = shuffle(list);
    if (count !== "all") list = list.slice(0, Number(count));
    setSession(list);
  }

  if (session) {
    const discName =
      discipline === "all" ? "Tüm dersler" : exam.disciplines.find((d) => d.id === discipline)?.name;
    return (
      <QuizSession
        title={`${exam.shortLabel} · Test Modu`}
        subtitle={`${discName} · ${
          revealMode === "immediate" ? "anında geri bildirim" : "sonda değerlendirme"
        } · ${session.length} soru`}
        questions={session}
        revealMode={revealMode}
        onRestart={start}
        backTo={`/sinav/${exam.id}`}
        backLabel="Sınav sayfası"
      />
    );
  }

  const questionCount = count === "all" ? pool.length : Math.min(pool.length, Number(count));

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <Link to={`/sinav/${exam.id}`} className="inline-flex items-center gap-1 transition hover:text-indigo-600 dark:hover:text-indigo-300">
          <ArrowLeft className="h-3.5 w-3.5" />
          {exam.shortLabel}
        </Link>
        <ChevronRight className="h-3 w-3" />
        <span className="font-medium text-slate-700 dark:text-slate-300">Test modu</span>
      </div>

      <div className="mt-4">
        <span className="chip border-indigo-200 bg-indigo-50 text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
          <Target className="h-3.5 w-3.5" />
          Test modu
        </span>
        <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
          {exam.label} testi
        </h1>
        <p className="mt-1.5 text-sm text-slate-500 dark:text-slate-400">
          Dersini, geri bildirim biçimini ve soru sayısını seç. Cevapların ilerlemene otomatik kaydedilir.
        </p>
      </div>

      <div className="mt-6 grid gap-4 lg:grid-cols-[minmax(0,1fr)_300px]">
        <div className="space-y-4">
          <section className="card p-5 sm:p-6">
            <h2 className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
              <ListChecks className="h-4 w-4 text-indigo-500" />
              1 · Ders seç
            </h2>
            <div className="mt-3 flex flex-wrap gap-2">
              <OptionChip
                active={discipline === "all"}
                onClick={() => setDiscipline("all")}
                label="Tüm dersler"
                hint={`${data.questions.length} soru`}
              />
              {exam.disciplines.map((d) => (
                <OptionChip
                  key={d.id}
                  active={discipline === d.id}
                  onClick={() => setDiscipline(d.id)}
                  label={d.name}
                  hint={`${d.questionCount} soru`}
                />
              ))}
            </div>
          </section>

          <section className="card p-5 sm:p-6">
            <h2 className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
              <Zap className="h-4 w-4 text-indigo-500" />
              2 · Geri bildirim
            </h2>
            <div className="mt-3 grid gap-3 sm:grid-cols-2">
              <ModeCard
                active={revealMode === "immediate"}
                onClick={() => setRevealMode("immediate")}
                icon={CheckCircle2}
                title="Anında geri bildirim"
                text="Her soruda cevabını işaretler işaretlemez doğrusunu görürsün."
              />
              <ModeCard
                active={revealMode === "end"}
                onClick={() => setRevealMode("end")}
                icon={Clock}
                title="Sonda değerlendirme"
                text="Test bitene kadar cevap gösterilmez; sonunda toplu sonuç alırsın."
              />
            </div>
          </section>

          <section className="card p-5 sm:p-6">
            <h2 className="flex items-center gap-2 text-sm font-bold text-slate-900 dark:text-white">
              <Shuffle className="h-4 w-4 text-indigo-500" />
              3 · Soru sayısı ve sıra
            </h2>
            <div className="mt-3 flex flex-wrap gap-2">
              {(["all", "10", "20", "50"] as CountOption[]).map((option) => (
                <OptionChip
                  key={option}
                  active={count === option}
                  onClick={() => setCount(option)}
                  label={option === "all" ? "Tümü" : `${option} soru`}
                  hint={option === "all" ? `${pool.length} soru` : undefined}
                />
              ))}
            </div>

            <label className="mt-4 flex cursor-pointer items-center gap-2.5 rounded-xl border border-slate-200 px-3.5 py-3 text-sm text-slate-700 transition hover:bg-slate-50 dark:border-slate-700 dark:text-slate-200 dark:hover:bg-slate-800/60">
              <input
                type="checkbox"
                checked={mixOrder}
                onChange={(e) => setMixOrder(e.target.checked)}
                className="h-4 w-4 rounded border-slate-300 text-indigo-600 accent-indigo-600"
              />
              <span>
                Soruları karıştır
                <span className="ml-1 text-xs text-slate-400">(sınav sırası yerine rastgele)</span>
              </span>
            </label>
          </section>
        </div>

        <aside>
          <div className="card p-5 lg:sticky lg:top-20">
            <h2 className="text-sm font-bold text-slate-900 dark:text-white">Test özeti</h2>
            <dl className="mt-4 space-y-2.5 text-sm">
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Sınav</dt>
                <dd className="font-semibold text-slate-900 dark:text-white">{exam.shortLabel}</dd>
              </div>
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Ders</dt>
                <dd className="max-w-[60%] truncate text-right font-semibold text-slate-900 dark:text-white">
                  {discipline === "all"
                    ? "Tüm dersler"
                    : exam.disciplines.find((d) => d.id === discipline)?.name}
                </dd>
              </div>
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Soru</dt>
                <dd className="font-semibold text-slate-900 dark:text-white">{questionCount}</dd>
              </div>
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Mod</dt>
                <dd className="font-semibold text-slate-900 dark:text-white">
                  {revealMode === "immediate" ? "Anında" : "Sonda"}
                </dd>
              </div>
              <div className="flex items-center justify-between gap-2">
                <dt className="text-slate-500 dark:text-slate-400">Sıra</dt>
                <dd className="font-semibold text-slate-900 dark:text-white">
                  {mixOrder ? "Karışık" : "Sınav sırası"}
                </dd>
              </div>
            </dl>

            <button type="button" className="btn-primary mt-5 w-full" onClick={start} disabled={questionCount === 0}>
              <Target className="h-4 w-4" />
              Testi başlat
            </button>

            <div className="mt-4 flex items-start gap-2 rounded-xl bg-slate-50 px-3 py-2.5 text-[11px] leading-relaxed text-slate-500 dark:bg-slate-800/60 dark:text-slate-400">
              <Sparkles className="mt-0.5 h-3.5 w-3.5 shrink-0 text-amber-500" />
              <p>
                Cevabı kaynakta okunamayan sorular AI çözümü olarak işaretlidir. Sonuç ekranında
                doğruluk oranlarını ders bazında görürsün.
              </p>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}

function OptionChip({
  active,
  onClick,
  label,
  hint,
}: {
  active: boolean;
  onClick: () => void;
  label: string;
  hint?: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "inline-flex items-center gap-2 rounded-xl border px-3 py-2 text-xs font-semibold transition",
        active
          ? "border-indigo-500 bg-indigo-50 text-indigo-700 ring-1 ring-indigo-500 dark:border-indigo-400 dark:bg-indigo-500/10 dark:text-indigo-300 dark:ring-indigo-400"
          : "border-slate-200 bg-white text-slate-600 hover:border-indigo-300 hover:text-indigo-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300 dark:hover:border-indigo-500/60 dark:hover:text-indigo-300",
      )}
    >
      {label}
      {hint && <span className="text-[10px] font-normal text-slate-400">{hint}</span>}
    </button>
  );
}

function ModeCard({
  active,
  onClick,
  icon: Icon,
  title,
  text,
}: {
  active: boolean;
  onClick: () => void;
  icon: typeof CheckCircle2;
  title: string;
  text: string;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "flex flex-col items-start rounded-xl border p-4 text-left transition",
        active
          ? "border-indigo-500 bg-indigo-50 ring-1 ring-indigo-500 dark:border-indigo-400 dark:bg-indigo-500/10 dark:ring-indigo-400"
          : "border-slate-200 bg-white hover:border-indigo-300 dark:border-slate-700 dark:bg-slate-900 dark:hover:border-indigo-500/60",
      )}
    >
      <Icon className={cn("h-4 w-4", active ? "text-indigo-600 dark:text-indigo-300" : "text-slate-400")} />
      <span className="mt-2 text-sm font-semibold text-slate-900 dark:text-white">{title}</span>
      <span className="mt-1 text-xs leading-relaxed text-slate-500 dark:text-slate-400">{text}</span>
    </button>
  );
}
