import sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading, time, openai, Utils, json, OmnionUtils

natureList = []

class Omnion:
    def __init__(self, name:str, role:str):
        self.name = name
        self.age = 0
        self.lock = threading.Lock()
        self.lifeSpeed = 1
        self.totalToken = 0
        roleDesc = Utils.GetRole(role)
        self.HistoriqueConv = [
                                {"role": "system", "content": roleDesc}
                              ]
        self.API_KEY = open(".env",'r',encoding="utf-8").read()
        self.client = openai.OpenAI(api_key=self.API_KEY)
        self.oldFileName = ""
        self.newFileName = ""
        self.debug = True

    def incrementAge(self):
        while True:
            with self.lock:
                self.age += self.lifeSpeed
            time.sleep(1)

    def printAge(self):
        sec = self.age
        y, sec = divmod(sec, 31536000)  # 1 an = 31 536 000 sec
        m, sec = divmod(sec, 2592000)   # 1 mois = 2 592 000 sec 
        d, sec = divmod(sec, 86400)     # 1 jour = 86 400 sec
        h, sec = divmod(sec, 3600)      # 1 heure = 3 600 sec
        min, sec = divmod(sec, 60)      # 1 minute = 60 sec
        print(f"l'age de {self.name} est de {y} années, {m} mois, {d} jours, {h} heures, {min} minutes, {sec} secondes")

    def changeLifeSpeed(self,speed):
        '''Voir tableau annexe'''
        self.lifeSpeed = speed

    def startLife(self):
        life = threading.Thread(target=self.incrementAge, daemon=True)
        life.start()

    def chat_with_ai(self,user_input,model:str):
        # Ajouter la question du joueur
        self.HistoriqueConv.append({"role": "user", "content": user_input})
        
        # Envoyer tout l'historique à OpenAI
        response = self.client.chat.completions.create(
            model=model,
            messages=self.HistoriqueConv,
            temperature=0.7,  # proche de 0 : droit dans ses basquettes, proche de 1 : il va prendre des libertés sur la réponse, + que 1 : chaotique askip 
            max_tokens=100
        )

        # c'est la réponse du NPC
        NPCResponse = response.choices[0].message.content

        # on ajoute la réponce sur NPC
        self.HistoriqueConv.append({"role": "assistant", "content": NPCResponse})

        ## On transfome le str() rendu par Omnion en dict() pour interprétation
        try:
            NPCResponse = json.loads(NPCResponse)
            if self.debug:print("loaded")
        except json.decoder.JSONDecodeError:
            NPCResponse = NPCResponse
            if self.debug:print("not loaded")

        return NPCResponse

    def talkTo(self):
        os.system("cls")

        ## Méssage de bienvenu (va changer pour une BDD de message selectionné au hasard)
        self.bvn()
        
        while True:
            ## On récupère la commande du GM
            userPrompt = input("> ")

            if userPrompt.lower().strip() != "":
                # Vérifie si l'utilisateur veut quitter
                if userPrompt.lower() in ["quit", "exit", "stop"]:
                    print("Fin de la conversation.")
                    break
                
                # Vérifie si l'utilisateur veut recharger le programme
                elif userPrompt.lower() == "reload":
                    Utils.reload()

                else:
                    ## Calcul du temps de réponse + récupération de la réponse d'Omnion
                    start_time = time.time()
                    jsonIA = self.chat_with_ai(userPrompt,"gpt-4-turbo")
                    end_time = time.time()
                    elapsed_time = end_time - start_time

                    
                    
                    ## Réponse de l'IA
                    print("Le json rendu par l'IA")
                    input(jsonIA)

                    ## Fonction qui se charge d'interpretter la réponse
                    self.printResponse(jsonIA,userPrompt)
                    
                    ## Calcul des tokens utilisés
                    tokenAI = Utils.CalcToken(jsonIA)
                    tokenU = Utils.CalcToken(userPrompt)
                    self.totalToken += tokenU + tokenAI

                    ## Print des tokens utilisés et du temps de réponse 
                    if self.debug:
                        print(f"Temps de réponse : {elapsed_time}")
                        print(f"Tokens utilisés : {tokenAI} + {tokenU} = {tokenAI+tokenU} | pour un total de : {self.totalToken}")


    def createFile(self,jsonIA):
        import os
        with open(f"{jsonIA['filename']}",'w',encoding='utf-8') as dest:
            dest.write(jsonIA["content"])
        if jsonIA["exec"] == "True":os.system(f"python3.10.exe {jsonIA['filename']}")


    def modifieOwnCode(self,content:str,originalUserPrompt):   
        OwnContent = open("Python/OmnionClass.py","r",encoding="utf-8").read()
        OmnionUtils.bkpFile("Python/OmnionClass.py",originalUserPrompt)
        prompt = "Tu est passer en mode changeOwnCode, le contenu de ton fichier sera cité ci dessous et le prompt (ce qu'il faut changer dans le fichier) que tu as générer toi même est : "+content+"\n\n\ncontenu du fichier :\n"+OwnContent+"tu rendras donc un json du code COMPLET et MODIFIER et le 'comm' sera les changements effectués"
        response = self.chat_with_ai(prompt,"gpt-4o-mini")
        input(response)
        self.createFile(response)

    def printResponse(self,jsonIA,userPrompt):
        match jsonIA["func"]:
            case "NormalTalk":
                print(f"\n{self.name} : {jsonIA['content']}\n")


            case "CreateFile":
                self.createFile(jsonIA)

            
            case "executeCode":
                # input(jsonIA["content"])
                result = OmnionUtils.execCode(jsonIA["content"])
                prompt = "la réponse est : "+result+"\nrédige moi une réponse pertinente"
                reponse = self.chat_with_ai(prompt,"gpt-4-turbo")
                self.printResponse(reponse,prompt)


            case "ToggleDebug":
                self.debug = jsonIA["content"]
                

            case "changeOwnCode":
                self.modifieOwnCode(jsonIA["content"],userPrompt)

                
            case other:
                print(f"{self.name} : {jsonIA}")
    
    def bvn(self):
        from random import randint
        src = open("data/dialogues/AllWelcomeMessages.dat","r",encoding="utf-8").read()

        print(src.split("\n")[randint(0,len(src.split("\n"))-1)])

        