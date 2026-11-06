# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
81: "D vitamini reseptörü hücre içi (nükleer) reseptördür; glisin, noradrenalin ve prostaglandinler membran reseptörüne sahiptir.",
82: "Nernst denklemi ile Na+ için hücre içi konsantrasyon 3 mEq/L bulunur.",
83: "Oral rehidratasyon çözeltisindeki glukoz ve Na+ emilimi Na+-glikoz kotransporteri (SGLT1) aracılığıyla sağlanır.",
84: "İnsülin eksikliğinde glukozun hücreye alınması (GLUT4 translokasyonu) bozulur; bu kolaylaştırılmış difüzyondur.",
85: "G proteininin adenilat siklazı aktive etmesi cAMP oluşturur; cGMP (PKG), DAG ve IP3 (fosfolipaz C) farklı yollardır.",
86: "Düşük doz aspirin tromboksan A2 sentezini (COX-1 inhibisyonu) baskılayarak prostasiklin lehine denge kurar.",
87: "Nitrik oksit guanilat siklazı aktive eder; cGMP artışı düz kas relaksasyonu (vazodilatasyon) sağlar.",
88: "Güdüler organizmanın gereksinimlerini başlatan ve dengeyi sağlayan içsel güçlerdir; değişmeyen/türe özgü değildir.",
89: "Bunaltıcı durumu sıkıntı vermeyecek bir nedenle açıklama bulmak 'rasyonalizasyon (akla uygunlaştırma)' savunma düzenegidir.",
90: "Günlük yaşamda dil sürçmeleri, unutkanlıklar, ertelemeler bastırma (repression) savunma düzenegine örnektir.",
91: "Alkol bağımlılığı tanısı için yeterli tanısal ölçütlerin en az 12 ay süredir karşılanıyor olması gerekir.",
92: "Biyopsikososyal model insanı sadece biyolojik açıdan değerlendirmenin eksik olduğunu söyler; hastalıklar çok etkenlidir.",
93: "Nörotransmitterler nöronda sentezlenir, sinaps aralığına salınır ve davranışın düzenlenmesinde rol oynar.",
94: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir.",
95: "Stres, organizmanın homeostazını tehdit eden durumlara karşı gösterdiği zorlanma ve uyum yanıtıdır.",
96: "Ayrımcılık kavramlarından biri değildir: toplumsal yargılar (yargı, önyargı, kalıpyargı, stereotip ve cinsiyetçilik ayrımcılıkla ilişkilidir).",
97: "'Ayrımcılık' tanımı içinde yer almayan: adil davranan (adil davranış ayrımcılık değildir).",
98: "Çocuğun kaza yoluyla yaralanması çocuk istismarı türü değildir (cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir).",
99: "Çocuklar ihmal/istismarı söylememelerinin nedenleri: inanılmayacağını düşünme, tehdit, ailenin parçalanacağı endişesi, anlatamama.",
100: "Kadim Hint tıbbında (Ayurveda) bütün hastalıkların tedavisi Hindistan'da üretilen ilaçlarla yapılmıştır ifadesi doğru değildir.",
101: "Madde bağımlılığı tanısal ölçütleri arasında yer almayan: alkol/maddenin yarattığı bedensel sorunların farkında olmama (farkında olma yer alır).",
102: "Madde bağımlılığında ilk kullanımdaki pekiştiriciler arasında sayılmayan: bırakınca oluşan yan etkilerden kurtulma (negatif pekiştirme, sürdürmede rol oynar).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
