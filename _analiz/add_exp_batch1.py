# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
1: "E doğrudur: Canlıların temel yapısal birimi hücredir ve bu hücre teorisi ile ortaya konmuştur; elektron mikroskobu sonradan gelir. A, B, C, D tanımlamaları doğrudur.",
2: "İnsan gözünün ayırma gücü hücreleri ayırt etmek için yeterli değildir; mikroskop gerekir. A, B, D, E doğru tanımlamalardır.",
3: "Elektron mikroskobik takipte gömme rezin, kesit ultramikrotom, boyama uranil asetat-kurşun sitrat kullanılır. Formalin tespit ve ksilol şeffaflandırma ışık mikroskobu içindir.",
4: "Kollajen liflerini boyamak için Masson trikrom tercih edilir. Van Gieson elastik lifler, PAS glikoproteinler, H&E genel yapı, gümüşleme retiküler lifler içindir.",
5: "Lizozomlar makrofaj/nötrofillerde boldur; membran iç yüzeyinin glikozillenmesi ve lizobifosfatidik asit onları kendi enzimlerinden korur; membran proteinleri Golgi'de sentezlenir.",
6: "Koagülasyon nekrozunda hücre genel yapısı korunur. Kazeifikasyon peynirimsi, fibrinoid damar duvarında eozinofilik birikim, likuefaksiyon sıvılaşma, gangrenöz iskemik nekrozdur.",
7: "Anterior mediastende timus, perikardiyum ön yüzü, aort kökü, trakea alt kısmı yer alır; posterior mediastende özofagus, aorta, vagus siniri bulunur.",
8: "Plazma hücresi antikor üreten terminal B hücresidir. Makrofaj fagositoz, mast hücresi histamin, eozinofil parazit/alergi, nötrofil akut inflamasyon ile ilişkilidir.",
9: "Glikokaliks hücre yüzeyinde glikoprotein ve glikolipitlerden oluşur; tanınma, koruma ve yapışma sağlar, enerji üretmez.",
10: "Sarkomerin A bandı kalın (miyozin), I bandı ince (aktin) filamentleri içerir; H bandı yalnız miyozin, Z çizgisi sınır, M çizgisi merkezdir.",
11: "Aktin-miyozin etkileşimi ATP ve Ca2+ gerektirir; tropomiyozin aktini örter, troponin Ca2+ bağlar. Kreatin fosfat enerji deposudur, glikojen depo polisakkarittir.",
12: "Mitokondri iç membranı kristalar (oksidatif fosforilasyon), dış membran porin içerir; matriste Krebs enzimleri ve mtDNA bulunur.",
13: "Hücre iskeleti mikrotübüller (tubulin), mikrofilamanlar (aktin) ve ara filamentlerden oluşur; miozin motor protein, dynein/kinesin mikrotübüllerde hareket sağlar.",
14: "Gap junction (nexus) hücreler arası iyon ve küçük molekül geçişine izin verir. Desmozom mekanik, hemidesmozom bazal membrana, tight junction bariyer, adherens junction aktin bağlantısıdır.",
15: "Bazal membran epitel ile bağ dokusu arasında bulunur; filtrasyon ve destek sağlar. Retiküler lamina ve lamina densa katmanlarından oluşur.",
16: "Hücre bölünmesinde sentrozom mikrotübülleri organize eder; sentriol çifti içerir. Sentrozom olmayan hücreler (örn. bitki) de bölünebilir.",
17: "Hücre membranı fosfolipit çift tabakadan oluşur; kolesterol akışkanlığı düzenler, proteinler transport ve sinyal görevi görür.",
18: "Endoplazmik retikulum ribozomlu (granüllü) protein sentezi, ribozomsuz (düz) lipid sentezi ve detoksifikasyon yapar.",
19: "Golgi kompleksi proteinleri modifiye eder, paketler ve hedefler; cis-Golgi ER'den alır, trans-Golgi salgılar.",
20: "Lizozomlar asidik hidrolazlar içerir; fagozitoz, otofaji ve heterofaji yapar; membran hasarı hücre ölümüne yol açar.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
