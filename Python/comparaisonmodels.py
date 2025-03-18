import threading, time, openai, Python.Utils as Utils

class PNJ:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.lock = threading.Lock()
        self.lifeSpeed = 1
        self.totalToken = 0
        
        role = """Tu es un marchand dans un MMORPG se déroulant dans la Rome antique et où les dieux sont présents. 
                  Prends le rôle de marchand à cœur, mais n'en fais pas trop non plus. Tes réponses doivent être courtes, 
                  il faut juste que tu aies l'air assez vivant. """

        # Historique unique, mais copié pour chaque modèle
        self.HistoriqueConv = [{"role": "system", "content": role}]
        
        # Clé API depuis un fichier
        self.API_KEY = open("secret", 'r', encoding="utf-8").read()
        self.client = openai.OpenAI(api_key=self.API_KEY)
        self.client2 = openai.OpenAI(api_key=self.API_KEY)

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
        print(f"L'âge de {self.name} est de {y} années, {m} mois, {d} jours, {h} heures, {min} minutes, {sec} secondes")

    def changeLifeSpeed(self, speed):
        self.lifeSpeed = speed

    def startLife(self):
        life = threading.Thread(target=self.incrementAge, daemon=True)
        life.start()

    def chat_with_ai(self, user_input):
        # Ajouter la question du joueur à l'historique
        self.HistoriqueConv.append({"role": "user", "content": user_input})

        # Copie de l'historique pour chaque modèle
        messages1 = self.HistoriqueConv.copy()
        messages2 = self.HistoriqueConv.copy()

        # Temps de réponse pour GPT-3.5-Turbo
        start_time1 = time.time()
        response1 = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages1,
            temperature=0.7,
            max_tokens=100
        )
        end_time1 = time.time()
        time_gpt3 = end_time1 - start_time1  # Calcul du temps

        # Temps de réponse pour GPT-4o-Mini
        start_time2 = time.time()
        response2 = self.client2.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages2,
            temperature=0.7,
            max_tokens=100
        )
        end_time2 = time.time()
        time_gpt4o = end_time2 - start_time2  # Calcul du temps

        # Récupération des réponses
        NPCResponse1 = response1.choices[0].message.content
        NPCResponse2 = response2.choices[0].message.content

        # Ajouter les réponses à l'historique
        self.HistoriqueConv.append({"role": "assistant", "content": NPCResponse1})
        self.HistoriqueConv.append({"role": "assistant", "content": NPCResponse2})

        return NPCResponse1, NPCResponse2, time_gpt3, time_gpt4o

    def talkTo(self):
        while True:
            user_message = input("Toi : ")
            if user_message.lower() in ["quit", "exit", "stop"]:
                print(f"\n🔹 Fin de la conversation. Total de tokens utilisés : {self.totalToken} tokens.")
                break

            response1, response2, time_gpt3, time_gpt4o = self.chat_with_ai(user_message)

            # Affichage des réponses des deux modèles
            print("\n💬 **Réponse GPT-3.5-Turbo :**")
            print(f"🛒 {response1}\n")
            print("💬 **Réponse GPT-4o-Mini :**")
            print(f"🛍️ {response2}\n")

            # Calcul des tokens
            tokenAI1 = Utils.CalcToken(response1)
            tokenAI2 = Utils.CalcToken(response2)
            tokenU = Utils.CalcToken(user_message)

            # Ajout au total
            self.totalToken += tokenU + tokenAI1 + tokenAI2

            # Affichage des temps de réponse distincts
            print(f"⏳ Temps de réponse :")
            print(f"   - GPT-3.5-Turbo : {time_gpt3:.2f} secondes")
            print(f"   - GPT-4o-Mini   : {time_gpt4o:.2f} secondes")
            
            # Affichage des tokens
            print(f"🔢 Tokens utilisés : {tokenU} (Utilisateur) + {tokenAI1} (GPT-3.5) + {tokenAI2} (GPT-4o) = {tokenU + tokenAI1 + tokenAI2} | Total : {self.totalToken}\n")
