import { Link } from "react-router-dom";
import { ArrowRight, BookOpenCheck, CalendarDays, Info, Layers } from "lucide-react";
import { useExamIndex } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { useProgressStore } from "../store/useProgressStore";
import { ExamCard } from "../components/ExamCard";
import { PageLoader, ErrorState } from "../components/Loading";
import { disciplineStyle } from "../lib/utils";

export function Browse() {
  usePageTitle("Çıkmışlar");
  const { index, loading, error } = useExamIndex();
  const answers = useProgressStore((s) => s.answers);

  if (loading) return <PageLoader label="Sınav arşivi yükleniyor…" />;
  if (error) return <ErrorState message={error} />;

  const exams = index?.exams ?? [];
  const disciplineMap = new Map<string, { id: string; name: string; count: number; examId: string }>();
  for (const exam of exams) {
    for (const d of exam.disciplines) {
      const current = disciplineMap.get(d.id);
      if (current) {
        current.count += d.questionCount;
      } else {
        disciplineMap.set(d.id, {
          id: d.id,
          name: d.name,
          count: d.questionCount,
          examId: exam.id,
        });
      }
    }
  }
  const disciplines = [...disciplineMap.values()].sort((a, b) => b.count - a.count);

  return (
    <div className="page-shell py-8 sm:py-10">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <span className="chip border-indigo-200 bg-indigo-50 text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
            <BookOpenCheck className="h-3.5 w-3.5" />
            Çıkmışlar
          </span>
          <h1 className="mt-3 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
            Dönem 1 / TEM 2 arşivi
          </h1>
          <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-slate-500 dark:text-slate-400">
            Sınavları yıla göre aç, derslere ayır, soruları tek tek çöz veya test moduna geçir.
          </p>
        </div>
        <Link to="/rastgele" className="btn-secondary self-start sm:self-auto">
          <Layers className="h-4 w-4" />
          Rastgele pratik
        </Link>
      </div>

      <div className="mt-6 grid gap-4 lg:grid-cols-2">
        {exams.map((exam) => {
          const examAnswered = Object.values(answers).filter((a) => a.examId === exam.id).length;
          return (
            <ExamCard
              key={exam.id}
              exam={exam}
              answered={examAnswered}
              total={exam.questionCount}
            />
          );
        })}
      </div>

      {exams.length === 0 && (
        <div className="card mt-6 p-8 text-center text-sm text-slate-500 dark:text-slate-400">
          Henüz yayınlanmış sınav yok.
        </div>
      )}

      <div className="mt-6 flex items-start gap-2 rounded-xl border border-slate-200 bg-white px-4 py-3 text-xs leading-relaxed text-slate-500 dark:border-slate-800 dark:bg-slate-900 dark:text-slate-400">
        <Info className="mt-0.5 h-4 w-4 shrink-0 text-indigo-500" />
        <p>
          Kapsam: Dönem 1 / TEM 2. Şu anda 2024-2025 sınavı yayında. Diğer yıllar aynı doğrulama
          hattından geçirilerek eklenir; cevabı kaynakta bulunmayan sorular AI çözümü olarak
          işaretlenir.
        </p>
      </div>

      <section className="mt-10">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-bold tracking-tight text-slate-900 dark:text-white">Dersler</h2>
          <span className="text-xs text-slate-400">
            {disciplines.length} ders · {disciplines.reduce((s, d) => s + d.count, 0)} soru
          </span>
        </div>

        <div className="mt-4 grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
          {disciplines.map((d) => {
            const style = disciplineStyle(d.id);
            return (
              <Link
                key={d.id}
                to={`/sinav/${d.examId}?ders=${d.id}`}
                className="card card-hover group flex items-center gap-3 p-4"
              >
                <span className={`h-9 w-1.5 rounded-full ${style.bar}`} />
                <span className="min-w-0 flex-1">
                  <span className="block truncate text-sm font-semibold text-slate-900 dark:text-white">
                    {d.name}
                  </span>
                  <span className="mt-0.5 block text-xs text-slate-500 dark:text-slate-400">
                    {d.count} soru
                  </span>
                </span>
                <ArrowRight className="h-4 w-4 text-slate-300 transition group-hover:translate-x-0.5 group-hover:text-indigo-500 dark:text-slate-600" />
              </Link>
            );
          })}
        </div>
      </section>

      <section className="mt-10">
        <h2 className="text-lg font-bold tracking-tight text-slate-900 dark:text-white">Yıl bazında</h2>
        <div className="mt-4 overflow-hidden rounded-2xl border border-slate-200 dark:border-slate-800">
          {exams.map((exam, i) => (
            <Link
              key={exam.id}
              to={`/sinav/${exam.id}`}
              className={`flex items-center gap-3 bg-white px-4 py-3.5 transition hover:bg-slate-50 sm:px-5 dark:bg-slate-900 dark:hover:bg-slate-800/60 ${
                i > 0 ? "border-t border-slate-100 dark:border-slate-800" : ""
              }`}
            >
              <CalendarDays className="h-4 w-4 shrink-0 text-indigo-500" />
              <span className="min-w-0 flex-1">
                <span className="block truncate text-sm font-semibold text-slate-900 dark:text-white">
                  {exam.label}
                </span>
                <span className="mt-0.5 block text-xs text-slate-500 dark:text-slate-400">
                  Dönem {exam.period} · {exam.term} · {exam.questionCount} soru
                </span>
              </span>
              <span className="chip hidden sm:inline-flex">{exam.disciplines.length} ders</span>
              <ArrowRight className="h-4 w-4 text-slate-300 dark:text-slate-600" />
            </Link>
          ))}
        </div>
      </section>
    </div>
  );
}
