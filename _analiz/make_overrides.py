# -*- coding: utf-8 -*-
"""Elle konu atamaları (yıl -> {soru no: konu id}). topic_overrides.json üretir."""
import json, os
Y = {
 "2021-2022": {
  # biyokimya
  21: "bk-glikoliz", 31: "bk-ozel-urun", 48: "bk-glukoneogenez", 54: "bk-glikojen", 44: "bk-eikosanoid",
  57: "bk-glikoz-disi", 22: "bk-yag-sentez", 23: "bk-kh-sindirim", 37: "bk-metabolizma", 40: "bk-metabolizma",
  # biyofizik
  78: "bf-enerji",
  # mikrobiyoloji
  10: "mb-giris", 11: "mb-bakteri", 12: "mb-bakteri", 13: "mb-virus-yapi", 14: "mb-virus-yapi", 15: "mb-virus-rep",
  16: "mb-virus-tani", 17: "mb-virus-tani", 18: "mb-virus-tani", 19: "mb-bakteri", 20: "mb-uretim",
  # fizyoloji
  60: "fz-homeostaz", 61: "fz-sivi", 62: "fz-genetik", 63: "fz-genetik", 64: "fz-iletisim", 65: "fz-iletisim",
  66: "fz-tasiyici", 67: "fz-difuzyon", 68: "fz-difuzyon", 69: "fz-difuzyon", 70: "fz-hucre", 71: "fz-difuzyon", 72: "fz-hucre",
 },
 "2022-2023": {
  8: "bk-metabolizma", 12: "bk-glukoneogenez", 15: "bk-glikoliz", 22: "bk-tg-fosfolipid", 18: "bk-yag-sentez",
  24: "bk-eikosanoid", 26: "bk-yag-sentez", 31: "bk-ozel-urun", 34: "bk-glukoneogenez", 35: "bk-glikoliz",
  57: "bf-difuzyon", 58: "bf-difuzyon",
  63: "fz-homeostaz", 64: "fz-hucre", 65: "fz-hucre", 66: "fz-genetik", 67: "fz-genetik", 68: "fz-sivi",
  69: "fz-difuzyon", 70: "fz-difuzyon", 71: "fz-difuzyon", 72: "fz-iletisim", 73: "fz-iletisim", 74: "fz-iletisim",
  75: "mb-bakteri", 76: "mb-giris", 77: "mb-bakteri", 78: "mb-bakteri", 79: "mb-virus-yapi", 80: "mb-virus-rep",
  81: "mb-virus-tani", 82: "mb-virus-yapi", 83: "mb-virus-tani", 84: "mb-uretim",
 },
 "2023-2024": {
  5: "bk-glukoneogenez", 9: "bk-glukoneogenez", 13: "bk-aminoasit", 14: "bk-yag-sentez", 22: "bk-metabolizma",
  23: "bk-ozel-urun", 35: "bk-glukoneogenez", 36: "bk-glikoliz", 39: "bk-beslenme",
  66: "bf-enerji", 75: "bf-zar-elektrik",
  50: "mb-bakteri", 51: "mb-giris", 52: "mb-virus-yapi", 53: "mb-virus-yapi", 54: "mb-virus-rep", 55: "mb-virus-tani",
  56: "mb-virus-tani", 57: "mb-uretim", 58: "mb-bakteri", 59: "mb-bakteri", 60: "mb-bakteri",
  77: "fz-homeostaz", 78: "fz-hucre", 79: "fz-hucre", 80: "fz-genetik", 81: "fz-iletisim", 82: "fz-difuzyon",
  83: "fz-tasiyici", 84: "fz-tasiyici", 85: "fz-iletisim", 86: "fz-iletisim", 87: "fz-iletisim",
 },
 "2024-2025": {
  35: "bk-etz", 44: "bk-glukoneogenez", 55: "bk-zar", 28: "bk-aminoasit", 27: "bk-aminoasit", 34: "bk-glikoliz",
  26: "bk-aminoasit", 23: "bk-metabolizma", 47: "bk-eser", 20: "bk-lipid-sindirim", 45: "bk-aminoasit",
  59: "bf-enerji", 61: "bf-difuzyon",
  73: "mb-virus-yapi", 74: "mb-virus-rep", 75: "mb-virus-yapi", 76: "mb-virus-tani", 77: "mb-virus-yapi",
  78: "mb-virus-tani", 79: "mb-bakteri", 80: "mb-bakteri", 81: "mb-uretim", 82: "mb-uretim", 83: "mb-bakteri", 84: "mb-bakteri",
  10: "fz-sivi", 11: "fz-homeostaz", 12: "fz-hucre", 13: "fz-hucre", 14: "fz-hucre", 15: "fz-difuzyon",
  16: "fz-tasiyici", 17: "fz-tasiyici", 18: "fz-iletisim", 19: "fz-iletisim",
 },
 "2025-2026": {
  32: "bk-kh-sindirim", 49: "bk-glukoneogenez", 60: "bk-glukoneogenez", 29: "bk-zar", 62: "bk-aminoasit",
  70: "bk-aminoasit", 51: "bk-glikoliz", 72: "bk-entegrasyon", 68: "bk-metabolizma", 43: "bk-ozel-urun",
  73: "bk-entegrasyon", 30: "bk-zar",
  82: "bf-enerji", 86: "bf-difuzyon", 91: "bf-zar-elektrik",
  13: "mb-giris", 14: "mb-virus-yapi", 15: "mb-virus-yapi", 16: "mb-virus-rep", 17: "mb-virus-rep", 18: "mb-virus-yapi",
  19: "mb-bakteri", 20: "mb-bakteri", 21: "mb-mantar", 22: "mb-sterilizasyon", 23: "mb-sterilizasyon",
  24: "mb-bakteri", 25: "mb-bakteri", 26: "mb-genetik", 27: "mb-uretim", 28: "mb-uretim",
  1: "fz-sivi", 2: "fz-hucre", 3: "fz-hucre", 4: "fz-hucre", 5: "fz-hucre", 6: "fz-hucre", 7: "fz-tasiyici",
  8: "fz-genetik", 9: "fz-genetik", 10: "fz-iletisim", 11: "fz-iletisim", 12: "fz-iletisim",
 },
}

