# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
21: "Triptofanın aşırı serotonin sentezine yönlendirilmesi niasin (B3) eksikliğine (pellagra) yol açar.",
22: "Aminoasit oksidaz reaksiyonunda H2O2 oluşur; glutamat dehidrogenaz NAD(P)H kullanır.",
23: "Fenilalanin hidroksilaz/dihidrobiyopterin redüktaz eksikliği fenilketonüriye yol açar; fenilketon cisimcikleri birikir.",
24: "Nitrik oksit (NO) arginin'den (NOS enzimi) sentezlenir; vazodilatasyon ve pıhtılaşma düzenlenmesinde rol oynar.",
25: "Toklukta insülin/glukagon oranı artar; glikojen fosforilaz inhibe olur, glikojen sentaz aktive olur. Glikojen fosforilaz aktivasyonu yanlıştır.",
26: "Yağdan fakir, karbonhidrat zengin diyetle şilomikron düzeyi düşer (diyet yağı azalır).",
27: "Akciğer surfaktanının ana bileşeni dipalmitoil fosfatidilkolin (DPPC) fosfatidilkolin grubundandır.",
28: "Statinler (HMG-CoA redüktaz inhibitörleri) hepatic LDL reseptörünü upregüle ederek plazma LDL'yi düşürür.",
29: "Kolesterolün hücre içi düzenlenmesinde LDL reseptörü ile hücreye alım (reseptör aracılı endositoz) etkilidir.",
30: "Ateroskleroz riski en çok LDL-HDL ikilisi ile ilişkilidir (LDL proaterojen, HDL antiaterojen).",
31: "HMG-CoA redüktaz aktivitesini diyet lipid, SREBP, insülin (aktive), glukagon (inhibe), kinazlar düzenler; diyet lipid etkisi en az belirgindir.",
32: "Kolesterol steroid hormonların (progesteron, kortizol, aldosteron), safra tuzlarının ve vitamin D'nin öncüsüdür; vitamin C değil.",
33: "Na+/K+ ATPaz aktif transport yapar (3 Na+ dışarı, 2 K+ içeri, ATP harcar).",
34: "SGLT1 sekonder aktif transport ile glukozu Na+ gradiyenti kullanarak hücreye taşır.",
35: "Cori döngüsü kas laktatının karaciğerde glukoza dönüşümüdür; kas-karaciğer glikojen/glukoz döngüsünü açıklar.",
36: "Pirüvat dehidrogenaz kompleksi (PDC) pirüvatı asetil-CoA'ya çevirir; kofaktörleri TPP, lipoik asit, CoA, FAD, NAD+ (tiamin, niasin, pantotenik asit).",
37: "Demir (Fe) hemoglobin ve sitokrom yapısında bulunur; eksikliği mikrositer anemiye yol açar.",
38: "Selenyum (Se) tiroid deiyodinaz ve glutatyon peroksidazın kofaktörüdür; tiroid fonksiyonları için önemlidir.",
39: "Kardiyovasküler hastalıklar, diyabet ve KOAH mortalitesi en yüksek hastalıklardır ve beslenme ile ilişkilidir.",
40: "Histoloji insanın çıplak gözle görülemeyen mikroskobik yapısını inceler; B seçeneği anatomi/tipoloji tanımıdır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
