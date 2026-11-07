import { Link } from "react-router-dom";
import {
  ArrowRight,
  BookOpenCheck,
  Brain,
  CheckCircle2,
  ClipboardList,
  FileQuestion,
  GraduationCap,
  Layers,
  Shuffle,
  Sparkles,
  Target,
  TrendingUp,
} from "lucide-react";
import { useExamIndex } from "../lib/hooks";
import { usePageTitle } from "../lib/useTitle";
import { useProgressStore } from "../store/useProgressStore";
import { ExamCard } from "../components/ExamCard";
import { LinearProgress } from "../components/Loading";
import { percent } from "../lib/utils";

const features = [
  {
    icon: BookOpenCheck,
    title: "Çıkmış sorular",
    text: "Yıla ve derse göre ayrılmış arşiv. Her sorunun kaynak PDF sayfasına tek tıkla ulaş.",
    to: "/cikmislar",
    cta: "Arşive göz at",
    color: "from-indigo-500 to-violet-500",
  },
  {
    icon: Target,
    title: "Test modu",
    text: "Anında geri bildirim ya da sonda toplu değerlendirme. Süre tut, soru haritasıyla ilerle.",
    to: "/cikmislar",
    cta: "Test çöz",
    color: "from-emerald-500 to-teal-500",
  },
  {
    icon: Shuffle,
    title: "Rastgele soru",
    text: "Ders ve yıl filtreleriyle arşivden rastgele sorular seç, kısa pratik seansları yap.",
    to: "/rastgele",
    cta: "Pratik yap",
    color: "from-amber-500 to-orange-500",
  },
  {
    icon: TrendingUp,
    title: "İlerleme takibi",
    text: "Cevapların tarayıcında saklanır. Ders bazında doğruluk oranını ve eksiklerini gör.",
    to: "/ilerleme",
    cta: "İlerlemeyi gör",
    color: "from-rose-500 to-pink-500",
  },
];

