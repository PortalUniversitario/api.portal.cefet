import infraestructure as infra
import entities as endi
import helper as hel

def getPeriodo(cookie,matricula):
    """
    Descrição:

    Obtem lista de periodos.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Periodo.getPeriodo(cookie, matricula)
        result.code = hel.HttpCodes.OK   
    except ValueError as erro:    #O que é isso?
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)
        
    return result

def getAllDisciplinas(cookie,matricula):
    """
    Descrição:

    Obtem lista de todas as disciplinas cursadas.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Periodo.getAllDisciplinas(cookie, matricula)
        result.code = hel.HttpCodes.OK  
    except ValueError as erro:   
        result.data = erro.args.__getitem__(0) # Esse erro ta fazendo referencia ao erro handler da api? 404 e 400?
        result.code = erro.args.__getitem__(1)
        
    return result

def getDiscByPeriodo(cookie,matricula):
    """
    Descrição:

    Obtem lista de disciplinas de determinado periodo.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Periodo.getDiscByPeriodo(cookie, matricula)
        result.code = hel.HttpCodes.OK  
    except ValueError as erro:   
        result.data = erro.args.__getitem__(0) 
        result.code = erro.args.__getitem__(1)
        
    return result