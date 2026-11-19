import { useEffect, useMemo, useState } from "react";
import { Link, useParams, useSearchParams } from "react-router-dom";
import { ArrowLeft, ChevronRight, Clock, Flame, ListTree, Play } from "lucide-react";
import type { Question, Topic } from "../types";
import { useAllExams } from "../lib/hooks";
import { loadTopics } from "../lib/data";
import { usePageTitle } from "../lib/useTitle";
import { useProgressStore } from "../store/useProgressStore";
import { PageLoader, ErrorState } from "../components/Loading";
import { QuestionCard } from "../components/QuestionCard";
import { QuizSession } from "../components/QuizSession";
import { cn, disciplineStyle, percent, shuffle } from "../lib/utils";

const DISCIPLINE_ORDER = [
  "biyokimya",
  "biyofizik",
  "fizyoloji",
  "histoloji",
  "mikrobiyoloji",
  "davranis-bilimleri",
  "tip-tarihi-etik",
  "diger",
];
const DISCIPLINE_NAME: Record<string, string> = {
  "davranis-bilimleri": "Davranış Bilimleri",
  "tip-tarihi-etik": "Tıp Tarihi ve Etik",
  diger: "Diğer",
  biyokimya: "Biyokimya",
  biyofizik: "Biyofizik",
  fizyoloji: "Fizyoloji",
  histoloji: "Histoloji",
  mikrobiyoloji: "Mikrobiyoloji",
};

function useTopicData() {
  const { data, loading, error } = useAllExams();
  const [topics, setTopics] = useState<Topic[] | null>(null);
  const [topicError, setTopicError] = useState<string | null>(null);

  useEffect(() => {
    let alive = true;
    loadTopics()
      .then((t) => {
        if (alive) setTopics(t.topics);
      })
      .catch((err: unknown) => {
        if (alive) setTopicError(err instanceof Error ? err.message : "Konular yüklenemedi.");
      });
    return () => {
      alive = false;
    };
  }, []);

  const byTopic = useMemo(() => {
    const map = new Map<string, Question[]>();
    for (const exam of data ?? []) {
      for (const q of exam.questions) {
        if (!q.topicId) continue;
        const list = map.get(q.topicId);
        if (list) list.push(q);
        else map.set(q.topicId, [q]);
      }
    }
    return map;
  }, [data]);

  const shortLabel = useMemo(() => {
    const m = new Map<string, string>();
    for (const exam of data ?? []) m.set(exam.exam.id, exam.exam.shortLabel);
    return m;
  }, [data]);

  return {
    loading: loading || (!topics && !topicError),
    error: error ?? topicError,
    topics: topics ?? [],
    byTopic,
    shortLabel,
    exams: data ?? [],
  };
}

/** Bir konunun hangi sınavlarda (yıllarda) kaç soruyla çıktığı. */
function yearCounts(questions: Question[], exams: { exam: { id: string; shortLabel: string } }[]) {
  return exams
    .map((e) => ({
      id: e.exam.id,
      label: e.exam.shortLabel,
      count: questions.filter((q) => q.examId === e.exam.id).length,
    }))
    .sort((a, b) => a.id.localeCompare(b.id));
}

function ViewToggle({ view, onChange }: { view: "ders" | "sik"; onChange: (v: "ders" | "sik") => void }) {
  const items: { id: "ders" | "sik"; label: string; icon: typeof ListTree }[] = [
    { id: "ders", label: "Ders ders", icon: ListTree },
    { id: "sik", label: "En sık çıkanlar", icon: Flame },
  ];
  return (
    <div className="mt-6 inline-flex rounded-xl border border-slate-200 bg-white p-1 dark:border-slate-700 dark:bg-slate-900" role="tablist">
      {items.map((it) => {
        const Icon = it.icon;
        return (
          <button
            key={it.id}
            type="button"
            role="tab"
            aria-selected={view === it.id}
            onClick={() => onChange(it.id)}
            className={cn(
              "inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-xs font-semibold transition",
              view === it.id
                ? "bg-indigo-600 text-white shadow-sm"
                : "text-slate-600 hover:text-indigo-600 dark:text-slate-300 dark:hover:text-indigo-300",
            )}
          >
            <Icon className="h-3.5 w-3.5" />
            {it.label}
          </button>
        );
      })}
    </div>
  );
}

