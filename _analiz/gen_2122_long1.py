import json,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
d=json.load(open(r'C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2021-2022-tem-2.json',encoding='utf-8'))
out=[]
for q in d['questions']:
    if 1<=q['number']<=25 and len(q.get('explanation',''))<200:
        out.append(f"{q['number']} | {q['discipline']} | {q['stem']}")
        for i,o in enumerate(q['options']): out.append(f"   {chr(65+i)}) {o}")
        out.append(f"   CEVAP: {q['correctAnswer']}")
        out.append(f"   MEVCUT: {q.get('explanation','')[:60]}")
        out.append('')
open(r'C:\Users\Berat\Desktop\KomiteninYeri\_analiz\2122_long1.txt','w',encoding='utf-8').write('\n'.join(out))
print('done')
