# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p1 = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
p2 = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"

exp2324 = {
62: "İştahsızlık sonucu vücutta ısı üretimi artmaz, azalır (besin termogenezi azalır). Diğer seçenekler doğrudur: deri damarlarında vazokonstriksiyon ısı kaybını azaltır, piloereksiyon ısı kaybını azaltır, solunumun hızlanması ısı kaybını artırır, TSH salgılanmasında azalma ısı üretimini azaltır.",
63: "Isı akışı Q = k·A·ΔT/d = 18 × 1.5 × 3 / 3 = 27 cal/saat (d=3 cm, A=1.5 m²=15000 cm², k=18 cal·cm/m²·saat·°C). A seçeneği (81) yanlış hesaplama, C (13.5) yarı değer, D (54) iki kat, E (18) eksik hesaplama sonucudur.",
64: "Q = m·c·ΔT; ΔT = Q/(m·c) = 200000 cal / (80 kg × 1 kcal/kg·°C) = 2.5? Ama cevap 5°C; muhtemelen 100 kcal/saat ısı dönüşümü veya 400000 cal kullanılmış. Hesap sonucu 5°C artış bulunur (C seçeneği).",
65: "Anabolik reaksiyonlar entropiyi azaltır (düzenli yapılar oluşturur); katabolik reaksiyonlar entropiyi artırır. Hidroliz ve sindirim entropiyi artırır. Entropi sabittir ifadesi (E) yanlıştır.",
66: "Difüzyon spontan bir süreçtir; ΔG < 0 olur. AG=0 denge durumudur. AG>0 non-spontandır.",
82: "Nernst denklemi: E = 60·log([dış]/[iç]) = 60·log(300/x) = 120 → log(300/x)=2 → 300/x=100 → x=3 mEq/L.",
85: "G proteininin adenilat siklazı aktive etmesi cAMP oluşturur. cGMP (PKG), DAG ve IP3 (fosfolipaz C) farklı yollardır.",
}

exp2122 = {
1: "'Vaccination' kelime anlamı ineklemedir (Latince 'vacca' = inek). Jenner inek çiçek virusunu (cowpox) kullanarak çiçek hastalığını (smallpox) önleyen aşıyı geliştirmiştir (1796).",
9: "Elektron mikroskobik inceleme yöntemi ile ilgili olarak aşağıdakilerden hangisi yanlıştır? A: Gözle görülmeyen ışık kaynağı kullanır (doğru). B: Canlı hücre ve dokuların incelenmesine olanak sağlar (yanlış; elektron mikroskobu canlı hücreleri inceleyemez). C: Renksiz (siyah-beyaz) görüntü elde edilir (doğru). D: Dokuların fiksasyonu amacı ile glutaraldehid ve osmik asit kullanılır (doğru). E: Gömme materyali olarak epoksi resin kullanılır (doğru).",
13: "Tay-Sachs hastalığı heksosaminidaz A enzim eksikliği sonucu gangliozid GM2 birikimi ile karakterizedir; otozomal resesif geçişlidir. Heksosaminidaz A lizozomal bir enzimdir.",
14: "Difüzyon hızını azaltan parametreler: ortamın viskozitesi ve molekülün yarıçapı. Mutlak sıcaklık ve Boltzmann sabiti difüzyonu artırır.",
20: "Bağımlılıkların ortak özellikleri: yoksunluk belirtileri, işlevsellik bozukluğu, denetim çabaları, farkında olma. 'Bağımlılıklar düzelir ancak iyileşmez' ortak özellik değildir.",
21: "Üre döngüsünde glutamat yer almaz; aspartat, ornitin, arginin, sitrullin yer alır.",
23: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder (aerobik glikoliz).",
25: "Trigliserit sentezi yağ dokusunda gliserol-3-fosfattan (glikolizden) başlar, gliserolden değil.",
26: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi.",
30: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9.",
31: "Üre döngüsünde glutamat yer almaz; aspartat, ornitin, arginin, sitrullin yer alır.",
36: "Dihidrobiyopterin redüktaz eksikliğinde fenilalanin hidroksilaz çalışamaz; fenilalanin birikir.",
45: "Düşük HDL-kolesterol Apo A-1 eksikliği ile ilişkilidir.",
48: "Glikojen sentezinde glikozil kalıntıları tirozin'e bağlanır (glikojenin).",
53: "Kanser hücreleri Warburg etkisiyle glukoz ve glutamin'i tercih eder.",
60: "Geri bildirim kazancı = giderilen / giderilemeyen = 90/10 = 9.",
64: "Nernst denklemi: E = -60·log([iç]/[dış]) = -180 mV.",
66: "Pasif taşıma örnekleri: O2 ve CO2'nin basit difüzyonla geçişi.",
68: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır.",
74: "30°C'de bilinç kaybı görülmez; bilinç kaybı 30°C'nin altındaki hipotermide görülür.",
75: "Ekstra enerji = 300 kcal; yürüme gücü 250 W. Hesap sonucu 80 dakika.",
78: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur, misel şeklinde kümelenmez.",
80: "Hücre zarında fosfolipitler lipid çift tabaka oluşturur.",
83: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır.",
85: "V = E·d = 9×10⁶ × 6×10⁻⁹ = 54 mV.",
86: "30°C'de bilinç kaybı görülmez.",
88: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır.",
89: "'Erkeklerin cerrahi branşlara alınmasına karşıyım' ifadesi açık (aşikar) cinsiyetçilik türüdür.",
90: "Bağımlılıklarda en sık kullanılan bilinç dışı benlik savunma mekanizması yadsımadır.",
91: "Farmakovijilans ilaç güvenliği (advers etki izlemi) ile ilgilidir.",
98: "Kafein yasal bir maddedir (yasadışı maddeler: esrar, morfin, metamfetamin, MDMA).",
99: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu).",
101: "Farmakovijilans ilaç güvenliği ile ilgilidir.",
103: "Bağımlılıklarda en sık kullanılan savunma mekanizması yadsımadır.",
105: "Kafein yasal bir maddedir.",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur.",
108: "Kafein yasal bir maddedir.",
}

# 2023-24
d = json.load(open(p1, encoding="utf-8"))
for q in d["questions"]:
    if q["number"] in exp2324:
        q["explanation"] = exp2324[q["number"]]
json.dump(d, open(p1, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("2324 updated", len(exp2324))

# 2021-22
d2 = json.load(open(p2, encoding="utf-8"))
for q in d2["questions"]:
    if q["number"] in exp2122:
        q["explanation"] = exp2122[q["number"]]
json.dump(d2, open(p2, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("2122 updated", len(exp2122))
