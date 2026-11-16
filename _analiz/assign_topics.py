# -*- coding: utf-8 -*-
"""Soruları konulara ayırır (konu listesi: 2026-2027 akademik takvimi, MED102 'Hücreden Dokuya').
Çalıştırma: python assign_topics.py [--report]
- public/data/topics.json  -> konu listesi (ders, ad, ders saati, sıra)
- public/data/exams/*.json -> her soruya topicId / topic yazar
"""
import json, os, re, sys, glob
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DATA = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data"

# (ders, id, ad, saat)
TOPICS = [
    # --- Histoloji ---
    ("histoloji", "hist-giris", "Tıpta Histoloji ve Embriyoloji", 2),
    ("histoloji", "hist-doku-hazirlama", "Doku hazırlama ve inceleme yöntemleri", 2),
    ("histoloji", "hist-hucre", "Hücre ve hücresel elemanlar", 5),
    # --- Biyokimya ---
    ("biyokimya", "bk-metabolizma", "Metabolizmanın genel olarak incelenmesi", 2),
    ("biyokimya", "bk-beslenme", "Beslenmeye biyokimyasal yaklaşım", 2),
    ("biyokimya", "bk-eser", "Eser elementler", 2),
    ("biyokimya", "bk-zar", "Biyolojik zarlar ve taşınma sistemleri", 2),
    ("biyokimya", "bk-kh-sindirim", "Karbonhidratların sindirimi ve emilimi", 1),
    ("biyokimya", "bk-glikoliz", "Glikoliz ve denetimi", 2),
    ("biyokimya", "bk-glukoneogenez", "Glukoneogenez", 2),
    ("biyokimya", "bk-pentoz", "Pentoz fosfat yolu", 1),
    ("biyokimya", "bk-krebs", "Krebs döngüsü", 2),
    ("biyokimya", "bk-etz", "Hücresel solunum zinciri ve ATP sentezi", 2),
    ("biyokimya", "bk-glikojen", "Glikojen sentez ve yıkımı", 2),
    ("biyokimya", "bk-glikoz-disi", "Glikoz dışı şekerlerin metabolizması", 1),
    ("biyokimya", "bk-lipid-sindirim", "Lipidlerin sindirimi ve emilimi", 1),
    ("biyokimya", "bk-yag-yikim", "Yağ asitlerinin yıkımı (β-oksidasyon, keton cisimcikleri)", 2),
    ("biyokimya", "bk-yag-sentez", "Yağ asitlerinin sentezi", 2),
    ("biyokimya", "bk-tg-fosfolipid", "Trigliserid ve fosfolipid metabolizması", 2),
    ("biyokimya", "bk-eikosanoid", "Eikosanoidler ve türevleri", 1),
    ("biyokimya", "bk-kol-sentez", "Kolesterol yapısı ve biyosentezi", 2),
    ("biyokimya", "bk-kol-safra", "Kolesterol metabolizması ve safra asitleri", 2),
    ("biyokimya", "bk-lipoprotein", "Lipoprotein metabolizması", 2),
    ("biyokimya", "bk-protein-sindirim", "Proteinlerin sindirimi ve emilimi", 1),
    ("biyokimya", "bk-aminoasit", "Aminoasit metabolizması ve üre sentezi", 3),
    ("biyokimya", "bk-ozel-urun", "Aminoasitlerin özel ürünlere dönüşmesi (hem dahil)", 2),
    ("biyokimya", "bk-entegrasyon", "Metabolizmanın entegrasyonu (tokluk/açlık)", 2),
    ("biyokimya", "bk-diger", "Diğer (biyokimya)", 0),
    # --- Biyofizik ---
    ("biyofizik", "bf-enerji", "Biyomoleküler sistemlerde enerji aktarımı (termodinamik)", 1),
    ("biyofizik", "bf-zar-yapi", "Hücre zarının yapısı ve zar modelleri", 2),
    ("biyofizik", "bf-difuzyon", "Difüzyon ve osmotik denge (Fick yasası)", 2),
    ("biyofizik", "bf-tasinim", "Madde taşınımı: konsantrasyon ve elektrokimyasal gradyent", 2),
    ("biyofizik", "bf-zar-elektrik", "Zarın elektriksel modeli ve dinlenim potansiyeli", 3),
    ("biyofizik", "bf-sicaklik", "Sıcaklık, ısı aktarımı ve aktivasyon enerjisi", 4),
    ("biyofizik", "bf-diger", "Diğer (biyofizik)", 0),
    # --- Mikrobiyoloji ---
    ("mikrobiyoloji", "mb-giris", "Mikrobiyolojiye giriş", 1),
    ("mikrobiyoloji", "mb-bakteri", "Bakteri yapısı ve metabolizması", 2),
    ("mikrobiyoloji", "mb-genetik", "Bakteri genetiği", 1),
    ("mikrobiyoloji", "mb-uretim", "Mikroorganizmaların üretilmesi (besiyerleri)", 2),
    ("mikrobiyoloji", "mb-virus-yapi", "Virüslerin yapısı ve genel özellikleri", 2),
    ("mikrobiyoloji", "mb-virus-rep", "Virüslerin replikasyonu", 1),
    ("mikrobiyoloji", "mb-virus-tani", "Virüslerin tanı yöntemleri", 2),
    ("mikrobiyoloji", "mb-mantar", "Mantar hücresi ince yapısı", 1),
    ("mikrobiyoloji", "mb-sterilizasyon", "Sterilizasyon ve dezenfeksiyon", 2),
    ("mikrobiyoloji", "mb-diger", "Diğer (mikrobiyoloji)", 0),
    # --- Fizyoloji ---
    ("fizyoloji", "fz-homeostaz", "Homeostaz ve geri bildirim devreleri", 1),
    ("fizyoloji", "fz-hucre", "Hücre fizyolojisi; organeller arası iş bölümü", 2),
    ("fizyoloji", "fz-genetik", "Hücre işlevlerinin genetik kontrolü", 1),
    ("fizyoloji", "fz-sivi", "Bedenin bileşimi ve vücut sıvı bölükleri", 1),
    ("fizyoloji", "fz-difuzyon", "Zardan madde geçişi: difüzyon ve ozmoz", 2),
    ("fizyoloji", "fz-tasiyici", "Aracılı taşıma sistemleri", 2),
    ("fizyoloji", "fz-iletisim", "Hücreler arası iletişim, reseptörler, ikincil haberciler", 2),
    ("fizyoloji", "fz-hucre-dongusu", "Hücre döngüsünün kontrolü", 2),
    ("fizyoloji", "fz-diger", "Diğer (fizyoloji)", 0),
    # --- Davranış Bilimleri (MED101) ---
    ("davranis-bilimleri", "dv-noro", "Davranışın nörobiyolojik temelleri", 1),
    ("davranis-bilimleri", "dv-psikodinamik", "Davranışın psikodinamik temelleri ve savunma düzenekleri", 2),
    ("davranis-bilimleri", "dv-kisilik", "Kişilik gelişimi", 2),
    ("davranis-bilimleri", "dv-biyopsikososyal", "Biyopsikososyal yaklaşım", 1),
    ("davranis-bilimleri", "dv-stres", "Stres ve stresle başa çıkma mekanizmaları", 2),
    ("davranis-bilimleri", "dv-ogrenme", "Öğrenme ve hafıza", 1),
    ("davranis-bilimleri", "dv-aliskanlik", "Alışkanlıklar ve bağımlılık", 2),
    ("davranis-bilimleri", "dv-hasta-hekim", "Hasta hekim ilişkileri", 1),
    ("davranis-bilimleri", "dv-iletisim", "İletişim becerileri", 2),
    # --- Tıp Tarihi ve Etik (MED101) ---
    ("tip-tarihi-etik", "th-tarih", "Tıp tarihi (tıbbın evrimi, Batı/Doğu/Türk tıbbı)", 9),
    ("tip-tarihi-etik", "th-etik", "Tıp etiği ön bilgileri", 3),
    # --- Diğer (takvimde karşılığı olmayanlar) ---
    ("diger", "dg-entegre", "Entegre oturum soruları", 0),
    ("diger", "dg-sbet", "SBET", 0),
    ("diger", "dg-ayrimcilik", "Ayrımcılık ve toplumsal cinsiyet", 0),
    ("diger", "dg-istismar", "Çocuk istismarı ve ihmali", 0),
    ("diger", "dg-insan", "Tıpta insan bilimleri (HIV danışmanlık vb.)", 0),
]
TOPIC_NAME = {t[1]: t[2] for t in TOPICS}
DISC_OF = {t[1]: t[0] for t in TOPICS}

