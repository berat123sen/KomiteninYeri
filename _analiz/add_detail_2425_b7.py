# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
91: "Alışkanlık sonradan edinilmiş, tekrarla otomatikleşmiş davranıştır (doğal refleks değil). Genetik, fiziksel hastalık veya doğuştan yetenek değildir.",
92: "Bağımlılık zamanla rutin ve aşırı şekilde tekrarlanan davranıştır. Doğuştan gelen özellik değildir; fiziksel ve psikolojik sağlığı etkiler; iyileşebilir (düzelmez değildir); maddeyi bırakmak zordur.",
93: "Çocuğun kaza yoluyla yaralanması istismar türü değildir. Cinsel, fiziksel, duygusal istismar ve ihmal istismar türleridir.",
94: "Çocuklar ihmal/istismarı söylememelerinin nedenleri: inanılmayacağını düşünme, başlarının belaya gireceğinden korkma, istismarcının tehditleri, ailenin parçalanacağı endişesi, nasıl anlatacağını bilmeme. 'Ailenin parçalanmasını isteyebilirler' ifadesi yanlıştır; ailenin parçalanmasından korkarlar.",
95: "Türk tıp tarihinin modern cerrahi ve tıp eğitimi alanındaki önemli siması Operatör Cemil Topuzlu Paşa'dır.",
96: "Akupunktur eski Çin tıbbından günümüze evrensel ölçekte benimsenen bir uygulamadır.",
97: "En az ayrımcılığa maruz kalan gruplar çoğunluğa sahip dini inanç/mezhep gruplarıdır (azınlik gruplar daha fazla ayrımcılığa maruz kalır).",
98: "Toplumsal cinsiyete dayalı ayrımcılıkta 'günümüzde özellikle sağlık alanında açık cinsiyetçilik yapılmaktadır' ifadesi yanlıştır; açık cinsiyetçilik yerini örtük cinsiyetçiliğe bırakmıştır.",
99: "Milgram deneyi otoriteye uyumu (itaat) açıklamak için yapılmıştır.",
100: "'Ayrımcılık' tanımı içinde yer almayan: itaatli davranan (itaat ayrımcılık değildir).",
101: "Dopaminerjik ödül sisteminde (mezolimbik yolak) nucleus accumbens (ventral striatum) ana yapıdır.",
102: "Esrar (cannabis) opioid grubunda yer almaz; cannabinoid grubundadır.",
103: "Bağımlılık tanısal ölçütleri arasında 'maddenin neden olduğu fizik/psikolojik sorunun farkında olmama' yer almaz (farkında olma yer alır).",
104: "Fensiklidin (PCP) halüsinojenler grubunda yer alır.",
105: "Kokain kuvvetli psikik bağımlılık yapma özelliği olan uyarıcıdır.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
