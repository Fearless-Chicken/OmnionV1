import threading, time
global tempsEcoulé
tempsEcoulé = 0
lock = threading.Lock()  

def Life():
    global tempsEcoulé
    while True:
        with lock:  
            tempsEcoulé += 1
        time.sleep(1)
temps = threading.Thread(target=Life, daemon=True)
temps.start()