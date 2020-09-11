import infraestructure as infra
import entities as endi
import helper as hel

def getHorarios(cookie,matricula):
    """
    Descrição:

    Obtem uma lista com os horários do período vigente.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Horarios.getHorarios(cookie, matricula)
        result.code = hel.HttpCodes.OK   
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)
        
    return result