# Kural: (konu_id, regex). Sıra önemli; ilk eşleşen kazanır. Önce soru kökü, sonra şıklar denenir.
R = {
 "davranis-bilimleri": [("dv-psikodinamik", r".*")],
 "tip-tarihi-etik": [("th-tarih", r".*")],
 "entegre": [("dg-entegre", r".*")],
 "sbet": [("dg-sbet", r".*")],
 "ayrimcilik": [("dg-ayrimcilik", r".*")],
 "tip-insan-bilimleri": [("dg-insan", r".*")],
 "histoloji": [
  ("hist-giris", r"^aşağıda verilen tanımlamalardan"),
  ("hist-doku-hazirlama", r"fiksat|fiksasyon|parafin|rezin|gömme|kesit|boyama|boya|hematoksilen|mikrotom|mikroskop|doku takip|dehidrat|tem\b|sem\b|ayırma gücü|büyütme|glutaraldehit|formalin|uranil|kurşun sitrat"),
  ("hist-giris", r"histoloji|embriyoloji|teratoloji|histos|tarihçe|hücre teorisi|robert hooke|robert brown"),
  ("hist-hucre", r".*"),
 ],
 "biyofizik": [
  ("bf-sicaklik", r"ısı|sıcaklık|aktivasyon enerji|katalizör|termoregülasyon|kondüksiyon|konveksiyon|radyasyon|evapora|terleme|ekzotermik|endotermik|vücut sıcaklığ"),
  ("bf-enerji", r"entropi|gibbs|serbest enerji|entalpi|termodinamik|atp.*(hidroliz|enerji)|enerji aktar|enerjetik"),
  ("bf-zar-elektrik", r"potansiyel|nernst|goldman|kapasit|direnç|iletkenlik|elektrik|donnan|pil\b|devre|akım|mv\b"),
  ("bf-difuzyon", r"difüzyon|fick|ozmo|osmo|ozmotik|ozmolar|osmolar|çözelti|çözünen"),
  ("bf-tasinim", r"taşınım|taşıma|gradyent|gradiyent|kanal|pompa|iyon"),
  ("bf-zar-yapi", r"zar|membran|lipit|lipid|misel|fosfolip"),
  ("bf-diger", r".*"),
 ],
 "mikrobiyoloji": [
  ("mb-sterilizasyon", r"sterilizasyon|dezenfe|antisepsi|asepsi|otoklav|pastör|tindal|uht|koch kazan|dezenfektan|antiseptik"),
  ("mb-virus-tani", r"pcr|elisa|western|lateks|nötralizasyon|lipa\b|hücre kültürü|serolojik|tanısında|tanı yöntem"),
  ("mb-virus-rep", r"replikasyon|replike|adsorpsiyon|adsorbsiyon|penetrasyon|eklips|erken protein|kapsid.*ayrıl|uncoating"),
  ("mb-virus-yapi", r"vir[uü]s|virion|kapsid|kapsomer|zarflı|zarfsız|inklüzyon|rna genom|dna genom|bakteriyofaj"),
  ("mb-mantar", r"mantar|spor\b|spor|maya|hif|mikoz|kandida"),
  ("mb-uretim", r"besiyer|agar|üret|koloni|kültür|hemoliz|çikolata|kanlı"),
  ("mb-genetik", r"plazmid|konjugasyon|transformasyon|transdüksiyon|transpozon|f faktör|fertilite|mutasyon|genetik"),
  ("mb-bakteri", r"bakteri|hücre duvar|peptidoglikan|flajel|fimbria|pilus|kapsül|siderofor|aerob|anaerob|mezofil|psikrofil|termofil|gram|lps|teikoik|mezozom|porin|endospor|l form"),
  ("mb-giris", r"pasteur|koch|lister|semmelweis|fleming|jenner|mikrobiyoloji|ehrlich|mikroorganizma"),
  ("mb-diger", r".*"),
 ],
 "fizyoloji": [
  ("fz-hucre-dongusu", r"hücre döngü|mitoz|mayoz|apopto|siklin|kanser|p53|g1|checkpoint"),
  ("fz-iletisim", r"reseptör|haberci|g protein|camp|cgmp|kinaz|sinyal|ip3|nitrik oksit|ligand|hormon|parakrin|oto[ck]rin|guanilil|adenilil|fosfodiesteraz|kolera|fotoreseptör|natriüretik|steroid"),
  ("fz-tasiyici", r"taşıyıcı|uniport|simport|antiport|kolaylaştırılmış|aktif taşı|pompa|atpaz|na\+?-?k|kotransport|karşıt taşın"),
  ("fz-difuzyon", r"difüzyon|ozmo|osmo|ozmotik|ozmolar|osmolar|ozmoz|fick|permeab|geçirgen|akı"),
  ("fz-sivi", r"vücut sıvı|hücre dışı sıvı|hücre içi sıvı|interstisyel|plazma|bölme|bölük|milieu|toplam vücut"),
  ("fz-homeostaz", r"homeosta|geri bildirim|negatif|pozitif|kazanç|kontrol sistem"),
  ("fz-genetik", r"dna|rna|telomer|gen\b|genetik|transkripsiyon|translasyon|primer|ribozom|helikaz|ligaz|polimeraz|eşlenme|mirna|kromatin|nükleotid"),
  ("fz-hucre", r"organel|mitokondri|lizozom|golgi|retikulum|peroksizom|ara filament|aktin|mikrotübül|sitoiskelet|glikokaliks|endositoz|ekzositoz|vezikül|çekirdek|hücre"),
  ("fz-diger", r".*"),
 ],
 "biyokimya": [
  ("bk-eser", r"eser element|selenyum|çinko|molibden|manganez|mangan|bakır|kobalt|iyot|krom\b|flor"),
  ("bk-eikosanoid", r"prostaglandin|araşidonik|lökotrien|tromboksan|prostasiklin|siklooksijenaz|lipooksijenaz|eikosanoid|eykozatetraenoik"),
  ("bk-lipoprotein", r"lipoprotein|vldl|ldl|hdl|idl|şilomikron|apo\s?[abce]|apo\(|lcat|lpl|lipoprotein lipaz"),
  ("bk-kol-safra", r"safra|kolik asit|kenodeoksi|konjugasyon|kolestanol|koprostanol|enterohepatik"),
  ("bk-kol-sentez", r"kolesterol|hmg|mevalon|skualen|srebp|steroid|statin|öncü maddesi"),
  ("bk-lipid-sindirim", r"lipaz|sindirim.*(yağ|lipid|trigliserit)|(yağ|lipid|trigliserit).*sindirim|misel|emülsi"),
  ("bk-yag-yikim", r"beta oksidasyon|β-oksidasyon|oksidasyon.*yağ|yağ asid.*(yıkım|oksidasyon)|karnitin|keton|asetoasetat|hidroksibütirat|palmit.*oksid|palmitoik"),
  ("bk-yag-sentez", r"yağ asidi sentez|malonil|asetil.?coa karboksilaz|asil taşıyıcı|acp|sitrat liyaz|yağ asidi sentaz|palmitat"),
  ("bk-tg-fosfolipid", r"fosfolipit|fosfolipid|gliserofosfolipit|trigliserit|trigliserid|triaçilgliserol|triasilgliserol|sfingo|fosfatidik|fosfatidil|plazmalojen|kardiyolipin|gliserol"),
  ("bk-etz", r"etz|elektron transport|solunum zinciri|oksidatif fosforilasyon|kompleks [iv]+\b|atp sentaz|koenzim q|sitokrom|proton gradyan|fosforilasyon|f0f1|nadh.*atp|kaç atp|atp.*net"),
  ("bk-krebs", r"krebs|sitrik asit|tca|süksinat|fumarat|malat|oksaloasetat|alfa.?keto|izositrat|sitrat\b"),
  ("bk-pentoz", r"pentoz|nadph|riboz|transketolaz|glukoz.?6.?fosfat dehidrogenaz|g6pd"),
  ("bk-glikojen", r"glikojen|glikojenez|glikojenolizis|fosforilaz|glikojen sentaz|udp.?glukoz|branching|dallanma"),
  ("bk-glukoneogenez", r"glukoneogenez|glukoz-6-fosfataz|fruktoz.?1,6.?bifosfataz|pep karboksikinaz|piruvat karboksilaz|pirüvat karboksilaz|cori"),
  ("bk-glikoliz", r"glikoliz|heksokinaz|glukokinaz|fosfofruktokinaz|piruvat kinaz|pirüvat kinaz|piruvat dehidrogenaz|pirüvat dehidrogenaz|laktat dehidrogenaz|2,3.?bifosfogliserat|substrat düzeyinde|gliseraldehit|fruktoz.?2,6"),
  ("bk-glikoz-disi", r"fruktoz|galaktoz|sorbitol|mannoz|aldolaz.?b|galaktozemi|aldoz redüktaz|polyol|katarakt|glukronat"),
  ("bk-kh-sindirim", r"amilaz|laktaz|sükraz|maltaz|isomaltaz|disakkarit|karbonhidrat.*(sindirim|emil)|glut|sglt|laktoz|trehalaz|selüloz|glukoz.*emil"),
  ("bk-protein-sindirim", r"pepsin|tripsin|kimotripsin|proteaz|karboksipeptidaz|peptid.*(parça|kesil)|proteinlerin sindirim|enterokinaz|zimojen"),
  ("bk-ozel-urun", r"tirozin|dopa\b|melanin|serotonin|histamin|katekolamin|adrenalin|noradrenalin|spermin|kreatin|glutatyon|hem\b|porfirin|protoporfirin|bilirubin|nitrik oksit|tetrahidrobiyopterin|homojentisik|niasin|nikotinat|taurin|gaba\b|fenilalanin hidroksilaz|alkapton"),
  ("bk-aminoasit", r"amino ?asit|aminoasit|üre|amonyak|transaminasyon|deaminasyon|karbamoil|sitrullin|arjinin|arginin|ornitin|homosistein|fenilketonüri|glutamin|glutamat|glisin|sistein|metionin|serin|aspartat|aspartik|alanin|triptofan|n-asetil.?glutamat|sistatyonin|bcaa|ketojenik|glukojenik"),
  ("bk-entegrasyon", r"tokluk|açlık|insülin|glukagon|entegrasyon|besleniyor|doku arası|kas ve karaciğer"),
  ("bk-beslenme", r"glisemik|beslenme|besin|vitamin|kalori|diyet|bazal metabolizma|vücut kitle|enerji yoğunluğu|mortalite"),
  ("bk-zar", r"zar|membran|taşıyıcı|gradiyent|kolaylaştırılmış"),
  ("bk-metabolizma", r"metabolizma|anabolik|katabolik|atp|nad|fad|enzim|koenzim|kofaktör"),
  ("bk-diger", r".*"),
 ],
}


