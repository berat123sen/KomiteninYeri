# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
31: "Tirozin aminoasidinden sentezlenen: T3/T4 (tiroid hormonları), epinefrin/norepinefrin/dopamin (katekolaminler), melanin (melanositlerde). Kreatinin (kreatin fosfatın non-enzimatik yıkım ürünü) tirozinden sentezlenemez.",
32: "İnsülin anabolik hormondur: glukoz girişini artırır (GLUT4 translokasyonu), glikolizi ve glikojen sentezini uyarır, protein sentezini artırır, lipogenezi uyarır. Hormon-duyarlı lipazı (HSL) inhibe eder (trigliserit yıkılımını azaltır). B seçeneği yanlıştır.",
33: "Aldolaz A fruktoz-1,6-bifosfatı gliseraldehid-3-fosfat ve dihidroksiaseton fosfat'a (trioz şekerler) kırar (aldol kırılması). Enolaz, trioz fosfat izomeraz, fosfogliserat kinaz, G3P dehidrogenaz bu kırılmayı yapmaz.",
34: "Pirüvattan tek reaksiyonla fosfoenolpirüvat (PEP) oluşamaz; pirüvat → PEP dönüşümü iki basamaklıdır (pirüvat karboksilaz + PEP karboksikinaz, glukoneogenez). Laktat (LDH), alanin (ALT), oksaloasetat (pirüvat karboksilaz), asetil-CoA (PDH) tek reaksiyonla oluşabilir.",
35: "Gliseraldehit-3-fosfat dehidrogenaz reaksiyonunda NADH üretilir; elektronlar ETZ'ye girer ve oksidatif fosforilasyonla 1.5 veya 2.5 ATP üretebilir (shunt'a bağlı). Diğer dehidrogenazlar (PDH, izositrat DH, α-KG DH, malat DH) NADH/FADH2 üretir ama doğrudan substrat düzeyinde fosforilasyon yapmaz.",
36: "Krebs siklusunda asetil-CoA pirüvata dönüştürülemez (tek yönlü reaksiyon). Asetil-CoA oksidasyonu, α-ketoglutarat oluşumu, CO2 ve NADH/FADH2 üretimi gerçekleşir.",
37: "FADH2 (süksinat dehidrogenaz'dan) ETZ'ye kompleks II üzerinden girer. NADH kompleks I, koenzim Q kompleks I/II sonrası, kompleks III ve IV daha sonra gelir.",
38: "Pentoz fosfat yolunun başlıca amacı NADPH (biyosentez, detoksifikasyon) ve riboz-5-fosfat (nükleotid sentezi) üretmektir.",
39: "Pirüvat dehidrogenaz (PDH) glukoneogenezde yer almaz; glukoneogenezde pirüvat karboksilaz (pirüvat → oksaloasetat) kullanılır. Fosfoglikoizomeraz, gliseraldehid-3-fosfat, aldolaz ve glukoz-6-fosfataz glukoneogenez enzimleridir.",
40: "Glikojen sentazın de-fosforile (defosforile) hali aktiftir; fosforile hali inaktiftir. İnsülin PP1 (protein fosfataz 1) aktive ederek defosforilasyon yapar. A, B, C, E doğru ifadelerdir.",
41: "Glikojen fosforilaz glikojeni fosforoliz ile glikoz-1-fosfat'a çevirir (hidroliz değil).",
42: "Fruktoz metabolizması karaciğerde fruktokinaz ile 1. karbondan fosforilasyon ile başlar (heksokinaz değil). Fruktoz metabolizması PFK kontrol basamağını atlar (hızlı). Fazla fruktoz hiperürisemi yapar (AMP deaminaz aktivasyonu). Aldolaz-B eksikliği herediter fruktoz intoleransı yapar. Diyabetik katarakt sorbitol birikiminden kaynaklanır.",
43: "Pentoz fosfat yolunu NADPH inhibe eder (ürün inhibisyonu). NAD+, FAD, asetil-CoA, NADH inhibitör değildir.",
44: "Hipoglisemide glukokinaz (karaciğer, düşük Km) inhibe olmalıdır (glukoz fosforilasyonu azalır); pirüvat karboksilaz, PEPCK, fruktoz-1,6-bifosfataz ve glukoz-6-fosfataz aktif olmalıdır.",
45: "Prolin hidroksilaz (prolil hidroksilaz) kollajen sentezinde prolini hidroksiprolin'e çevirir; kofaktörü C vitamini (askorbik asit), Fe2+ ve α-ketoglutarat'tır. C vitamini eksikliği (skorbüt) kollajen sentez bozukluğuna yol açar.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
