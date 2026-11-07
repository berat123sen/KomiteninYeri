# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
21: """Palmitoil-CoA (16:0, doymuş yağ asidi) beta-oksidasyonu: 7 döngü → 8 asetil-CoA + 7 FADH2 + 7 NADH. Net ATP = 8×10 (asetil-CoA, TCA'da) + 7×1.5 (FADH2) + 7×2.5 (NADH) - 2 (aktivasyon, karnitin) = 106 ATP. A seçeneği (net 106 ATP) doğrudur. B seçeneği (7 döngü, 8 asetil-CoA) doğrudur. C seçeneği (7 FADH2) doğrudur. D seçeneği: 17 karbonlu yağ asidi (heptadekanoik) 8 asetil-CoA + 1 propiyonil-CoA üretir; propiyonil-CoA glukoneojenik (süksinil-CoA'ya dönüşür) ve daha az ATP üretir; 16 karbonlu palmitat daha fazla ATP üretir. Doğrudur. E seçeneği: Oksidasyon için gerekli NADPH'ler pentoz fosfat yolundan elde edilir ifadesi yanlıştır; beta-oksidasyon NADH ve FADH2 kullanır, NADPH kullanmaz. NADPH pentoz fosfat yolunda üretilir ve biyosentez/detoksifikasyonda kullanılır.""",
22: """Keton cisimcikleri (asetoasetat, beta-hidroksibütirat, aseton) karaciğerde (hepatosit mitokondrisinde) HMG-CoA yolağı ile sentezlenir. A seçeneği: Toklukta kan düzeyleri çok yükselir ifadesi yanlıştır; keton cisimcikleri açlıkta (uzun süreli açlık, diyabetik ketoasidoz) yükselir, toklukta düşük olur. B seçeneği: Kas ve beyin hücreleri tarafından üretilir ifadesi yanlıştır; keton cisimcikleri karaciğerde üretilir (karaciğer ketonları kullanamaz, çünkü tiyoforaz enzimi yoktur). C seçeneği: Sitoplazmada HMG-CoA redüktaz tarafından üretilir ifadesi yanlıştır; HMG-CoA sentaz (redüktaz değil) mitokondride sentezde rol oynar. D seçeneği: Karaciğer tarafından enerji yakıtı olarak kullanılırlar ifadesi yanlıştır; karaciğer ketonları kullanamaz, diğer dokular (beyin, kas, böbrek) kullanır. E seçeneği: Kanda en yüksek konsantrasyonda beta-hidroksibütirat bulunur ifadesi doğrudur (asetoasetat ve aseton daha düşük konsantrasyondadır; aseton uçucu olup akciğerlerden atılır).""",
23: """Asetil-CoA'dan sentezlenemeyen: gliserol-3-fosfat (glikolizden, gliseraldehid-3-fosfattan gelir; gliserol kinaz ile gliserolden de sentezlenir). Kolesterol asetil-CoA'dan sentezlenir (HMG-CoA yolağı). Arakidonik asit (esansiyel yağ asidi linoleik asitten) asetil-CoA'dan sentezlenemez? Aslında arakidonik asit (20:4) linoleik asitten (18:2) elongasyon ve desatürasyon ile sentezlenir; linoleik asit esansiyeldir. HMG-CoA (hidroksimetilglutaril-CoA) asetil-CoA'dan sentezlenir (asetoasetil-CoA + asetil-CoA). Asetoasetat asetil-CoA'dan sentezlenir (ketogenez). A seçeneği (gliserol-3-fosfat) asetil-CoA'dan sentezlenemez; glikolizden gelir.""",
24: """Prostaglandinler (PG) arakidonik asitten (20:4 n-6, esansiyel yağ asidi linoleik asitten sentezlenir) siklooksijenaz (COX-1/COX-2) enzimi ile sentezlenir. I. Prostaglandinlerin öncü maddesi arakidonik asittir: Doğrudur. II. Arakidonik asit esansiyel bir yağ asididir: Yanlıştır; arakidonik asit linoleik asitten sentezlenir; linoleik asit esansiyeldir (insan sentezleyemez). III. Prostaglandin sentezi için siklooksijenaz enzimine gereksinim vardır: Doğrudur. Doğru cevap B'dir (I ve III).""",
25: """Asetil-CoA karboksilaz (ACC) biyotin (B7 vitamini) içeren enzimdir; malonil-CoA üretir (asetil-CoA + HCO3- + ATP → malonil-CoA + ADP + Pi). A seçeneği: malonil-CoA üretimi sağlar (doğru). B seçeneği: substrat olarak asetil-CoA kullanır (doğru). C seçeneği: yapıda prostetik grup olarak piridoksal fosfat (B6) bulunur ifadesi yanlıştır; ACC biyotin (B7) içerir, piridoksal fosfat transaminasyonlarda kofaktördür. D seçeneği: reaksiyon sırasında 1 mol ATP kullanır (doğru). E seçeneği: sentez için HCO3- (bikarbonat) gereksinimi vardır (doğru).""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
