from requests import Session
from bs4 import BeautifulSoup as bs
#import re
import helper as hel
import entities as entity

def getPeriodo(cookie, matricula):
    """
    Descrição:

    Obtem lista de periodos para o usuário.
    Em caso de sucesso retorna uma lista do tipo entities.Periodo().
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        sitePeriodos = requestSession.get(hel.URLs.PERIODO + matricula)
        sitePeriodosBS = bs(sitePeriodos.content, "html.parser")
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        Periodos=[]
        for item in sitePeriodosBS.find_all('a', class_= "accordionTurma"):
            a = ""
            a = hel.string.strNormalize(item.string)
            periodo = entity.Periodo()
            periodo.cod = a[13:] + "." + a[:1]
            Periodos.append(periodo)
        return Periodos
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)
    
def getAllDisciplinas(cookie,matricula):
    """
    Descrição:

    Obtem lista de todas as disciplinas para o usuário.
    Em caso de sucesso retorna uma lista do tipo entities.Disciplina().
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        sitePeriodos = requestSession.get(hel.URLs.PERIODO + matricula)
        sitePeriodosBS = bs(sitePeriodos.content, "html.parser")
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        Disciplinas=[]

        tabelas = sitePeriodosBS.find_all("table", {"class": "table-turmas"})
        for tabela in tabelas:
            tbody = tabela.find("tbody")
            linhas = tbody.find_all("tr")
            for linha in linhas:
                itens = linha.find_all("td")
                if (len(itens) >= 3):
                    disciplina= entity.Disciplina()
                    nome, cod = trataDisciplina(itens[0].get_text())
                    disciplina.nome          = nome
                    disciplina.codDisciplina = cod
                    disciplina.situacao      = hel.string.strNormalize(itens[1].get_text())
                    disciplina.codTurma      = hel.string.strNormalize(itens[2].get_text())
                    Disciplinas.append(disciplina)
                
        return Disciplinas
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)
    
def getDiscByPeriodo(cookie,matricula,codPeriodo):
    """
    Descrição:

    Resulta em uma lista de disciplinas por período para o usuário.
    Em caso de sucesso retorna uma lista do tipo entities.Disciplina().
    """
    
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        sitePeriodos = requestSession.get(hel.URLs.PERIODO + matricula)
        sitePeriodosBS = bs(sitePeriodos.content, "html.parser")
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        Disciplinas=[]
        Periodos=getPeriodo(cookie,matricula)
        for i in range(len(Periodos)):
            if (Periodos[i].cod == codPeriodo):
                tabelas = sitePeriodosBS.find_all("table", {"class": "table-turmas"})
                tbody = tabelas[i].find("tbody")
                linhas = tbody.find_all("tr")
                for linha in linhas:
                    itens = linha.find_all("td")
                    if (len(itens) >= 3):
                        disciplina= entity.Disciplina()
                        nome, cod = trataDisciplina(itens[0].get_text())
                        disciplina.nome          = nome
                        disciplina.codDisciplina = cod
                        disciplina.situacao      = hel.string.strNormalize(itens[1].get_text())
                        disciplina.codTurma      = hel.string.strNormalize(itens[2].get_text())
                
                        Disciplinas.append(disciplina)
        return Disciplinas
            
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)
    
    
#region FUNCOES AUX 
def trataDisciplina(texto):
    try:
        texto2 = texto.split("(")
        nome = hel.string.strNormalize(texto2[0]).strip()
        cod  = hel.string.strNormalize(texto2[1]).replace(")","").strip()
        return nome, cod
    except:
        return texto2, texto2
#endregion
