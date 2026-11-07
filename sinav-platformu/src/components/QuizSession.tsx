import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import {
  ArrowLeft,
  ArrowRight,
  CheckCircle2,
  ChevronLeft,
  ChevronRight,
  Circle,
  Clock,
  Flag,
  LayoutGrid,
  RotateCcw,
  Trophy,
  XCircle,
} from "lucide-react";
import type { AnswerKey, Question } from "../types";
import { useProgressStore } from "../store/useProgressStore";
import { ANSWER_STATUS_HINT, LETTERS, cn, disciplineStyle, formatClock, percent } from "../lib/utils";
import { AnswerOption, type OptionState } from "./AnswerOption";
import { AnswerStatusBadge, SourceLink } from "./QuestionCard";
import { DisciplineBadge } from "./DisciplineBadge";
import { LinearProgress } from "./Loading";

type RevealMode = "immediate" | "end";
type Phase = "running" | "result" | "review";

interface QuizSessionProps {
  title: string;
  subtitle?: string;
  questions: Question[];
  revealMode: RevealMode;
  onRestart: () => void;
  backTo: string;
  backLabel: string;
}

export function QuizSession({
  title,
  subtitle,
  questions,
  revealMode,
  onRestart,
  backTo,
  backLabel,
}: QuizSessionProps) {
  const recordAnswer = useProgressStore((s) => s.record);
  const [index, setIndex] = useState(0);
  const [selected, setSelected] = useState<Record<string, AnswerKey>>({});
  const [phase, setPhase] = useState<Phase>("running");
  const [elapsed, setElapsed] = useState(0);
  const [paletteOpen, setPaletteOpen] = useState(false);

  useEffect(() => {
    setIndex(0);
    setSelected({});
    setPhase("running");
    setElapsed(0);
  }, [questions]);

  useEffect(() => {
    if (phase !== "running") return;
    const timer = window.setInterval(() => setElapsed((e) => e + 1), 1000);
    return () => window.clearInterval(timer);
  }, [phase]);

  const total = questions.length;
  const question = questions[Math.min(index, Math.max(0, total - 1))];
  const answeredCount = Object.keys(selected).length;

  const stats = useMemo(() => {
    let correct = 0;
    for (const q of questions) {
      if (selected[q.id] === q.correctAnswer) correct += 1;
    }
    const answered = questions.filter((q) => selected[q.id]).length;
    return {
      correct,
      answered,
      wrong: answered - correct,
      blank: questions.length - answered,
      score: percent(correct, questions.length),
    };
  }, [questions, selected]);

  if (!question) {
    return (
      <div className="page-shell py-16">
        <div className="card p-6 text-center text-sm text-slate-600 dark:text-slate-300">
          Bu filtreyle gösterilecek soru bulunamadı.
        </div>
      </div>
    );
  }

  const currentAnswer = selected[question.id];
  const locked =
    phase !== "running" || (revealMode === "immediate" && Boolean(currentAnswer));
  const revealed =
    phase !== "running" || (revealMode === "immediate" && Boolean(currentAnswer));
  const isLast = index === total - 1;

  function select(letter: AnswerKey) {
    if (revealMode === "immediate" && currentAnswer) return;
    if (phase !== "running") return;
    setSelected((prev) => ({ ...prev, [question.id]: letter }));
    void recordAnswer(question, letter);
  }

  function finish() {
    if (phase !== "running") return;
    if (answeredCount < total) {
      const ok = window.confirm(
        `${total - answeredCount} soru boş kaldı. Yine de testi bitirmek istiyor musun?`,
      );
      if (!ok) return;
    }
    setPhase("result");
  }

  function optionState(letter: AnswerKey): OptionState {
    if (revealed) {
      if (letter === question.correctAnswer) return "correct";
      if (letter === currentAnswer) return "wrong";
      return "muted";
    }
    if (letter === currentAnswer) return "selected";
    return "idle";
  }

  const style = disciplineStyle(question.disciplineId);

  return (
    <div className="page-shell py-6 sm:py-8">
      <div className="mb-5 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <div className="min-w-0">
          <Link
            to={backTo}
            className="inline-flex items-center gap-1 text-xs font-medium text-slate-500 transition hover:text-indigo-600 dark:text-slate-400 dark:hover:text-indigo-300"
          >
            <ChevronLeft className="h-3.5 w-3.5" />
            {backLabel}
          </Link>
          <h1 className="mt-1 truncate text-xl font-bold tracking-tight text-slate-900 sm:text-2xl dark:text-white">
            {title}
          </h1>
          {subtitle && <p className="mt-0.5 text-sm text-slate-500 dark:text-slate-400">{subtitle}</p>}
        </div>
        <div className="flex items-center gap-2">
          <span className="inline-flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-2 text-sm font-semibold tabular-nums text-slate-700 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200">
            <Clock className="h-4 w-4 text-slate-400" />
            {formatClock(elapsed)}
          </span>
          {phase === "running" ? (
            <button type="button" className="btn-primary" onClick={finish}>
              <Flag className="h-4 w-4" />
              Bitir
            </button>
          ) : (
            <button type="button" className="btn-secondary" onClick={() => setPhase("result")}>
              <Trophy className="h-4 w-4" />
              Sonuçlar
            </button>
          )}
        </div>
      </div>

      {phase === "result" ? (
        <ResultPanel
          stats={stats}
          questions={questions}
          selected={selected}
          elapsed={elapsed}
          onReview={() => {
            setIndex(0);
            setPhase("review");
          }}
          onRestart={onRestart}
          backTo={backTo}
          backLabel={backLabel}
        />
      ) : (
        <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_270px]">
          <div>
            <div className="mb-3 flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
              <span>
                Soru <strong className="text-slate-800 dark:text-slate-100">{index + 1}</strong> / {total}
              </span>
              <span>{answeredCount} cevaplandı</span>
            </div>
            <LinearProgress value={percent(index + 1, total)} className="mb-4" />

            {phase === "review" && (
              <div className="mb-4 rounded-xl bg-indigo-50 px-4 py-3 text-sm text-indigo-800 dark:bg-indigo-500/10 dark:text-indigo-200">
                Cevapları inceliyorsun. Doğru cevaplar yeşil, senin işaretlediğin yanlışlar kırmızı
                gösteriliyor.
              </div>
            )}

            <article className="card p-5 sm:p-6">
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
                <DisciplineBadge id={question.disciplineId} name={question.discipline} />
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
                      disabled={locked}
                      onClick={() => select(letter)}
                    />
                  );
                })}
              </div>

              {revealed && (
                <div
                  className={cn(
                    "mt-4 flex items-start gap-2 rounded-xl px-3.5 py-3 text-sm",
                    currentAnswer === question.correctAnswer
                      ? "bg-emerald-50 text-emerald-800 dark:bg-emerald-500/10 dark:text-emerald-200"
                      : "bg-rose-50 text-rose-800 dark:bg-rose-500/10 dark:text-rose-200",
                  )}
                >
                  {currentAnswer === question.correctAnswer ? (
                    <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0" />
                  ) : (
                    <XCircle className="mt-0.5 h-4 w-4 shrink-0" />
                  )}
                  <p>
                    {!currentAnswer
                      ? `Boş bırakıldı. Doğru cevap ${question.correctAnswer}.`
                      : currentAnswer === question.correctAnswer
                        ? "Doğru cevap!"
                        : `Yanlış. Doğru cevap ${question.correctAnswer}.`}
                    {question.answerStatus !== "official" && (
                      <span className="mt-1 block text-xs opacity-80">
                        {ANSWER_STATUS_HINT[question.answerStatus]}
                      </span>
                    )}
                    {question.explanation && (
                      <span className="mt-2 block text-xs opacity-90">{question.explanation}</span>
                    )}
                  </p>
                </div>
              )}

              <div className="mt-5 flex items-center justify-between gap-2 border-t border-slate-100 pt-4 dark:border-slate-800">
                <button
                  type="button"
                  className="btn-secondary"
                  disabled={index === 0}
                  onClick={() => setIndex((i) => Math.max(0, i - 1))}
                >
                  <ArrowLeft className="h-4 w-4" />
                  Önceki
                </button>

                {isLast ? (
                  phase === "running" ? (
                    <button type="button" className="btn-primary" onClick={finish}>
                      <Flag className="h-4 w-4" />
                      Testi bitir
                    </button>
                  ) : (
                    <button type="button" className="btn-primary" onClick={() => setPhase("result")}>
                      <Trophy className="h-4 w-4" />
                      Sonuçlar
                    </button>
                  )
                ) : (
                  <button
                    type="button"
                    className="btn-primary"
                    onClick={() => setIndex((i) => Math.min(total - 1, i + 1))}
                  >
                    Sonraki
                    <ArrowRight className="h-4 w-4" />
                  </button>
                )}
              </div>
            </article>
          </div>

          <aside className="order-first lg:order-none">
            <div className="card p-4 lg:sticky lg:top-20">
              <button
                type="button"
                className="flex w-full items-center justify-between text-sm font-semibold text-slate-700 lg:pointer-events-none dark:text-slate-200"
                onClick={() => setPaletteOpen((v) => !v)}
              >
                <span className="inline-flex items-center gap-2">
                  <LayoutGrid className="h-4 w-4" />
                  Soru haritası
                </span>
                <span className="text-xs font-medium text-slate-400 lg:hidden">
                  {answeredCount}/{total}
                  <ChevronRight
                    className={cn("ml-1 inline h-3.5 w-3.5 transition", paletteOpen && "rotate-90")}
                  />
                </span>
              </button>

              <div className={cn("mt-3 grid grid-cols-10 gap-1.5 lg:grid-cols-6", !paletteOpen && "hidden lg:grid")}>
                {questions.map((q, i) => {
                  const chosen = selected[q.id];
                  const review = phase === "review";
                  const stateClass = review
                    ? chosen === q.correctAnswer
                      ? "border-emerald-500 bg-emerald-500 text-white"
                      : chosen
                        ? "border-rose-500 bg-rose-500 text-white"
                        : "border-slate-200 bg-white text-slate-500 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-400"
                    : chosen
                      ? "border-indigo-500 bg-indigo-500 text-white"
                      : "border-slate-200 bg-white text-slate-500 hover:border-indigo-300 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-400";
                  return (
                    <button
                      key={q.id}
                      type="button"
                      onClick={() => {
                        setIndex(i);
                        setPaletteOpen(false);
                      }}
                      className={cn(
                        "flex h-7 items-center justify-center rounded-md border text-[11px] font-semibold tabular-nums transition",
                        stateClass,
                        i === index && "ring-2 ring-indigo-400 ring-offset-1 dark:ring-offset-slate-900",
                      )}
                      title={`${q.number}. soru`}
                    >
                      {i + 1}
                    </button>
                  );
                })}
              </div>

              <div className="mt-4 hidden space-y-1.5 border-t border-slate-100 pt-3 text-[11px] text-slate-500 lg:block dark:border-slate-800 dark:text-slate-400">
                <p className="flex items-center gap-2">
                  <span className="h-2.5 w-2.5 rounded-sm border border-slate-300 bg-white dark:border-slate-600 dark:bg-slate-900" />
                  Boş
                </p>
                <p className="flex items-center gap-2">
                  <span className="h-2.5 w-2.5 rounded-sm bg-indigo-500" />
                  Cevaplandı
                </p>
                {phase === "review" && (
                  <>
                    <p className="flex items-center gap-2">
                      <span className="h-2.5 w-2.5 rounded-sm bg-emerald-500" />
                      Doğru
                    </p>
                    <p className="flex items-center gap-2">
                      <span className="h-2.5 w-2.5 rounded-sm bg-rose-500" />
                      Yanlış
                    </p>
                  </>
                )}
              </div>
            </div>
          </aside>
        </div>
      )}
    </div>
  );
}

