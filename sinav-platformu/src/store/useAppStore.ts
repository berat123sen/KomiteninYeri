import { create } from "zustand";

export type Theme = "light" | "dark";

function initialTheme(): Theme {
  try {
    const stored = localStorage.getItem("sp-theme");
    if (stored === "light" || stored === "dark") return stored;
  } catch {
    /* ignore */
  }
  if (typeof window !== "undefined" && window.matchMedia("(prefers-color-scheme: dark)").matches) {
    return "dark";
  }
  return "light";
}

function applyTheme(theme: Theme) {
  const root = document.documentElement;
  root.classList.toggle("dark", theme === "dark");
  root.style.colorScheme = theme;
  try {
    localStorage.setItem("sp-theme", theme);
  } catch {
    /* ignore */
  }
}

interface AppState {
  theme: Theme;
  lastExamId: string | null;
  setTheme: (theme: Theme) => void;
  toggleTheme: () => void;
  setLastExam: (examId: string) => void;
}

export const useAppStore = create<AppState>()((set, get) => ({
  theme: initialTheme(),
  lastExamId: (() => {
    try {
      return localStorage.getItem("sp-last-exam");
    } catch {
      return null;
    }
  })(),
  setTheme: (theme) => {
    applyTheme(theme);
    set({ theme });
  },
  toggleTheme: () => {
    const next = get().theme === "dark" ? "light" : "dark";
    applyTheme(next);
    set({ theme: next });
  },
  setLastExam: (examId) => {
    try {
      localStorage.setItem("sp-last-exam", examId);
    } catch {
      /* ignore */
    }
    set({ lastExamId: examId });
  },
}));

// İlk yüklemede temayı uygula.
applyTheme(initialTheme());
