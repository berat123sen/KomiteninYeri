import type { AnswerKey } from "../types";
import { cn } from "../lib/utils";
import { Check, X } from "lucide-react";

export type OptionState = "idle" | "selected" | "correct" | "wrong" | "muted";

const BOX: Record<OptionState, string> = {
  idle: "border-slate-200 bg-white hover:border-indigo-300 hover:bg-indigo-50/50 dark:border-slate-700 dark:bg-slate-900 dark:hover:border-indigo-500/60 dark:hover:bg-indigo-500/5",
  selected:
    "border-indigo-500 bg-indigo-50 ring-1 ring-indigo-500 dark:border-indigo-400 dark:bg-indigo-500/10 dark:ring-indigo-400",
  correct:
    "border-emerald-500 bg-emerald-50 ring-1 ring-emerald-500 dark:border-emerald-400 dark:bg-emerald-500/10 dark:ring-emerald-400",
  wrong:
    "border-rose-500 bg-rose-50 ring-1 ring-rose-500 dark:border-rose-400 dark:bg-rose-500/10 dark:ring-rose-400",
  muted:
    "border-slate-200 bg-white opacity-55 dark:border-slate-800 dark:bg-slate-900",
};

const BADGE: Record<OptionState, string> = {
  idle: "bg-slate-100 text-slate-600 group-hover:bg-indigo-100 group-hover:text-indigo-700 dark:bg-slate-800 dark:text-slate-300",
  selected: "bg-indigo-600 text-white",
  correct: "bg-emerald-600 text-white",
  wrong: "bg-rose-600 text-white",
  muted: "bg-slate-100 text-slate-500 dark:bg-slate-800 dark:text-slate-400",
};

interface AnswerOptionProps {
  letter: AnswerKey;
  text: string;
  state: OptionState;
  onClick?: () => void;
  disabled?: boolean;
}

export function AnswerOption({ letter, text, state, onClick, disabled }: AnswerOptionProps) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={disabled}
      className={cn(
        "group flex w-full items-start gap-3 rounded-xl border px-3.5 py-3 text-left transition",
        BOX[state],
        disabled ? "cursor-default" : "cursor-pointer",
      )}
    >
      <span
        className={cn(
          "mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-lg text-xs font-bold transition",
          BADGE[state],
        )}
      >
        {state === "correct" ? (
          <Check className="h-3.5 w-3.5" />
        ) : state === "wrong" ? (
          <X className="h-3.5 w-3.5" />
        ) : (
          letter
        )}
      </span>
      <span className="whitespace-pre-line text-[14px] leading-relaxed text-slate-700 dark:text-slate-200">
        {text}
      </span>
    </button>
  );
}
