from requests import Session
from bs4 import BeautifulSoup as bs
from helper import URLs, HttpCodes
import entities as entity

def postAutenticacao(usuario, senha):
    """
    Descrição:

    Envia credenciais para validação no portal.
    Em caso de sucesso retorna um objeto do tipo entities.Sessao().
    """
    try:
        requestSession = Session()
        
        #TODO: Melhorar forma de acesso a AUTENTICACAO
        #Tratamento para evitar redirecionamento automático ao acessar login 
        requestSession.headers.update({'referer': URLs.MATRICULA})
        requestSession.get(URLs.LOGIN)
        
        body = {"j_username": usuario, "j_password": senha}
        response = requestSession.post(URLs.AUTENTICACAO, data=body)
        requestBS = bs(response.content, "html.parser")
    except:
        raise ValueError("Falha ao acessar portal do aluno", HttpCodes.REQUEST_TIMEOUT)
    
    try:
        #TODO: Melhorar tratamento de login inválido
        sessao = entity.Sessao()
        sessao.matricula = requestBS.find("input", id="matricula")["value"]
        sessao.cookie = (requestSession.cookies.get_dict()['JSESSIONID'])
        return sessao
    except:
        raise ValueError("Usuário ou Senha incorretos", HttpCodes.NOT_ACCEPTABLE)

def getCookieStatus(cookie):
    """
    DESCONTINUADA
    """
    sessao = Session()
    sessao.cookies.set("JSESSIONID", cookie)
    sessao.headers.update({'referer': URLs.MATRICULA})

    acesso = sessao.get(URLs.PRINCIPAL, allow_redirects=False)

    if (acesso.status_code == 302):
        return False
    else:
        return True