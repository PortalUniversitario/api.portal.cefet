import json

def toJson(obj):    
    return json.loads(json.dumps(obj.__dict__, default=lambda obj: obj.__dict__))

def getNomeCampus(codCampus):
    try:
        with open('sources/campus.json', 'r', encoding="utf8") as arquivo:
            campusSrc = arquivo.read()
            campusJson = json.loads(campusSrc)
        return (campusJson[codCampus])['nome']
    except:
        return None