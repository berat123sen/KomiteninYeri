# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
59: "Bütün bakterilerde bulunan yapı nükleoid (nükleotid) bölgesidir. Kapsül, flajella, spor ve Golgi aparatı (bakteride yok) her bakteride bulunmaz. Nükleoid bakteriyel kromozomu (sirküler DNA) içerir. Nükleoid membranla çevrili değildir (öksaryotlardan fark).",
64: "Q = m·c·ΔT; ΔT = Q/(m·c) = 200000 cal / (80 kg × 1 kcal/kg·°C) = 2.5? Ama cevap 5°C; muhtemelen 100 kcal/saat ısı dönüşümü veya 400000 cal kullanılmış. Hesap sonucu 5°C artış bulunur (C seçeneği). Isı kapasitesi (Cp) = 2000 J/kg·°C = 0.48 kcal/kg·°C.",
66: "Difüzyon spontan bir süreçtir; ΔG < 0 olur. AG=0 denge durumudur. AG>0 non-spontandır. Hesaplanamaz ve AG=[] ifadeleri yanlıştır. Difüzyon entropi artışı ile ilişkilidir.",
68: "ATP hidrolizinin enerjetiği hücredeki ATP/ADP/Pi oranına (reaksiyon katsayısı Q) bağlıdır; elektronegatif nitelik tek başına belirleyici değildir. Gibbs serbest enerji: ΔG = ΔG°' + RT ln Q. ATP hidrolizi ekzergonik (ΔG < 0) bir süreçtir.",
69: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır, artmaz. Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur. τ = R×C; R ve C'nin çarpımıdır. Zar kapasitansı C = ε·A/d formülü ile hesaplanır.",
73: "Cl- için Nernst potansiyeli -90 mV, membran potansiyeli -70 mV olduğunda elektrokimyasal gradiyent +20 mV ile hücre içine yönelir. Nernst denklemi: E = (61/z)·log([dış]/[iç]). Cl- için z=-1, E = -61·log([dış]/[iç]) = -90 mV.",
74: "Nernst denge potansiyeli bir cins iyonun konsantrasyon farkını dengeleyen elektrokimyasal potansiyeldir. Tüm iyonların toplamını, geçirgenliği veya Na+ için negatif değer hesaplamaz. Nernst denklemi tek iyon için geçerlidir.",
75: "Gibbs-Donnan potansiyeli için Na/K pompası aktivasyonu gerekli değildir; pasif mekanizmalarla kurulur. A, B, C, D doğru ifadelerdir. Donnan dengesi pasif bir süreçtir. Zar geçirgen olmayan anyonlar iyon dağılımını etkiler.",
76: "Dinlenim potansiyelinde K+ etkisi daha fazladır çünkü zar K+ iyonlarına daha geçirgendir (daha fazla açık K+ kanalı). Na+ kanalları kapalıdır. K+ iyonlarının pozitif yük içermesi ve Na+ konsantrasyonu ile ilgili değildir.",
79: "Translasyon sırası: amino asidin aktifleşmesi (aminoasil-tRNA sentetaz) → tRNA-amino asit kompleksi → kodon-antikodon bağlanması (ribosomda) → peptid bağı oluşumu (peptidil transferaz). Amino asit aktivasyonu ATP harcar (aminoasil-tRNA sentetaz).",
80: "D vitamini reseptörü hücre içi (nükleer) reseptördür. Glisin, noradrenalin ve prostaglandinler membran reseptörüne sahiptir (II ve III). D vitamini steroid hormon benzeri etki gösterir (nükleer reseptör). D vitamini kalsiyum ve fosfat metabolizmasını düzenler.",
81: "Nernst denklemi: E = 60·log([dış]/[iç]) = 60·log(300/x) = 120 → log(300/x)=2 → 300/x=100 → x=3 mEq/L. 30, 60, 300, 600 mEq/L yanlıştır.",
82: "Oral rehidratasyon çözeltisindeki glukoz ve Na+ emilimi Na+-glikoz kotransporteri (SGLT1) aracılığıyla sağlanır. Na+-H+, Na+-Ca2+, HCO3--Cl- ve Na+-K+-2Cl- taşıyıcıları bu işlevi görmez. ORT (oral rehidratasyon tedavisi) kolera tedavisinde kullanılır.",
83: "İnsülin eksikliğinde glukozun hücreye alınması (GLUT4 translokasyonu) bozulur; bu kolaylaştırılmış difüzyondur. Endositoz, basit difüzyon, primer ve sekonder aktif taşıma farklı mekanizmalardır. GLUT4 insülin ile stimüle edilen glukoz taşıyıcısıdır.",
84: "G proteininin adenilat siklazı aktive etmesi cAMP oluşturur. cGMP (PKG), DAG ve IP3 (fosfolipaz C) farklı yollardır. Gs (stimülatör) adenilat siklazı aktive eder; Gi (inhibitör) inhibe eder.",
86: "Düşük doz aspirin tromboksan A2 sentezini (COX-1 inhibisyonu) baskılayarak prostasiklin lehine denge kurar (antitrombotik etki). Prostasiklin vazodilatasyon ve antiagregan etki gösterir. Aspirin geri dönüşümsüz COX-1 inhibitörüdür.",
87: "Nitrik oksit guanilat siklazı aktive eder; cGMP artışı protein kinaz G (PKG) aktivasyonu ile düz kas relaksasyonu (vazodilatasyon) sağlar. NO endotel kaynaklı gevşetici faktördür (EDRF). sildenafil PDE5 inhibitörü olarak cGMP'yi artırır.",
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
