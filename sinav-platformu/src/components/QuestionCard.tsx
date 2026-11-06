import { CheckCircle2, FileText, Info, Sparkles, XCircle } from "lucide-react";
import type { AnswerStatus, Question } from "../types";
import { useProgressStore } from "../store/useProgressStore";
import { sourcePdfUrl } from "../lib/data";
import { ANSWER_STATUS_HINT, ANSWER_STATUS_LABEL, LETTERS, cn, disciplineStyle } from "../lib/utils";
import { AnswerOption, type OptionState } from "./AnswerOption";
import { DisciplineBadge } from "./DisciplineBadge";

export function AnswerStatusBadge({ status, compact = false }: { status: AnswerStatus; compact?: boolean }) {
  if (status === "official") {
    return (
      <span className="inline-flex items-center gap-1 rounded-full bg-emerald-50 px-2 py-0.5 text-[10px] font-semibold text-emerald-700 ring-1 ring-emerald-200/70 dark:bg-emerald-500/10 dark:text-emerald-300 dark:ring-emerald-500/20">
        <CheckCircle2 className="h-3 w-3" />
        {compact ? "Resmî" : "Resmî anahtar"}
      </span>
    );
  }
  if (status === "derived") {
    return (
      <span className="inline-flex items-center gap-1 rounded-full bg-amber-50 px-2 py-0.5 text-[10px] font-semibold text-amber-700 ring-1 ring-amber-200/70 dark:bg-amber-500/10 dark:text-amber-300 dark:ring-amber-500/20">
        <Sparkles className="h-3 w-3" />
        {compact ? "AI çözümü" : "AI ile çözüldü"}
      </span>
    );
  }
  return (
    <span className="inline-flex items-center gap-1 rounded-full bg-slate-100 px-2 py-0.5 text-[10px] font-semibold text-slate-600 ring-1 ring-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:ring-slate-700">
      <Info className="h-3 w-3" />
      Cevap yok
    </span>
  );
}

export function SourceLink({ question, className }: { question: Question; className?: string }) {
  return (
    <a
      href={sourcePdfUrl(question.examId, question.sourcePage)}
      target="_blank"
      rel="noreferrer"
      className={cn(
        "inline-flex items-center gap-1 text-[11px] font-medium text-slate-400 transition hover:text-indigo-600 dark:text-slate-500 dark:hover:text-indigo-300",
        className,
      )}
      title="Sorunun kaynak PDF sayfasını aç"
    >
      <FileText className="h-3 w-3" />
      Kaynak · s. {question.sourcePage}
    </a>
  );
}

interface QuestionCardProps {
  question: Question;
  showDiscipline?: boolean;
}

export function QuestionCard({ question, showDiscipline = true }: QuestionCardProps) {
  const record = useProgressStore((s) => s.answers[question.id]);
  const recordAnswer = useProgressStore((s) => s.record);

  const selected = record?.selected;
  const answered = Boolean(record);
  const isCorrect = selected === question.correctAnswer;
  const style = disciplineStyle(question.disciplineId);

  function handleSelect(letter: (typeof LETTERS)[number]) {
    void recordAnswer(question, letter);
  }

  function optionState(letter: (typeof LETTERS)[number]): OptionState {
    if (!answered) return "idle";
    if (letter === question.correctAnswer) return "correct";
    if (letter === selected) return "wrong";
    return "muted";
  }

  return (
    <article
      id={`soru-${question.number}`}
      className="card scroll-mt-48 overflow-hidden p-5 sm:p-6"
    >
      <div className="mb-4 flex flex-wrap items-center gap-2">
        <span
          className={cn(
            "flex h-8 min-w-8 items-center justify-center rounded-lg px-2 text-sm font-bold",
            style.soft,
            style.text,
          )}
        >
          {question.number}
        </span>
        {showDiscipline && <DisciplineBadge id={question.disciplineId} name={question.discipline} />}
        <AnswerStatusBadge status={question.answerStatus} />
        <SourceLink question={question} className="ml-auto" />
      </div>

      <p className="prose-question">{question.stem}</p>

      <div className="mt-4 grid gap-2">
        {question.options.map((option, i) => {
          const letter = LETTERS[i];
          return (
            <AnswerOption
              key={letter}
              letter={letter}
              text={option}
              state={optionState(letter)}
              onClick={() => handleSelect(letter)}
            />
          );
        })}
      </div>

      {answered && (
        <div
          className={cn(
            "mt-4 flex items-start gap-2 rounded-xl px-3.5 py-3 text-sm",
            isCorrect
              ? "bg-emerald-50 text-emerald-800 dark:bg-emerald-500/10 dark:text-emerald-200"
              : "bg-rose-50 text-rose-800 dark:bg-rose-500/10 dark:text-rose-200",
          )}
        >
          {isCorrect ? (
            <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0" />
          ) : (
            <XCircle className="mt-0.5 h-4 w-4 shrink-0" />
          )}
          <p>
            {isCorrect ? (
              <>Doğru cevap. Tebrikler!</>
            ) : (
              <>
                Yanlış cevap. Doğru cevap <strong>{question.correctAnswer}</strong>.
              </>
            )}{" "}
            <span className="opacity-70">Değiştirmek için başka bir şık seçebilirsin.</span>
          </p>
        </div>
      )}

      {question.explanation && answered && (
        <div className="mt-3 flex items-start gap-2 rounded-xl bg-sky-50 px-3.5 py-3 text-xs leading-relaxed text-sky-800 dark:bg-sky-500/10 dark:text-sky-200">
          <Info className="mt-0.5 h-4 w-4 shrink-0" />
          <p>{question.explanation}</p>
        </div>
      )}

      {question.note && (
        <div className="mt-3 flex items-start gap-2 rounded-xl bg-amber-50 px-3.5 py-3 text-xs leading-relaxed text-amber-800 dark:bg-amber-500/10 dark:text-amber-200">
          <Info className="mt-0.5 h-4 w-4 shrink-0" />
          <p>
            <strong>{ANSWER_STATUS_LABEL[question.answerStatus]}.</strong>{" "}
            {question.note ?? ANSWER_STATUS_HINT[question.answerStatus]}
          </p>
        </div>
      )}
    </article>
  );
}
