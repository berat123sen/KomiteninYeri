# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
91: """Alışkanlık (habit) sonradan edinilmiş, tekrarla otomatikleşmiş davranıştır (doğal refleks değil). Genetik faktörlerle belirlenen davranışlar, fiziksel bir rahatsızlığa bağlı davranışlar veya doğuştan gelen yetenekler alışkanlık değildir. A, C, D, E seçenekleri alışkanlık tanımına uymaz. B seçeneği (zamanla otomatik bir tepki haline dönüşen, sonradan edinilmiş davranışlar) doğrudur.""",
92: """Bağımlılık (addiction) zamanla rutin ve aşırı şekilde tekrarlanan davranıştır. Doğuştan gelen bir özellik değildir (A yanlıştır). Yalnızca fiziksel sağlığı etkilemez; psikolojik ve sosyal sağlığı da etkiler (C yanlıştır). İyileşebilir (düzelmez değildir, D yanlıştır). Bağımlı bireyler maddeyi kolayca bırakamaz (E yanlıştır). B seçeneği (bağımlılık davranışının zamanla rutin ve aşırı şekilde tekrarlanması) doğrudur.""",
93: """Çocuğun kaza yoluyla yaralanması istismar türü değildir. Cinsel istismar (A), fiziksel istismar (B), duygusal istismar (C) ve ihmal (D) çocuk istismarı türleridir. E seçeneği (çocuğun kaza yolu ile yaralanması) istismar türü değildir.""",
94: """Çocuklar ihmal/istismarı söylememelerinin nedenleri: kendilerine inanılmayacağını düşünme (A), başlarının belaya gireceğinden korkma (B), istismarcının tehditleri (C), ailenin parçalanacağı endişesi (D seçeneği 'isteyebilirler' olarak ifade edildiği için yanlıştır; çocuklar ailenin parçalanmasından korkarlar, istemezler), nasıl anlatacağını bilmeme (E). D seçeneği (ailenin parçalanmasını isteyebilirler) yanlıştır.""",
95: """Türk tıp tarihinin özellikle modern cerrahi ve tıp eğitimi başlıkları altında önemli yere sahip siması Operatör Cemil Topuzlu Paşa'dır. Gazi Osman Paşa, Kazım Karabekir Paşa, Sokullu Mehmet Paşa ve Tiryaki Hasan Paşa askeri/siyasi liderlerdir. C seçeneği doğrudur.""",
96: """Akupunktur eski Çin tıbbından (MÖ 1000) günümüze evrensel ölçekte benimsenen bir uygulamadır (WHO tarafından ağrı, bulantı, baş ağrısı vb. için kabul edilmiştir). Ayurveda (A) Hint tıbbıdır. Radyolojik görüntüleme (B) modern tıbbın ürünüdür. Damar yoluyla sıvı verme (D) modern tıbbın ürünüdür. Yoga (E) Hint felsefesi/egzersiz sistemidir. C seçeneği doğrudur.""",
97: """En az ayrımcılığa maruz kalan gruplar çoğunluğa sahip dini inanç/mezhep gruplarıdır (E seçeneği). Azınlık gruplar (farklı cinsel yönelim, engelli, göçmen, muhalif) daha fazla ayrımcılığa maruz kalır. A, B, C, D seçenekleri ayrımcılığa maruz kalan gruplardır. E seçeneği (çoğunluğa sahip dini inanç/mezhep grupları) en az ayrımcılığa maruz kalan gruptur.""",
98: """Toplumsal cinsiyete dayalı ayrımcılıkta 'günümüzde özellikle sağlık alanında açık cinsiyetçilik yapılmaktadır' ifadesi yanlıştır; açık cinsiyetçilik yerini örtük cinsiyetçiliğe bırakmıştır. A, C, D, E doğru ifadelerdir. B seçeneği yanlıştır.""",
99: """Milgram deneyi (1961) otoriteye uyumu (itaat) açıklamak için yapılmıştır; katılımcıların %65'i otorite figürünün (deney yöneticisi) talimatıyla maksimum 450V şok vermiştir. Kalıp yargı (A), öznel inançlar (C), görev bilinci (D), işkenceci kişilik (E) Milgram deneyinin temel kavramı değildir. B seçeneği (otoriteye uyum) doğrudur.""",
100: """'Ayrımcılık' tanımı içinde yer almayan: itaatli davranan (D seçeneği). Ayrımcılık: kendi grubunun avantajını düşünen, diğer grubun dezavantajını görmezden gelen, pekiştiren ve diğerine acı verici tutum/davranış sergileyen davranıştır. A, B, C, E ayrımcılık tanımına girer. D (itaatli davranan) ayrımcılık değildir.""",
101: """Dopaminerjik ödül sisteminde (mezolimbik yolak: VTA → nucleus accumbens → prefrontal korteks) nucleus accumbens (ventral striatum) ana yapıdır; bağımlılık, ödül ve motivasyon ile ilişkilidir. Nucleus caudatus, globus pallidus, corpus striatum ve putamen motor kontrol ile ilişkilidir. B seçeneği doğrudur.""",
102: """Esrar (cannabis) cannabinoid grubunda yer alır (THC, CBD). Opioid grubu: eroin, morfin, kodein, metadon, fentanil. A seçeneği (esrar) opioid grubunda yer almaz.""",
103: """Bağımlılık tanısal ölçütleri (DSM-5) arasında yer almayan: 'maddenin neden olduğu fizik ya da psikolojik bir sorunun olduğunu farkında olmama' (D seçeneği). DSM-5'te 'farkında olma' (craving) yer alır, 'farkında olmama' yer almaz. A, B, C, E DSM-5 ölçütleridir.""",
104: """Fensiklidin (PCP, 'angel dust') halüsinojenler (dissosiatif anestezikler) grubunda yer alır. Opioidler, uyarıcılar, sedatifler, hipnotikler farklı gruplardır. E seçeneği doğrudur.""",
105: """Kokain kuvvetli psikik bağımlılık yapma özelliği olan uyarıcıdır (stimulan). Alkol, esrar, nikotin, amfetamin de bağımlılık yapar ancak kokain en kuvvetli psikik bağımlılık yapma özelliği ile bilinir. A seçeneği doğrudur.""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