export function TopicsPage() {
  usePageTitle("Konular");
  const { loading, error, topics, byTopic, exams } = useTopicData();
  const answers = useProgressStore((s) => s.answers);
  const [params, setParams] = useSearchParams();
  const view: "ders" | "sik" = params.get("gorunum") === "sik" ? "sik" : "ders";
  const active = params.get("ders") ?? (view === "sik" ? "hepsi" : "biyokimya");

  if (loading) return <PageLoader label="Konular hazırlanıyor…" />;
  if (error) return <ErrorState message={error} />;

  function setView(v: "ders" | "sik") {
    setParams(v === "sik" ? { gorunum: "sik" } : {}, { replace: true });
  }

  if (view === "sik") {
    const rows = topics
      .map((t) => {
        const qs = byTopic.get(t.id) ?? [];
        const years = yearCounts(qs, exams);
        return { topic: t, total: qs.length, years, hit: years.filter((y) => y.count > 0).length };
      })
      .filter((r) => r.topic.id !== "dg-entegre")
      .filter((r) => r.total > 0 && (active === "hepsi" || r.topic.disciplineId === active))
      .sort((a, b) => b.hit - a.hit || b.total - a.total);
    const yearLabels = yearCounts([], exams);
    const maxCell = Math.max(1, ...rows.flatMap((r) => r.years.map((y) => y.count)));

    return (
      <div className="page-shell py-8 sm:py-10">
        <span className="chip border-indigo-200 bg-indigo-50 text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
          <ListTree className="h-3.5 w-3.5" />
          Konular
        </span>
        <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
          En sık çıkan konular
        </h1>
        <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          {exams.length} yılın sorularına göre sıralandı: önce kaç farklı yıl çıktığına, sonra toplam soru sayısına
          bakılır. Kutudaki sayı o yıl o konudan kaç soru geldiğini gösterir.
        </p>

        <ViewToggle view={view} onChange={setView} />

        <div className="mt-4 flex flex-wrap gap-2">
          {["hepsi", ...DISCIPLINE_ORDER].map((id) => (
            <button
              key={id}
              type="button"
              onClick={() => setParams({ gorunum: "sik", ders: id }, { replace: true })}
              className={cn(
                "rounded-xl border px-3 py-1.5 text-xs font-semibold transition",
                active === id
                  ? "border-indigo-500 bg-indigo-50 text-indigo-700 ring-1 ring-indigo-500 dark:border-indigo-400 dark:bg-indigo-500/10 dark:text-indigo-300 dark:ring-indigo-400"
                  : "border-slate-200 bg-white text-slate-600 hover:border-indigo-300 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300",
              )}
            >
              {id === "hepsi" ? "Tüm dersler" : DISCIPLINE_NAME[id]}
            </button>
          ))}
        </div>

        <div className="card mt-5 overflow-x-auto">
          <table className="w-full min-w-[640px] border-collapse text-left text-sm">
            <thead>
              <tr className="border-b border-slate-200 text-[11px] uppercase tracking-wide text-slate-400 dark:border-slate-800">
                <th className="px-4 py-3 font-semibold">Konu</th>
                {yearLabels.map((y) => (
                  <th key={y.id} className="px-1 py-3 text-center font-semibold">
                    {y.label}
                  </th>
                ))}
                <th className="px-4 py-3 text-right font-semibold">Yıl</th>
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.topic.id} className="border-b border-slate-100 last:border-0 dark:border-slate-800/70">
                  <td className="px-4 py-2.5">
                    <Link
                      to={`/konular/${r.topic.id}`}
                      className="font-semibold text-slate-900 hover:text-indigo-600 dark:text-white dark:hover:text-indigo-300"
                    >
                      {r.topic.name}
                    </Link>
                    {active === "hepsi" && (
                      <span className="ml-2 text-[11px] text-slate-400">{DISCIPLINE_NAME[r.topic.disciplineId]}</span>
                    )}
                  </td>
                  {r.years.map((y) => (
                    <td key={y.id} className="px-1 py-2.5 text-center">
                      <span
                        className={cn(
                          "inline-flex h-7 w-9 items-center justify-center rounded-md text-xs font-bold tabular-nums",
                          y.count === 0
                            ? "bg-slate-100 text-slate-300 dark:bg-slate-800 dark:text-slate-600"
                            : "text-white",
                        )}
                        style={
                          y.count > 0
                            ? { backgroundColor: `rgba(79, 70, 229, ${0.35 + 0.65 * (y.count / maxCell)})` }
                            : undefined
                        }
                        title={`${y.label}: ${y.count} soru`}
                      >
                        {y.count === 0 ? "–" : y.count}
                      </span>
                    </td>
                  ))}
                  <td className="px-4 py-2.5 text-right">
                    <span
                      className={cn(
                        "rounded-full px-2 py-0.5 text-[11px] font-bold tabular-nums",
                        r.hit === exams.length
                          ? "bg-emerald-100 text-emerald-700 dark:bg-emerald-500/15 dark:text-emerald-300"
                          : "bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-300",
                      )}
                    >
                      {r.hit}/{exams.length}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {rows.length === 0 && (
            <p className="p-8 text-center text-sm text-slate-500 dark:text-slate-400">Bu derste konu bulunamadı.</p>
          )}
        </div>
      </div>
    );
  }

  const counts = new Map<string, number>();
  for (const t of topics) counts.set(t.disciplineId, (counts.get(t.disciplineId) ?? 0) + (byTopic.get(t.id)?.length ?? 0));
  const list = topics.filter((t) => t.disciplineId === active).filter((t) => (byTopic.get(t.id)?.length ?? 0) > 0);
  const style = disciplineStyle(active);

  return (
    <div className="page-shell py-8 sm:py-10">
      <span className="chip border-indigo-200 bg-indigo-50 text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
        <ListTree className="h-3.5 w-3.5" />
        Konular
      </span>
      <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
        Konu konu çıkmışlar
      </h1>
      <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-slate-500 dark:text-slate-400">
        Dersi seç, konuyu aç; tüm yıllardaki o konunun soruları tek yerde. Yeşil çubuk doğrularını,
        kırmızı yanlışlarını gösterir. Takvimde karşılığı olmayan sorular “Diğer” başlığında.
      </p>

      <ViewToggle view={view} onChange={setView} />

      <div className="mt-4 flex flex-wrap gap-2">
        {DISCIPLINE_ORDER.map((id) => (
          <button
            key={id}
            type="button"
            onClick={() => setParams({ ders: id }, { replace: true })}
            className={cn(
              "rounded-xl border px-3 py-2 text-xs font-semibold transition",
              active === id
                ? "border-indigo-500 bg-indigo-50 text-indigo-700 ring-1 ring-indigo-500 dark:border-indigo-400 dark:bg-indigo-500/10 dark:text-indigo-300 dark:ring-indigo-400"
                : "border-slate-200 bg-white text-slate-600 hover:border-indigo-300 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300",
            )}
          >
            {DISCIPLINE_NAME[id]} · {counts.get(id) ?? 0}
          </button>
        ))}
      </div>

      <div className="mt-5 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {list.map((t) => {
          const qs = byTopic.get(t.id) ?? [];
          const done = qs.filter((q) => answers[q.id]).length;
          const correct = qs.filter((q) => answers[q.id]?.correct).length;
          const hit = new Set(qs.map((q) => q.examId)).size;
          return (
            <Link
              key={t.id}
              to={`/konular/${t.id}`}
              className="card group flex flex-col gap-3 p-4 transition hover:border-indigo-300 dark:hover:border-indigo-500/60"
            >
              <div className="flex items-start justify-between gap-2">
                <h2 className="text-sm font-bold leading-snug text-slate-900 dark:text-white">{t.name}</h2>
                <ChevronRight className="mt-0.5 h-4 w-4 shrink-0 text-slate-300 transition group-hover:translate-x-0.5 group-hover:text-indigo-500" />
              </div>
              <div className="mt-auto flex flex-wrap items-center gap-2 text-[11px]">
                <span className={cn("rounded-full px-2 py-0.5 font-semibold", style.soft, style.text)}>
                  {qs.length} soru
                </span>
                <span
                  className={cn(
                    "inline-flex items-center gap-1 rounded-full px-2 py-0.5 font-semibold",
                    hit === exams.length
                      ? "bg-emerald-100 text-emerald-700 dark:bg-emerald-500/15 dark:text-emerald-300"
                      : "bg-slate-100 text-slate-500 dark:bg-slate-800 dark:text-slate-400",
                  )}
                  title={`${exams.length} sınavın ${hit} tanesinde çıktı`}
                >
                  <Flame className="h-3 w-3" />
                  {hit}/{exams.length} yıl
                </span>
                {t.hours > 0 && (
                  <span className="inline-flex items-center gap-1 text-slate-400">
                    <Clock className="h-3 w-3" />
                    {t.hours} saat
                  </span>
                )}
                {done >= 3 && percent(correct, done) < 60 && (
                  <span className="ml-auto rounded-full bg-amber-100 px-2 py-0.5 font-semibold text-amber-700 dark:bg-amber-500/15 dark:text-amber-300">
                    Zayıf
                  </span>
                )}
                {done >= 3 && percent(correct, done) >= 80 && (
                  <span className="ml-auto rounded-full bg-emerald-100 px-2 py-0.5 font-semibold text-emerald-700 dark:bg-emerald-500/15 dark:text-emerald-300">
                    Güçlü
                  </span>
                )}
              </div>
              <div>
                <div
                  className="flex h-1.5 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800"
                  role="progressbar"
                  aria-label={`${t.name}: ${done} / ${qs.length} soru çözüldü, ${correct} doğru`}
                  aria-valuemin={0}
                  aria-valuemax={qs.length}
                  aria-valuenow={done}
                >
                  <div className="bg-emerald-500" style={{ width: `${percent(correct, qs.length)}%` }} />
                  <div className="bg-rose-400" style={{ width: `${percent(done - correct, qs.length)}%` }} />
                </div>
                <p className="mt-1.5 text-[11px] text-slate-400 dark:text-slate-500">
                  {done === 0
                    ? "Henüz çözmedin"
                    : `${done}/${qs.length} çözüldü · ${correct} doğru`}
                </p>
              </div>
            </Link>
          );
        })}
      </div>
      {list.length === 0 && (
        <div className="card mt-5 p-8 text-center text-sm text-slate-500 dark:text-slate-400">Bu derste konu bulunamadı.</div>
      )}
    </div>
  );
}

