import { useMemo, useState } from "react";
import { Link } from "react-router-dom";
import {
  ArrowRight,
  BarChart3,
  BookOpenCheck,
  CheckCircle2,
  Target,
  Trash2,
  TrendingUp,
  XCircle,
} from "lucide-react";
import { useAllExams } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { useProgressStore } from "../store/useProgressStore";
import { PageLoader, ErrorState, LinearProgress } from "../components/Loading";
import { cn, disciplineStyle, percent } from "../lib/utils";

export function ProgressPage() {
  usePageTitle("İlerleme");
  const { data, loading, error } = useAllExams();
  const answers = useProgressStore((s) => s.answers);
  const reset = useProgressStore((s) => s.reset);
  const [resetting, setResetting] = useState(false);

  const stats = useMemo(() => {
    const list = Object.values(answers);
    const correct = list.filter((a) => a.correct).length;
    return {
      answered: list.length,
      correct,
      wrong: list.length - correct,
      accuracy: percent(correct, list.length),
    };
  }, [answers]);

  const perExam = useMemo(() => {
    if (!data) return [];
    return data.map((exam) => {
      const list = Object.values(answers).filter((a) => a.examId === exam.exam.id);
      const correct = list.filter((a) => a.correct).length;
      return {
        exam: exam.exam,
        total: exam.questions.length,
        answered: list.length,
        correct,
        accuracy: percent(correct, list.length),
      };
    });
  }, [data, answers]);

  const perDiscipline = useMemo(() => {
    if (!data) return [];
    const map = new Map<
      string,
      { id: string; name: string; total: number; answered: number; correct: number }
    >();
    for (const exam of data) {
      for (const q of exam.questions) {
        const item = map.get(q.disciplineId) ?? {
          id: q.disciplineId,
          name: q.discipline,
          total: 0,
          answered: 0,
          correct: 0,
        };
        item.total += 1;
        const a = answers[q.id];
        if (a) {
          item.answered += 1;
          if (a.correct) item.correct += 1;
        }
        map.set(q.disciplineId, item);
      }
    }
    return [...map.values()].sort((a, b) => b.total - a.total);
  }, [data, answers]);

  if (loading) return <PageLoader label="İlerleme yükleniyor…" />;
  if (error) return <ErrorState message={error} />;

  const totalQuestions = (data ?? []).reduce((sum, exam) => sum + exam.questions.length, 0);

  async function handleReset() {
    if (!window.confirm("Tüm çözüm geçmişin silinecek. Emin misin?")) return;
    setResetting(true);
    try {
      await reset();
    } finally {
      setResetting(false);
    }
  }

  return (
    <div className="page-shell py-6 sm:py-8">
      <div>
        <span className="chip border-indigo-200 bg-indigo-50 text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
          <BarChart3 className="h-3.5 w-3.5" />
          İlerleme
        </span>
        <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
          Nerede olduğunu gör
        </h1>
        <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          Cevapların bu tarayıcıda saklanır. Ders bazında doğruluk oranlarını ve eksik kalan
          soruları buradan takip edebilirsin.
        </p>
      </div>

      {stats.answered === 0 ? (
        <div className="card mt-6 p-10 text-center">
          <span className="mx-auto flex h-12 w-12 items-center justify-center rounded-2xl bg-indigo-50 text-indigo-600 dark:bg-indigo-500/10 dark:text-indigo-300">
            <Target className="h-6 w-6" />
          </span>
          <h2 className="mt-4 text-lg font-bold text-slate-900 dark:text-white">Henüz soru çözmedin</h2>
          <p className="mx-auto mt-2 max-w-md text-sm text-slate-500 dark:text-slate-400">
            İlk soruyu çözdüğünde burada genel doğruluk oranın, ders dağılımın ve kalan soruların
            görünecek.
          </p>
          <div className="mt-5 flex flex-wrap justify-center gap-2">
            <Link to="/cikmislar" className="btn-primary">
              <BookOpenCheck className="h-4 w-4" />
              Çıkmışlara git
            </Link>
            <Link to="/rastgele" className="btn-secondary">
              Rastgele soru
            </Link>
          </div>
        </div>
      ) : (
        <>
          <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
            <StatCard
              label="Genel ilerleme"
              value={`${stats.answered}`}
              hint={`/ ${totalQuestions} soru`}
              icon={TrendingUp}
              tone="indigo"
            />
            <StatCard label="Doğru" value={`${stats.correct}`} hint="cevap" icon={CheckCircle2} tone="emerald" />
            <StatCard label="Yanlış" value={`${stats.wrong}`} hint="cevap" icon={XCircle} tone="rose" />
            <StatCard label="Doğruluk" value={`%${stats.accuracy}`} hint="cevaplanan içinde" icon={Target} tone="amber" />
          </div>

          <div className="card mt-4 p-5 sm:p-6">
            <div className="flex flex-wrap items-center justify-between gap-2">
              <h2 className="text-sm font-bold text-slate-900 dark:text-white">Genel tamamlanma</h2>
              <span className="text-xs font-semibold text-indigo-600 dark:text-indigo-300">
                %{percent(stats.answered, totalQuestions)}
              </span>
            </div>
            <LinearProgress value={percent(stats.answered, totalQuestions)} className="mt-3" />
            <p className="mt-2 text-xs text-slate-500 dark:text-slate-400">
              {stats.answered} / {totalQuestions} soru çözüldü. {Math.max(0, totalQuestions - stats.answered)} soru
              seni bekliyor.
            </p>
          </div>

          <div className="mt-6 grid gap-4 lg:grid-cols-2">
            <section className="card p-5 sm:p-6">
              <h2 className="text-sm font-bold text-slate-900 dark:text-white">Sınavlar</h2>
              <div className="mt-4 space-y-4">
                {perExam.map((item) => (
                  <div key={item.exam.id}>
                    <div className="mb-1.5 flex items-center justify-between gap-2">
                      <Link
                        to={`/sinav/${item.exam.id}`}
                        className="truncate text-sm font-semibold text-slate-800 hover:text-indigo-600 dark:text-slate-100 dark:hover:text-indigo-300"
                      >
                        {item.exam.label}
                      </Link>
                      <span className="shrink-0 text-xs tabular-nums text-slate-500 dark:text-slate-400">
                        {item.answered}/{item.total} · %{item.accuracy}
                      </span>
                    </div>
                    <LinearProgress value={percent(item.answered, item.total)} />
                  </div>
                ))}
              </div>
            </section>

            <section className="card p-5 sm:p-6">
              <h2 className="text-sm font-bold text-slate-900 dark:text-white">Ders bazında doğruluk</h2>
              <div className="mt-4 space-y-3">
                {perDiscipline.map((d) => {
                  const style = disciplineStyle(d.id);
                  return (
                    <div key={d.id}>
                      <div className="mb-1 flex items-center justify-between gap-2 text-xs">
                        <span className="flex min-w-0 items-center gap-1.5 font-medium text-slate-700 dark:text-slate-200">
                          <span className={cn("h-1.5 w-1.5 shrink-0 rounded-full", style.dot)} />
                          <span className="truncate">{d.name}</span>
                        </span>
                        <span className="shrink-0 tabular-nums text-slate-500 dark:text-slate-400">
                          {d.correct}/{d.answered || 0} · %{percent(d.correct, d.answered)}
                        </span>
                      </div>
                      <div className="h-1.5 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
                        <div
                          className={cn("h-full rounded-full", style.bar)}
                          style={{ width: `${percent(d.correct, d.answered)}` }}
                        />
                      </div>
                    </div>
                  );
                })}
              </div>
            </section>
          </div>

          <div className="mt-6 flex flex-col items-start justify-between gap-3 rounded-2xl border border-slate-200 bg-white p-5 sm:flex-row sm:items-center dark:border-slate-800 dark:bg-slate-900">
            <div>
              <h2 className="text-sm font-semibold text-slate-900 dark:text-white">Çözüm geçmişini sıfırla</h2>
              <p className="mt-1 text-xs text-slate-500 dark:text-slate-400">
                Bu işlem yalnızca bu tarayıcıdaki cevap kayıtlarını siler, geri alınamaz.
              </p>
            </div>
            <button
              type="button"
              onClick={handleReset}
              disabled={resetting}
              className="btn border border-rose-200 bg-rose-50 text-rose-700 hover:bg-rose-100 dark:border-rose-500/30 dark:bg-rose-500/10 dark:text-rose-300 dark:hover:bg-rose-500/20"
            >
              <Trash2 className="h-4 w-4" />
              {resetting ? "Sıfırlanıyor…" : "Geçmişi sıfırla"}
            </button>
          </div>

          <div className="mt-6 flex justify-end">
            <Link
              to="/cikmislar"
              className="inline-flex items-center gap-1 text-sm font-semibold text-indigo-600 hover:text-indigo-700 dark:text-indigo-300"
            >
              Çalışmaya devam et
              <ArrowRight className="h-4 w-4" />
            </Link>
          </div>
        </>
      )}
    </div>
  );
}

const TONES = {
  indigo: "bg-indigo-50 text-indigo-600 dark:bg-indigo-500/10 dark:text-indigo-300",
  emerald: "bg-emerald-50 text-emerald-600 dark:bg-emerald-500/10 dark:text-emerald-300",
  rose: "bg-rose-50 text-rose-600 dark:bg-rose-500/10 dark:text-rose-300",
  amber: "bg-amber-50 text-amber-600 dark:bg-amber-500/10 dark:text-amber-300",
} as const;

function StatCard({
  label,
  value,
  hint,
  icon: Icon,
  tone,
}: {
  label: string;
  value: string;
  hint: string;
  icon: typeof TrendingUp;
  tone: keyof typeof TONES;
}) {
  return (
    <div className="card p-4 sm:p-5">
      <div className="flex items-center justify-between">
        <p className="text-xs font-medium text-slate-500 dark:text-slate-400">{label}</p>
        <span className={cn("flex h-8 w-8 items-center justify-center rounded-lg", TONES[tone])}>
          <Icon className="h-4 w-4" />
        </span>
      </div>
      <p className="mt-2 text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
        {value}
        <span className="ml-1 text-xs font-medium text-slate-400">{hint}</span>
      </p>
    </div>
  );
}
