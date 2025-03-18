import json,os
a = json.loads(open('test.json','r',encoding='utf-8').read())

with open(a["filename"],'w',encoding='utf-8') as dest:
    dest.write(a["content"])

os.system(f"python3.10.exe {a['filename']}")