export function TopicDetailPage() {
  const { topicId } = useParams<{ topicId: string }>();
  const { loading, error, topics, byTopic, shortLabel, exams } = useTopicData();
  const [examFilter, setExamFilter] = useState("all");
  const [session, setSession] = useState<Question[] | null>(null);
  const topic = topics.find((t) => t.id === topicId);
  usePageTitle(topic?.name);

  const all = byTopic.get(topicId ?? "") ?? [];
  const questions = useMemo(
    () =>
      all
        .filter((q) => examFilter === "all" || q.examId === examFilter)
        .sort((a, b) => (a.examId === b.examId ? a.number - b.number : b.examId.localeCompare(a.examId))),
    [all, examFilter],
  );

  if (loading) return <PageLoader label="Konu yükleniyor…" />;
  if (error) return <ErrorState message={error} />;
  if (!topic) return <ErrorState message="Konu bulunamadı." />;

  const examChips = exams
    .map((e) => ({ id: e.exam.id, label: e.exam.shortLabel, count: all.filter((q) => q.examId === e.exam.id).length }))
    .filter((e) => e.count > 0);
  const style = disciplineStyle(topic.disciplineId);

  if (session) {
    return (
      <QuizSession
        title={topic.name}
        subtitle={`${DISCIPLINE_NAME[topic.disciplineId]} · ${session.length} soru`}
        questions={session}
        revealMode="immediate"
        onRestart={() => setSession(shuffle(questions))}
        backTo={`/konular/${topic.id}`}
        backLabel="Konu sayfası"
      />
    );
  }

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <Link
          to={`/konular?ders=${topic.disciplineId}`}
          className="inline-flex items-center gap-1 transition hover:text-indigo-600 dark:hover:text-indigo-300"
        >
          <ArrowLeft className="h-3.5 w-3.5" />
          Konular
        </Link>
        <ChevronRight className="h-3 w-3" />
        <span className="font-medium text-slate-700 dark:text-slate-300">{DISCIPLINE_NAME[topic.disciplineId]}</span>
      </div>

      <div className="mt-4 flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <span className={cn("rounded-full px-2.5 py-1 text-[11px] font-semibold", style.soft, style.text)}>
            {DISCIPLINE_NAME[topic.disciplineId]}
          </span>
          <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
            {topic.name}
          </h1>
          <p className="mt-1.5 text-sm text-slate-500 dark:text-slate-400">
            {all.length} soru · {examChips.length} sınavdan
            {topic.hours > 0 && ` · takvimde ${topic.hours} saat`}
          </p>
        </div>
        <button
          type="button"
          className="btn-primary self-start sm:self-auto"
          disabled={questions.length === 0}
          onClick={() => setSession(shuffle(questions))}
        >
          <Play className="h-4 w-4" />
          Bu konudan çöz ({questions.length})
        </button>
      </div>

      <div className="mt-5 flex flex-wrap gap-1.5">
        <Chip active={examFilter === "all"} label="Tüm yıllar" count={all.length} onClick={() => setExamFilter("all")} />
        {examChips.map((e) => (
          <Chip key={e.id} active={examFilter === e.id} label={e.label} count={e.count} onClick={() => setExamFilter(e.id)} />
        ))}
      </div>

      <div className="mt-4 grid gap-4">
        {questions.map((q) => (
          <QuestionCard key={q.id} question={q} showDiscipline={topic.disciplineId === "diger"} examLabel={shortLabel.get(q.examId)} />
        ))}
      </div>
    </div>
  );
}

function Chip({ active, label, count, onClick }: { active: boolean; label: string; count: number; onClick: () => void }) {
  return (
    <button
      type="button"
      onClick={onClick}
      className={cn(
        "inline-flex h-7 items-center gap-1.5 rounded-full border px-2.5 text-[11px] font-semibold transition",
        active
          ? "border-indigo-600 bg-indigo-600 text-white shadow-sm"
          : "border-slate-200 bg-white text-slate-600 hover:border-indigo-300 hover:text-indigo-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-300",
      )}
    >
      {label}
      <span className={cn("rounded-full px-1 text-[10px] tabular-nums", active ? "bg-white/20" : "bg-slate-100 text-slate-500 dark:bg-slate-800 dark:text-slate-400")}>
        {count}
      </span>
    </button>
  );
}
