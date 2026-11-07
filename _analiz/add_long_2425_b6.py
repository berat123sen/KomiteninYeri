# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
26: """Transaminasyon (aminotransferaz) reaksiyonları hem sentez hem yıkımda görev alır; amino grup bir ketoaside transfer edilir (serbest amonyak açığa çıkmaz). I. Hem sentez hem de yıkımda görev alırlar: Doğrudur. II. Yıkım sırasında serbest amonyak açığa çıkar: Yanlıştır; amino grup ketoaside transfer edilir, serbest amonyak çıkmaz (oksidatif deaminasyon ve dehidratazyon reaksiyonlarında amonyak açığa çıkar). III. Sentez sırasında serbest amonyak bir ketoaside bağlanır: Yanlıştır; transaminasyonda serbest amonyak kullanılmaz. Doğru cevap A'dır (sadece I).""",
27: """Glutamat dehidrogenaz (GDH) mitokondri matrisinde bulunur; glutamat + NAD(P)+ → α-ketoglutarat + NH4+ + NAD(P)H dönüşümünü katalize eder (oksidatif deaminasyon). I. Tepkime sonucunda alfa-ketoglutarat oluşur: Doğrudur. II. Bu enzim mitokondri matriksinde bulunur: Doğrudur. III. Kofaktör olarak NAD ve NADP'yi kullanır: Doğrudur (NAD+ veya NADP+). C seçeneği (I, II ve III) doğrudur.""",
28: """Karbamoil fosfat sentetaz I (CPS I) üre döngüsünün ilk enzimidir: NH4+ + HCO3- + 2ATP → karbamoil fosfat + 2ADP + Pi. I. Tepkime için N-asetil glutamat'a gereksinimi vardır: Doğrudur (NAG allosterik aktivatördür). II. Substrat olarak bikarbonat ve serbest amonyak kullanılır: Doğrudur. III. Reaksiyon sırasında 2 ATP'den 2 ADP oluşur: Doğrudur (2 ATP harcanır). C seçeneği (I, II ve III) doğrudur.""",
29: """Homosistein→metionin dönüşümü metionin sentaz (B12 vitamini kofaktörü) ve metiltetrahidrofolat (folik asit türevi) gerektirir. B12 eksikliği homosistein birikimine (hiperhomosisteinemi) yol açar. Biotin (B7), niasin (B3), tiamin (B1) bu reaksiyonda rol oynamaz. D seçeneği (folik asit) doğrudur.""",
30: """Triptofanın aşırı serotonin sentezine yönlendirilmesi niasin (B3) eksikliğine (pellagra) yol açar; triptofan niasin sentezinin öncüsüdür (kinürenin yolağı). B12 vitamini, biotin, folik asit ve tiamin bu süreçte rol oynamaz. C seçeneği (niasin) doğrudur.""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
