def Boot():
    import os, random as r, time

    def clear():
        os.system("cls")

    spin = ["|","/","-","\\"]
    done = []


    phrases = [
        "Booting Omnion... Establishing cognitive link.",
        "System Initialization... Synchronizing neural pathways.",
        "Activating Omnion Core... Preparing interactive environment.",
        "AI Network Online... Optimizing response algorithms.",
        "Loading Memory Modules... Context adaptation in progress."
    ]

    for phrase in phrases:
        i = 0
        l = 0
        while i < 100:
            clear()
            for item in done:
                print(f"{item} 100%")
            print(f"{spin[l]} {phrase} {'.' * l} {i}%")
            i += r.randint(0,15) if r.randint(1,2) != 1 else r.randint(15,25)
            l += 1
            time.sleep(0.05)
            if l == 4: l = 0
        done.append(phrase)