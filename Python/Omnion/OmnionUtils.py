import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import PNJclass
import IAGeneratorClass
import OmnionClass
    
def CreatePNJ(PNJs:dict,nom:str,role:str)->dict:
    if role == "generator":
        _ = IAGeneratorClass.IAGenerator(nom,role)
    elif role == "Omnion":
        _ = OmnionClass.Omnion(nom,role)
    else:
        _ = PNJclass.PNJ(nom,role)
    _.startLife()
    _.changeLifeSpeed(10000000)
    PNJs[nom] = _
    return PNJs

def execCode(code):
    import subprocess

    result = subprocess.run(["powershell", "-Command", code], capture_output=True, text=True, shell=True)
    return result.stdout.strip() if result.stdout else result.stderr.strip()

def readSelf():
    return open("test.py","r",encoding="utf-8").read()

def getDateTime():
    from datetime import datetime
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%d%m%Y-%H%M%S")
    return formatted_datetime

def bkpFile(filetobkp:str,prompt:str):
    import shutil
    timestamp = getDateTime()
    os.system(f"mkdir bkp\{timestamp}")
    shutil.copy(filetobkp, f"bkp/{timestamp}/{filetobkp.split('/')[1]}.bkp")
    with open(f"bkp/{timestamp}/Prompt",'w',encoding="utf-8") as dest:
        dest.write(prompt)