# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
90: "Günlük yaşamda dil sürçmeleri, kasıtsız unutkanlıklar, ertelemeler, dalgınlıklar bastırma (repression) savunma düzenegine örnektir.",
91: "Alkol bağımlılığı tanısı için yeterli tanısal ölçütlerin en az 12 ay süredir karşılanıyor olması gerekir.",
92: "Biyopsikososyal model insanı sadece biyolojik açıdan değerlendirmenin eksik olduğunu söyler; hastalıklar çok etkenlidir. A seçeneği (hastalıkların çoğu sadece biyolojik etkenler tarafından belirlenir) yanlıştır.",
93: "Nörotransmitterler nöronda sentezlenir, sinaps aralığına salınır ve davranışın düzenlenmesinde rol oynar. Postsinaptik uçtan salınmaz (presinaptik uçtan salınır).",
94: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir.",
95: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır.",
96: "Ayrımcılık kavramlarından biri değildir: toplumsal yargılar (yargı, önyargı, kalıpyargı, stereotip ve cinsiyetçilik ayrımcılıkla ilişkilidir).",
97: "'Ayrımcılık' tanımı içinde yer almayan: adil davranan (adil davranış ayrımcılık değildir).",
98: "Çocuğun kaza yoluyla yaralanması çocuk istismarı türü değildir (cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir).",
99: "Çocuklar ihmal/istismarı söylememelerinin nedenleri: inanılmayacağını düşünme, tehdit, ailenin parçalanacağı endişesi, anlatamama. 'Tümü' seçeneği yanlıştır çünkü D (nasıl anlatacağını bilemeyebilirler) en doğru ifadedir.",
100: "Kadim Hint tıbbında (Ayurveda) bütün hastalıkların tedavisi Hindistan'da üretilen ilaçlarla yapılmıştır ifadesi doğru değildir.",
101: "Madde bağımlılığı tanısal ölçütleri arasında yer almayan: alkol/maddenin yarattığı bedensel sorunların farkında olmama (farkında olma yer alır).",
102: "Madde bağımlılığında ilk kullanımdaki pekiştiriciler arasında sayılmayan: bırakınca oluşan yan etkilerden kurtulma (negatif pekiştirme, sürdürmede rol oynar).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
