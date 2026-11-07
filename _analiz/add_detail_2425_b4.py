# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
46: "Koenzim Q10 (ubikinon) lipidik yapıdadır; ETZ'de elektronları kompleks I/II'den kompleks III'e taşır. Piruvat, alfa lipoik asit, alfa-ketoglutarat ve asetil-CoA protein/enzim veya metabolit olup lipidik formatta değildir.",
47: "Krom (Cr3+) insülinin glukozu hücre içine almasında rol oynar; glukoz tolerans faktörü (GTF) yapısında bulunur ve insülin etkisini potansiyalize eder. Demir, iyot, mangan, molibden bu işlevde rol oynamaz.",
48: "Tiroid hormonları (T3, T4) sentezi için iyot (I) (tirozin iyodinasyonu) ve selenyum (Se) (deiyodinaz enzimleri, T4→T3 dönüşümü) gereklidir.",
49: "Kardiyovasküler hastalıklar, diyabet mellitus ve stroke mortalitesi en yüksek hastalıklar grubunda olup beslenme ile ilişkisi kanıtlanmıştır. A, B, C, D seçenekleri (yalnızca biri veya ikisi) yanlıştır; üçü de bu grupta yer alır.",
50: "Akciğer surfaktanının esas lipid bileşeni dipalmitoil fosfatidilkolin (DPPC, fosfatidilkolin) olup alveol kollapsını önler. Fosfatidilinozitol, fosfatidiletanolamin, glikosfingolipid, sfingomiyelin surfaktanın minor bileşenleridir.",
51: "Statinler (HMG-CoA redüktaz inhibitörleri) kolesterol sentezinin hız sınırlayıcı basamağını (HMG-CoA → mevalonat) bloke eder; mevalonat azalınca LDL reseptörü upregüle olur. A, B, C, E statinlerin birincil mekanizması değildir.",
52: "Kolesterolün hücre içi düzenlenmesinde ACAT ile esterifikasyon, LDL reseptörü ile alım, HMG-CoA redüktaz transkripsiyonu ve HDL'ye aktarım rol oynar. Apo C-II ifadesi (C seçeneği) kolesterol düzenlenmesinde etkili değildir (Apo C-II lipoprotein lipaz aktivatörüdür).",
53: "HMG-CoA redüktaz aktivitesini SREBP (transkripsiyon), insülin (aktive eder), glukagon (inhibe eder), kinazlar (fosforilasyon ile inhibe) ve kolesterol (ürün inhibisyonu) düzenler. Diyetle alınan lipid (C seçeneği) en az etkili faktördür.",
54: "Kolesterol steroid hormonların (progesteron, kortizol, aldosteron), safra tuzlarının ve vitamin D'nin öncüsüdür. Vitamin C (askorbik asit) kolesterol kökenli değildir.",
55: "Na+/K+-ATPaz pompası aktif transport yapar: 3 Na+ dışarı, 2 K+ içeri, ATP harcar (elektrojenik). Basit difüzyon, kolaylaştırılmış difüzyon, osmotik transport ve iyonik transport pasif mekanizmalardır.",
56: "SGLT1 (sodyum-glukoz kotransporteri 1) sekonder aktif transport ile glukozu Na+ gradiyenti kullanarak hücreye taşır. Kalsiyum-ATPaz, GLUT2, Na/K-ATPaz ve Na/Ca değiş-tokuş diğer mekanizmalardır.",
57: "Sfingolipitler serin ve palmitoil-CoA'dan sentezlenir (lesitinden değil). Plazmalojenler ve PAF eter lipidlerdir (dihidroksiaseton fosfattan). Trigliseritler ve fosfogliseroller gliserol-3-P'den sentezlenir. Sfingomiyelin ve glikosfingolipitler yapısal eleman, gangliozidler reseptör/antijendir. B seçeneği yanlıştır.",
58: "Proteinlerin lipid membrana bağlanması (prenilasyon) Ras/Rho proteinlerinin membrana bağlanması için gereklidir; prenil grupları (farnesil, geranilgeranil) kovalent bağ ile eklenir. Denatürasyon, metilasyon, renatürasyon, açılasyon farklı modifikasyonlardır.",
59: "Glukozun potansiyel enerjisi 686 kcal/mol; hücresel solunumda 277 kcal/mol ATP olarak elde edilir; verim %40 (277/686). Fazla enerji ısıya dönüşür. %27 (A, D) ve 'tüm enerji içe dönüşür' (C) yanlıştır.",
60: "Fosfolipit çift tabakasının oluşumunda temel sürücü kuvvet hidrofobik etkileşimlerdir (lipid kuyrukları suyu dışlar). Hidrojen bağı, kovalent bağ, ATP hidrolizi ve mekanik kuvvetler temel sürücü değildir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
