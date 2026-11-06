# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
 1: "Canlıların temel yapısal biriminin hücre olduğu hücre teorisiyle ortaya konulmuştur; elektron mikroskobunun keşfi daha sonra gelmiştir. A, B, C ve D doğru tanımlamalardır.",
 2: "İnsan gözünün ayırma gücü hücreleri ayırt etmek için yeterli değildir; mikroskop gerekir. Diğer seçenekler doğrudur.",
 3: "Elektron mikroskobik takipte gömme materyali rezin, kesit için ultramikrotom, boyama için uranil asetat-kurşun sitrat kullanılır; formalin tespit ve ksilol şeffaflandırma ışık mikroskobu içindir.",
 4: "Kollajen liflerini boyamak için Masson trikrom (mavi/yeşil) tercih edilir; Van Gieson elastik lifler için, PAS glikoproteinler için kullanılır.",
 5: "Lizozomlar makrofaj ve nötrofillerde bol bulunur ve hidrolitik enzim içerir; membran iç yüzeyinin glikozillenmesi ve lizobifosfatidik asit içeriği lizozomu kendi enzimlerinden korur; membran proteinleri Golgi'de sentezlenir.",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
