import Python.PNJclass as PNJclass
import Python.IAGeneratorClass as IAGeneratorClass
import Python.OmnionClass as OmnionClass

def printPNJ(PNJs:dict)->None:
    for values in PNJs.values():
        values.printAge()

def clear():
    import os
    os.system('cls')

def CalcToken(text:str)->int:
    import tiktoken
    return len(tiktoken.encoding_for_model("gpt-4o-mini").encode(str(text)))

def GetRole(role):
    return open(f"data/roles/{role}.dat", "r", encoding="utf-8").read()

def reload():
    import time,os
    os.system("cls")
    print("🔄 Redémarrage en cours... Ne touchez à rien !")
    time.sleep(1)
    os.system("cls")
    os.execv("StartOmnion.bat", ["StartOmnion.bat"])