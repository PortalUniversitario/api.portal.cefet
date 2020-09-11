import infraestructure as infra
import entities as endi
import helper as hel

def getImagem(campus):
    """
    Descrição:

    Obtem foto do campus indicado.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Campus.getFileFoto(campus)
        result.code = hel.HttpCodes.OK
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def getNoticias(campus):
    """
    Descrição:

    Obtem a url da noticias do campus indicado.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Campus.getNoticias(campus)
        result.code = hel.HttpCodes.OK
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result