import type { AnswerKey, AnswerStatus } from "../types";

export const LETTERS: AnswerKey[] = ["A", "B", "C", "D", "E"];

export function cn(...parts: Array<string | false | null | undefined>): string {
  return parts.filter(Boolean).join(" ");
}

export function percent(part: number, total: number): number {
  if (!total) return 0;
  return Math.round((part / total) * 100);
}

export function formatClock(totalSeconds: number): string {
  const safe = Math.max(0, Math.floor(totalSeconds));
  const m = Math.floor(safe / 60);
  const s = safe % 60;
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

export function shuffle<T>(items: T[]): T[] {
  const copy = [...items];
  for (let i = copy.length - 1; i > 0; i -= 1) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

interface Style {
  chip: string;
  dot: string;
  bar: string;
  text: string;
  soft: string;
}

const DISCIPLINE_STYLES: Record<string, Style> = {
  histoloji: {
    chip: "bg-rose-50 text-rose-700 ring-1 ring-rose-200/70 dark:bg-rose-500/10 dark:text-rose-300 dark:ring-rose-500/20",
    dot: "bg-rose-500",
    bar: "bg-rose-500",
    text: "text-rose-600 dark:text-rose-300",
    soft: "bg-rose-50 dark:bg-rose-500/10",
  },
  fizyoloji: {
    chip: "bg-sky-50 text-sky-700 ring-1 ring-sky-200/70 dark:bg-sky-500/10 dark:text-sky-300 dark:ring-sky-500/20",
    dot: "bg-sky-500",
    bar: "bg-sky-500",
    text: "text-sky-600 dark:text-sky-300",
    soft: "bg-sky-50 dark:bg-sky-500/10",
  },
  biyokimya: {
    chip: "bg-emerald-50 text-emerald-700 ring-1 ring-emerald-200/70 dark:bg-emerald-500/10 dark:text-emerald-300 dark:ring-emerald-500/20",
    dot: "bg-emerald-500",
    bar: "bg-emerald-500",
    text: "text-emerald-600 dark:text-emerald-300",
    soft: "bg-emerald-50 dark:bg-emerald-500/10",
  },
  biyofizik: {
    chip: "bg-violet-50 text-violet-700 ring-1 ring-violet-200/70 dark:bg-violet-500/10 dark:text-violet-300 dark:ring-violet-500/20",
    dot: "bg-violet-500",
    bar: "bg-violet-500",
    text: "text-violet-600 dark:text-violet-300",
    soft: "bg-violet-50 dark:bg-violet-500/10",
  },
  mikrobiyoloji: {
    chip: "bg-amber-50 text-amber-700 ring-1 ring-amber-200/70 dark:bg-amber-500/10 dark:text-amber-300 dark:ring-amber-500/20",
    dot: "bg-amber-500",
    bar: "bg-amber-500",
    text: "text-amber-600 dark:text-amber-300",
    soft: "bg-amber-50 dark:bg-amber-500/10",
  },
  "davranis-bilimleri": {
    chip: "bg-cyan-50 text-cyan-700 ring-1 ring-cyan-200/70 dark:bg-cyan-500/10 dark:text-cyan-300 dark:ring-cyan-500/20",
    dot: "bg-cyan-500",
    bar: "bg-cyan-500",
    text: "text-cyan-600 dark:text-cyan-300",
    soft: "bg-cyan-50 dark:bg-cyan-500/10",
  },
  "tip-tarihi-etik": {
    chip: "bg-orange-50 text-orange-700 ring-1 ring-orange-200/70 dark:bg-orange-500/10 dark:text-orange-300 dark:ring-orange-500/20",
    dot: "bg-orange-500",
    bar: "bg-orange-500",
    text: "text-orange-600 dark:text-orange-300",
    soft: "bg-orange-50 dark:bg-orange-500/10",
  },
  sbet: {
    chip: "bg-pink-50 text-pink-700 ring-1 ring-pink-200/70 dark:bg-pink-500/10 dark:text-pink-300 dark:ring-pink-500/20",
    dot: "bg-pink-500",
    bar: "bg-pink-500",
    text: "text-pink-600 dark:text-pink-300",
    soft: "bg-pink-50 dark:bg-pink-500/10",
  },
  entegre: {
    chip: "bg-indigo-50 text-indigo-700 ring-1 ring-indigo-200/70 dark:bg-indigo-500/10 dark:text-indigo-300 dark:ring-indigo-500/20",
    dot: "bg-indigo-500",
    bar: "bg-indigo-500",
    text: "text-indigo-600 dark:text-indigo-300",
    soft: "bg-indigo-50 dark:bg-indigo-500/10",
  },
};

const FALLBACK_STYLE: Style = {
  chip: "bg-slate-100 text-slate-700 ring-1 ring-slate-200 dark:bg-slate-800 dark:text-slate-200 dark:ring-slate-700",
  dot: "bg-slate-500",
  bar: "bg-slate-500",
  text: "text-slate-600 dark:text-slate-300",
  soft: "bg-slate-100 dark:bg-slate-800",
};

export function disciplineStyle(id: string): Style {
  return DISCIPLINE_STYLES[id] ?? FALLBACK_STYLE;
}

export const ANSWER_STATUS_LABEL: Record<AnswerStatus, string> = {
  official: "Resmî cevap anahtarı",
  derived: "AI ile çözüldü",
  missing: "Cevap anahtarı yok",
};

export const ANSWER_STATUS_HINT: Record<AnswerStatus, string> = {
  official: "Cevap, sınavın resmî cevap anahtarından alınmıştır.",
  derived:
    "Bu sorunun basılı cevabı kaynakta okunamadığı için yapay zekâ tarafından çözülmüştür. Kontrol edilmesi önerilir.",
  missing: "Bu sorunun cevabı henüz eklenmemiştir.",
};
