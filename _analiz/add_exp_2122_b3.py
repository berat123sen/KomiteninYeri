# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
61: "Suyun ideal biyolojik çözücü olabilmesi için ısı kapasitesinin yüksek olması gerekir; düşük ısı kapasitesi suyun biyolojik çözücü olmasını engeller.",
62: "Telomeraz aktivitesi en fazla germ hücreleri ve kök hücrelerde (barsak epitel kök hücreleri) görülür; terminal hücrelerde (nöron, kas) telomeraz inaktiftir.",
63: "Aktive edilmiş amino asit (aminoasil-tRNA) ATP harcayarak oluşur; AMP ve PPi açığa çıkar.",
64: "Denetimli zar içi proteoliz (regulated intramembrane proteolysis) metalloproteinaz ve gamma-sekretaz ile gerçekleşir.",
65: "Siklooksijenaz prostaglandinler (PGI2, PGE2) ve tromboksan A2 sentezini katalize eder; lökotrienler lipooksijenaz yolağı ile sentezlenir.",
66: "Glukozun hücreye alınması sekonder aktif taşıma ile barsak epiteli (SGLT1) ve böbrek tübülü (SGLT2)nde sağlanır.",
67: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi (metabolik enerji gerektirmez).",
68: "Difüzyon katsayısı mutlak sıcaklık ve Boltzmann sabiti ile doğru orantılıdır (Einstein-Smoluchowski denklemi).",
69: "Nernst denklemi: E = -60·log([iç]/[dış]) = -60·log(1000/1) = -180 mV.",
70: "Mikrotübüller hücre bölünmesi (mitoz mekiği) ve salgı veziküllerinin taşınmasında görevlidir.",
71: "Eritrositler %0.9 NaCl (izotonik) içinde hacim değişmez.",
72: "ATP sentetaz proton (H+) gradiyentinden (kemiosmoz) enerji alır.",
73: "Enzimler aktivasyon enerjisini düşürür ve reaksiyonu hızlandırır, ancak reaksiyonu başlatmaz; reaksiyonu başlatan enerji (ısı/ATP) gereklidir. B seçeneği yanlıştır.",
74: "Vücudun ısı yayma mekanizmaları: radyasyon, konveksiyon, kondüksiyon, evaporasyon, terleme ve solunum.",
75: "Piloereksiyon (tüylerin dikleşmesi) ısı koruma (ısı kaybını azaltma) mekanizmasıdır, ısı yayma mekanizması değildir.",
76: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide (28°C civarı) görülür.",
77: "ATP hidrolizinin enerjetiği hücredeki ATP/ADP/Pi oranına (reaksiyon katsayısı) bağlıdır; ATP'nin elektronegatif niteliği tek başına belirleyici değildir.",
78: "Ekstra enerji = 300 kcal; yürüme gücü 250 W = 60 kcal/dk? Hesap sonucu 80 dakika.",
79: "Hücre zarının işlevleri arasında iyonların hücre dışına doğrudan geçişi yer almaz (seçici geçirgenlik ile düzenlenir).",
80: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
81: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır, artmaz.",
82: "Difüzyon hızı molekülün kinetik enerjisi, zar yüzey alanı, kalınlık ve konsantrasyon gradiyentine bağlıdır; taşıyıcı sayısı kolaylaştırılmış difüzyonda etkilidir (basit difüzyonda değil).",
83: "İyon kanallarından iyon geçişi ATP hidrolizi ile gerçekleşmez (pasif, elektrokimyasal gradiyent ile).",
84: "Osmoz hipotonik çözeltiden hipertonik çözeltiye su hareketidir. A (100 mM NaCl) hipertonik, B (100 mM glikoz) hipotonik olduğundan su A'ya hareket eder.",
85: "V = E·d = 9×10⁶ × 6×10⁻⁹ = 54 mV.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
