import Python.PNJclass as PNJclass
import Python.IAGeneratorClass as IAGeneratorClass
import Python.OmnionClass as OmnionClass
    
def CreatePNJ(PNJs:dict,nom:str,role:str)->dict:
    if role == "generator":
        _ = IAGeneratorClass.IAGenerator(nom,role)
    elif role == "Omnion":
        _ = OmnionClass.Omnion(nom,role)
    else:
        _ = PNJclass.PNJ(nom,role)
    _.startLife()
    _.changeLifeSpeed(10000000)
    PNJs[nom] = _
    return PNJs

def execCode(code):
    import subprocess

    result = subprocess.run(["powershell", "-Command", code], capture_output=True, text=True, shell=True)
    return result.stdout.strip() if result.stdout else result.stderr.strip()
