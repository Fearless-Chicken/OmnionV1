import os
import datetime

def log_message(log):
    # Obtenir la date et l'heure actuelles
    today = datetime.date.today().strftime("%Y-%m-%d")  # Format: YYYY-MM-DD
    current_hour = datetime.datetime.now().strftime("%H")  # Format: HH
    
    # Définir le chemin du fichier de log
    log_dir = f"./log/{today}/{current_hour}/"
    
    # Créer les dossiers si ils n'existent pas
    os.makedirs(log_dir, exist_ok=True)
    
    # Définir le chemin du fichier de log (utilisation du jour comme nom de fichier)
    log_file = os.path.join(log_dir, f"{today}.log")
    
    # Écrire le message dans le fichier
    with open(log_file, "a",encoding="utf-8") as f:
        # Ajoute un timestamp à chaque log
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp} - {log}\n")

# Exemple d'utilisation
log_message("Ceci est un test de log.")