def norm(s):
    return s.replace("İ", "i").replace("I", "ı").lower()


def classify(q):
    rules = R.get(q["disciplineId"])
    if not rules:
        return None
    stem = norm(q["stem"])
    opts = norm(" ".join(q["options"]))
    for tid, rx in rules:
        if rx == r".*":
            continue
        if re.search(rx, stem):
            return tid
    for tid, rx in rules:
        if rx == r".*":
            continue
        if re.search(rx, opts):
            return tid
    return rules[-1][0]


# Elle düzeltmeler (soru id -> konu id); gözden geçirmeden sonra buraya eklenir.
OVERRIDES = {}
try:
    OVERRIDES = json.load(open(os.path.join(os.path.dirname(__file__), "topic_overrides.json"), encoding="utf-8"))
except Exception:
    pass


def main():
    report = "--report" in sys.argv
    topics_out = []
    order = 0
    for disc, tid, name, hrs in TOPICS:
        order += 1
        topics_out.append({"id": tid, "disciplineId": disc, "name": name, "hours": hrs, "order": order})
    files = sorted(glob.glob(os.path.join(DATA, "exams", "*.json")))
    per = defaultdict(list)
    for f in files:
        d = json.load(open(f, encoding="utf-8"))
        for q in d["questions"]:
            tid = OVERRIDES.get(q["id"]) or classify(q)
            if tid:
                q["topicId"] = tid
                q["topic"] = TOPIC_NAME[tid]
                per[tid].append((q["examId"][:9], q["number"], q["stem"][:95].replace("\n", " ")))
            else:
                q.pop("topicId", None)
                q.pop("topic", None)
        json.dump(d, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    json.dump({"version": 1, "source": "2026-2027 1. Sınıf Akademik Takvimi (MED102 Hücreden Dokuya)", "topics": topics_out},
              open(os.path.join(DATA, "topics.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    cnt = Counter({t: len(v) for t, v in per.items()})
    for disc, tid, name, hrs in TOPICS:
        print(f"{cnt.get(tid, 0):4d}  {tid:22s} {name}")
    if report:
        for disc, tid, name, hrs in TOPICS:
            print(f"\n## {tid} ({name})")
            for e, n, s in per.get(tid, []):
                print(f"  {e}#{n}: {s}")


main()
