# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
22: "Aminoasit oksidaz reaksiyonunda H2O2 oluşur (D-aminoasit oksidaz, L-aminoasit oksidaz). Glutamat dehidrogenaz NAD(P)H kullanır; transaminasyon, glutaminaz ve glutamin sentetaz H2O2 üretmez. Aminoasit oksidazlar peroksizomlarda bulunur ve H2O2 üretir; katalaz ile H2O2 suya dönüştürülür.",
24: "Nitrik oksit (NO) arginin'den (NOS enzimi) sentezlenir; vazodilatasyon ve pıhtılaşma düzenlenmesinde rol oynar. Glutamik asit, glisin, tirozin, histidin NO sentezinde kullanılmaz. NO guanilil siklazı aktive eder → cGMP artışı → protein kinaz G aktivasyonu → düz kas relaksasyonu.",
26: "Yağdan fakir, karbonhidrat zengin diyetle şilomikron düzeyi düşer (diyet yağı azalır); VLDL artabilir (karbonhidrat → trigliserit → VLDL). Şilomikronlar diyet trigliseritlerini taşır; VLDL endojen trigliseritleri taşır.",
32: "Kolesterol steroid hormonların (progesteron, kortizol, aldosteron), safra tuzlarının ve vitamin D'nin öncüsüdür. Vitamin C (askorbik asit) kolesterol kökenli değildir; glukozdan sentezlenir. Kolesterol HMG-CoA yolağı ile asetil-CoA'dan sentezlenir.",
36: "Pirüvat dehidrogenaz kompleksi (PDC) pirüvatı asetil-CoA'ya çevirir; kofaktörleri TPP (tiamin), lipoik asit, CoA (pantotenik asit), FAD (riboflavin), NAD+ (niasin) içerir. PDC mitokondri matrisinde bulunur ve pirüvat dekarboksilasyonunu katalize eder.",
37: "Demir (Fe) hemoglobin ve sitokrom yapısında bulunur; eksikliği mikrositer anemiye yol açar. Mn, Zn, Cr, Co hemoglobin yapısında bulunmaz. Demir eksikliği en yaygın anemi türüdür.",
38: "Selenyum (Se) tiroid deiyodinaz ve glutatyon peroksidazın kofaktörüdür; tiroid fonksiyonları için önemlidir. Molibden, mangan, çinko, krom tiroid fonksiyonlarında bu kadar kritik değildir. Se eksikliği Keshan hastalığına (kardiyomiyopati) yol açar.",
40: "Histoloji insanın çıplak gözle görülemeyen mikroskobik yapısını inceler; B seçeneği (insanın çıplak gözle görülebilen vücut kısımlarını inceleyen bilim alanı) anatomi/tipoloji tanımıdır. Histoloji mikroskop ile inceleme yapar.",
41: "İnsan gözünün ayırma gücü hücreleri ayırt etmek için yeterli değildir; mikroskop gerekir. Diğer seçenekler doğru tanımlamalardır.",
42: "Formalin tespit (fiksasyon) ile otolitik ve bakteriyolitik reaksiyonlar önlenir; yıkama, şeffaflandırma, dehidratasyon ve gömme sonraki adımlardır.",
43: "Işık ve elektron mikroskobunda ortak nokta dokuların önce fikse edilmesidir; ışık kaynağı, canlı inceleme, renkli görüntü ve çözünürlük farklıdır.",
44: "Eosin asidik boyadır ve sitoplazmayı (asidofilik yapıları) pembe boyar; hematoksilen bazik boyadır (çekirdeği mavi boyar). Eosin-hematoksilen (H&E) en yaygın histolojik boyama yöntemidir.",
45: "Peroksizomlar tek membranla çevrili organellerdir (membransız değildir). Bol hidrolitik enzim içeren organel lizozomdur. B, C, D, E doğru tanımlamalardır.",
46: "Pinositozda klatrin kaplı veziküller oluşmaz; klatrin reseptör aracılı endositozda rol oynar. Pinocitozda kaveolin/flotillin proteinleri vezikül formasyonunda rol oynar. A, C, D, E doğru ifadelerdir.",
47: "Erken endozom hücreye alınan reseptör-protein kompleksinin geri dönüşüm veya yıkıma gideceğini belirler (sorting endosome). Lizozom, peroksizom, Golgi ve geç endozom bu işlevi görmez.",
49: "Golgi kompleksi steroid sentezleyen hücrelerde en fazla bulunan organel değildir (düz endoplazmik retikulum daha fazladır). Salgı proteinlerini yoğunlaştırır. A, C, D, E doğru ifadelerdir.",
50: "Sideroforlar bakterilerin ve mantarların demir yakalama molekülleridir; Fe3+ bağlar ve hücreye taşır. Aksiyal filaman, flajella, porin ve mezozom demir taşıma ile ilgili değildir.",
52: "Keşfedilen ilk virus tütün mozaik virusudur (Ivanovsky/Beijerinck, 1892). İnfluenza, çiçek, polio ve kuduz virusları daha sonra keşfedilmiştir.",
55: "ELISA'da substrat eklendikten sonra yıkama yapılmaz; renkli ürün antikor varlığını gösterir. A, B, C, D doğru aşamalardır (C'de enzim bağlı antikor konduktan sonra yıkama yapılır).",
57: "Temel (basit) besiyerlerinde kan bulunmaz; kanlı besiyeri zenginleştirilmiş besiyeridir. Et suyu, tuz, agar ve pepton temel besiyerlerinde bulunur.",
58: "Zorunlu anaeroblar SOD ve katalaz enzimleri bulunmaz; oksijen varlığında üreyemezler. Zorunlu aerob, fakültatif anaerob, aerotolerant ve mikroaerofil diğer gruplardır.",
59: "Bütün bakterilerde bulunan yapı nükleoid (nükleotid) bölgesidir. Kapsül, flajella, spor ve Golgi aparatı (bakteride yok) her bakteride bulunmaz.",
60: "Gram boyanma özelliği hücre duvarı yapısı ile ilişkilidir (peptidoglikan kalınlığı). Mezozom, nukleus, ribozom ve kapsül Gram boyanma ile ilişkili değildir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
