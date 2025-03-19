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
    
    # Obtenir le chemin absolu relatif au dossier courant
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Obtient le chemin du dossier du script
    bat_file = os.path.join(current_dir, "Python", "Omnion", "Omnion.bat")  # Chemin relatif vers le .bat
    
    # Vérifie si le fichier existe

    subprocess.run([bat_file], shell=True)
