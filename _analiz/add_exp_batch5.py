# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
81: "Pnömoni alveol inflamasyonu ve konsolidasyon ile karakterize; tipik (bakteriyel) ve atipik (Mycoplasma, viral) ayrılır.",
82: "Tüberküloz Mycobacterium tuberculosis ile oluşur; granülom, kazeifikasyon, Ghon kompleksi; PPD/IGRA ve balgam ARB ile tanı.",
83: "GİS anatomi ve fizyoloji: özofagus, mide, ince/kalın bağırsak; sindirim, emilim, motilite ve sekresyon süreçleri.",
84: "Gastrit akut (eroziv/eroziv olmayan) veya kronik (H. pylori, otoimmün) olabilir; peptik ülser asit-pepsin dengesizliği ile oluşur.",
85: "İnflamatuar barsak hastalığı: Crohn (transmural, skip lezyon) ve ülseratif kolit (mukoza, sürekli) olarak ayrılır.",
86: "Karaciğer fonksiyonları: sentez (albumin, faktörler), detoksifikasyon, metabolizma, safra üretimi; AST/ALT, bilirubin, albumin ile değerlendirilir.",
87: "Siroz karaciğer fibrozisi ve nodül oluşumu ile karakterize; portal hipertansiyon, asit, varis ve hepatosellüler karsinom komplikasyonları gelişir.",
88: "Böbrek fonksiyonları: filtrasyon (GFR), reabsorbsiyon, sekresyon; kreatinin, BUN, idrar analizi ile değerlendirilir.",
89: "Akut böbrek hasarı prerenal, renal, postrenal nedenlerle oluşur; oligüri, kreatinin artışı ve elektrolit bozuklukları görülür.",
90: "Kronik böbrek hastalığı GFR <60 ml/dk/1.73m2 ve >3 ay; diyabet ve hipertansiyon en sık nedenlerdir.",
91: "Endokrin sistem: hipofiz, tiroid, paratiroid, adrenal, pankreas; hormonlar negatif feedback ile düzenlenir.",
92: "Diyabet mellitus insülin eksikliği/direnci sonucu hiperglisemi; Tip 1 otoimmün, Tip 2 insülin direnci ile karakterizedir.",
93: "Tiroid hastalıkları: hipertiroidi (Graves, toksik nodül) ve hipotiroidi (Hashimoto, iyot eksikliği); TSH, T3, T4 ile değerlendirilir.",
94: "Adrenal hastalıklar: Cushing (kortizol fazlası), Addison (kortizol eksikliği), feokromositoma (katekolamin fazlası).",
95: "Reproduktif sistem: menstrual siklus, spermatogenez, gebelik; hormonlar (FSH, LH, östrojen, progesteron, testosteron) düzenlenir.",
96: "Sinir sistemi: MSS (beyin, omurilik) ve PSS (sinirler); nöron ve glia hücreleri; aksiyon potansiyeli ile sinyal iletimi.",
97: "Serebrovasküler hastalıklar: iskemik (tromboembolik) ve hemorajik (intrakraniyal kanama) inme; risk faktörleri HT, DM, AF.",
98: "Epilepsi nöbetlerle karakterize kronik hastalık; EEG ile tanı; antiepileptik ilaçlarla tedavi.",
99: "Parkinson hastalığı substantia nigra'da dopaminerjik nöron kaybı; tremor, rijidite, bradikinezi, postüral instabilite.",
100: "Alzheimer hastalığı amiloid plak ve nörofibriler yumaklarla karakterize; progresif demans, kolinesteraz inhibitörleri ile tedavi.",
101: "Psikiyatrik bozukluklar: depresyon, anksiyete, bipolar, şizofreni; biyopsikososyal model ile değerlendirilir.",
102: "Madde bağımlılığı tolerans, yoksunluk, kompulsif kullanım ile karakterize; tedavi detoksifikasyon ve rehabilitasyon içerir.",
103: "Pediyatri: büyüme ve gelişme, aşılama, beslenme; yaşa özgü hastalıklar ve gelişimsel kilometre taşları.",
104: "Geriyatri: yaşlılıkta fizyolojik değişiklikler, polifarmasi, düşme, kognitif bozukluk riski artar.",
105: "Halk sağlığı: epidemiyoloji, bulaşıcı hastalıklar kontrolü, aşılama, çevre sağlığı, sağlık politikaları.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
