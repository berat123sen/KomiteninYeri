# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
16: "ABC (ATP-binding cassette) taşıyıcılar ATP hidrolizi ile primer aktif taşıma yapar. Vitamin (B, C, folat vb.) ve ksenobiyotik (ilaç, toksin) taşımasında rol oynarlar. Ca2+ taşıması SERCA (P-tipi ATPaz) ile, H+ taşıması V-tipi ATPaz ile yapılır; ABC taşıyıcıları değildir. I ve III doğrudur (C seçeneği).",
17: "Kolera toksini (koleragen) adenilat siklazı aktive eder → cAMP artışı → CFTR klor kanalı açılması → sekretuar diyare. Oral rehidratasyon tedavisinde (ORT) Na+-glikoz kotransporteri (SGLT1) kullanılır; glukoz ve Na+ sekonder aktif taşıma ile emilir, su osmozla takip eder. Endositoz, basit difüzyon, primer aktif taşıma ve kolaylaştırılmış difüzyon bu mekanizmayı açıklamaz.",
18: "Fosfodiesteraz (PDE) cAMP ve cGMP'yi 5'-AMP ve 5'-GMP'ye hidrolize eder; ikinci habercileri inaktive eder. IP3 ve DAG (fosfolipaz C ürünleridir), NF-κB (transkripsiyon faktörü), PGE2 (prostaglandin) fosfodiesteraz substratı değildir. cGMP'yi etkisiz hale getiren PDE'dir (PDE5: sildenafil hedefi).",
19: "Nitrik oksit (NO) guanilil siklazı (sGC) aktive eder → cGMP artışı → protein kinaz G (PKG) aktivasyonu → düz kas relaksasyonu (vazodilatasyon). Tirozin kinaz-IP3, serin-treonin kinaz-cAMP, adenilil siklaz-cAMP, fosfataz-cGMP eşleşmeleri yanlıştır.",
20: "Yağ sindiriminde lingual lipaz (dil, pH 4-6) ve gastrik lipaz (mide, pH 4-6) aktif olup kofaktör gerektirmez; pankreatik lipaz için kofaktör koloipazdır (C seçeneği yanlıştır). A: barsak hücreleri apo B-48 üretir (doğru). B: pankreatik lipaz trigliseritleri monoasilgliserol ve serbest yağ asidine yıkar (doğru). C: barsak epitelyumunda tekrar trigliserit sentezlenir (doğru). E: şilomikronlar diyet trigliseritlerini taşır (doğru).",
21: "Palmitoil-CoA (16:0) beta-oksidasyonu: 7 döngü → 8 asetil-CoA + 7 FADH2 + 7 NADH. Net ATP = 8×10 + 7×1.5 + 7×2.5 - 2 (aktivasyon) = 106 ATP. 17 karbonlu yağ asidi (heptadekanoik) 8 asetil-CoA + 1 propiyonil-CoA üretir; daha az ATP üretir. NADPH pentoz fosfat yolundan değil, NADH beta-oksidasyondan gelir. E seçeneği yanlıştır.",
22: "Keton cisimcikleri (asetoasetat, beta-hidroksibütirat, aseton) karaciğerde (hepatosit mitokondrisinde) sentezlenir; kas ve beyin kullanır (üretmez). Toklukta düşük, açlıkta yüksek. En yüksek konsantrasyonda beta-hidroksibütirat bulunur (aseton değil). C seçeneği: HMG-CoA sentaz (redüktaz değil) sentezde rol oynar. A, B, C, D yanlıştır.",
23: "Asetil-CoA'dan sentezlenemeyen: gliserol-3-fosfat (glikolizden/gliseraldehitten gelir). Kolesterol, arakidonik asit, HMG-CoA ve asetoasetat asetil-CoA'dan sentezlenir.",
24: "Prostaglandinler arakidonik asitten (esansiyel yağ asidi linoleik asitten sentezlenir) siklooksijenaz (COX) ile sentezlenir. I. doğru (arakidonik asit öncül). II. yanlış (arakidonik asit esansiyel değildir, linoleik asit esansiyeldir). III. doğru (COX gerekli). B seçeneği (I ve III) doğrudur.",
25: "Asetil-CoA karboksilaz (ACC) biyotin (B7) içeren enzimdir; malonil-CoA üretir, 1 ATP harcar, HCO3- (bikarbonat) gereklidir. Piridoksal fosfat (B6) transaminasyonlarda kofaktördür, ACC'de bulunmaz. C seçeneği yanlıştır.",
26: "Transaminasyon (aminotransferaz) reaksiyonları hem sentez hem yıkımda görev alır; serbest amonyak açığa çıkmaz (amino grup amino aside transfer edilir). I doğru, II ve III yanlıştır. A seçeneği doğrudur.",
27: "Glutamat dehidrogenaz (GDH) mitokondri matrisinde bulunur; glutamat → α-ketoglutarat + NH4+ + NAD(P)H dönüşümünü katalize eder. Kofaktör olarak NAD+ ve NADP+ kullanır. I, II, III doğrudur (C seçeneği).",
28: "Karbamoil fosfat sentetaz I (CPS I) üre döngüsünün ilk enzimidir: NH4+ + HCO3- + 2ATP → karbamoil fosfat + 2ADP + Pi. N-asetilglutamat (NAG) allosterik aktivatördür. I, II, III doğrudur (C seçeneği).",
29: "Homosistein→metionin dönüşümü metionin sentaz (B12 vitamini kofaktörü) ve metiltetrahidrofolat (folik asit türevi) gerektirir. B12 eksikliği homosistein birikimine yol açar. D seçeneği (folik asit) gereklidir.",
30: "Triptofan aşırı serotonin sentezine yönlendirildiğinde niasin (B3) eksikliği (pellagra) gelişir; triptofan niasin sentezinin öncüsüdür.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
