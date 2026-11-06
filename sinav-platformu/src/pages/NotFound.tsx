import { Link } from "react-router-dom";
import { ArrowLeft, Compass, Home as HomeIcon, Shuffle } from "lucide-react";
import { usePageTitle } from "../lib/useTitle";

export function NotFound() {
  usePageTitle("Sayfa bulunamadı");
  return (
    <div className="page-shell py-20">
      <div className="mx-auto max-w-lg text-center">
        <span className="mx-auto flex h-14 w-14 items-center justify-center rounded-2xl bg-indigo-50 text-indigo-600 dark:bg-indigo-500/10 dark:text-indigo-300">
          <Compass className="h-7 w-7" />
        </span>
        <p className="mt-5 text-sm font-bold uppercase tracking-widest text-indigo-600 dark:text-indigo-300">
          404
        </p>
        <h1 className="mt-2 text-2xl font-extrabold tracking-tight text-slate-900 sm:text-3xl dark:text-white">
          Bu sayfayı bulamadık
        </h1>
        <p className="mt-2 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
          Bağlantı eski olabilir veya sayfa taşınmış olabilir. Arşive dönüp aradığın sınavı
          seçebilirsin.
        </p>
        <div className="mt-6 flex flex-wrap justify-center gap-2">
          <Link to="/" className="btn-primary">
            <HomeIcon className="h-4 w-4" />
            Ana sayfa
          </Link>
          <Link to="/cikmislar" className="btn-secondary">
            <ArrowLeft className="h-4 w-4" />
            Çıkmışlar
          </Link>
          <Link to="/rastgele" className="btn-ghost">
            <Shuffle className="h-4 w-4" />
            Rastgele
          </Link>
        </div>
      </div>
    </div>
  );
}
