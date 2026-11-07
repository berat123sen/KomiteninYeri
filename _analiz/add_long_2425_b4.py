# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
16: """ABC (ATP-binding cassette) taşıyıcılar ATP hidrolizi ile primer aktif taşıma yapar ve birçok maddenin taşınmasında rol oynar. I. Vitamin: ABC taşıyıcılar (örn. MRP, BCRP) vitamin ve metabolit taşımasında rol oynar. Doğrudur. II. Ca2+: Ca2+ taşıması SERCA (sarko/endoplazmik retikulum Ca2+-ATPaz, P-tipi) ve PMCA (plazma membran Ca2+-ATPaz) ile yapılır; ABC taşıyıcıları Ca2+ taşımaz. Yanlıştır. III. Ksenobiyotik: ABC taşıyıcılar (P-glikoprotein/MDR1, MRP1) ilaç ve toksin (ksenobiyotik) taşımasında önemli rol oynar. Doğrudur. IV. H+: H+ taşıması V-tipi ATPaz (vakuoler proton pompası) ile yapılır. ABC taşıyıcıları H+ taşımaz. Yanlıştır. Doğru cevap C'dir (I ve III).""",
17: """Kolera toksini (koleragen, Vibrio cholerae tarafından üretilir) ince bağırsak epitel hücrelerinde adenilat siklazı aktive eder → cAMP artışı → CFTR (kistik fibrozis transmembran iletkenlik düzenleyici) klor kanalı açılması → Cl- ve su sekresyonu → profus diyare. Oral rehidratasyon tedavisinde (ORT) Na+-glikoz kotransporteri (SGLT1) kullanılır; glukoz ve Na+ sekonder aktif taşıma ile emilir, su osmozla takip eder. Bu mekanizma kolera toksininin etkisini bypass eder. A seçeneği: Endositoz madde alınmasıdır. B seçeneği: Basit difüzyon enerji gerektirmeyen pasif taşımadır. C seçeneği: Primer aktif taşıma ATP harcar (Na/K-ATPaz). E seçeneği: Kolaylaştırılmış difüzyon taşıyıcı protein ile pasif taşımadır. Doğru cevap D'dir (sekonder aktif taşıma).""",
18: """Fosfodiesteraz (PDE) enzimi cAMP ve cGMP'yi (ikinci haberciler) 5'-AMP ve 5'-GMP'ye hidrolize eder; ikinci habercileri inaktive eder. IP3 (inositol trisfosfat) ve DAG (diasilgliserol) fosfolipaz C ürünleridir, PDE substratı değildir. NF-κB transkripsiyon faktörüdür. PGE2 prostaglandindir. cGMP'yi etkisiz hale getiren PDE'dir (PDE5: sildenafil hedefi, erektil disfonksiyon tedavisinde kullanılır).""",
19: """Nitrik oksit (NO) guanilil siklazı (sGC) aktive eder → cGMP artışı → protein kinaz G (PKG) aktivasyonu → düz kas relaksasyonu (vazodilatasyon). Tirozin kinaz-IP3 (yanlış: tirozin kinaz reseptör tirozin kinazları, IP3 fosfolipaz C ürünü), serin-treonin kinaz-cAMP (yanlış: serin-treonin kinazlar farklı yollar), adenilil siklaz-cAMP (adenilil siklaz cAMP üretir ama NO hedefi değildir), fosfataz-cGMP (fosfataz fosfat grubu uzaklaştırır, NO hedefi değildir) eşleşmeleri yanlıştır. Doğru eşleştirme E'dir (guanilil siklaz-cGMP).""",
20: """Yağ sindiriminde lingual lipaz (dil, pH 4-6) ve gastrik lipaz (mide, pH 4-6) aktif olup kofaktör gerektirmez; pankreatik lipaz (ince bağırsak, pH 8) için kofaktör koloipazdır (colipase). A seçeneği: barsak hücreleri (enterositler) apo B-48 üretir (şilomikron yapı proteini). Doğrudur. B seçeneği: pankreatik lipaz trigliseritleri monoasilgliserol ve serbest yağ asidine yıkar. Doğrudur. C seçeneği: barsak epitel hücrelerinde tekrar trigliserit sentezlenir (monoasilgliserol yolu). Doğrudur. E seçeneği: barsakta sentezlenen şilomikronlar diyet trigliseritlerini taşır. Doğrudur. D seçeneği lingual ve gastrik lipazın aktivasyonu için koloipaz gereksinimi olduğunu iddia ettiği için yanlıştır; koloipaz sadece pankreatik lipaz için gereklidir.""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
