import { Link, useParams } from "react-router-dom";
import { ArrowLeft, ArrowRight, ChevronRight, Target } from "lucide-react";
import { useExam } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { PageLoader, ErrorState } from "../components/Loading";
import { QuestionCard } from "../components/QuestionCard";

export function QuestionDetail() {
  const { examId, number } = useParams<{ examId: string; number: string }>();
  const { data, loading, error } = useExam(examId);
  usePageTitle(data ? `${data.exam.shortLabel} · ${number}. soru` : undefined);

  if (loading) return <PageLoader label="Soru yükleniyor…" />;
  if (error) return <ErrorState message={error} />;
  if (!data) return <ErrorState message="Sınav bulunamadı." />;

  const num = Number(number);
  const question = data.questions.find((q) => q.number === num);

  if (!question) {
    return (
      <div className="page-shell py-16">
        <div className="card mx-auto max-w-lg p-8 text-center">
          <h1 className="text-lg font-bold text-slate-900 dark:text-white">Soru bulunamadı</h1>
          <p className="mt-2 text-sm text-slate-500 dark:text-slate-400">
            {data.exam.label} sınavında {number} numaralı bir soru yok.
          </p>
          <Link to={`/sinav/${data.exam.id}`} className="btn-primary mt-5">
            Sınava dön
          </Link>
        </div>
      </div>
    );
  }

  const prev = data.questions.find((q) => q.number === num - 1);
  const next = data.questions.find((q) => q.number === num + 1);

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="flex flex-wrap items-center gap-2 text-xs text-slate-500 dark:text-slate-400">
        <Link to="/cikmislar" className="transition hover:text-indigo-600 dark:hover:text-indigo-300">
          Çıkmışlar
        </Link>
        <ChevronRight className="h-3 w-3" />
        <Link to={`/sinav/${data.exam.id}`} className="transition hover:text-indigo-600 dark:hover:text-indigo-300">
          {data.exam.shortLabel}
        </Link>
        <ChevronRight className="h-3 w-3" />
        <span className="font-medium text-slate-700 dark:text-slate-300">{question.number}. soru</span>
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
        <div>
          <h1 className="text-xl font-bold tracking-tight text-slate-900 dark:text-white">
            {question.discipline} · {question.number}. soru
          </h1>
          <p className="mt-0.5 text-xs text-slate-500 dark:text-slate-400">
            {data.exam.label} · {data.exam.questionCount} soru içinden
          </p>
        </div>
        <div className="flex gap-2">
          <Link
            to={`/sinav/${data.exam.id}?ders=${question.disciplineId}`}
            className="btn-secondary"
          >
            <ArrowLeft className="h-4 w-4" />
            Derse dön
          </Link>
          <Link to={`/test/${data.exam.id}?ders=${question.disciplineId}`} className="btn-primary">
            <Target className="h-4 w-4" />
            Test modu
          </Link>
        </div>
      </div>

      <div className="mt-5">
        <QuestionCard question={question} />
      </div>

      <div className="mt-5 flex items-center justify-between gap-2">
        {prev ? (
          <Link to={`/sinav/${data.exam.id}/soru/${prev.number}`} className="btn-secondary">
            <ArrowLeft className="h-4 w-4" />
            {prev.number}. soru
          </Link>
        ) : (
          <span />
        )}
        {next ? (
          <Link to={`/sinav/${data.exam.id}/soru/${next.number}`} className="btn-secondary">
            {next.number}. soru
            <ArrowRight className="h-4 w-4" />
          </Link>
        ) : (
          <span />
        )}
      </div>

      <p className="mt-6 text-center text-xs text-slate-400 dark:text-slate-500">
        Soru numarasıyla doğrudan bağlantı: /sinav/{data.exam.id}/soru/{question.number}
      </p>
    </div>
  );
}
