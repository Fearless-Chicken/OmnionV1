import os

def GetEveryFilesContent():
    with open("Total.txt","w",encoding="utf-8") as dest:
        res = ""
        root_dir = os.getcwd()  # Répertoire courant
        for root, _, files in os.walk(root_dir):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), root_dir)
                if "pycache" not in relative_path:
                    res += "path : Project\\"+relative_path
                    res += open(relative_path,"r",encoding="utf-8").read()
        dest.write(res)



