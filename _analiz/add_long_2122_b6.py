# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
1: "Canlıların temel yapısal biriminin hücre olduğu hücre teorisi (Schleiden-Schwann, 1838-1839) ile ortaya konmuştur; elektron mikroskobunun keşfi (1930'lar) daha sonra gelir. A seçeneği: Histoloji terimi Yunanca 'histos' (doku) ve 'logos' (bilim/çalışma) kelimelerinden türemiştir ve doğrudur. B seçeneği: Histoloji, insanın hücre, doku ve organlarının normal mikroskobik yapısını inceler ve doğrudur. C seçeneği: Histoloji ve Embriyolojinin çalışma alanları arasında normal yapı ve gelişimin yanında hücre/doku hasarının mikroskobik araştırılması, kök hücre biyolojisi, rejeneratif tıp ve IVF yer alır; doğrudur. D seçeneği: Embriyoloji fertilizasyondan doğuma kadar insanın normal gelişimini inceleyen bilim alanıdır; doğrudur. E seçeneği ise temel yapısal birimi hücreler arası maddeler olarak tanımladığı için yanlıştır; temel birim hücredir.",
2: "Canlıların temel yapısal biriminin hücre olduğu hücre teorisi ile ortaya konmuştur; elektron mikroskobu sonradan gelir. A, B, C, E doğru tanımlamalardır. D seçeneği (canlıların temel yapısal biriminin hücre olduğu gerçeği ancak elektron mikroskobunun keşfinden sonra ortaya konulmuştur) yanlıştır.",
3: "Membran proteinlerinin hepsi transmembran değildir; periferal proteinler yüzeyde bulunur. A seçeneği: Fosfolipid, kolesterol ve protein moleküllerinden oluşan 8-10 nm kalınlığında bir membrandır (doğru). B seçeneği: Lipid molekülleri amfipatik karakterdedir (doğru). D seçeneği: Periferal proteinler ekstrasellüler ve intrasellüler yüzeylerde bulunur (doğru). E seçeneği: İntegral proteinler pompalar, kanallar, reseptörler olarak fonksiyon görür (doğru). C seçeneği yanlıştır.",
4: "Klatrin bağımlı endositoz tipidir; pinositoz klatrinsiz (kaveolin/flotillin) veziküllerle olur. A, B, C, D doğru ifadelerdir. E seçeneği (klatrin bağımlı endositoz tipidir) pinositoz için yanlıştır.",
5: "Lizozomal membran proteinleri Golgi'de sentezlenip lizozoma taşınır; endozomlarda sentezlenmez. A, B, C, E doğru tanımlamalardır. D seçeneği (lizozomal membran proteinleri direkt olarak erken ve geç endozomlarda sentezlenip lizozoma aktarılır) yanlıştır.",
6: "Peroksizomlar yapısal protein sentezi yapmaz; aktin, miyozin, hemoglobin ribozomlarda sentezlenir. A, C, D, E doğru eşleşmelerdir. B seçeneği (peroksizom-hücrede aktin, miyozin ve hemoglobin gibi yapısal proteinlerin sentezi) yanlıştır.",
7: "Hücrede mikrotübüller veziküler transport, silya/flagella hareketi, mitoz mekiği ve hücre şeklinin korunmasında görevlidir. Aktin filaman, sentriyoller, bazal cisimcik, ara filamanlar farklı yapısal elemanlardır. Doğru cevap C'dir (mikrotübüller).",
8: "Canlıdan alınan dokuyu otolitik/bakteriyolitik reaksiyonlardan koruyan işlem tespit (fiksasyon)dur. Yıkama, dehidratasyon, gömme ve kapatma sonraki adımlardır. Doğru cevap A'dır.",
13: "İnfluenza virus zarflı, segmentli tek sarmallı RNA virusudur; zarfsız değildir. Rotavirus zarfsız, çift sarmallı ve segmentli RNA virusudur (A doğru). Herpes viruslar zarflı, çift sarmallı DNA virusudur (B doğru). HIV zarflı, diploid RNA'ya sahiptir (D doğru). HBV zarflı, kısmen çift sarmallı DNA virusudur (E doğru). C seçeneği (influenza virus zarfsız) yanlıştır.",
14: "HIV RNA virusu olup RNA polimeraz taşımaz; ters transkriptaz (RT) taşır. Helikal veya ikosahedral kapsidi olabilir (A doğru). Negatif polariteli RNA virusları hazır RNA polimeraz taşır (B doğru). RNA virusları birkaç istisna hariç sitoplazmada çoğalır (C doğru). Pozitif polariteli RNA virusları direk ribozoma gidebilir (D doğru). E seçeneği (HIV virusu RNA polimeraza sahiptir) yanlıştır.",
15: "Latent dönem (eclipse) genom replikasyonu ve protein sentezi öncesi dönemdir; ilk virus oluşumundan önceki dönem değildir. Glikoproteinler hücredeki spesifik reseptörlere bağlanır (A doğru). Hem zarflı hem zarfsız viruslar endositozla hücreye girebilir (B doğru). Erken proteinler genom replikasyonu için gerekli enzimlerdir (D doğru). Zarfsız viruslar hücreyi lizise uğratarak salınır (E doğru). C seçeneği yanlıştır.",
16: "Nötralizasyon testi canlı hücre kültürü gerektirir; ELISA, strip test, lateks aglütinasyon test ve line probe assay (LIPA) hücre kültürü gerektirmez. B seçeneği doğrudur.",
17: "PCR'de ekstensiyonda (72°C) Taq polimeraz DNA sentezler; primer bağlanması annealing aşamasındadır (50-65°C). Denatürasyon 94°C'de gerçekleşir. Ekstensiyonda primer genoma bağlanmaz (primerler annealing'de bağlanır). DNA ekstraktları Taq polimeraz ile RNA'ya çevrilmez (ters transkriptaz ile RNA'dan DNA'ya). D seçeneği (ekstensiyon'da primer genoma bağlanır) yanlıştır.",
18: "ELISA'da substrat eklendikten sonra yıkama yapılmaz; renkli ürün antikor varlığını gösterir. A, B, C, E doğru aşamalardır. D seçeneği (substrat ilave edilir, sonra yıkama yapılır) yanlıştır.",
19: "Mikroorganizma enzim aktivitesini ısı, pH, tuz yoğunluğu ve kimyasal maddeler (ağır metal vb.) etkiler; mikroorganizmanın cinsi enzim tipini belirler ama aktiviteyi etkileyen dış etken değildir. E seçeneği (mikroorganizmanın cinsi) yanlıştır.",
20: "Agar mutlaka gerekli değildir; sıvı besiyerlerinde (buyyon) agar olmadan da üreme olur. A, B, C, E doğru ifadelerdir. D seçeneği (agar mutlaka gerekli) yanlıştır.",
24: "Yağlarla birlikte yağda eriyen vitaminler (A, D, E, K) emilir. Vitamin B12, C, folik asit, B6 suda eriyen vitaminlerdir ve yağ sindirimi ile birlikte emilmez. B seçeneği (vitamin D) doğrudur.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
