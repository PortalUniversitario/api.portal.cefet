import infraestructure as infra
import entities as endi
import helper as hel

def getAll(cookie, matricula):
    """
    Descrição:

    Obtem todos os dados de perfil.
    Retorna um objeto do tipo entities.Resultado().
    """
    perfil = endi.Perfil()
    result = endi.Resultado()
    try:
        perfil.academico = infra.Perfil.getDadosAcademicos(cookie, matricula)
        perfil.pessoal = infra.Perfil.getDadosPessoais(cookie, matricula)
        perfil.endereco = infra.Perfil.getDadosEndereco(cookie, matricula)

        result.data = perfil
        result.code = hel.HttpCodes.OK    
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def getAcademico(cookie, matricula):
    """
    Descrição:

    Obtem dados acadêmicos de perfil.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Perfil.getDadosAcademicos(cookie, matricula)
        result.code = hel.HttpCodes.OK    
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def getPessoal(cookie, matricula):
    """
    Descrição:

    Obtem dados pessoais de perfil.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Perfil.getDadosPessoais(cookie, matricula)
        result.code = hel.HttpCodes.OK    
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def getEndereco(cookie, matricula):
    """
    Descrição:

    Obtem dados de endereço de perfil.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Perfil.getDadosEndereco(cookie, matricula)
        result.code = hel.HttpCodes.OK    
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def getImagem(cookie):
    """
    Descrição:

    Obtem foto de perfil.
    Retorna um objeto do tipo entities.Resultado().
    """
    result = endi.Resultado()
    try:
        result.data = infra.Perfil.getFileFoto(cookie)
        result.code = hel.HttpCodes.OK
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result