import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import  time, pick, Python.PNJclass as PNJclass, Python.Utils as Utils, ast, traceback, Python.Omnion.OmnionUtils as OmnionUtils


PNJsClasses = ast.literal_eval(open("data/roles/roleslist.dat","r",encoding="utf-8").read())
menu = ["Creer un PNJ","Menu PNJ","Reload Omnion","Créer une erreur"]
while True:
    PNJs = {}
    PNJs = OmnionUtils.CreatePNJ(PNJs,"Omnion","Omnion")
    PNJsList = []
    for pnj in PNJs.keys():
        PNJsList.append(pnj)
    choice,_=pick.pick(menu,title="Faites un choix",indicator=">")
    match choice:
        case "Creer un PNJ":
            nom = str(input("Comment s'appel t il ? :> "))
            role,_ = pick.pick(PNJsClasses,title=f"Quel est le role de {nom}",indicator=">")
            PNJs = OmnionUtils.CreatePNJ(PNJs,nom,role)
        case "Menu PNJ":
            PNJname,_=pick.pick(PNJsList+["Retour"],title="Faites un choix",indicator=">")
            if PNJname != "Retour":
                choix,_=pick.pick(["Lui parler","Le supprimer","Retour"],f"Que voulez vous faire avec {PNJname}",indicator=">")
                match choix:
                    case "Lui parler":
                        PNJs[PNJname].talkTo()
                    case "Le supprimer":
                        PNJs.pop(PNJname) 