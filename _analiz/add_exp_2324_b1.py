# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
1: "Pentoz fosfat yolunun görevleri arasında NADPH üretimi ve riboz-5-fosfat sentezi yer alır; ATP üretimi görülmez.",
2: "Pentoz fosfat yolunu NADPH inhibe eder (ürün inhibisyonu).",
3: "Karbonhidrat, protein ve yağ metabolizmasının ortak ürünü Asetil-CoA'dır.",
4: "Glukoz sorbitol yolunda (poliol yolu) sorbitol üzerinden fruktoza dönüştürülür.",
5: "Hipoglisemide glukoneogenez enzimleri (PEPCK, fruktoz-1,6-bifosfataz, glukoz-6-fosfataz) aktif olmalıdır; fosfofruktokinaz-1 (glikoliz enzimi) inhibe edilmelidir.",
6: "ATP sentazın Fo kısmı proton kanalıdır; oligomisin bu kanalı bloke ederek ATP sentezini durdurur.",
7: "Glikojen sentezinde glikozil kalıntıları glikojenin protein çekirdeğindeki tirozin'e bağlanır (glikojenin).",
8: "Glikojen yıkımı sonrası kana aktif glukoz salınımı için glukoz-6-fosfataz gereklidir (karaciğer).",
9: "Glikoneogenezde enerji GTP (PEPCK) ve ATP kullanılır; UTP glikojen sentezi, CTP fosfolipit sentezi içindir.",
10: "TCA döngüsünün kontrol enzimleri sitrat sentaz, izositrat dehidrogenaz ve α-ketoglutarat dehidrogenazdır; malat dehidrogenaz kontrol enzimi değildir.",
11: "Malat-aspartat şantı ile mitokondriye giren NADH, kompleks I (NADH dehidrogenaz) üzerinden solunum zincirine katılır.",
12: "Krebs siklusunda asetil-CoA pirüvata dönüştürülemez; bu glukoneogenezdeki pirüvat karboksilaz reaksiyonunun tersidir.",
13: "Sitozolde asetil-CoA karboksilaz (yağ asidi sentezi) aktivitesi saptanır; diğer enzimler mitokondriyal veya membrana bağlıdır.",
14: "İşaretli CO2 fotosentez (Calvin döngüsü) ile fikse edilir; hayvanlarda CO2 solunumla atılır, C14 lipitlerde tespit edilemez (malonil-CoA hariç).",
15: "Lökotrienler arakidonik asitten lipooksijenaz yolağı ile sentezlenir, siklooksijenaz yolağı ile değil.",
16: "Tek karbonlu (tek zincirli) yağ asitleri beta-oksidasyonda propiyonil-CoA üretir; peroksizomlarda da okside olabilirler.",
17: "Karnitin palmitoil transferaz I (KPT I) malonil-CoA tarafından inhibe edilir (yağ asidi sentezi aktifken oksidasyon durur).",
18: "Fosfatidil kolin + fosfolipaz A2 → lizofosfatidil kolin (lizolesitin) + yağ asidi.",
19: "Glutamat dehidrogenaz eksikliği üre döngüsü bozukluğu yapmaz; N-asetilglutamat sentaz, CPS, OTC, ASS, ASL eksiklikleri hiperamonyemi yapar.",
20: "Metiltetrahidrofolat homosistein→metionin dönüşümünde (metionin sentaz) kullanılır; folat tuzağından kurtarır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
