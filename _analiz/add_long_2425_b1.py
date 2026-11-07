# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2024-2025-tem-2.json"
d = json.load(open(p, encoding="utf-8"))

exp = {
1: """Histoloji, Yunanca 'histos' (doku) ve 'logos' (bilim/çalışma) kelimelerinden türemiş bir terimdir ve insanın hücre, doku ve organlarının normal mikroskobik yapısını inceleyen bilim alanıdır. A seçeneği bu etimolojik tanımı doğru vermektedir. B seçeneği histolojinin temel tanımını doğru ifade eder: hücre, doku ve organların normal yapılarını mikroskop altında incelemek. C seçeneği de doğrudur: histoloji ve embriyoloji yalnızca normal yapı ve gelişimi değil, hücre ve doku hasarının mikroskobik düzeyde araştırılması (patolojik histoloji), kök hücre biyolojisi, rejeneratif tıp araştırmaları ve in vitro fertilizasyon (IVF) gibi alanları da kapsar. D seçeneği insan vücudunun esas yapısal bileşenlerini (hücreler, hücrelerarası maddeler, vücut sıvıları) doğru listeler. E seçeneği ise temel yapısal birimi 'hücreler arası maddeler' olarak tanımladığı için yanlıştır; canlıların temel yapısal ve işlevsel birimi hücredir. Bu gerçek hücre teorisi (Schleiden ve Schwann, 1838-1839) ile ortaya konmuştur. Elektron mikroskobunun keşfi (1930'lar) daha sonra gelmiş ve hücre içi organellerin (mitokondri, endoplazmik retikulum, ribozom, Golgi) ayrıntılı yapısını ortaya çıkarmıştır. Temel yapısal birim hücre olmakla birlikte, hücreler arası maddeler (ekstrasellüler matriks) de dokuların bütünlüğü ve işlevi için hayati önem taşır.""",
2: """İnsan gözünün ayırma gücü (rezolüsyon) yaklaşık 0.2 mm (200 µm) düzeyindedir. Hücreler (10-100 µm) ve hücre içi yapılar (1-10 µm) gözle ayırt edilemez; bunlar için ışık mikroskobu (rezolüsyon ~0.2 µm) veya elektron mikroskobu (rezolüsyon ~0.1 nm) gerekir. A seçeneği: Histoloji, hücre, doku ve organların normal yapısını mikroskop ile inceleyen bilim alanıdır ve doğrudur. B seçeneği: Mikroskobik incelemelerde en önemli iki faktör büyütme (magnification) ve ayırma gücü (resolution) dür; doğrudur. D seçeneği: Histoloji bilim alanının gelişiminde hücrenin tanımlanması (Robert Hooke, 1665), hücre teorisinin ortaya konulması (Schleiden-Schwann, 1838-39) ve elektron mikroskobunun keşfi (Knoll-Ruska, 1931) çok önemli aşamalardır; doğrudur. E seçeneği: Robert Hooke ilk defa hücreyi (mantar dokusunda) tanımlamış, Robert Brown (1831) çekirdeği keşfetmiştir; doğrudur. C seçeneği insan gözünün ayırma gücünün hücreleri ayırt etmek için yeterli olduğunu iddia ettiği için yanlıştır; mikroskop olmadan hücre düzeyi incelemeler yapılamaz.""",
}

for q in d["questions"]:
    if q["number"] in exp:
        q["explanation"] = exp[q["number"]]

json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("done", len(exp))
