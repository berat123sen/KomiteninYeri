# -*- coding: utf-8 -*-
"""2022-2023 ve 2025-2026 sınavları için ortak yardımcılar."""
import json
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT_DIR = r"C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data"
EXAM_DIR = os.path.join(OUT_DIR, "exams")
os.makedirs(EXAM_DIR, exist_ok=True)

DISC = {
    "histoloji": "Histoloji",
    "fizyoloji": "Fizyoloji",
    "biyokimya": "Biyokimya",
    "biyofizik": "Biyofizik",
    "mikrobiyoloji": "Mikrobiyoloji",
    "davranis-bilimleri": "Davranış Bilimleri",
    "tip-tarihi-etik": "Tıp Tarihi ve Etik",
    "sbet": "SBET",
    "entegre": "Entegre",
    "ayrimcilik": "Ayrımcılık ve Toplumsal Cinsiyet",
    "tip-insan-bilimleri": "Tıpta İnsan Bilimleri",
}


class Builder:
    def __init__(self, exam_id):
        self.exam_id = exam_id
        self.questions = []

    def add(self, n, disc, stem, opts, ans, page, status="official", conf=0.95, note=None, review="approved"):
        assert len(opts) == 5, f"Soru {n}: 5 şık değil ({len(opts)})"
        assert ans in "ABCDE" and len(ans) == 1, f"Soru {n}: geçersiz cevap {ans}"
        rec = {
            "id": f"{self.exam_id}-q{n:03d}",
            "examId": self.exam_id,
            "number": n,
            "disciplineId": disc,
            "discipline": DISC[disc],
            "type": "multiple_choice",
            "stem": stem.strip(),
            "options": [o.strip() for o in opts],
            "correctAnswer": ans,
            "sourcePage": page,
            "answerStatus": status,
            "confidence": conf,
            "reviewStatus": review,
        }
        if note:
            rec["note"] = note
        self.questions.append(rec)

    def finish(self, exam, expected):
        qs = self.questions
        nums = [q["number"] for q in qs]
        assert nums == list(range(1, expected + 1)), (
            f"Eksik/fazla: {sorted(set(range(1, expected + 1)) - set(nums))}"
        )
        # ders aralıklarını soru listesinden türet
        discs = []
        for q in qs:
            if not discs or discs[-1]["id"] != q["disciplineId"]:
                discs.append({"id": q["disciplineId"], "name": q["discipline"],
                              "questionCount": 0, "first": q["number"], "last": q["number"]})
            discs[-1]["questionCount"] += 1
            discs[-1]["last"] = q["number"]
        exam["questionCount"] = len(qs)
        exam["disciplines"] = discs
        path = os.path.join(EXAM_DIR, f"{exam['id']}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"exam": exam, "questions": qs}, f, ensure_ascii=False, indent=2)

        # index.json'a ekle / güncelle (yeni yıl önce)
        ipath = os.path.join(OUT_DIR, "index.json")
        with open(ipath, encoding="utf-8") as f:
            index = json.load(f)
        summ = {k: exam[k] for k in ("id", "label", "shortLabel", "year", "period", "term",
                                     "questionCount", "answerStatus", "disciplines")}
        index["exams"] = [e for e in index["exams"] if e["id"] != exam["id"]] + [summ]
        index["exams"].sort(key=lambda e: e["year"], reverse=True)
        with open(ipath, "w", encoding="utf-8") as f:
            json.dump(index, f, ensure_ascii=False, indent=2)
        print(f"OK {exam['id']}: {len(qs)} soru -> {path}")
        print(dict(Counter(q["correctAnswer"] for q in qs)))
        print([(d["id"], d["first"], d["last"]) for d in discs])
