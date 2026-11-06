# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
41: "İnsan gözünün ayırma gücü hücreleri ayırt etmek için yeterli değildir; mikroskop gerekir. Diğer seçenekler doğru tanımlamalardır.",
42: "Formalin tespit (fiksasyon) ile otolitik ve bakteriyolitik reaksiyonlar önlenir; yıkama, şeffaflandırma, dehidratasyon ve gömme sonraki adımlardır.",
43: "Işık ve elektron mikroskobunda ortak nokta dokuların önce fikse edilmesidir; ışık kaynağı, canlı inceleme, renkli görüntü ve çözünürlük farklıdır.",
44: "Eosin asidik boyadır ve sitoplazmayı (asidofilik yapıları) pembe boyar; hematoksilen bazik boyadır.",
45: "Peroksizomlar membransız değildir; tek membranla çevrilidir. Bol hidrolitik enzim içeren organel lizozomdur.",
46: "Pinositozda klatrin kaplı veziküller oluşmaz; klatrin reseptör aracılı endositoz ve pinositozun bazı tiplerinde rol oynar. Yanlış ifade B'dir.",
47: "Erken endozom hücreye alınan reseptör-protein kompleksinin geri dönüşüm veya yıkıma gideceğini belirler.",
48: "Aktin filamanları (mikrofilamanlar) hücre iskeletinin periferik elemanıdır; hücre hareketi, bölünme ve mikrovillus yapısında rol oynar.",
49: "Golgi kompleksi steroid sentezleyen hücrelerde en fazla bulunan organel değildir (SER daha fazladır); salgı proteinlerini yoğunlaştırır.",
50: "Sideroforlar bakterilerin ve mantarların demir yakalama molekülleridir; Fe3+ bağlar ve hücreye taşır.",
51: "Mikrop teorisini kanıtlayan ve kuduz aşısını geliştiren Louis Pasteur'dur.",
52: "Keşfedilen ilk virus tütün mozaik virusudur (Ivanovsky/Beijerinck).",
53: "DNA virusları lineer, segmentli veya sirküler olabilir. Parvovirus tek sarmallı DNA virusudur; influenza segmentli RNA virusudur.",
54: "Endositoz nötral pH'da gerçekleşmez; endozom asidifikasyonu (pH düşmesi) gerekir. Yanlış ifade E'dir.",
55: "ELISA'da substrat eklendikten sonra yıkama yapılmaz; renkli ürün pozitif sonucu gösterir. Yanlış aşama C'dir (enzim bağlı antikor konduktan sonra yıkama yapılır).",
56: "PCR'de annealing'de Taq polimeraz aktivite yapmaz; primerler hedef bölgeye bağlanır. Yanlış ifade B'dir.",
57: "Temel besiyerlerinde (buyyon/jeloz) kan bulunmaz; kanlı besiyeri zenginleştirilmiş besiyeridir.",
58: "Zorunlu anaeroblar SOD ve katalaz enzimleri bulunmaz; oksijen varlığında üreyemezler.",
59: "Bütün bakterilerde bulunan yapı nükleoid (nükleotid) bölgesidir; kapsül, flajella, spor ve Golgi aparatı (bakteride yok) her bakteride bulunmaz.",
60: "Gram boyanma özelliği hücre duvarı yapısı ile ilişkilidir (peptidoglikan kalınlığı).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
