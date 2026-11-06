import { useEffect } from "react";

const DEFAULT_TITLE = "Sınav Platformu — Dönem 1 TEM 2 Çıkmış Sorular";

export function usePageTitle(title?: string) {
  useEffect(() => {
    document.title = title ? `${title} · Sınav Platformu` : DEFAULT_TITLE;
  }, [title]);
}
