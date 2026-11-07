import json,sys
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
d=json.load(open(r'C:\Users\Berat\Desktop\KomiteninYeri\sinav-platformu\public\data\exams\2023-2024-tem-2.json',encoding='utf-8'))
out=[]
for q in d['questions']:
    if 61<=q['number']<=76:
        out.append(f"{q['number']} | {q['discipline']} | {q['stem']}")
        for i,o in enumerate(q['options']): out.append(f"   {chr(65+i)}) {o}")
        out.append(f"   CEVAP: {q['correctAnswer']}")
        out.append('')
open(r'C:\Users\Berat\Desktop\KomiteninYeri\_analiz\det_2324_b5.txt','w',encoding='utf-8').write('\n'.join(out))
print('done')