function ResultPanel({
  stats,
  questions,
  selected,
  elapsed,
  onReview,
  onRestart,
  backTo,
  backLabel,
}: {
  stats: { correct: number; answered: number; wrong: number; blank: number; score: number };
  questions: Question[];
  selected: Record<string, AnswerKey>;
  elapsed: number;
  onReview: () => void;
  onRestart: () => void;
  backTo: string;
  backLabel: string;
}) {
  const byDiscipline = useMemo(() => {
    const map = new Map<string, { name: string; id: string; total: number; correct: number }>();
    for (const q of questions) {
      const item = map.get(q.disciplineId) ?? {
        id: q.disciplineId,
        name: q.discipline,
        total: 0,
        correct: 0,
      };
      item.total += 1;
      if (selected[q.id] === q.correctAnswer) item.correct += 1;
      map.set(q.disciplineId, item);
    }
    return [...map.values()].sort((a, b) => b.total - a.total);
  }, [questions, selected]);

  return (
    <div className="space-y-5">
      <div className="card overflow-hidden">
        <div className="bg-gradient-to-br from-[var(--accent)] to-[var(--accent-hover)] px-6 py-8 text-white">
          <p className="text-sm font-medium text-indigo-100">Test tamamlandı</p>
          <div className="mt-2 flex flex-wrap items-end gap-x-4 gap-y-1">
            <span className="text-5xl font-extrabold tracking-tight">%{stats.score}</span>
            <span className="pb-1.5 text-sm text-indigo-100">
              {stats.correct} doğru · {stats.wrong} yanlış · {stats.blank} boş
            </span>
          </div>
          <p className="mt-3 inline-flex items-center gap-1.5 rounded-full bg-white/15 px-3 py-1 text-xs font-medium">
            <Clock className="h-3.5 w-3.5" />
            Süre {formatClock(elapsed)} · {questions.length} soru
          </p>
        </div>

        <div className="grid grid-cols-2 divide-x divide-slate-100 border-b border-slate-100 sm:grid-cols-4 dark:divide-slate-800 dark:border-slate-800">
          {[
            { label: "Doğru", value: stats.correct, icon: CheckCircle2, cls: "text-emerald-600 dark:text-emerald-400" },
            { label: "Yanlış", value: stats.wrong, icon: XCircle, cls: "text-rose-600 dark:text-rose-400" },
            { label: "Boş", value: stats.blank, icon: Circle, cls: "text-slate-500 dark:text-slate-400" },
            {
              label: "Cevaplanan",
              value: stats.answered,
              icon: LayoutGrid,
              cls: "text-indigo-600 dark:text-indigo-400",
            },
          ].map((item) => {
            const Icon = item.icon;
            return (
              <div key={item.label} className="px-4 py-4">
                <p className="flex items-center gap-1.5 text-xs font-medium text-slate-500 dark:text-slate-400">
                  <Icon className={cn("h-3.5 w-3.5", item.cls)} />
                  {item.label}
                </p>
                <p className="mt-1 text-xl font-bold text-slate-900 dark:text-white">{item.value}</p>
              </div>
            );
          })}
        </div>

        <div className="flex flex-wrap gap-2 p-5">
          <button type="button" className="btn-primary" onClick={onReview}>
            <LayoutGrid className="h-4 w-4" />
            Cevapları incele
          </button>
          <button type="button" className="btn-secondary" onClick={onRestart}>
            <RotateCcw className="h-4 w-4" />
            Yeniden başla
          </button>
          <Link to={backTo} className="btn-ghost">
            <ChevronLeft className="h-4 w-4" />
            {backLabel}
          </Link>
        </div>
      </div>

      <div className="card p-5 sm:p-6">
        <h2 className="text-sm font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
          Derse göre performans
        </h2>
        <div className="mt-4 space-y-3">
          {byDiscipline.map((d) => {
            const style = disciplineStyle(d.id);
            const value = percent(d.correct, d.total);
            return (
              <div key={d.id}>
                <div className="mb-1 flex items-center justify-between text-xs">
                  <DisciplineBadge id={d.id} name={d.name} />
                  <span className="tabular-nums text-slate-500 dark:text-slate-400">
                    {d.correct}/{d.total} · %{value}
                  </span>
                </div>
                <div className="h-1.5 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
                  <div className={cn("h-full rounded-full", style.bar)} style={{ width: `${value}%` }} />
                </div>
              </div>
            );
          })}
        </div>
      </div>

      <div className="card p-5 sm:p-6">
        <h2 className="text-sm font-bold uppercase tracking-wide text-slate-500 dark:text-slate-400">
          Soru özeti
        </h2>
        <div className="mt-3 grid grid-cols-8 gap-1.5 sm:grid-cols-12 md:grid-cols-16">
          {questions.map((q) => {
            const chosen = selected[q.id];
            const cls =
              chosen === q.correctAnswer
                ? "border-emerald-500 bg-emerald-500 text-white"
                : chosen
                  ? "border-rose-500 bg-rose-500 text-white"
                  : "border-slate-200 bg-white text-slate-400 dark:border-slate-700 dark:bg-slate-900";
            return (
              <span
                key={q.id}
                className={cn(
                  "flex h-7 items-center justify-center rounded-md border text-[11px] font-semibold tabular-nums",
                  cls,
                )}
                title={`${q.number}. soru — ${
                  chosen === q.correctAnswer ? "doğru" : chosen ? "yanlış" : "boş"
                }`}
              >
                {q.number}
              </span>
            );
          })}
        </div>
      </div>
    </div>
  );
}
