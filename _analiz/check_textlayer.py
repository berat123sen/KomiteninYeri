# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import pymupdf

F = r"C:\Users\Berat\Desktop\KomiteninYeri\sınavlar"
f = [x for x in os.listdir(F) if "24-25" in x][0]
print("using:", repr(f))
doc = pymupdf.open(os.path.join(F, f))
print("pages", doc.page_count)
for p in range(doc.page_count):
    t = doc[p].get_text()
    print("page", p + 1, "chars", len(t), "blocks", len(doc[p].get_text("blocks")))
doc.close()
