# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
1: "Pentoz fosfat yolunun görevleri: NADPH üretimi (biyosentez, detoksifikasyon, glutatyon redüksiyonu), riboz-5-fosfat üretimi (nükleotid ve nükleik asit sentezi), 3-7 karbonlu şekerlerin dönüştümü (transketolaz/transaldolaz). A seçeneği: Glikoz metabolizmasında alternatif bir yolaktır (doğru). B seçeneği: Pentoz Fosfat yolunda ATP üretimi ve tüketimi görülür (yanlış; bu yolak ATP üretmez, NADPH üretir). C seçeneği: Nükleotid sentezi için riboz-5-fosfat üretilir (doğru). D seçeneği: Sitozoldeki biyosentetik reaksiyonlar için NADPH üretilir (doğru). E seçeneği: 3-7 karbonlu şekerlerin birbirine dönüşümünü ve glikolize bağlantısını sağlar (doğru). Doğru cevap B'dir. Pentoz fosfat yolu oksidatif (G6PD) ve non-oksidatif (transketolaz/transaldolaz) fazlardan oluşur. Oksidatif fazda glukoz-6-fosfat → ribuloz-5-fosfat + 2 NADPH + CO2 dönüşümü gerçekleşir. NADPH, glutatyon redüktaz, sitokrom P450 ve nitrik oksit sentaz için gereklidir.",
2: "Pentoz fosfat yolunu NADPH (ürün) inhibe eder (geri bildirim inhibisyonu). NAD+, FAD, asetil-CoA ve NADH inhibitör değildir. NADPH üretimi arttıkça glukoz-6-fosfat dehidrogenaz (G6PD, hız sınırlayıcı enzim) inhibe olur. G6PD eksikliğinde hemolitik anemi gelişir (favizm, primaquin duyarlılığı). NADPH ayrıca yağ asidi sentezi, kolesterol sentezi ve nükleotid sentezi için gereklidir.",
3: "Karbonhidrat, protein ve yağ metabolizmasının ortak ürünü Asetil-CoA'dır (mitokondride üretilir). Yağ asitleri (A), glukoz (B), gliserol (C) ve üre (E) bu ortak ürün değildir. Asetil-CoA Krebs döngüsüne girer ve enerji (ATP) üretir. Asetil-CoA ayrıca ketogenez, kolesterol sentezi ve yağ asidi sentezi için öncü moleküldür.",
4: "Glukoz sorbitol (poliol) yolunda aldöz redüktaz ile sorbitole, sorbitol dehidrogenaz ile fruktoza dönüştürülür. Galaktoz (A), glukronat (C), askorbat (D), mannoz (E) bu yolakta üretilmez. Poliol yolu diyabetik komplikasyonlarda (katarakt, nöropati, nefropati, retinopati) rol oynar. Aldöz redüktaz inhibitörleri (epalrestat) diyabetik komplikasyonları önlemede kullanılır.",
5: "Hipoglisemide glukoneogenez enzimleri (PEPCK, fruktoz-1,6-bifosfataz, glukoz-6-fosfataz) aktif olmalıdır; fosfofruktokinaz-1 (glikoliz anahtar enzimi) inhibe edilmelidir. Pirüvat karboksilaz (A), PEP karboksikinaz (B), fruktoz-1,6-bifosfataz (C), glukoz-6-fosfataz (D) aktif olmalıdır. E seçeneği (fosfofruktokinaz-1) inhibe olmalıdır. Fosfofruktokinaz-1 (PFK-1) glikolizin hız sınırlayıcı basamağıdır ve insülin tarafından aktive, glukagon tarafından inhibe edilir.",
6: "ATP sentazın Fo kısmı proton kanalıdır; oligomisin bu kanalı bloke ederek proton akışını ve ATP sentezini durdurur. Rotenon (kompleks I inhibitörü), amital (kompleks I), antimisin A (kompleks III) farklı hedeflere etki eder. Dimerkaprol şelatör bir maddedir. Oligomisin mitokondriyal ATP sentaz inhibitörüdür.",
7: "Glikojen sentezinde glikozil kalıntıları glikojenin protein çekirdeğindeki tirozin'e bağlanır (glikojenin). Asparajin, triptofan, glisin, alanin glikojen çekirdeği değildir. Glikojen sentezi glikojenin (protein) + UDP-glukoz ile başlar. Glikojenin, glikojen sentezinin primer (başlangıç) molekülüdür.",
8: "Glikojen yıkımı sonrası kana aktif glukoz salınımı için glukoz-6-fosfataz gereklidir (karaciğer ve böbrek). Dallandıran enzim (branching enzyme), dalları yıkan enzim (debranching enzyme), glikojen fosforilaz ve fosfoglikomutaz glikoz-6-fosfat üretir ama serbest glukoz salınımı için glukoz-6-fosfataz gerekir. Glukoz-6-fosfataz eksikliği (von Gierke hastalığı, tip 1 glikojen depo hastalığı) hepatomegali ve hipoglisemiye yol açar.",
9: "Glikoneogenezde enerji GTP (PEPCK reaksiyonunda) ve ATP (pirüvat karboksilaz, fosfoglisero kinaz) kullanılır. CTP (fosfolipit sentezi), UTP (glikojen sentezi), TTP (DNA sentezi) glikoneogenezde kullanılmaz. D seçeneği (UTP) yanlıştır; doğru cevap A'dır (GTP).",
10: "TCA döngüsünün kontrol enzimleri sitrat sentaz, izositrat dehidrogenaz ve α-ketoglutarat dehidrogenazdır. Malat dehidrogenaz kontrol enzimi değildir. Asetil-CoA tek başına yeterli değildir (oksalasetat gerekir). Pirüvat dehidrogenaz TCA enzimi değildir (pirüvatı asetil-CoA'ya çevirir). TCA mitokondri matrisinde gerçekleşir. Kontrol enzimleri allosterik olarak (ATP, NADH, sitrat) ve kovalent modifikasyonla (fosforilasyon) düzenlenir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
