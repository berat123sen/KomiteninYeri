# -*- coding: utf-8 -*-
"""Metin PDF'lerinde sınav sınırlarını ve yapıyı bul."""
import os
import re
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = r"C:\Users\Berat\Desktop\KomiteninYeri\_analiz"

for fname in ["2_241126_200803.txt", "102_23-24_19_Haz_24__062932_1.txt"]:
    path = os.path.join(OUT, fname)
    with open(path, encoding="utf-8") as f:
        text = f.read()

    print("=" * 80)
    print("DOSYA:", fname)
    print("=" * 80)

    # Sınav/dönem/yıl belirteçleri
    patterns = [
        r"TEM\s*I{1,3}",
        r"DÖNEM\s*[12]",
        r"DÖNEM[-\s]*[12]",
        r"\(1[0-9]{3}\)",  # parantezli yıl
        r"20[0-2][0-9]\s*[-–]\s*20[0-2][0-9]",  # 2014-2015
        r"\b20[0-2][0-9]\b",
        r"YANIT\s*:",
        r"CEVAP\s*:?",
        r"\( *\d+\s*[-–]\s*\d+\.\s*SORULAR *\)",
    ]
    for p in patterns:
        matches = list(re.finditer(p, text, re.IGNORECASE))
        print(f"\n--- /{p}/ -> {len(matches)} eşleşme")
        for m in matches[:15]:
            start = max(0, m.start() - 40)
            end = min(len(text), m.end() + 40)
            snippet = text[start:end].replace("\n", " ")
            print(f"    @{m.start():6d}: ...{snippet}...")

    # Ders başlıkları (bilinen tıp dersleri)
    print("\n--- Ders başlıkları ---")
    dersler = ["ANATOMİ", "FİZYOLOJİ", "BİYOKİMYA", "HİSTOLOJİ", "EMBRİYOLOJİ",
               "MİKROBİYOLOJİ", "PATOLOJİ", "FARMAKOLOJİ", "BİYOFİZİK",
               "BİYOİSTATİSTİK", "GENETİK", "PARAZİTOLOJİ", "İMMÜNOLOJİ"]
    for d in dersler:
        ms = list(re.finditer(d, text, re.IGNORECASE))
        if ms:
            print(f"    {d}: {len(ms)} kez")
