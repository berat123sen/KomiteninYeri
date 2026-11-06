# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
1: "İnsan vücudunun esas yapısal birimi hücrelerdir, hücreler arası maddeler değil. A, B, C, D doğru tanımlamalardır.",
2: "Canlıların temel yapısal biriminin hücre olduğu hücre teorisiyle ortaya konmuştur; elektron mikroskobu sonradan gelir. A, B, C, E doğru tanımlamalardır.",
3: "Membran proteinlerinin hepsi transmembran değildir; periferal proteinler yüzeyde bulunur. A, B, D, E doğru tanımlamalardır.",
4: "Klatrin bağımlı endositoz tipidir; pinositoz klatrinsiz (kaveolin/flotillin) veziküllerle olur. A, B, C, D doğru ifadelerdir.",
5: "Lizozomal membran proteinleri Golgi'de sentezlenip lizozoma taşınır; erken/geç endozomlarda sentezlenmez. A, B, C, E doğru tanımlamalardır.",
6: "Peroksizomlar yapısal protein sentezi yapmaz; aktin, miyozin, hemoglobin ribozomlarda sentezlenir. A, C, D, E doğru eşleşmelerdir.",
7: "Hücrede mikrotübüller veziküler transport, silya/flagella hareketi, mitoz mekiği ve hücre şeklinin korunmasında görevlidir. A, B, D, E diğer yapısal elemanlardır.",
8: "Canlıdan alınan dokuyu otolitik/bakteriyolitik reaksiyonlardan koruyan işlem tespit (fiksasyon)dur. B, C, D, E sonraki adımlardır.",
9: "Elektron mikroskobu canlı hücreleri inceleyemez (vakum ve fiksasyon gerektirir). A, C, D, E doğru ifadelerdir.",
10: "'Vaccination' kelime anlamı ineklemedir (vacca=inek). Jenner inek çiçek virusunu kullanmıştır.",
11: "Bakterilerde peptidoglikan sentezinde rol oynayan enzimler Penisilin Bağlayan Proteinler (PBP)'dir.",
12: "Gram (-) bakterilerde somatik antijen (O antijeni) LPS (lipopolisakkarit) yapısındadır.",
13: "İnfluenza virus zarflı, segmentli tek sarmallı RNA virusudur; zarfsız değildir. A, B, D, E doğru tanımlamalardır.",
14: "HIV RNA virusu olup RNA polimeraz taşımaz; ters transkriptaz (RT) taşır. A, B, C, D doğru ifadelerdir.",
15: "Latent dönem (eclipse) genom replikasyonu ve protein sentezi öncesi dönemdir; ilk virus oluşumundan önceki dönem değildir. A, B, D, E doğru ifadelerdir.",
16: "Nötralizasyon testi canlı hücre kültürü gerektirir; ELISA, strip, lateks aglütinasyon ve LIPA hücre kültürü gerektirmez.",
17: "PCR'de ekstensiyonda (72°C) Taq polimeraz DNA sentezler; primer bağlanması annealing aşamasındadır. A, B, C, E yanlış ifadelerdir.",
18: "ELISA'da substrat eklendikten sonra yıkama yapılmaz; renkli ürün antikor varlığını gösterir. A, B, C, E doğru aşamalardır.",
19: "Mikroorganizma enzim aktivitesini ısı, pH, tuz yoğunluğu ve kimyasal maddeler etkiler; mikroorganizmanın cinsi enzim tipini belirler ama aktiviteyi etkileyen dış etken değildir.",
20: "Agar mutlaka gerekli değildir; sıvı besiyerlerinde (buyyon) agar olmadan da üreme olur. A, B, C, E doğru ifadelerdir.",
21: "Yüksek ATP/AMP oranı fosfofruktokinaz (PFK-1, glikoliz anahtar enzimi) ve pirüvat kinazı inhibe eder.",
22: "Sitrik asit (sitrat) asetil-CoA karboksilazı (yağ asidi sentezi) uyarır.",
23: "Viral gastroenterit sonrası laktoz intoleransı gelişebilir (brush border hasarı). Çölyak daha kroniktir.",
24: "Yağlarla birlikte yağda eriyen vitaminler (A, D, E, K) emilir; vitamin D yağda eriyendir.",
25: "Yağ asidi oksidasyonu bozulunca asetil-CoA üretimi azalır; glukoneogenez (pirüvat karboksilaz) etkilenir.",
26: "Malonil-CoA karnitin-asil transferaz I (KPT I)'i inhibe eder; yağ asidi sentezi aktifken oksidasyon durur.",
27: "Kanda en yüksek konsantrasyonda gözlenen keton cisimciği aseton değil, beta-hidroksibütirat'tır. B, C, D, E doğru ifadelerdir.",
28: "Yağ asidi sentazda ACP (asil taşıyıcı protein) asetil gruplarını bağlar.",
29: "Trigliserit sentezi yağ dokusunda gliserol-3-fosfattan (glikolizden) başlar, gliserolden değil.",
30: "Glutamin sentetaz amonyak + glutamat → glutamin dönüşümünü katalize eder; amonyak miktarını azaltır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
