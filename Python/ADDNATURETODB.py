import pymysql

con = pymysql.connect(host="127.0.0.1", user="admin", password="admin", port=3306)
cur = con.cursor()
cur.execute("use omnionv1")
with open("nature.csv", 'r', encoding='utf-8') as src:
    for line in src:
        if "##" not in line:
            line = line.strip()  # Évite les espaces et \n
            values = line.split(";")  # Découpe la ligne CSV

            # Vérifie que la ligne contient bien toutes les colonnes
            if len(values) != 26:  
                print(f"Erreur : Ligne invalide -> {line}")
                continue
            
            # Requête SQL avec des placeholders (%s)
            query = '''
            INSERT INTO `npcnatures` 
            (`Nature`, `Agressivité`, `Fuite`, `Prise_d_initiative`, `Obéissance`, `Exploration`, 
            `Interaction_sociale`, `Méfiance`, `Altruisme`, `Provocation`, `Réflexion`, `Précipitation`, 
            `Attachement`, `Prise_de_risque`, `Évitement`, `Patience`, `Adaptabilité`, `Curiosité`, 
            `Loyauté`, `Coopération`, `Individualisme`, `Autonomie`, `Réactivité`, `Persévérance`, `Optimisation_ressources`, `Empathie`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            try:
                cur.execute(query, values)
                con.commit()
            except pymysql.Error as e:
                print(f"Erreur SQL : {e}")
