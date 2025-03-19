import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading, time, pick, PNJclass as PNJclass, Utils as Utils, ast, traceback, OmnionUtils

os.chdir("../..")

global tempsEcoulé
tempsEcoulé = 0
lock = threading.Lock()  

def goOn():
    global tempsEcoulé
    while True:
        with lock:  
            tempsEcoulé += 1
        time.sleep(1)

if __name__ == '__main__':
    try:
        PNJs = {}
        PNJs = OmnionUtils.CreatePNJ(PNJs,"Omnion","Omnion")
        PNJs["Omnion"].talkTo()
        
        # PNJsClasses = ast.literal_eval(open("data/roles/roleslist.dat","r",encoding="utf-8").read())
        # menu = ["Creer un PNJ","Menu PNJ","Reload Omnion","Créer une erreur"]
        # while True:
        #     PNJs = {}
        #     PNJs = OmnionUtils.CreatePNJ(PNJs,"Omnion","Omnion")
        #     PNJsList = []
        #     for pnj in PNJs.keys():
        #         PNJsList.append(pnj)
        #     choice,_=pick.pick(menu,title="Faites un choix",indicator=">")
        #     match choice:
        #         case "Creer un PNJ":
        #             nom = str(input("Comment s'appel t il ? :> "))
        #             role,_ = pick.pick(PNJsClasses,title=f"Quel est le role de {nom}",indicator=">")
        #             PNJs = OmnionUtils.CreatePNJ(PNJs,nom,role)
        #         case "Menu PNJ":
        #             PNJname,_=pick.pick(PNJsList+["Retour"],title="Faites un choix",indicator=">")
        #             if PNJname != "Retour":
        #                 choix,_=pick.pick(["Lui parler","Le supprimer","Retour"],f"Que voulez vous faire avec {PNJname}",indicator=">")
        #                 match choix:
        #                     case "Lui parler":
        #                         PNJs[PNJname].talkTo()
        #                     case "Le supprimer":
        #                         PNJs.pop(PNJname)
        #         case "Reload Omnion":
        #             Utils.reload()
            
        #         case "Créer une erreur":
        #             print(0/0)
            
            # PNJs = UtiOmnionUtilsls.CreatePNJ(PNJs,"Omnion","generator")
            # time.sleep(10)
            # PNJs = OmnionUtils.CreatePNJ(PNJs,"Samantha")
            
            # temps = threading.Thread(target=goOn, daemon=True)
            # temps.start()

            # PNJs["Omnion"].talkTo()
            
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