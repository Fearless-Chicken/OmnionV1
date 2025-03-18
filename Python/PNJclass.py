import threading, time, openai, Python.Utils as Utils

natureList = []

class PNJ:
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
        self.API_KEY = open("secret",'r',encoding="utf-8").read()
        self.client = openai.OpenAI(api_key=self.API_KEY)

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

    def chat_with_ai(self,user_input):
        # Ajouter la question du joueur
        self.HistoriqueConv.append({"role": "user", "content": user_input})
        
        # Envoyer tout l'historique à OpenAI
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=self.HistoriqueConv,
            temperature=0.7,  # proche de 0 : droit dans ses basquettes, proche de 1 : il va prendre des libertés sur la réponse, + que 1 : chaotique askip 
            max_tokens=100
        )

        # c'est la réponse du NPC
        NPCResponse = response.choices[0].message.content

        # on ajoute la réponce sur NPC
        self.HistoriqueConv.append({"role": "assistant", "content": NPCResponse})

        return NPCResponse

    def talkTo(self):
        while True:
            user_message = input("Toi : ")
            if user_message.lower() in ["quit", "exit", "stop"]:
                print("Fin de la conversation.")
                break

            start_time = time.time()
            response = self.chat_with_ai(user_message)
            end_time = time.time()

            elapsed_time = end_time - start_time

            print(f"IA : {response}")

            tokenAI = Utils.CalcToken(response)
            tokenU = Utils.CalcToken(user_message)

            self.totalToken += tokenU+tokenAI
            print(f"Temps de réponse : {elapsed_time}")
            print(f"Tokens utilisés : {tokenAI} + {tokenU} = {tokenAI+tokenU} | pour un total de : {self.totalToken}")


            