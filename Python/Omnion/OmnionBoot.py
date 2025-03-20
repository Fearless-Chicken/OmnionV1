import os, random as r, time, sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def Boot():
    spin = ["|", "/", "-", "\\"]
    done = []

    phrases = [
        "🔄 Booting Omnion... Establishing cognitive link.",
        "🖥️ System Initialization... Synchronizing neural pathways.",
        "⚙️ Activating Omnion Core... Preparing interactive environment.",
        "🌐 AI Network Online... Optimizing response algorithms.",
        "📀 Loading Memory Modules... Context adaptation in progress."
    ]

    for phrase in phrases:
        i, l = 0, 0
        loading_speed = r.randint(5, 15)  # Charge plus progressivement

        while i < 100:
            clear()
            for item in done:
                print(f"\033[92m✔ {item} 100%\033[0m")  # ✅ Ajoute du vert une fois chargé
            
            dots = "." * ((i // 20) % 4)  # ⚡ Animation fluide des points "..."
            sys.stdout.write(f"\r{spin[l]} {phrase} {dots} {i}%")
            sys.stdout.flush()

            i += r.randint(loading_speed - 3, loading_speed + 5)  # ⚡ Variations naturelles
            l = (l + 1) % 4
            time.sleep(0.08)  # 💡 Un peu plus lent pour plus d'effet

        done.append(phrase)

    clear()
    print("\033[92m✔ Omnion is now online. Ready for interaction.\033[0m")  # 🔥 Message final stylé
    time.sleep(1)

