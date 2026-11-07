# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
10: """Pozitif geri bildirim (positive feedback) bir sürecin kendi kendini amplifiye etmesidir; çıktı, girdiyi artırır ve süreç hızlanır. Kanayan damarda pıhtılaşma (trombin → daha fazla trombin → fibrin) ve doğumda oksitosin ile uterin kasılmaların artması (Ferguson refleksi) pozitif geri bildirim örnekleridir. Barorefleks (kan basıncı düzenlenmesi) ve insülin-glukoz düzenlenmesi negatif geri bildirimdir (çıktı girdiyi azaltır, homeostazı korur). A, C, D, E seçenekleri pozitif ve negatif geri bildirimi yanlış eşleştirmiştir. Doğru cevap B'dir (II ve III).""",
11: """Ara filament ailesi: vimentin (mezenkimal hücreler), desmin (kas hücreleri), keratin (epitel hücreleri), GFAP (glia hücreleri), nörofilamanlar (nöronlar). Dinein ve kinesin motor proteinlerdir (mikrotübüller üzerinde hareket eder), ara filament değildir. A seçeneği (I ve II) dinein (motor protein) içerdiği için yanlıştır. B seçeneği (II ve III) kinesin (motor protein) içerir. C seçeneği (I ve III) her ikisi motor proteindir. E seçeneği (III ve IV) kinesin içerir. Doğru cevap D'dir (II ve IV: vimentin ve desmin).""",
12: """Tay-Sachs hastalığı heksosaminidaz A enzim eksikliği sonucu gangliozid GM2 birikimi ile karakterizedir; otozomal resesif geçişlidir, sinir sistemi hasarı ve ölümle sonuçlanır. Heksosaminidaz A lizozomal bir enzimdir (glikoprotein yıkımında rol oynar). A seçeneği: Golgi aygıtı protein modifikasyonu yapar. B seçeneği: Peroksizom yağ asidi oksidasyonu ve detoksifikasyon yapar. C seçeneği: Mitokondri enerji üretimi yapar. D seçeneği: Sentrozom mikrotübülleri organize eder. Doğru cevap E'dir (lizozom).""",
13: """Mitokondriler enerji üretimi (ATP, oksidatif fosforilasyon) dışında apoptozda (sitokrom c salınımı, kaspaz aktivasyonu, Bcl-2 ailesi proteinleri) ve Ca2+ depolamada (matris, uniporter ile) rol oynar. Kondroitin sülfat üretimi (glikozaminoglikan sentezi) Golgi'de, hasarlı organel sindirimi (otofaji) lizozomda gerçekleşir. A seçeneği (I ve II) doğrudur. B (II ve III), C (I ve III), D (I ve IV), E (II ve IV) yanlıştır.""",
14: """Difüzyon hızını azaltan parametreler: ortamın viskozitesi (yüksek viskozite molekül hareketini yavaşlatır) ve molekülün yarıçapı (büyük molekül daha yavaş difüze olur; Stokes-Einstein denklemi: D = kT/(6πηr)). Mutlak sıcaklık (T) ve Boltzmann sabiti (k) difüzyonu artırır (sıcaklık arttıkça kinetik enerji artar). A seçeneği (I ve II) viskozite azaltır ama sıcaklık artırır. C (I ve III) viskozite azaltır ama yarıçap artırır. D (II ve IV) sıcaklık ve Boltzmann artırır. E (I ve IV) viskozite azaltır ama Boltzmann artırır. Doğru cevap B'dir (II ve III: viskozite ve yarıçap).""",
15: """Lizozomlar tek membranla çevrili organellerdir ve hidrolitik enzimler (proteaz, nükleaz, glikozidaz, lipaz, fosfataz, sülfataz) içerir; asidik pH'da (pH 4.5-5.0) çalışır. A seçeneği: Lizozomal membranın iç yüzeyinde glikoprotein (LAMP-1, LAMP-2) ve lizobifosfatidik asit bulunur; bu yapı lizozomu kendi hidrolitik enzimlerinden korur (membran direnci). Doğrudur. B seçeneği: Lizozomal membran proteinleri endoplazmik retikulumda sentezlenir, Golgi kompleksinde mannoz-6-fosfat (M6P) etiketi ile işaretlenir ve M6P reseptörü aracılığıyla geç endozom/lizozoma taşınır; endozomlarda sentezlenmez. Yanlıştır. C seçeneği: Lizozomlar fagositoz, reseptör aracılı endositoz ve otofaji süreçlerinde aktif rol oynar. Doğrudur. D seçeneği: Lipaz, proteaz, nükleaz gibi yıkıcı enzimler içerirler. Doğrudur. E seçeneği: Aktif fagositoz yapan makrofaj ve nötrofillerde bol miktarda bulunur (gelişmiş lizozomal sistem). Doğrudur. Yanlış şık B'dir.""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