export function Home() {
  usePageTitle();
  const { index, loading, error } = useExamIndex();
  const answers = useProgressStore((s) => s.answers);

  const exams = index?.exams ?? [];
  const totalQuestions = exams.reduce((sum, e) => sum + e.questionCount, 0);
  const totalDisciplines = new Set(exams.flatMap((e) => e.disciplines.map((d) => d.id))).size;
  const answered = Object.keys(answers).length;
  const featured = exams[0];

  return (
    <div>
      <section className="relative overflow-hidden border-b border-slate-200/80 dark:border-slate-800/80">
        <div className="pointer-events-none absolute inset-0 -z-10">
          <div className="absolute -left-24 -top-24 h-80 w-80 rounded-full bg-indigo-200/50 blur-3xl dark:bg-indigo-600/20" />
          <div className="absolute -right-16 top-10 h-72 w-72 rounded-full bg-indigo-200/40 blur-3xl dark:bg-indigo-600/15" />
          <div className="absolute bottom-0 left-1/3 h-56 w-56 rounded-full bg-emerald-200/30 blur-3xl dark:bg-emerald-600/10" />
        </div>

        <div className="page-shell grid items-center gap-10 py-14 sm:py-20 lg:grid-cols-[1.15fr_0.85fr] lg:py-24">
          <div>
            <span className="inline-flex items-center gap-2 rounded-full border border-indigo-200 bg-white/80 px-3 py-1 text-xs font-semibold text-indigo-700 shadow-sm backdrop-blur dark:border-indigo-500/30 dark:bg-indigo-500/10 dark:text-indigo-300">
              <GraduationCap className="h-3.5 w-3.5" />
              Çukurova Üniversitesi Tıp Fakültesi · Dönem 1
            </span>

            <h1 className="mt-5 text-3xl font-extrabold leading-tight tracking-tight text-slate-900 sm:text-5xl dark:text-white">
              TEM 2 çıkmış soruları,{" "}
              <span className="bg-gradient-to-r from-[var(--accent)] via-[var(--accent-hover)] to-[var(--accent)] bg-clip-text text-transparent">
                ders ders
              </span>{" "}
              tek yerde.
            </h1>

            <p className="mt-4 max-w-xl text-base leading-relaxed text-slate-600 sm:text-lg dark:text-slate-300">
              Biyokimya’dan Histoloji’ye bütün dersleri ayrı ayrı çalış. Resmî cevap anahtarlı
              soruları test modunda çöz, rastgele sorularla kendini sına, ilerlemeni takip et.
            </p>

            <div className="mt-7 flex flex-wrap gap-3">
              <Link to="/cikmislar" className="btn-primary">
                Çıkmış soruları çöz
                <ArrowRight className="h-4 w-4" />
              </Link>
              <Link to="/rastgele" className="btn-secondary">
                <Shuffle className="h-4 w-4" />
                Rastgele soru
              </Link>
            </div>

            <dl className="mt-9 grid max-w-lg grid-cols-3 gap-4">
              {[
                { label: "Sınav", value: exams.length || "—", icon: ClipboardList },
                { label: "Soru", value: totalQuestions || "—", icon: FileQuestion },
                { label: "Ders", value: totalDisciplines || "—", icon: Layers },
              ].map((item) => {
                const Icon = item.icon;
                return (
                  <div key={item.label} className="rounded-xl border border-slate-200/80 bg-white/70 px-3 py-3 backdrop-blur dark:border-slate-800 dark:bg-slate-900/60">
                    <Icon className="h-4 w-4 text-indigo-500 dark:text-indigo-400" />
                    <dd className="mt-1.5 text-2xl font-extrabold tracking-tight text-slate-900 dark:text-white">
                      {item.value}
                    </dd>
                    <dt className="text-[11px] font-medium uppercase tracking-wide text-slate-500 dark:text-slate-400">
                      {item.label}
                    </dt>
                  </div>
                );
              })}
            </dl>
          </div>

          <div className="relative">
            <div className="card relative overflow-hidden p-5 sm:p-6">
              <div className="flex items-center justify-between">
                <span className="inline-flex items-center gap-2 text-sm font-semibold text-slate-900 dark:text-white">
                  <Brain className="h-4 w-4 text-indigo-500" />
                  Hızlı başlangıç
                </span>
                <span className="chip">
                  <CheckCircle2 className="h-3.5 w-3.5 text-emerald-500" />
                  Pilot hazır
                </span>
              </div>

              {featured ? (
                <>
                  <p className="mt-4 text-xs font-semibold uppercase tracking-wide text-slate-400">
                    Öne çıkan sınav
                  </p>
                  <p className="mt-1 text-lg font-bold text-slate-900 dark:text-white">
                    {featured.label}
                  </p>
                  <div className="mt-3 flex flex-wrap gap-1.5">
                    {featured.disciplines.slice(0, 5).map((d) => (
                      <span key={d.id} className="chip">
                        {d.name}
                      </span>
                    ))}
                    {featured.disciplines.length > 5 && (
                      <span className="chip">+{featured.disciplines.length - 5}</span>
                    )}
                  </div>

                  <div className="mt-5 space-y-2">
                    <div className="flex items-center justify-between text-xs text-slate-500 dark:text-slate-400">
                      <span>İlerlemen</span>
                      <span className="font-semibold text-indigo-600 dark:text-indigo-300">
                        {Object.keys(answers).length} / {featured.questionCount}
                      </span>
                    </div>
                    <LinearProgress value={percent(Object.keys(answers).length, featured.questionCount)} />
                  </div>

                  <Link
                    to={`/sinav/${featured.id}`}
                    className="btn-primary mt-5 w-full"
                  >
                    {featured.shortLabel} sınavına git
                    <ArrowRight className="h-4 w-4" />
                  </Link>
                </>
              ) : (
                <div className="mt-6 space-y-2">
                  <div className="h-3 w-2/3 animate-pulse rounded bg-slate-100 dark:bg-slate-800" />
                  <div className="h-3 w-1/2 animate-pulse rounded bg-slate-100 dark:bg-slate-800" />
                  <div className="h-9 w-full animate-pulse rounded-xl bg-slate-100 dark:bg-slate-800" />
                </div>
              )}

              <div className="mt-5 flex items-start gap-2 rounded-xl bg-slate-50 px-3 py-2.5 text-[11px] leading-relaxed text-slate-500 dark:bg-slate-800/60 dark:text-slate-400">
                <Sparkles className="mt-0.5 h-3.5 w-3.5 shrink-0 text-amber-500" />
                <p>
                  Cevabı kaynakta okunamayan sorular yapay zekâ ile çözülüp ayrıca işaretlenir.
                  Her soruda kaynak PDF bağlantısı bulunur.
                </p>
              </div>
            </div>

            <div className="card absolute -bottom-5 -left-4 hidden items-center gap-2 px-3 py-2 text-xs font-medium text-slate-600 sm:flex dark:text-slate-300">
              <span className="flex h-6 w-6 items-center justify-center rounded-full bg-emerald-100 text-emerald-600 dark:bg-emerald-500/15 dark:text-emerald-400">
                <CheckCircle2 className="h-3.5 w-3.5" />
              </span>
              {answered} soru çözüldü
            </div>
          </div>
        </div>
      </section>

      <section className="page-shell py-14 sm:py-16">
        <div className="flex flex-wrap items-end justify-between gap-3">
          <div>
            <h2 className="text-2xl font-bold tracking-tight text-slate-900 dark:text-white">
              Nasıl çalışmak istersin?
            </h2>
            <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
              Dört farklı çalışma akışı, tek arşiv.
            </p>
          </div>
          <Link
            to="/cikmislar"
            className="inline-flex items-center gap-1 text-sm font-semibold text-indigo-600 hover:text-indigo-700 dark:text-indigo-300"
          >
            Tümünü gör
            <ArrowRight className="h-4 w-4" />
          </Link>
        </div>

        <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => {
            const Icon = feature.icon;
            return (
              <Link key={feature.title} to={feature.to} className="card card-hover group flex flex-col p-5">
                <span className={`flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br ${feature.color} text-white shadow-sm`}>
                  <Icon className="h-5 w-5" />
                </span>
                <h3 className="mt-4 text-base font-bold text-slate-900 dark:text-white">{feature.title}</h3>
                <p className="mt-1.5 flex-1 text-sm leading-relaxed text-slate-500 dark:text-slate-400">
                  {feature.text}
                </p>
                <span className="mt-4 inline-flex items-center gap-1 text-xs font-semibold text-indigo-600 dark:text-indigo-300">
                  {feature.cta}
                  <ArrowRight className="h-3.5 w-3.5 transition group-hover:translate-x-0.5" />
                </span>
              </Link>
            );
          })}
        </div>
      </section>

      <section className="border-y border-slate-200/80 bg-white dark:border-slate-800/80 dark:bg-slate-900/40">
        <div className="page-shell py-14 sm:py-16">
          <div className="grid gap-8 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
            <div>
              <span className="chip border-emerald-200 bg-emerald-50 text-emerald-700 dark:border-emerald-500/30 dark:bg-emerald-500/10 dark:text-emerald-300">
                <CheckCircle2 className="h-3.5 w-3.5" />
                Şeffaf cevap anahtarı
              </span>
              <h2 className="mt-4 text-2xl font-bold tracking-tight text-slate-900 dark:text-white">
                Hangi cevap nereden geliyor, biliyorsun.
              </h2>
              <p className="mt-3 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
                Her soru resmî anahtar, yapay zekâ çözümü veya eksik olarak etiketlenir. Böylece
                hangi soruya ne kadar güvenebileceğini görür, kaynağından kendin kontrol edebilirsin.
              </p>
              <ul className="mt-5 space-y-3 text-sm text-slate-600 dark:text-slate-300">
                {[
                  "Resmî cevap anahtarı: sınav kâğıdındaki basılı cevap.",
                  "AI ile çözüldü: basılı cevabı okunamayan sorular, ayrıca işaretli.",
                  "Kaynak PDF: her sorunun bulunduğu sayfaya doğrudan bağlantı.",
                ].map((text) => (
                  <li key={text} className="flex items-start gap-2">
                    <CheckCircle2 className="mt-0.5 h-4 w-4 shrink-0 text-emerald-500" />
                    {text}
                  </li>
                ))}
              </ul>
            </div>

            <div className="space-y-4">
              {index?.exams.map((exam) => {
                const examAnswered = Object.values(answers).filter((a) => a.examId === exam.id).length;
                return (
                  <ExamCard
                    key={exam.id}
                    exam={exam}
                    answered={examAnswered}
                    total={exam.questionCount}
                  />
                );
              })}

              {loading && (
                <div className="card space-y-3 p-6">
                  <div className="h-4 w-1/3 animate-pulse rounded bg-slate-100 dark:bg-slate-800" />
                  <div className="h-3 w-2/3 animate-pulse rounded bg-slate-100 dark:bg-slate-800" />
                  <div className="h-2 w-full animate-pulse rounded bg-slate-100 dark:bg-slate-800" />
                </div>
              )}

              {error && (
                <div className="card border-amber-200 bg-amber-50 p-5 text-sm text-amber-800 dark:border-amber-500/30 dark:bg-amber-500/10 dark:text-amber-200">
                  Veriler yüklenemedi: {error}
                </div>
              )}

              <p className="px-1 text-xs leading-relaxed text-slate-400 dark:text-slate-500">
                Arşiv şu anda Dönem 1 / TEM 2 kapsamındadır. Yeni yıllar aynı doğrulama sürecinden
                geçirilerek sırayla eklenir.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="page-shell py-14 sm:py-16">
        <div className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-indigo-600 via-violet-600 to-indigo-700 px-6 py-10 text-white sm:px-10">
          <div className="pointer-events-none absolute -right-16 -top-16 h-56 w-56 rounded-full bg-white/10 blur-2xl" />
          <div className="pointer-events-none absolute -bottom-20 left-1/3 h-56 w-56 rounded-full bg-white/10 blur-2xl" />
          <div className="relative flex flex-col items-start justify-between gap-6 sm:flex-row sm:items-center">
            <div>
              <h2 className="text-2xl font-bold tracking-tight">Hazırsan başlayalım.</h2>
              <p className="mt-2 max-w-xl text-sm text-indigo-100">
                2024-2025 Dönem 1 TEM 2 sınavının 105 sorusu hazır. Ders seç, test modunu ayarla ve
                çözmeye başla.
              </p>
            </div>
            <div className="flex flex-wrap gap-2">
              <Link
                to={featured ? `/test/${featured.id}` : "/cikmislar"}
                className="btn bg-white text-indigo-700 hover:bg-indigo-50"
              >
                Teste başla
                <ArrowRight className="h-4 w-4" />
              </Link>
              <Link
                to="/ilerleme"
                className="btn border border-white/30 bg-white/10 text-white hover:bg-white/20"
              >
                İlerlemem
              </Link>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
