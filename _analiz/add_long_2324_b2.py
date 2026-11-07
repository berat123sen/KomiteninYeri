# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
16: """Tek karbonlu (tek zincirli) yağ asitlerinin beta-oksidasyonu sonucunda propiyonil-CoA (glukoneojenik) oluşur; peroksizomlarda da okside olabilirler. 17 karbonlu yağ asidi 8 asetil-CoA + 1 propiyonil-CoA üretir. C seçeneği (son oksidasyonda 1 mol Asetil-CoA + 1 mol Propiyonil-CoA) doğrudur. E seçeneği (peroksizomlarda gerçekleşir) yanlıştır çünkü beta-oksidasyon temel olarak mitokondride gerçekleşir (peroksizomlar çok uzun zincirli yağ asitlerini okside eder ama temel yer mitokondridir).""",
17: """Karnitin palmitoil transferaz I (KPT I) malonil-CoA tarafından inhibe edilir; yağ asidi sentezi aktifken (malonil-CoA yüksek) oksidasyon durur. KPT I, yağ asitlerinin mitokondri iç membranına taşınmasında (karnitin mekiği) rol oynar. Asetil-CoA, sitrat, oksaloasetat ve palmitoil-CoA inhibitör değildir.""",
18: """Fosfolipaz A2 fosfatidil kolinin sn-2 pozisyonundaki yağ asidini hidrolize eder; lizofosfatidil kolin (lizolesitin) + serbest yağ asidi oluşur. Fosfokolin, fosfatidik asit, kolin ve diasilgliserol diğer fosfolipaz ürünleridir.""",
19: """Glutamat dehidrogenaz eksikliği üre döngüsü bozukluğu yapmaz (glutamat dehidrogenaz üre döngüsünde yer almaz, amonyak detoksifikasyonunda rol oynar). N-asetilglutamat sentaz, CPS I, OTC, ASS, ASL eksiklikleri hiperamonyemi yapar. B seçeneği (glutamat dehidrogenaz) bu tabloya yol açmaz.""",
20: """Metiltetrahidrofolat homosistein→metionin dönüşümünde (metionin sentaz) metil verir; folat tuzağından kurtarır. Norepinefrin-epinefrin dönüşümü (A), homosistein-sistatyonin dönüşümü (B), spermin-spermidin dönüşümü (D), arginin-ornitin dönüşümü (E) metiltetrahidrofolat kullanmaz.""",
21: """Triptofanın aşırı serotonin sentezine yönlendirilmesi niasin (B3) eksikliğine (pellagra) yol açar; triptofan niasin sentezinin öncüsüdür (kinürenin yolağı). Piridoksal fosfat, biotin, B12, tiamin bu süreçte rol oynamaz.""",
22: """Aminoasit oksidaz reaksiyonunda H2O2 oluşur (D-aminoasit oksidaz, L-aminoasit oksidaz). Glutamat dehidrogenaz NAD(P)H kullanır; transaminasyon, glutaminaz ve glutamin sentetaz H2O2 üretmez.""",
23: """Fenilalanin hidroksilaz veya dihidrobiyopterin redüktaz eksikliği fenilketonüriye yol açar; kanda ve idrarda fenilketon cisimcikleri (fenilpirüvat, fenilasetat, fenillaktat) artar. Katalaz, fenilalanin aminotransferaz, fenilalanin dekarboksilaz, fenilalanin oksidaz eksikliği bu tabloya yol açmaz.""",
24: """Nitrik oksit (NO) arginin'den (NOS enzimi) sentezlenir; vazodilatasyon ve pıhtılaşma düzenlenmesinde rol oynar. Glutamik asit, glisin, tirozin, histidin NO sentezinde kullanılmaz.""",
25: """Toklukta insülin/glukagon oranı artar; glikojen fosforilaz inhibe olur, glikojen sentaz aktive olur. Glikojen fosforilaz aktivasyonu (A seçeneği) yanlıştır; glikojen fosforilaz glukagon ve adrenalin ile aktive olur.""",
26: """Yağdan fakir, karbonhidrat zengin diyetle şilomikron düzeyi düşer (diyet yağı azalır); VLDL artabilir (karbonhidrat → trigliserit → VLDL).""",
27: """Akciğer surfaktanının ana bileşeni dipalmitoil fosfatidilkolin (DPPC, fosfatidilkolin) olup alveol kollapsını önler. Fosfatidilinozitol, fosfatidiletanolamin, glikosfingolipid, sfingomiyelin surfaktanın minor bileşenleridir.""",
28: """Statinler (HMG-CoA redüktaz inhibitörleri) hepatic LDL reseptörünü upregüle ederek plazma LDL'yi düşürür. Kolesterolün ince bağırsaktan emilimini azaltma (ezetimib), safra asidi dönüşümü (kolestiramin), mevalonat yıkımı statinlerin birincil mekanizması değildir.""",
29: """Kolesterolün hücre içi düzenlenmesinde LDL reseptörü ile hücreye alım (reseptör aracılı endositoz) etkilidir. Apo C-II ifadesi (B seçeneği) kolesterol düzenlenmesinde etkili değildir (Apo C-II lipoprotein lipaz aktivatörüdür). ACAT ile esterifikasyon, HMG-KoA redüktaz transkripsiyonu ve HDL'ye aktarım etkilidir.""",
30: """Ateroskleroz riski en çok LDL-HDL ikilisi ile ilişkilidir (LDL proaterojen, HDL antiaterojen). LDL-şilomikron (A), HDL-IDL (B), VLDL-LDL (D), şilomikron-VLDL (E) ikilileri ateroskleroz riski ile en çok ilişkili değildir.""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