D = {
 "2021-2022": {88:"stres",89:"stres",90:"stres",91:"psikodinamik",92:"psikodinamik",93:"psikodinamik",94:"biyopsikososyal",95:"aliskanlik",96:"aliskanlik",97:"istismar",98:"istismar",99:"ayrimcilik",100:"ayrimcilik"},
 "2022-2023": {85:"noro",86:"stres",87:"stres",88:"psikodinamik",89:"psikodinamik",90:"psikodinamik",91:"biyopsikososyal",92:"aliskanlik"},
 "2023-2024": {88:"noro",89:"psikodinamik",90:"psikodinamik",91:"aliskanlik",92:"biyopsikososyal",93:"noro",94:"stres",95:"stres",96:"ayrimcilik",97:"ayrimcilik",98:"istismar",99:"istismar"},
 "2024-2025": {85:"noro",86:"biyopsikososyal",87:"psikodinamik",88:"kisilik",89:"kisilik",90:"stres",91:"aliskanlik",92:"aliskanlik",93:"istismar",94:"istismar"},
}
for y, m in D.items():
    for n, t in m.items():
        pre = "dg-" if t in ("istismar", "ayrimcilik") else "dv-"
        Y[y][n] = pre + t
Y["2023-2024"][100] = "th-tarih"
Y["2024-2025"][95] = "th-tarih"
Y["2024-2025"][96] = "th-tarih"
out = {}
for y, m in Y.items():
    for n, t in m.items():
        out[f"{y}-tem-2-q{n:03d}"] = t
json.dump(out, open(os.path.join(os.path.dirname(__file__), "topic_overrides.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
