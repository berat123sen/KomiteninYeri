# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
11: "Malat-aspartat şantı ile mitokondriye giren NADH, kompleks I (NADH dehidrogenaz) üzerinden solunum zincirine katılır. Sitokrom b, sitokrom c oksidaz, kompleks III ve süksinat koenzim Q redüktaz (kompleks II) farklı giriş noktalarıdır. Malat-aspartat şantı sitozolik NADH'yi mitokondriye taşır; gliserol-3-fosfat şantı ise FADH2 üretir (kompleks II).",
12: "Krebs siklusunda asetil-CoA pirüvata dönüştürülemez (tek yönlü reaksiyon). Asetil-CoA oksidasyonu (sitrat sentaz), α-ketoglutarat oluşumu (izositrat dehidrogenaz), CO2 üretimi (izositrat DH, α-KG DH), NADH ve FADH2 üretimi (izositrat DH, α-KG DH, süksinat DH, malat DH) gerçekleşir. Pirüvat dehidrogenaz TCA enzimi değildir (pirüvatı asetil-CoA'ya çevirir).",
13: "Sitoplazmada asetil-CoA karboksilaz (yağ asidi sentezi) aktivitesi saptanır. Pirüvat karboksilaz, glutamat dehidrogenaz, ornitin transkarbamoilaz ve asil-CoA dehidrogenaz mitokondriyal enzimlerdir. Asetil-CoA karboksilaz biyotin (B7) içeren enzimdir.",
14: "İşaretli CO2 fotosentez (Calvin döngüsü) ile fikse edilir; hayvanlarda CO2 solunumla atılır. C14 lipitlerde tespit edilemez (malonil-CoA hariç, çünkü malonil-CoA CO2'den sentezlenir). Hayvanlarda CO2 solunumla atılır, fotosentez yapılmaz.",
15: "Lökotrienler arakidonik asitten lipooksijenaz yolağı ile sentezlenir, siklooksijenaz yolağı ile değil. Prostasiklin, tromboksan, prostaglandin E2 ve H2 siklooksijenaz yolağı ürünleridir. Lökotrienler (LTA4, LTB4, LTC4, LTD4, LTE4) inflamasyon ve bronkospazmda rol oynar.",
16: "Tek karbonlu (tek zincirli) yağ asitlerinin beta-oksidasyonu sonucunda propiyonil-CoA (glukoneojenik) oluşur; peroksizomlarda da okside olabilirler. 17 karbonlu yağ asidi 8 asetil-CoA + 1 propiyonil-CoA üretir. C seçeneği (son oksidasyonda 1 mol Asetil-CoA + 1 mol Propiyonil-CoA) doğrudur. E seçeneği (peroksizomlarda gerçekleşir) yanlıştır çünkü beta-oksidasyon temel olarak mitokondride gerçekleşir.",
17: "Karnitin palmitoil transferaz I (KPT I) malonil-CoA tarafından inhibe edilir; yağ asidi sentezi aktifken (malonil-CoA yüksek) oksidasyon durur. KPT I, yağ asitlerinin mitokondri iç membranına taşınmasında (karnitin mekiği) rol oynar. Asetil-CoA, sitrat, oksaloasetat ve palmitoil-CoA inhibitör değildir.",
18: "Fosfolipaz A2 fosfatidil kolinin sn-2 pozisyonundaki yağ asidini hidrolize eder; lizofosfatidil kolin (lizolesitin) + serbest yağ asidi oluşur. Fosfokolin, fosfatidik asit, kolin ve diasilgliserol diğer fosfolipaz ürünleridir.",
19: "Glutamat dehidrogenaz eksikliği üre döngüsü bozukluğu yapmaz (glutamat dehidrogenaz üre döngüsünde yer almaz, amonyak detoksifikasyonunda rol oynar). N-asetilglutamat sentaz, CPS I, OTC, ASS, ASL eksiklikleri hiperamonyemi yapar.",
20: "Metiltetrahidrofolat homosistein→metionin dönüşümünde (metionin sentaz) metil verir; folat tuzağından kurtarır. Norepinefrin-epinefrin dönüşümü (A), homosistein-sistatyonin dönüşümü (B), spermin-spermidin dönüşümü (D), arginin-ornitin dönüşümü (E) metiltetrahidrofolat kullanmaz.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
