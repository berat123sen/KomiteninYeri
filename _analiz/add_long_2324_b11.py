# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
31: "HMG-CoA redüktaz aktivitesini SREBP (transkripsiyon faktörü), insülin (aktive eder), glukagon (inhibe eder), kinazlar (fosforilasyon ile inhibe) ve kolesterol (ürün inhibisyonu) düzenler. Diyetle alınan lipid (A seçeneği) en az etkili faktördür.",
32: "Kolesterol steroid hormonların (progesteron, kortizol, aldosteron), safra tuzlarının ve vitamin D'nin öncüsüdür. Vitamin C (askorbik asit) kolesterol kökenli değildir; glukozdan sentezlenir.",
33: "Na+/K+-ATPaz pompası aktif transport yapar: 3 Na+ dışarı, 2 K+ içeri, ATP harcar (elektrojenik pompa). Basit difüzyon, kolaylaştırılmış difüzyon, osmotik transport ve iyonik transport pasif mekanizmalardır.",
34: "SGLT1 (sodyum-glukoz kotransporteri 1) sekonder aktif transport ile glukozu Na+ gradiyenti kullanarak hücreye taşır (ince bağırsak, böbrek proksimal tübül). Kalsiyum-ATPaz, GLUT2, Na/K-ATPaz ve Na/Ca değiş-tokuş diğer mekanizmalardır.",
35: "Cori döngüsü kas laktatının karaciğerde glukoza dönüşümüdür; kas-karaciğer glikojen/glukoz döngüsünü açıklar. Glukoneogenezis, glikojenez, glikojenoliz ve miyoinositol döngüsü farklı metabolik yollardır.",
36: "Pirüvat dehidrogenaz kompleksi (PDC) pirüvatı asetil-CoA'ya çevirir; kofaktörleri TPP (tiamin), lipoik asit, CoA (pantotenik asit), FAD (riboflavin), NAD+ (niasin) içerir.",
37: "Demir (Fe) hemoglobin ve sitokrom yapısında bulunur; eksikliği mikrositer anemiye yol açar. Mn, Zn, Cr, Co hemoglobin yapısında bulunmaz.",
38: "Selenyum (Se) tiroid deiyodinaz ve glutatyon peroksidazın kofaktörüdür; tiroid fonksiyonları için önemlidir. Molibden, mangan, çinko, krom tiroid fonksiyonlarında bu kadar kritik değildir.",
39: "Kardiyovasküler hastalıklar, diyabet mellitus ve KOAH mortalitesi en yüksek hastalıklar grubunda olup beslenme ile ilişkisi kanıtlanmıştır. Yalnızca I veya II (A, B) ve I ve III (C) ya da II ve III (D) seçenekleri eksik; üçü de bu grupta yer alır.",
40: "Histoloji insanın çıplak gözle görülemeyen mikroskobik yapısını inceler; B seçeneği (insanın çıplak gözle görülebilen vücut kısımlarını inceleyen bilim alanı) anatomi/tipoloji tanımıdır.",
41: "İnsan gözünün ayırma gücü hücreleri ayırt etmek için yeterli değildir; mikroskop gerekir. Diğer seçenekler doğru tanımlamalardır.",
42: "Formalin tespit (fiksasyon) ile otolitik ve bakteriyolitik reaksiyonlar önlenir; yıkama, şeffaflandırma, dehidratasyon ve gömme sonraki adımlardır.",
43: "Işık ve elektron mikroskobunda ortak nokta dokuların önce fikse edilmesidir; ışık kaynağı, canlı inceleme, renkli görüntü ve çözünürlük farklıdır.",
44: "Eosin asidik boyadır ve sitoplazmayı (asidofilik yapıları) pembe boyar; hematoksilen bazik boyadır (çekirdeği mavi boyar).",
45: "Peroksizomlar tek membranla çevrili organellerdir (membransız değildir). Bol hidrolitik enzim içeren organel lizozomdur. B, C, D, E doğru tanımlamalardır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
