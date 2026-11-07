# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
76: "Hemaglütinasyon inhibisyon testi (HAI) influenza ve diğer hemaglütinasyon yapan virusların tanısında eritrositler kullanır. Lateks aglütinasyon, IFA, ELISA ve immünokromotografik kart testleri eritrosit kullanmaz.",
77: "Tekrarlayan (reaktivasyon) enfeksiyon: IgG yüksek avidite (+) ve IgM (+) birlikteliği. Primer enfeksiyonda IgG düşük avidite (+), IgM (+). Past enfeksiyonda IgG (+), IgM (-).",
78: "Tzanck testi herpes simplex ve varisella-zoster viruslarının veziküler lezyonlarından kazıntı ile yapılır; sitopatik etki olarak çok çekirdekli (multinükleer) dev hücreler (syncytia) görülür.",
79: "Mezofil bakteriler 20-45°C'de en iyi ürer (insan patojenleri mezofildir). Psikrofil (0-20°C), termofil (45-80°C), halofil (tuz seven), hemofil (kan seven) diğer gruplardır.",
80: "Bordetella pertussis zorunlu aerob (oksijen gerektirir). Bacteroides fragilis, Clostridium perfringens, Peptostreptococcus, Veillonella anaerob bakterilerdir.",
81: "Hemoliz özelliği kanlı agar (koyun kanlı agar) üzerinde değerlendirilir; alfa (kısmi), beta (tam), gamma (yok) hemoliz. MacConkey agar (selektif, Gram -) ve buyyon (sıvı) hemoliz değerlendirilmez.",
82: "Çikolata besiyeri kanlı agarın ısıtılmasıyla elde edilen zenginleştirilmiş besiyeridir; Neisseria ve Haemophilus (faktör V ve X gerektiren) türleri için kullanılır. I, II, III doğrudur (D seçeneği).",
83: "Gram pozitif bakteri hücre duvarında LPS (lipopolisakkarit) bulunmaz; LPS Gram negatif bakterilerin dış membranında bulunur (endotoksin). Peptidoglikan ve teikoik asit Gram pozitifte bulunur.",
84: "Bakteri hücre duvarı basınc değişikliklerine karşı korur, şekli korur, Gram boyanma özelliğinden sorumludur. Peptidoglikan tabaka (murein) bulunur. Penisilin/lizozim etkisiyle L-form (hücre duvarı kaybı) gelişebilir. D seçeneği (peptidoglikan bulunmaz) yanlıştır.",
85: "Temporal lob (özellikle amigdala ve hipokampüs) duygular ve bellek ile ilişkilidir. Oksipital lob görme, frontal lob motor/kognisyon, pons beyin sapı, parietal lob duyu ile ilişkilidir.",
86: "Deskriptif (tanımlayıcı) psikiyatri hastalıkların tanımlanması, sınıflandırılması, ayırıcı tanı ve tedavi planı oluşturmayı içerir; nedensel etkenleri araştırmak etyolojik (açıklayıcı) psikiyatrinin alanıdır.",
87: "Benlik (ego) görevleri: gerçeği değerlendirme, dürtüleri düzenleme/ertelemeyi, değer yargıları (süperego görevi), ruhsal dengeyi sağlama. Değer yargıları ile dürtülerin doyurulmasında yargılama mekanizması süperegonun (vicdan) görevidir, egonun değil.",
88: "Fallik dönem (3-6 yaş, Freud) Erikson'un 'girişime karşı suçluluk' (initiative vs guilt) evresine denk gelir. Oral dönem 'temel güvene karşı güvensizlik' evresine denk gelir.",
89: "Oral dönem (0-18 ay, Freud) Erikson'un 'temel güvene karşı güvensizlik' (trust vs mistrust) evresine denk gelir.",
90: "Stresi azaltmak için kafeinli içecekler tüketilmemelidir; fiziksel egzersiz, dengeli beslenme ve uyku önerilir. A, B, C, E doğru önerilerdir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
