# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
66: "Difüzyon spontan bir süreçtir; ΔG < 0 olur. AG=0 denge durumudur. AG>0 non-spontandır. Hesaplanamaz ve AG=[] ifadeleri yanlıştır. Difüzyon entropi artışı ile ilişkilidir.",
81: "Nernst denklemi: E = 60·log([dış]/[iç]) = 60·log(300/x) = 120 → log(300/x)=2 → 300/x=100 → x=3 mEq/L. 30, 60, 300, 600 mEq/L yanlıştır. Nernst denklemi bir iyonun denge potansiyelini hesaplar.",
84: "G proteininin adenilat siklazı aktive etmesi cAMP oluşturur. cGMP (PKG), DAG ve IP3 (fosfolipaz C) farklı yollardır. Gs (stimülatör) adenilat siklazı aktive eder; Gi (inhibitör) inhibe eder.",
88: "Güdüler organizmanın gereksinimlerini başlatan ve dengeyi sağlayan içsel güçlerdir; değişmeyen/türe özgü güçler değildir. Güdüler fizyolojik (açlık, susuzluk) ve psikolojik (başarı, merak) olabilir.",
89: "Bunaltıcı durumu sıkıntı vermeyecek bir nedenle açıklama bulmak 'rasyonalizasyon (akla uygunlaştırma)' savunma düzenegidir. Düşünselleştirme (intellectualization) farklı bir savunma mekanizmasıdır.",
94: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir. Kafein sempatik aktiviteyi artırır ve stresi artırabilir.",
98: "Çocuğun kaza yoluyla yaralanması çocuk istismarı türü değildir (cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir). Kaza ile yaralanma istismar değildir.",
100: "Kadim Hint tıbbında (Ayurveda) bütün hastalıkların tedavisi Hindistan'da üretilen ilaçlarla yapılmıştır ifadesi doğru değildir. Ayurveda bitkisel, mineral ve hayvansal kökenli ilaçlar kullanır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
