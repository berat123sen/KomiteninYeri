# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
61: "Eşit konsantrasyonlarda (g/L) glukoz (180 g/mol) ve sükröz (342 g/mol) çözeltilerinde molarite farklıdır: glukoz 1/180, sükröz 1/342; glukoz tarafında daha fazla molekül, daha düşük osmotik basınç → su glukoz tarafına hareket eder (hipotonik taraf). A, B, D, E yanlıştır.",
62: "Fick difüzyon yasasına göre net difüzyon hızı J = -D·A·(dC/dx); zar kalınlığının artması difüzyon hızını azaltır. Zar geçirgenliği, konsantrasyon gradiyenti ve yüzey alanı artması hızı artırır; molekül ağırlığının azalması hızı artırır.",
63: "İyon kanallarından iyon geçişi pasif (elektrokimyasal gradiyent) olur, ATP hidrolizi gerektirmez. Pasif taşıma metabolik enerji harcamaz. İyon kanalı seçiciliğinde yük ve şekil önemlidir. Kolaylaştırılmış difüzyon doygunluk gösterir. Na+ ile ortaklaşa/karşıt taşıma için enerji kaynağı ATP'dir (sekonder aktif transport). C seçeneği yanlıştır.",
64: "Zar direnci iyonların geçiş kolaylığının tersidir; açık kanal sayısı arttıkça direnç azalır (ters orantılı). Zar kapasitansı yüzey alanı ile doğru, kalınlık ile ters orantılıdır. Zaman sabiti τ=RC iletim hızı hesaplamasında kullanılır. B seçeneği (açık kanal sayısı ile direnç doğru orantılı) yanlıştır.",
65: "Nernst denklemi: E = (61/z)·log([dış]/[iç]) mV (25°C). Ca2+ için z=2: E = (61/2)·log(1/0.0001) = 30.5·log(10000) = 30.5·4 = 122 mV. Doğru cevap A'dır.",
66: "Metabolik enerji gerektirmeyen (pasif) taşıma: pasif difüzyon, kolaylaştırılmış difüzyon, osmoz. Birincil aktif taşıma ATP harcar. Sadece elektriksel kuvvet etki etmez (elektrokimyasal kuvvet). ATP kullanılmaz. Elektrokimyasal kuvvetler sıfırdan farklıdır (denge potansiyeli sıfır değildir). E seçeneği doğrudur.",
67: "Donnan dengesi: zar geçirgen olmayan anyonlar (A-) iki taraf arasında iyon dağılımını etkiler. Elektronötralite: [Na+]₁ = [Cl-]₁ + [A-]₁ → [Cl-]₁ = 0.326-0.266 = 0.06. Donnan: [Na+]₁[Cl-]₁ = [Na+]₂[Cl-]₂ → 0.326×0.06 = [Na+]₂×0.14 → [Na+]₂ = 0.01956/0.14 = 0.1397 ≈ 0.14. Doğru cevap B'dir.",
68: "Dinlenim zar potansiyelinde K+ etkisi daha fazladır çünkü zar K+ iyonlarına daha geçirgendir (daha fazla açık K+ kanalı). Na+ kanalları kapalıdır. K+ iyonlarının pozitif yük içermesi ve Na+ konsantrasyonu ile ilgili değildir.",
69: "Katalizörler (enzimler) tepkimeyi başlatmaz, tepkimenin hızını artırır, aktivasyon enerjisini düşürür, tepkime sonunda yapısal değişikliğe uğramaz ve yeniden kullanılır. Tepkimeyi başlatmaz, yönünü değiştirmez, kademeli tepkimelerde en hızlı adımda etkili değildir. Yalnızca II (hızı değiştirir) doğrudur. E seçeneği doğrudur.",
70: "Radyasyon tüm cisimler tarafından yayılır (mutlak sıfırın üzerindeki her cisim). Konveksiyon enerjinin sıvı/gaz içinde transferidir. Kondüksiyon moleküller arası enerji transferidir. Evaporasyon sıvı→gaz geçişinde ısı alır. D seçeneği doğrudur.",
71: "Sıcaklığı yükselten mekanizmalar: titreme (iskelet kası kasılması), vazokonstriksiyon (ısı kaybını azaltır), piloereksiyon (ısı kaybını azaltır). Vazodilatasyon, solunumda artış ve terleme ısı kaybetme (soğutma) mekanizmalarıdır. D seçeneği (II ve IV) doğrudur.",
72: "Isı akışı Q = k·A·ΔT/d = 18 × 1.5 × 3 / 3 = 27 cal/saat (d=3 cm, A=1.5 m²=15000 cm², k=18 cal·cm/m²·saat·°C). Doğru cevap B'dir.",
73: "DNA viruslarının çoğu çift sarmallıdır (herpes, adenovirus, poxvirus, HBV). RNA viruslarının çoğu tek sarmallıdır (influenza, HIV, HCV). Çift sarmallı RNA virusları (rotavirus, reovirus) istisnadır. D seçeneği (RNA viruslarının çoğu çift sarmallıdır) yanlıştır.",
74: "DNA virusları RNA polimeraz taşımaz; konak hücrenin RNA polimeraz II'sini kullanır. RNA viruslarının çoğu sitoplazmada çoğalır (influenza çekirdekte). DNA virusları çoğunlukla nükleusta çoğalır. Zarfsız viruslar lizis ile, zarflı viruslar tomurcuklanma ile salınır. C seçeneği (DNA virusları RNA polimeraz taşır) yanlıştır.",
75: "Hepatit B virus (HBV) zarflı, kısmen çift sarmallı (relaxed circular) DNA virusudur. Herpesvirus çift sarmallı DNA, parvovirus tek sarmallı DNA, poxvirus çift sarmallı DNA, adenovirus çift sarmallı DNA'dır. E seçeneği doğrudur.",
76: "Hemaglütinasyon inhibisyon testi (HAI) influenza ve diğer hemaglütinasyon yapan virusların tanısında eritrositler kullanır. Lateks aglütinasyon, IFA, ELISA ve immünokromotografik kart testleri eritrosit kullanmaz. E seçeneği doğrudur.",
77: "Tekrarlayan (reaktivasyon) enfeksiyon: IgG yüksek avidite (+) ve IgM (+) birlikteliği. Primer enfeksiyonda IgG düşük avidite (+), IgM (+). Past enfeksiyonda IgG (+), IgM (-). Avidite testi primer ve sekonder enfeksiyonu ayırt eder. C seçeneği doğrudur.",
78: "Tzanck testi herpes simplex ve varisella-zoster viruslarının veziküler lezyonlarından kazıntı ile yapılır; sitopatik etki olarak çok çekirdekli (multinükleer) dev hücreler (syncytia) görülür. Piknozis, agregasyon, minimal sitopatik etki ve sitomegali diğer sitopatik etkilerdir. C seçeneği doğrudur.",
79: "Mezofil bakteriler 20-45°C'de en iyi ürer (insan patojenleri mezofildir). Psikrofil (0-20°C), termofil (45-80°C), halofil (tuz seven), hemofil (kan seven) diğer gruplardır. C seçeneği (mezofil) doğrudur.",
80: "Bordetella pertussis zorunlu aerob (oksijen gerektirir). Bacteroides fragilis, Clostridium perfringens, Peptostreptococcus, Veillonella anaerob bakterilerdir. A seçeneği doğrudur.",
81: "Hemoliz özelliği kanlı agar (koyun kanlı agar) üzerinde değerlendirilir; alfa (kısmi), beta (tam), gamma (yok) hemoliz. MacConkey agar (selektif, Gram -) ve buyyon (sıvı) hemoliz değerlendirilmez. C seçeneği (sadece III) doğrudur.",
82: "Çikolata besiyeri kanlı agarın ısıtılmasıyla elde edilen zenginleştirilmiş besiyeridir; Neisseria ve Haemophilus (faktör V ve X gerektiren) türleri için kullanılır. I, II, III doğrudur (D seçeneği: hepsi).",
83: "Gram pozitif bakteri hücre duvarında LPS (lipopolisakkarit) bulunmaz; LPS Gram negatif bakterilerin dış membranında bulunur (endotoksin). Peptidoglikan ve teikoik asit Gram pozitifte bulunur. E seçeneği (sadece III) doğrudur.",
84: "Bakteri hücre duvarı basınc değişikliklerine karşı korur, şekli korur, Gram boyanma özelliğinden sorumludur. Peptidoglikan tabaka (murein) bulunur. Penisilin/lizozim etkisiyle L-form (hücre duvarı kaybı) gelişebilir. D seçeneği (peptidoglikan bulunmaz) yanlıştır.",
85: "Temporal lob (özellikle amigdala ve hipokampüs) duygular ve bellek ile ilişkilidir. Oksipital lob görme, frontal lob motor/kognisyon, pons beyin sapı, parietal lob duyu ile ilişkilidir. D seçeneği doğrudur.",
86: "Deskriptif (tanımlayıcı) psikiyatri hastalıkların tanımlanması, sınıflandırılması, ayırıcı tanı ve tedavi planı oluşturmayı içerir; nedensel etkenleri araştırmak etyolojik (açıklayıcı) psikiyatrinin alanıdır. D seçeneği (nedensel etkenleri araştırma) deskriptif psikiyatri ile ilgili değildir.",
87: "Benlik (ego) görevleri: gerçeği değerlendirme, dürtüleri düzenleme/ertelemeyi, ruhsal dengeyi sağlama. Değer yargıları ile dürtülerin doyurulmasında yargılama mekanizması süperegonun (vicdan) görevidir, egonun değil. D seçeneği (değer yargıları ile dürtülerin doyurulmasında yargılama) benlik görevleri arasında yer almaz.",
88: "Fallik dönem (3-6 yaş, Freud) Erikson'un 'girişime karşı suçluluk' (initiative vs guilt) evresine denk gelir. Oral dönem 'temel güvene karşı güvensizlik' evresine denk gelir. Anal dönem 'özerkliğe karşı utanç' evresine denk gelir.",
89: "Oral dönem (0-18 ay, Freud) Erikson'un 'temel güvene karşı güvensizlik' (trust vs mistrust) evresine denk gelir. A seçeneği doğrudur.",
90: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir. A, B, C, E doğru önerilerdir. D seçeneği (kafeinli içecekler) yanlıştır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
