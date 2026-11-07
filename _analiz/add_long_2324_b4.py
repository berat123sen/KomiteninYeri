# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
46: "Pinositozda klatrin kaplı veziküller oluşmaz; klatrin reseptör aracılı endositozda rol oynar. Pinocitozda kaveolin/flotillin proteinleri vezikül formasyonunda rol oynar. A, C, D, E doğru ifadelerdir.",
47: "Erken endozom hücreye alınan reseptör-protein kompleksinin geri dönüşüm veya yıkıma gideceğini belirler (sorting endosome). Lizozom, peroksizom, Golgi ve geç endozom bu işlevi görmez.",
48: "Aktin filamanları (mikrofilamanlar) hücre iskeletinin periferik elemanıdır; hücre hareketi, bölünme (sitokinez) ve mikrovillus yapısında rol oynar. Mikrotübüller, ara filamentler, sentrioller ve ribozomlar bu işlevde rol oynamaz.",
49: "Golgi kompleksi steroid sentezleyen hücrelerde en fazla bulunan organel değildir (düz endoplazmik retikulum daha fazladır). Salgı proteinlerini yoğunlaştırır. A, C, D, E doğru ifadelerdir.",
50: "Sideroforlar bakterilerin ve mantarların demir yakalama molekülleridir; Fe3+ bağlar ve hücreye taşır. Aksiyal filaman, flajella, porin ve mezozom demir taşıma ile ilgili değildir.",
51: "Mikrop teorisini kanıtlayan ve kuduz aşısını geliştiren Louis Pasteur'dur. Antonie van Leeuwenhoek mikroskobu, Robert Koch postulatları, Alexander Fleming penisilin, Joseph Lister antisepsi ile ilişkilidir.",
52: "Keşfedilen ilk virus tütün mozaik virusudur (Ivanovsky/Beijerinck, 1892). İnfluenza, çiçek, polio ve kuduz virusları daha sonra keşfedilmiştir.",
53: "DNA virusları lineer, segmentli veya sirküler olabilir. Parvovirus tek sarmallı DNA virusudur. İnfluenza segmentli RNA virusudur (tek sarmallı, segmentsiz değil). Rotavirus dışındaki RNA virusları tek sarmallıdır.",
54: "Endositoz nötral pH'da gerçekleşmez; endozom asidifikasyonu (pH düşmesi, V-ATPaz) gerekir. Zarflı viruslar endositoz veya füzyon ile girer. Zarfsız viruslar lizis ile salınır. Viropeksis zarfsız virusların hücreye giriş yoludur.",
55: "ELISA'da substrat eklendikten sonra yıkama yapılmaz; renkli ürün antikor varlığını gösterir. A, B, C, D doğru aşamalardır (C'de enzim bağlı antikor konduktan sonra yıkama yapılır).",
56: "PCR'de annealing'de (50-65°C) primerler hedef bölgeye bağlanır; Taq polimeraz bu aşamada aktivite yapmaz. Denatürasyon 94°C, elongasyon 72°C'de gerçekleşir. Primerler 3' ucuna bağlanır. dNTP'ler ekstensiyonda DNA zincirine girer.",
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
