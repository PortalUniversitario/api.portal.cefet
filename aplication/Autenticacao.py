import infraestructure as infra
from aplication.ControleAcesso import Regras
import entities as endi
import helper as hel

def getSessao(usuario, senha):
    """
    Descrição:

    Obtem nova sessão a partir das credenciais passadas.
    Retorna um objeto do tipo entities.Resultado().
    """
    try:
        result = endi.Resultado()
        sessao = infra.Autenticacao.postAutenticacao(usuario, senha)
        rule = Regras.Usuario(usuario)
        if (rule == None):
            #TODO: Encontrar maneira melhor de fazer bloqueios internos
            academico = infra.Perfil.getDadosAcademicos(sessao.cookie, sessao.matricula)
            rule = Regras.Perfil(academico)
            if (rule == None):
                result.data = sessao
                result.code = hel.HttpCodes.OK
            else:
               result.data = rule
               result.code = hel.HttpCodes.LOCKED
        else:
            result.data = rule
            result.code = hel.HttpCodes.LOCKED
    except ValueError as erro:
        result.data = erro.args.__getitem__(0)
        result.code = erro.args.__getitem__(1)

    return result

def cookieValido(cookie):
    """
    DESCONTINUADO
    """
    return infra.Autenticacao.getCookieStatus(cookie)