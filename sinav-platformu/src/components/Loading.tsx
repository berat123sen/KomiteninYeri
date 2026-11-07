export function LinearProgress({ value, className = "" }: { value: number; className?: string }) {
  const clamped = Math.max(0, Math.min(100, value));
  return (
    <div className={`h-1.5 w-full overflow-hidden rounded-full bg-slate-100 dark:bg-slate-800 ${className}`}>
      <div
        className="h-full rounded-full transition-all duration-500"
        style={{ width: `${clamped}%`, background: "linear-gradient(90deg, var(--accent), var(--accent-hover))" }}
      />
    </div>
  );
}

export function PageLoader({ label = "Yükleniyor…" }: { label?: string }) {
  return (
    <div className="flex min-h-[50vh] flex-col items-center justify-center gap-3">
      <span className="h-8 w-8 animate-spin rounded-full border-2 border-slate-200 border-t-indigo-600 dark:border-slate-700 dark:border-t-indigo-400" />
      <p className="text-sm text-slate-500 dark:text-slate-400">{label}</p>
    </div>
  );
}

export function ErrorState({ message }: { message: string }) {
  return (
    <div className="page-shell py-16">
      <div className="card mx-auto max-w-lg p-6 text-center">
        <h2 className="text-lg font-semibold text-slate-900 dark:text-white">Bir şeyler ters gitti</h2>
        <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">{message}</p>
        <button type="button" className="btn-secondary mt-5" onClick={() => window.location.reload()}>
          Sayfayı yenile
        </button>
      </div>
    </div>
  );
}
