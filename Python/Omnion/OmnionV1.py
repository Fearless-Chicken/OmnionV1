import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import  time, pick, PNJclass as PNJclass, Utils as Utils, ast, traceback, OmnionUtils

if __name__ == '__main__':
    try:
        PNJs = {}
        PNJs = OmnionUtils.CreatePNJ(PNJs,"Omnion","Omnion")
        PNJs["Omnion"].talkTo()
    except Exception as e:
        while True:
            choix,_ = pick.pick(["Tentative de reload","Voir l'erreur","Quitter"],"Erreure detectée...",indicator=">")
            match choix:
                case "Tentative de reload":
                    Utils.reload()
                case "Quitter":
                    Utils.clear()
                    exit()
                case "Voir l'erreur":
                    Utils.clear()
                    print(os.getcwd())
                    traceback.print_exc()
                    input("Appuyez sur une entrer pour continuer ...")
                    pass