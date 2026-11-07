import { useState } from "react";
import { Link, NavLink, Outlet, useLocation } from "react-router-dom";
import {
  BarChart3,
  BookOpenCheck,
  GraduationCap,
  Menu,
  Moon,
  Shuffle,
  Skull,
  Sun,
  X,
} from "lucide-react";
import { useAppStore, type Accent } from "../store/useAppStore";
import { useEffect } from "react";

const navItems = [
  { to: "/", label: "Ana Sayfa", icon: GraduationCap, end: true },
  { to: "/cikmislar", label: "Çıkmışlar", icon: BookOpenCheck },
  { to: "/rastgele", label: "Rastgele Soru", icon: Shuffle },
  { to: "/iskelet", label: "3D İskelet", icon: Skull },
  { to: "/ilerleme", label: "İlerleme", icon: BarChart3 },
];

export function Layout() {
  const { theme, toggleTheme, accent, setAccent } = useAppStore();
  const [colorOpen, setColorOpen] = useState(false);
  const [mobileOpen, setMobileOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    setMobileOpen(false);
    window.scrollTo({ top: 0, behavior: "instant" as ScrollBehavior });
  }, [location.pathname]);

  return (
    <div className="flex min-h-screen flex-col">
      <header className="sticky top-0 z-40 border-b border-slate-200/80 bg-white/80 backdrop-blur-xl dark:border-slate-800/80 dark:bg-slate-950/80">
        <div className="page-shell flex h-16 items-center justify-between gap-3">
          <Link to="/" className="group flex items-center gap-2.5">
            <span className="flex h-9 w-9 items-center justify-center rounded-xl bg-gradient-to-br from-[var(--accent)] to-[var(--accent-hover)] text-white shadow-md shadow-indigo-600/20">
              <GraduationCap className="h-5 w-5" />
            </span>
            <span className="leading-tight">
              <span className="block text-sm font-bold tracking-tight text-slate-900 dark:text-white">
                Sınav Platformu
              </span>
              <span className="block text-[11px] font-medium text-slate-500 dark:text-slate-400">
                Dönem 1 · TEM 2
              </span>
            </span>
          </Link>

          <nav className="hidden items-center gap-1 md:flex">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <NavLink
                  key={item.to}
                  to={item.to}
                  end={item.end}
                  className={({ isActive }) =>
                    [
                      "flex items-center gap-1.5 rounded-lg px-3 py-2 text-sm font-medium transition",
                      isActive
                        ? "bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-300"
                        : "text-slate-600 hover:bg-slate-100 hover:text-slate-900 dark:text-slate-300 dark:hover:bg-slate-800 dark:hover:text-white",
                    ].join(" ")
                  }
                >
                  <Icon className="h-4 w-4" />
                  {item.label}
                </NavLink>
              );
            })}
          </nav>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              onClick={toggleTheme}
              className="flex h-9 w-9 items-center justify-center rounded-lg text-slate-500 transition hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white"
              aria-label={theme === "dark" ? "Açık temaya geç" : "Koyu temaya geç"}
              title={theme === "dark" ? "Açık tema" : "Koyu tema"}
            >
              {theme === "dark" ? <Sun className="h-4.5 w-4.5" /> : <Moon className="h-4.5 w-4.5" />}
            </button>
            <div className="relative">
              <button
                type="button"
                onClick={() => setColorOpen((v) => !v)}
                className="flex h-9 w-9 items-center justify-center rounded-lg text-slate-500 transition hover:bg-slate-100 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-white"
                aria-label="Renk teması"
                title="Renk teması"
              >
                <span className="h-4 w-4 rounded-full" style={{ background: "var(--accent)" }} />
              </button>
              {colorOpen && (
                <div className="absolute right-0 top-11 z-50 flex gap-2 rounded-xl border border-slate-200 bg-white p-2 shadow-lg dark:border-slate-700 dark:bg-slate-900">
                  {(["indigo","emerald","rose","amber","sky","violet"] as Accent[]).map((c) => (
                    <button
                      key={c}
                      type="button"
                      onClick={() => { setAccent(c); setColorOpen(false); }}
                      className={"h-6 w-6 rounded-full border-2 transition " + (accent === c ? "border-slate-900 dark:border-white" : "border-transparent")}
                      style={{ background: "var(--accent-" + c + ")" }}
                      aria-label={c}
                    />
                  ))}
                </div>
              )}
            </div>
            <button
              type="button"
              onClick={() => setMobileOpen((v) => !v)}
              className="flex h-9 w-9 items-center justify-center rounded-lg text-slate-600 transition hover:bg-slate-100 md:hidden dark:text-slate-300 dark:hover:bg-slate-800"
              aria-label="Menü"
              aria-expanded={mobileOpen}
            >
              {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
            </button>
          </div>
        </div>

        {mobileOpen && (
          <nav className="border-t border-slate-200 bg-white px-4 pb-4 pt-2 md:hidden dark:border-slate-800 dark:bg-slate-950">
            <div className="grid gap-1">
              {navItems.map((item) => {
                const Icon = item.icon;
                return (
                  <NavLink
                    key={item.to}
                    to={item.to}
                    end={item.end}
                    className={({ isActive }) =>
                      [
                        "flex items-center gap-2 rounded-lg px-3 py-2.5 text-sm font-medium",
                        isActive
                          ? "bg-indigo-50 text-indigo-700 dark:bg-indigo-500/10 dark:text-indigo-300"
                          : "text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800",
                      ].join(" ")
                    }
                  >
                    <Icon className="h-4 w-4" />
                    {item.label}
                  </NavLink>
                );
              })}
            </div>
          </nav>
        )}
      </header>

      <main className="flex-1">
        <Outlet />
      </main>

      <footer className="border-t border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950">
        <div className="page-shell flex flex-col gap-3 py-8 text-sm text-slate-500 sm:flex-row sm:items-center sm:justify-between dark:text-slate-400">
          <p>
            <span className="font-semibold text-slate-700 dark:text-slate-200">Sınav Platformu</span>{" "}
            · Çukurova Üniversitesi Tıp Fakültesi Dönem 1 TEM 2 arşivi
          </p>
          <p className="text-xs">
            Resmî bir üniversite sitesi değildir. Soruların hakları ilgili fakülteye aittir.
          </p>
        </div>
      </footer>
    </div>
  );
}
