# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
61: "İmmun sistem innate (doğal) ve adaptif (kazanılmış) olarak ayrılır; adaptif T ve B hücreleri ile hümoral ve hücre-sel yanıt verir.",
62: "Antijen sunan hücreler (APC): dendritik hücreler, makrofajlar, B hücreleri; MHC II ile CD4+ T hücrelerine sunum yapar.",
63: "MHC I tüm nükleuslu hücrelerde bulunur ve CD8+ sitotoksik T hücrelerine endojen antijen sunar.",
64: "Antikor sınıfları: IgM (ilk yanıt), IgG (plasenta geçer), IgA (sekretuar), IgE (alerji/parazit), IgD (B hücre reseptörü).",
65: "Kompleman sistemi klasik (antikor), lektin (mannoz) ve alternatif (mikrobik yüzey) yollarla aktive olur; opsonizasyon ve lizis yapar.",
66: "Hipertansiyon tanımı: sistolik ≥140 veya diyastolik ≥90 mmHg; primer (esansiyel) %90-95, sekonder %5-10'dur.",
67: "Ateroskleroz risk faktörleri: hiperlipidemi, hipertansiyon, sigara, diyabet, yaş, erkek cinsiyet, aile öyküsü.",
68: "Miyokard enfarktüsünde troponin I/T ve CK-MB yükselir; ST elevasyonu (STEMI) veya non-ST (NSTEMI) olarak ayrılır.",
69: "Kalp yetmezliğinde sol (dispne, ortopne) veya sağ (periferik ödem, hepatomegali) bulgular baskın olabilir.",
70: "Aritmiler sinüs, atriyal, ventriküler ve AV blok olarak sınıflanır; ventriküler fibrilasyon acil defibrilasyon gerektirir.",
71: "Anemi tanımı: hemoglobin düşüklüğü; mikrositer (demir), makrositer (B12/folat), normositer (kronik hastalık) olarak ayrılır.",
72: "Lökosit formülü: nötrofil %40-70, lenfosit %20-40, monosit %2-8, eozinofil %1-4, bazofil %0-1.",
73: "Trombositopeni kanama riskini artırır; ITP, TTP, HIT ve kemik iliği baskılanması nedenler arasındadır.",
74: "Hemostaz vasküler spazm, trombosit tıkaç ve koagülasyon kaskadı ile sağlanır; PT (ekstrinsik), aPTT (intrinsik) ölçülür.",
75: "Kan grupları ABO ve Rh; transfüzyon reaksiyonları hemolitik, febril, alerjik, TRALI, TACO olarak ayrılır.",
76: "Hemofili A (faktör VIII) ve B (faktör IX) X'e bağlı resesif; von Willebrand hastalığı en sık kanama diyatezidir.",
77: "Solunum fizyolojisi: tidal volüm, vital kapasite, total akciğer kapasitesi; gaz değişimi alveol-kapiller membranda olur.",
78: "Hipoksi tipleri: hipoksemik (PaO2 düşük), anemik (Hb düşük), iskemik (kan akımı düşük), histotoksik (hücre kullanamaz).",
79: "Astım reversibl bronkospazm ve inflamasyon ile karakterize; spirometri ile FEV1/FVC düşüklüğü ve reversibilite gösterilir.",
80: "KOAH progresif hava akımı kısıtlılığı; spirometri FEV1/FVC <0.70; sigara en önemli risk faktörüdür.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
