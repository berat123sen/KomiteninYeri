# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
22: "Sitrik asit (sitrat) asetil-CoA karboksilazı (yağ asidi sentezi anahtar enzimi) uyarır. Sitrat, asetil-CoA'yı sitozole taşır ve allosterik olarak ACC'yi aktive eder. Piruvat karboksilaz, transketolaz, transaldolaz ve enolaz sitrat tarafından uyarılmaz.",
28: "Yağ asidi sentazda ACP (asil taşıyıcı protein) asetil gruplarını bağlar. ACP, fosfopantetein prostetik grubu ile yağ asidi zincirini taşır. Ketoasil sentaz, malonil/asetil transasilaz, ketoasil redüktaz ve enoil redüktaz diğer domainlerdir.",
34: "Homosistein artışı sistatyonin beta sentaz eksikliğinde (homosistinüri) görülür. Sistatyonin beta sentaz piridoksal fosfat (B6) kofaktörü ile homosistein→sistatyonin dönüşümünü katalize eder. Eksikliğinde homosistein birikir ve ateroskleroz, tromboz, mental retardasyon görülür.",
38: "Pürin katabolizmasının son ürünü ürik asittir (insanda ürikaz enzimi yoktur, primatlarda da yoktur). H2O, amonyak, asetil-CoA ve CO2 pürin katabolizmasının son ürünü değildir.",
44: "Tromboksan A2 (TXA2) trombosit agregasyonunu ve vazokonstriksiyonu tetikler. Anandamid endokannabinoid, LTA4 lökotrien öncülü, LXA4 lipoksin (anti-inflamatuar), PGI2 (prostasiklin) vazodilatasyon ve antiagregan etkilidir.",
49: "Karbonhidrat, protein ve yağ metabolizmasının ortak ürünü Asetil-CoA'dır (mitokondride). Yağ asitleri, glukoz, gliserol ve üre bu ortak ürün değildir.",
50: "Glikojen fosforilaz glikojeni fosforoliz ile glikoz-1-fosfat'a çevirir (hidroliz değil). Glikoz, UDP-glikoz, glikoz-6-fosfat ve glikoz-1,6-bifosfat farklı metabolitlerdir.",
51: "Eritrosit oksidatif direnci pentoz fosfat yoluna (NADPH üretimi) bağlıdır. NADPH glutatyon redüktaz ile redükte glutatyon (GSH) üretir; GSH oksidatif hasarı önler. G6PD eksikliğinde hemolitik anemi gelişir.",
58: "Süksinat dehidrogenaz hem TCA döngüsü hem de ETZ (kompleks II) enzimidir. NADH dehidrogenaz (kompleks I), sitokrom c oksidoredüktaz (kompleks III), sitokrom oksidaz (kompleks IV) ve ATP sentetaz (kompleks V) sadece ETZ'de bulunur.",
69: "Nernst denklemi: E = -60·log([iç]/[dış]) mV. E = -60·log(1000/1) = -60·3 = -180 mV. Pozitif iyonun iç konsantrasyonu dışından fazla olduğunda denge potansiyeli negatif olur.",
71: "Eritrositler %0.9 NaCl (izotonik, 0.154 M) içinde hacim değişmez. %1.8, %3.6, %7.2 ve %14.4 hipertonik çözeltilerdir; eritrositler büzüşür (krenasyon).",
72: "ATP sentetaz proton (H+) gradiyentinden (kemiosmoz, Mitchell hipotezi) enerji alır. Na+, Ca2+, K+, Cl- gradiyentleri ATP sentezinde kullanılmaz.",
81: "Zar kapasitansı küçüldükçe zaman sabiti (τ=RC) azalır (artmaz). Zar direnci, kapasitans, yüzey alanı ve kalınlık ile ilgili diğer ifadeler doğrudur.",
85: "V = E·d = 9×10⁶ V/m × 6×10⁻⁹ m = 54 mV. Hesap: 9×6 = 54, 10⁶×10⁻⁹ = 10⁻³, 54×10⁻³ V = 54 mV.",
101: "Eroin opiyatlar (opioidler) grubunda yer alır; esrar cannabinoid, morfin/kodein/metadon opioid grubundadır.",
102: "Alışkanlıklar düzelir ve iyileşebilir; 'iyileşmez' ifadesi yanlıştır. Alışkanlıklar rutin, otomatik ve değiştirilebilir davranışlardır.",
106: "Farmakovijilans ilaç güvenliği (advers etki izlemi, ilaç güvenlilik izlemi) ile ilgilidir.",
107: "Ülkemizde uyuşturucu madde kullanımı suçtur (Türk Ceza Kanunu).",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
