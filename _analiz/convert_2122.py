# -*- coding: utf-8 -*-
import json, os, sys, shutil
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
base = r"C:\Users\Berat\Desktop\KomiteninYeri"
src = r"C:\Users\Berat\Downloads\tum_tibbi_sorular.json"
root = os.path.join(base, "sinav-platformu")
data = json.load(open(src, encoding="utf-8"))

EXAM_ID = "2021-2022-tem-2"
disc_map = {
    "Histoloji": ("histoloji", "Histoloji"),
    "Biyokimya": ("biyokimya", "Biyokimya"),
    "Biyofizik": ("biyofizik", "Biyofizik"),
    "Fizyoloji": ("fizyoloji", "Fizyoloji"),
    "Mikrobiyoloji": ("mikrobiyoloji", "Mikrobiyoloji"),
    "Ruh Sağlığı": ("davranis-bilimleri", "Davranış Bilimleri"),
    "Ayrımcılık ve Toplumsal Cinsiyet": ("davranis-bilimleri", "Davranış Bilimleri"),
    "Entegre": ("entegre", "Entegre Oturum"),
}

QS = []
for q in data:
    did, dname = disc_map.get(q["ders"], ("davranis-bilimleri", q["ders"]))
    opts = [q["secenekler"].get(k, "") for k in ["A","B","C","D","E"]]
    QS.append({
        "id": f"{EXAM_ID}-q{q['id']:03d}",
        "examId": EXAM_ID,
        "number": q["id"],
        "disciplineId": did,
        "discipline": dname,
        "type": "multiple_choice",
        "stem": q["soru"],
        "options": opts,
        "correctAnswer": q["dogru_cevap"],
        "sourcePage": 1,
        "answerStatus": "official",
        "confidence": 0.95,
        "reviewStatus": "approved",
        "note": None,
        "explanation": None,
    })

from collections import OrderedDict
disc = OrderedDict()
for q in QS:
    d = disc.setdefault(q["disciplineId"], {"id": q["disciplineId"], "name": q["discipline"], "questionCount": 0, "first": q["number"], "last": q["number"]})
    d["questionCount"] += 1
    d["first"] = min(d["first"], q["number"])
    d["last"] = max(d["last"], q["number"])

exam = {
    "exam": {
        "id": EXAM_ID,
        "label": "2021-2022 Dönem 1 TEM 2",
        "shortLabel": "2021-22",
        "year": "2021-2022",
        "period": 1,
        "term": "TEM 2",
        "questionCount": len(QS),
        "answerStatus": "official",
        "sourcePdf": "/kaynak/2021-2022-tem-2.pdf",
        "disciplines": list(disc.values()),
    },
    "questions": QS,
}

out_dir = os.path.join(root, "public", "data", "exams")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, f"{EXAM_ID}.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(exam, f, ensure_ascii=False, indent=2)
print("written", out_path, len(QS))

# index.json
index_path = os.path.join(root, "public", "data", "index.json")
idx = json.load(open(index_path, encoding="utf-8"))
ids = [e["id"] for e in idx["exams"]]
if EXAM_ID not in ids:
    idx["exams"].append({
        "id": EXAM_ID,
        "label": exam["exam"]["label"],
        "shortLabel": exam["exam"]["shortLabel"],
        "year": exam["exam"]["year"],
        "period": exam["exam"]["period"],
        "term": exam["exam"]["term"],
        "questionCount": exam["exam"]["questionCount"],
        "answerStatus": exam["exam"]["answerStatus"],
        "disciplines": exam["exam"]["disciplines"],
    })
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False, indent=2)
    print("index updated")

# copy pdf (use 2021)
src_pdf = os.path.join(base, "sınavlar", "2021 tem 2.pdf")
dst_pdf = os.path.join(root, "public", "kaynak", "2021-2022-tem-2.pdf")
shutil.copyfile(src_pdf, dst_pdf)
print("pdf copied")
