import helper as hel
import json
import io

def getFileFoto(campus):
    """
    Descrição:
    Obtem foto do campus indicado.
    Em caso de sucesso retorna um objeto do tipo File.
    """
    try:
        with open('sources/campus.json', 'r', encoding="utf8") as arquivo:
            campusSrc = arquivo.read()
            campusJson = json.loads(campusSrc)
        
        return (campusJson[campus])['img']
    except:
        raise ValueError("Falha ao baixar Imagem", hel.HttpCodes.NOT_ACCEPTABLE)