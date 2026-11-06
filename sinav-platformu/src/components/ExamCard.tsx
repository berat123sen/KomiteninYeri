import { LinearProgress } from "./Loading";
import type { ExamSummary } from "../types";
import { cn, percent } from "../lib/utils";
import { Link } from "react-router-dom";
import { ArrowUpRight, CalendarDays, FileQuestion } from "lucide-react";

interface ExamCardProps {
  exam: ExamSummary;
  answered?: number;
  total: number;
}

export function ExamCard({ exam, answered = 0, total }: ExamCardProps) {
  const done = percent(answered, total);

  return (
    <Link
      to={`/sinav/${exam.id}`}
      className="card card-hover group flex flex-col gap-5 p-5 sm:p-6"
    >
      <div className="flex items-start justify-between gap-3">
        <div>
          <div className="flex flex-wrap items-center gap-2">
            <span className="chip border-indigo-200 bg-indigo-50 text-indigo-700 dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
              <CalendarDays className="h-3.5 w-3.5" />
              {exam.year}
            </span>
            <span className="chip">{exam.term}</span>
          </div>
          <h3 className="mt-3 text-lg font-bold tracking-tight text-slate-900 dark:text-white">
            Dönem {exam.period} · {exam.term}
          </h3>
          <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
            {exam.label} · {exam.disciplines.length} ders · {total} soru
          </p>
        </div>
        <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-slate-100 text-slate-500 transition group-hover:bg-indigo-600 group-hover:text-white dark:bg-slate-800 dark:text-slate-400">
          <ArrowUpRight className="h-5 w-5" />
        </span>
      </div>

      <div className="flex flex-wrap gap-1.5">
        {exam.disciplines.map((d) => (
          <span
            key={d.id}
            className="inline-flex items-center rounded-md bg-slate-100 px-1.5 py-0.5 text-[11px] font-medium text-slate-600 dark:bg-slate-800 dark:text-slate-300"
          >
            {d.name} <span className="ml-1 text-slate-400">{d.questionCount}</span>
          </span>
        ))}
      </div>

      <div>
        <div className="mb-1.5 flex items-center justify-between text-xs">
          <span className="inline-flex items-center gap-1 text-slate-500 dark:text-slate-400">
            <FileQuestion className="h-3.5 w-3.5" />
            {answered} / {total} soru çözüldü
          </span>
          <span className={cn("font-semibold", done > 0 ? "text-indigo-600 dark:text-indigo-300" : "text-slate-400")}>
            %{done}
          </span>
        </div>
        <LinearProgress value={done} />
      </div>
    </Link>
  );
}

export function ExamProgressLine({
  label,
  answered,
  total,
  barClass,
}: {
  label: string;
  answered: number;
  total: number;
  barClass?: string;
}) {
  const done = percent(answered, total);
  return (
    <div className="flex items-center gap-3">
      <span className="w-32 shrink-0 truncate text-sm text-slate-600 dark:text-slate-300">{label}</span>
      <div className="h-2 flex-1 overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800">
        <div className={cn("h-full rounded-full bg-indigo-500 transition-all", barClass)} style={{ width: `${done}%` }} />
      </div>
      <span className="w-20 shrink-0 text-right text-xs tabular-nums text-slate-500 dark:text-slate-400">
        {answered}/{total}
      </span>
    </div>
  );
}
