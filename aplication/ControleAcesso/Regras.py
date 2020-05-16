import infraestructure as infra
import json
import entities as enti
import helper as hel

def Usuario(matricula):
    if (not getRestricoes('matricula', matricula)):
        return "Matricula Sem Acesso ao Sistema"
    return None

def Perfil(academico):
    if (not getRestricoes('campus', hel.string.strNormalize(academico.codCampus))):
        return "Campus Sem Acesso ao Sistema"
    if (not getRestricoes('curso', hel.string.strNormalize(academico.curso))):
        return "Curso Sem Acesso ao Sistema"
    return None

def cookieValido(cookie):
    return infra.Autenticacao.getCookieStatus(cookie)

def getRestricoes(itemType, dado):
    with open('aplication/ControleAcesso/restricoes.json', 'r') as arquivo:
        restricoes = arquivo.read()
    restricoesJson = json.loads(restricoes)
    try:
        validList = (restricoesJson[itemType])['valid']
        invalidList = (restricoesJson[itemType])['invalid']
    except:
        return True
    if (invalidList != None):
        if ("*" in invalidList) or (dado in invalidList):
            return False
    if (validList != None):
        if ("*" in validList) or (dado in validList):
            return True

    return False
        
     