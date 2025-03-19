import PNJclass
import IAGeneratorClass
import Omnion.OmnionClass

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
    import time,os,subprocess
    os.system("cls")  # Clear the screen
    print("🔄 Redémarrage en cours... Ne touchez à rien !")
    time.sleep(1)
    os.system("cls")  # Clear the screen again
    print("\n")

    bat_path = os.path.join(os.path.dirname(__file__), "../Omnion.bat")
    
    # Vérifie si le fichier .bat existe
    if not os.path.isfile(bat_path):
        print(f"Le fichier {bat_path} est introuvable")
        return

    # Exécuter le fichier .bat
    subprocess.run([bat_path], shell=True)