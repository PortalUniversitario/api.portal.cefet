import helper as hel
from requests import Session
import entities as entity
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


def getNoticias(campus):
    """
    Descrição:
    Obtem url de noticias do campus indicado.
    Em caso de sucesso retorna um objeto do tipo String.
    """
    try:
        with open('sources/campus.json', 'r', encoding="utf8") as arquivo:
            campusSrc = arquivo.read()
            campusJson = json.loads(campusSrc)

        rss = (campusJson[campus])['rss']

        requestSession = Session()
        noticias_json = requestSession.get(rss).content

        lstNoticias = []

        NoticiasJson = json.loads(noticias_json)
        print(NoticiasJson)

        for item in NoticiasJson['items']:
            noticia = entity.Noticias()
            noticia.link = item['link']
            noticia.title = item['title']
            noticia.pubDate = item['pubDate']
            noticia.thumbnail = item['thumbnail']
            lstNoticias.append(noticia)
        return lstNoticias
    except:
        raise ValueError("Falha ao obter RSS", hel.HttpCodes.NOT_ACCEPTABLE)




