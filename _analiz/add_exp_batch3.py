# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
41: "İnflamasyon akut (nötrofil, hızlı) veya kronik (lenfosit/makrofaj, uzun) olabilir; kardinal bulgular rubor, calor, tumor, dolor, functio laesa'dır.",
42: "Akut inflamasyonda vazodilatasyon, artmış geçirgenlik, lökosit göçü (kemotaksis, adezyon, transmigrasyon) görülür.",
43: "Kronik inflamasyonda makrofaj, lenfosit ve plazma hücreleri baskındır; granülom (epiteloid makrofaj) oluşabilir.",
44: "İnflamasyon mediatörleri: histamin, prostaglandinler, lökotrienler, sitokinler (IL-1, TNF-α), kompleman, kininler.",
45: "Eksüda inflamasyon sonucu protein ve hücre içeren sıvıdır; transüda hidrostatik basınç artışı sonucu düşük proteinli sıvıdır.",
46: "Nötrofil akut inflamasyonun ilk hücresidir; kemotaksis, fagositoz ve ROS üretimi yapar.",
47: "Makrofaj kronik inflamasyon ve doku onarımında ana hücredir; antijen sunumu ve sitokin salgısı yapar.",
48: "Lenfosit adaptif immunitede görevli; T hücreleri hücre-sel, B hücreleri humoral immuniti sağlar.",
49: "Plazma hücresi antikor üreten terminal B hücresidir; inflamasyon ve multipl miyelomda görülür.",
50: "Granülom epitelioid makrofaj agregatıdır; tüberküloz, sarkoidoz, yabancı cisim reaksiyonlarında görülür.",
51: "Fibrozis doku onarımında kollajen birikimidir; skar dokusu oluşturur, fonksiyon kaybına yol açabilir.",
52: "Rejenerasyon aynı hücre tipiyle onarım; labil (epitel), stabil (hepatosit) ve kalıcı (nöron, kardiyomiyosit) hücreler ayrılır.",
53: "Apoptoz morfolojisi: hücre büzüşmesi, kromatin yoğunlaşması, apoptotik cisimcikler, fagositoz; inflamasyon yoktur.",
54: "Nekroz morfolojisi: hücre şişmesi, membran rüptürü, inflamasyon; koagülasyon, likuefaksiyon, kazeifikasyon tipleri vardır.",
55: "İskemi hipoksi sonucu ATP azalması, Na/K pompa bozukluğu, hücre şişmesi ve nekroz ile sonuçlanır.",
56: "Reperfüzyon hasarı ROS, Ca2+ yüklenmesi, mitokondriyal disfonksiyon ve inflamasyon ile oluşur.",
57: "Kimyasal hasar: CCl4 karaciğer nekrozu, asetaminofen hepatotoksisite, kurşun nörotoksisite yapar.",
58: "Fiziksel hasar: ısı, radyasyon, elektrik, travma; ısı yanık, radyasyon DNA hasarı ve kanser yapar.",
59: "İmmunolojik hasar: hipersensitivite (Tip I-IV), otoimmünite, graft rejeksiyonu.",
60: "Genetik hasar: kromozom anomalileri, tek gen mutasyonları; kistik fibrozis, orak hücre anemisi gibi.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
