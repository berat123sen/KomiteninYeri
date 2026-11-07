# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
77: "Soğuk ortamda vücut ısısını korumak için deri damarlarında vazokonstriksiyon ve tiroid hormon salgısında artma görülür (I ve II). Adrenalin salgısı ve piloereksiyon (III, IV) de devreye girer ancak seçeneklerde I ve II birlikteliği doğrudur.",
78: "Lökosit granüllerinin (hidrolazlar) sentezi granüllü endoplazmik retikulum ve Golgi aygıtı üzerinden yapılır. Düz ER, peroksizom, serbest ribozom ve salgı granülü bu sentezde rol oynamaz.",
79: "Uzun zincirli yağ asitlerinin peroksizomlarda beta-oksidasyonu (oksidasyon) gerçekleşir. Hidroksilasyon, lizozom ve Golgi aparatı bu süreçte rol oynamaz.",
80: "Translasyon sırası: amino asidin aktifleşmesi (aminoasil-tRNA sentetaz) → tRNA-amino asit kompleksi → kodon-antikodon bağlanması (ribosomda) → peptid bağı oluşumu (peptidil transferaz).",
81: "D vitamini reseptörü hücre içi (nükleer) reseptördür. Glisin, noradrenalin ve prostaglandinler membran reseptörüne sahiptir (II ve III).",
82: "Nernst denklemi: E = 60·log([dış]/[iç]) = 60·log(300/x) = 120 → log(300/x)=2 → 300/x=100 → x=3 mEq/L.",
83: "Oral rehidratasyon çözeltisindeki glukoz ve Na+ emilimi Na+-glikoz kotransporteri (SGLT1) aracılığıyla sağlanır. Na+-H+, Na+-Ca2+, HCO3--Cl- ve Na+-K+-2Cl- taşıyıcıları bu işlevi görmez.",
84: "İnsülin eksikliğinde glukozun hücreye alınması (GLUT4 translokasyonu) bozulur; bu kolaylaştırılmış difüzyondur. Endositoz, basit difüzyon, primer ve sekonder aktif taşıma farklı mekanizmalardır.",
85: "G proteininin adenilat siklazı aktive etmesi cAMP oluşturur. cGMP (PKG), DAG ve IP3 (fosfolipaz C) farklı yollardır.",
86: "Düşük doz aspirin tromboksan A2 sentezini (COX-1 inhibisyonu) baskılayarak prostasiklin lehine denge kurar (antitrombotik etki).",
87: "Nitrik oksit guanilat siklazı aktive eder; cGMP artışı protein kinaz G (PKG) aktivasyonu ile düz kas relaksasyonu (vazodilatasyon) sağlar.",
88: "Güdüler organizmanın gereksinimlerini başlatan ve dengeyi sağlayan içsel güçlerdir; değişmeyen/türe özgü güçler değildir.",
89: "Bunaltıcı durumu sıkıntı vermeyecek bir nedenle açıklama bulmak 'rasyonalizasyon (akla uygunlaştırma)' savunma düzenegidir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
