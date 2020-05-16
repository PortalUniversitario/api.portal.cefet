import infraestructure as infra
import entities as endi
import helper as hel

def getLista(cookie, matricula):
    """
    Descrição:

    Obtem lista de relatorios.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Relatorio.getLista(cookie, matricula)
        result.code = hel.HttpCodes.OK    
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def getPdf(cookie, link):
    """
    Descrição:

    Obtem arquivo de relatorio.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Relatorio.getFilePdf(cookie, link)
        result.code = hel.HttpCodes.OK
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result