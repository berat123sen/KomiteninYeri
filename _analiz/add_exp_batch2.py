# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
21: "Peroksizomlar katalaz içerir ve H2O2'yi yıkar; beta-oksidasyon ve detoksifikasyon yapar. Lizozomlar sindirim, mitokondri enerji, Golgi paketleme görevi görür.",
22: "Hücre zarı fosfolipit çift tabakadır; seçici geçirgenlik, transport proteinleri ve reseptörler içerir; hücre iskeleti ile bağlantılıdır.",
23: "Nükleus DNA'yı içerir; çekirdekçik ribozom alt birimlerini sentezler; porlar RNA/protein geçişini sağlar.",
24: "Mitokondri ATP üretir; iç membran kristalar, matris Krebs enzimleri ve mtDNA içerir; hücrenin enerji santralidir.",
25: "Ribozomlar protein sentezler; serbest sitoplazmada veya RER membranına bağlı bulunur; prokaryotlarda 70S, eukaryotlarda 80S'dir.",
26: "RER protein sentezi ve modifikasyonu yapar; SER lipid sentezi, steroid sentezi ve detoksifikasyon görevi görür.",
27: "Golgi kompleksi cis-trans polaritesi gösterir; glikozilasyon, fosforilasyon ve paketleme yapar; lizozomal enzimleri etiketler.",
28: "Hücre iskeleti mikrotübüller (tubulin), mikrofilamanlar (aktin) ve ara filamentlerden oluşur; mekanik destek ve hareket sağlar.",
29: "Hücre bölünmesinde profaz kromozom yoğunlaşması, metafaz ekvator dizilimi, anafaz ayrılma, telofaz çekirdek yeniden oluşumu ile karakterizedir.",
30: "Apoptoz programlı hücre ölümüdür; kaspazlar aktive olur, hücre büzüşür, fagositozla temizlenir; inflamasyon oluşturmaz.",
31: "Nekroz patolojik hücre ölümüdür; membran bütünlüğü bozulur, içerikler sızar, inflamasyon oluşur.",
32: "Hücre adaptasyonları: atrofi (küçülme), hipertrofi (büyüme), hiperplazi (sayı artışı), metaplazi (dönüşüm), displazi (düzensizlik).",
33: "Metaplazi bir hücre tipinin başka bir hücre tipine dönüşümüdür; kronik irritasyon sonucu görülür, geri dönüşümlüdür.",
34: "Displazi hücre boyutu, şekil ve organizasyon bozukluğudur; prekanseröz lezyon olabilir.",
35: "Hiperplazi hücre sayısının artmasıdır; hormon veya büyüme faktörü uyarısı sonucu görülür.",
36: "Hipertrofi hücre boyutunun artmasıdır; iş yükü artışı sonucu (örn. kalp) görülür.",
37: "Atrofi hücre boyutunun küçülmesidir; kullanmama, iskemi veya beslenme eksikliği sonucu görülür.",
38: "Hücre hasarı nedenleri: hipoksi, kimyasal, enfeksiyon, immunolojik, genetik, beslenme, fiziksel ajanlar.",
39: "Reperfüzyon hasarı iskemi sonrası kan akımı dönüşünde ROS üretimi ve inflamasyon ile oluşur.",
40: "Serbest radikal hasarı lipid peroksidasyonu, protein oksidasyonu ve DNA hasarı ile hücreyi etkiler; antioksidanlar korur.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
