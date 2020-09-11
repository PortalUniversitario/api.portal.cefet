from requests import Session
from bs4 import BeautifulSoup as bs
import helper as hel
import entities as entity

def getHorarios(cookie,matricula):   
    """
    Descrição:

    Obtem lista de horários do período vigente para o usuário.
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
        lstHorarios=[]
        tabela = sitePeriodosBS.find("table", {"class": "table-turmas"})
        tbody = tabela.find("tbody")
        linhas = tbody.find_all("tr")

        for linha in linhas:
            itens = linha.find_all("td")
            horarios = entity.Horarios()
            horarios.disciplina   = trataNome(itens[0].get_text())
            horarios.codTurma     = hel.string.strNormalize(itens[2].get_text())
            horarios.segunda      = getTabelaHorarios(trataLinkHorario(itens[2].find("a")["href"]), '2', requestSession)
            horarios.terca        = getTabelaHorarios(trataLinkHorario(itens[2].find("a")["href"]), '3', requestSession)
            horarios.quarta       = getTabelaHorarios(trataLinkHorario(itens[2].find("a")["href"]), '4', requestSession)
            horarios.quinta       = getTabelaHorarios(trataLinkHorario(itens[2].find("a")["href"]), '5', requestSession)
            horarios.sexta        = getTabelaHorarios(trataLinkHorario(itens[2].find("a")["href"]), '6', requestSession)
            horarios.sabado       = getTabelaHorarios(trataLinkHorario(itens[2].find("a")["href"]), '7', requestSession)
            
            lstHorarios.append(horarios)
            
        return lstHorarios
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)


# AUX functions region
def trataNome(nome):
    try:
        nome2 = nome.split("(")
        nome3 = hel.string.strNormalize(nome2[0]).strip()
        return nome3
    except:
        return nome2
    
def trataLinkHorario(texto):
    try:
        texto2 = texto.split(",")
        link = hel.URLs.ENDPOINT + texto2[0].replace("javascript:loadDialog(", "").replace("'", "")
        return link
    except:
        return texto2

def getTabelaHorarios(link,numero, requestSession):
    try:
        siteHorarios   = requestSession.get(link)
        siteHorariosBS = bs(siteHorarios.content, "html.parser")
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        blocoHorarios  = siteHorariosBS.find("div", {"title": "Horários"})
        tabelaHorarios = blocoHorarios.find("table", {"class":"tableborder"})
        tbody  = tabelaHorarios.find("tbody")
        linhas = tbody.find_all("tr")

        for linha in linhas:
            horario = ""
            colunas = linha.find_all("td")

            if(  numero  == hel.string.strNormalize( colunas[0].get_text() )[0] ): 
                horario  += hel.string.strNormalize(colunas[1].get_text()) + " - " + hel.string.strNormalize(colunas[2].get_text())
                return horario

        return None
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

#endregion