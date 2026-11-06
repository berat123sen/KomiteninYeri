import { useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import {
  ArrowLeft,
  CheckCircle2,
  ChevronRight,
  FileText,
  Filter,
  Search,
  Shuffle,
  Sparkles,
  Target,
  X,
  RotateCcw,
} from "lucide-react";
import { useExam } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { useProgressStore } from "../store/useProgressStore";
import { PageLoader, ErrorState } from "../components/Loading";
import { QuestionCard } from "../components/QuestionCard";
import { sourcePdfUrl } from "../lib/data";
import { cn, percent } from "../lib/utils";

export function ExamPage() {
  const { examId } = useParams<{ examId: string }>();
  const { data, loading, error } = useExam(examId);
  usePageTitle(data?.exam.label);
  const [params, setParams] = useSearchParams();
  const answers = useProgressStore((s) => s.answers);
  const resetExam = useProgressStore((s) => s.resetExam);
  const [query, setQuery] = useState("");
  const [onlyUnanswered, setOnlyUnanswered] = useState(false);

  const activeDiscipline = params.get("ders") ?? "all";

  const stats = useMemo(() => {
    if (!data) return { answered: 0, correct: 0, derived: 0 };
    let answered = 0;
    let correct = 0;
    let derived = 0;
    for (const q of data.questions) {
      const a = answers[q.id];
      if (a) {
        answered += 1;
        if (a.correct) correct += 1;
      }
      if (q.answerStatus !== "official") derived += 1;
    }
    return { answered, correct, derived };
  }, [data, answers]);

  if (loading) return <PageLoader label="Sınav yükleniyor…" />;
  if (error) return <ErrorState message={error} />;
  if (!data) return <ErrorState message="Sınav bulunamadı." />;

  const exam = data.exam;
  const norm = (value: string) => value.toLocaleLowerCase("tr");
  const filtered = data.questions.filter((q) => {
    if (activeDiscipline !== "all" && q.disciplineId !== activeDiscipline) return false;
    if (onlyUnanswered && answers[q.id]) return false;
    if (query.trim()) {
      const haystack = norm(`${q.stem} ${q.options.join(" ")}`);
      if (!haystack.includes(norm(query.trim()))) return false;
    }
    return true;
  });

  function setDiscipline(id: string) {
    const next = new URLSearchParams(params);
    if (id === "all") next.delete("ders");
    else next.set("ders", id);
    setParams(next, { replace: true });
  }

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <Link to="/cikmislar" className="inline-flex items-center gap-1 transition hover:text-indigo-600 dark:hover:text-indigo-300">
          <ArrowLeft className="h-3.5 w-3.5" />
          Çıkmışlar
        </Link>
        <ChevronRight className="h-3 w-3" />
        <span className="font-medium text-slate-700 dark:text-slate-300">{exam.label}</span>
      </div>

      <div className="mt-4 overflow-hidden rounded-2xl border border-slate-200 bg-gradient-to-br from-slate-900 to-slate-800 p-6 text-white sm:p-8 dark:border-slate-700">
        <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
          <div>
            <div className="flex flex-wrap items-center gap-2">
              <span className="rounded-full bg-white/10 px-2.5 py-1 text-[11px] font-semibold text-indigo-100">
                {exam.year}
              </span>
              <span className="rounded-full bg-white/10 px-2.5 py-1 text-[11px] font-semibold text-indigo-100">
                {exam.term}
              </span>
              <span
                className={cn(
                  "rounded-full px-2.5 py-1 text-[11px] font-semibold",
                  stats.derived > 0
                    ? "bg-amber-500/20 text-amber-200"
                    : "bg-emerald-500/20 text-emerald-200",
                )}
              >
                {stats.derived > 0
                  ? `Resmî + ${stats.derived} AI çözümü`
                  : exam.answerStatus === "official"
                    ? "Resmî cevap anahtarı"
                    : "AI çözümü"}
              </span>
            </div>
            <h1 className="mt-3 text-2xl font-extrabold tracking-tight sm:text-3xl">{exam.label}</h1>
            <p className="mt-1.5 max-w-2xl text-sm text-slate-300">
              Dönem {exam.period} · {exam.disciplines.length} ders · {exam.questionCount} soru
              {stats.derived > 0 && ` · ${stats.derived} AI çözümü`}
            </p>
          </div>

          <div className="flex flex-wrap gap-2">
            <Link to={`/test/${exam.id}`} className="btn bg-white text-slate-900 hover:bg-slate-100">
              <Target className="h-4 w-4" />
              Test modu
            </Link>
            <Link
              to={`/rastgele?ders=${activeDiscipline === "all" ? "" : activeDiscipline}`}
              className="btn border border-white/25 bg-white/10 text-white hover:bg-white/20"
            >
              <Shuffle className="h-4 w-4" />
              Rastgele
            </Link>
            <a
              href={sourcePdfUrl(exam.id)}
              target="_blank"
              rel="noreferrer"
              className="btn border border-white/25 bg-white/10 text-white hover:bg-white/20"
            >
              <FileText className="h-4 w-4" />
              Kaynak PDF
            </a>
            <button
              type="button"
              onClick={async () => {
                if (!window.confirm("Bu sınavın tüm işaretlemeleri silinecek. Yeniden çözmek istiyor musun?")) return;
                await resetExam(exam.id);
              }}
              className="btn border border-white/25 bg-white/10 text-white hover:bg-white/20"
            >
              <RotateCcw className="h-4 w-4" />
              Sıfırla
            </button>
          </div>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-3 sm:grid-cols-4">
          {[
            { label: "Toplam soru", value: exam.questionCount },
            { label: "Cevaplanan", value: stats.answered },
            {
              label: "Doğru",
              value: stats.correct,
              hint: `%${percent(stats.correct, Math.max(1, stats.answered))}`,
            },
            { label: "AI çözümü", value: stats.derived },
          ].map((item) => (
            <div key={item.label} className="rounded-xl bg-white/10 px-3 py-2.5">
              <p className="text-[11px] font-medium text-slate-300">{item.label}</p>
              <p className="mt-0.5 text-xl font-bold">
                {item.value}
                {item.hint && <span className="ml-1 text-xs font-medium text-slate-400">{item.hint}</span>}
              </p>
            </div>
          ))}
        </div>
      </div>

      <div className="z-30 -mx-4 mt-5 border-b border-slate-200/80 bg-slate-50/95 px-4 py-3 backdrop-blur sm:-mx-6 sm:px-6 lg:sticky lg:top-16 lg:-mx-8 lg:px-8 dark:border-slate-800/80 dark:bg-slate-950/95">
        <div className="flex flex-col gap-3 lg:flex-row lg:items-center lg:justify-between">
          <div className="flex flex-wrap gap-1.5">
            <FilterChip
              active={activeDiscipline === "all"}
              label="Tümü"
              count={exam.questionCount}
              onClick={() => setDiscipline("all")}
            />
            {exam.disciplines.map((d) => (
              <FilterChip
                key={d.id}
                active={activeDiscipline === d.id}
                label={d.name}
                count={d.questionCount}
                onClick={() => setDiscipline(d.id)}
              />
            ))}
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <div className="relative">
              <Search className="pointer-events-none absolute left-3 top-1/2 h-3.5 w-3.5 -translate-y-1/2 text-slate-400" />
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Sorularda ara…"
                className="h-9 w-44 rounded-lg border border-slate-200 bg-white pl-8 pr-8 text-xs text-slate-700 outline-none transition placeholder:text-slate-400 focus:border-indigo-400 focus:ring-2 focus:ring-indigo-100 sm:w-56 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200 dark:focus:border-indigo-500 dark:focus:ring-indigo-500/20"
              />
              {query && (
                <button
                  type="button"
                  onClick={() => setQuery("")}
                  className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600 dark:hover:text-slate-200"
                  aria-label="Aramayı temizle"
                >
                  <X className="h-3.5 w-3.5" />
                </button>
              )}
            </div>
            <button
              type="button"
              onClick={() => setOnlyUnanswered((v) => !v)}
              className={cn(
                "inline-flex h-9 items-center gap-1.5 rounded-lg border px-2.5 text-xs font-semibold transition",
                onlyUnanswered
                  ? "border-indigo-500 bg-indigo-50 text-indigo-700 dark:border-indigo-400 dark:bg-indigo-500/10 dark:text-indigo-300"
                  : "border-slate-200 bg-white text-slate-600 hover:bg-slate-50 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300 dark:hover:bg-slate-800",
              )}
            >
              <Filter className="h-3.5 w-3.5" />
              Çözülmeyenler
            </button>
          </div>
        </div>
      </div>

      <div className="mt-4 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
        <span>
          <strong className="text-slate-700 dark:text-slate-200">{filtered.length}</strong> soru
          gösteriliyor
        </span>
        <span className="inline-flex items-center gap-1">
          <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500" />
          {stats.answered} / {exam.questionCount} çözüldü
        </span>
      </div>

      {activeDiscipline !== "all" && (
        <div className="mt-4 flex items-start gap-2 rounded-xl bg-indigo-50 px-4 py-3 text-xs leading-relaxed text-indigo-800 dark:bg-indigo-500/10 dark:text-indigo-200">
          <Sparkles className="mt-0.5 h-4 w-4 shrink-0" />
          <p>
            {exam.disciplines.find((d) => d.id === activeDiscipline)?.name} filtresi aktif. Bu dersin
            sorularını test modunda çözmek için{" "}
            <Link to={`/test/${exam.id}?ders=${activeDiscipline}`} className="font-semibold underline">
              buraya tıkla
            </Link>
            .
          </p>
        </div>
      )}

      <div className="mt-4 grid gap-4">
        {filtered.map((q) => (
          <QuestionCard key={q.id} question={q} />
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="card mt-4 p-10 text-center">
          <p className="text-sm font-semibold text-slate-700 dark:text-slate-200">Sonuç bulunamadı</p>
          <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">
            Arama ifadesini veya filtreleri değiştirmeyi dene.
          </p>
          <button
            type="button"
            className="btn-secondary mt-4"
            onClick={() => {
              setQuery("");
              setOnlyUnanswered(false);
              setDiscipline("all");
            }}
          >
            Filtreleri temizle
          </button>
        </div>
      )}
    </div>
  );
}

function FilterChip({
  active,
  label,
  count,
  onClick,
}: {
  active: boolean;
  label: string;
  count: number;
  onClick: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "inline-flex h-7 items-center gap-1.5 rounded-full border px-2.5 text-[11px] font-semibold transition",
        active
          ? "border-indigo-600 bg-indigo-600 text-white shadow-sm"
          : "border-slate-200 bg-white text-slate-600 hover:border-indigo-300 hover:text-indigo-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300 dark:hover:border-indigo-500/60 dark:hover:text-indigo-300",
      )}
    >
      {label}
      <span
        className={cn(
          "rounded-full px-1 text-[10px] tabular-nums",
          active ? "bg-white/20 text-white" : "bg-slate-100 text-slate-500 dark:bg-slate-800 dark:text-slate-400",
        )}
      >
        {count}
      </span>
    </button>
  );
}
