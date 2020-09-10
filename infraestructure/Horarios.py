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
        Horarios=[]
        sitePeriodosBS= BeautifulSoup(html, 'html.parser')
        tabela = sitePeriodosBS.find("table", {"class": "table-turmas"})
        tbody = tabela.find("tbody")
        linhas = tbody.find_all("tr")
        for linha in linhas:
            itens = linha.find_all("td")
            horarios = entity.Horarios()
            horarios.disciplina   = trataNome(itens[0].get_text())
            horarios.codTurma     = strNormalize(itens[2].get_text())
            horarios.segunda      = getTabelaHorarios(TrataLinkHorario(itens[2].find("a")["href"]), '2', requestSession)
            horarios.terca        = getTabelaHorarios(TrataLinkHorario(itens[2].find("a")["href"]), '3', requestSession)
            horarios.quarta       = getTabelaHorarios(TrataLinkHorario(itens[2].find("a")["href"]), '4', requestSession)
            horarios.quinta       = getTabelaHorarios(TrataLinkHorario(itens[2].find("a")["href"]), '5', requestSession)
            horarios.sexta        = getTabelaHorarios(TrataLinkHorario(itens[2].find("a")["href"]), '6', requestSession)
            horarios.sabado       = getTabelaHorarios(TrataLinkHorario(itens[2].find("a")["href"]), '7', requestSession)
            #Sabado pode dar erro, pode ser que nao usem o 7 para sábado
            
            Horarios.append(horarios)
            
        return Horarios
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)


# AUX functions region
def trataNome(nome):
    try:
        nome2 = nome.split("(")
        nome3 = strNormalize(nome2[0]).strip()
        return nome3
    except:
        return texto2
    
def trataLinkHorario(texto):
    try:
        texto2 = texto.split(",")
        link = hel.URLs.ENDPOINT + texto2[0].replace("javascript:loadDialog(", "").replace("'", "")
        return link
    except:
        return texto2

def getTabelaHorarios(link,numero, requestSession):  #Falta pôr RequestSession e link como parâmetros
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
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
            colunas = linha.find_all("td") 
            
            if(  numero  == strNormalize( colunas[0].get_text() )[0] ): 
                horario  += strNormalize(colunas[1].get_text()) + " - " + strNormalize(colunas[2].get_text())
                
            elif( numero == strNormalize( colunas[0].get_text() )[0] ): 
                horario  += strNormalize(colunas[1].get_text()) + " - " + strNormalize(colunas[2].get_text()) 
                    
            elif( numero == strNormalize( colunas[0].get_text() )[0] ): 
                horario  += strNormalize(colunas[1].get_text()) + " - " + strNormalize(colunas[2].get_text())
                
            elif( numero == strNormalize( colunas[0].get_text() )[0] ): 
                horario  += strNormalize(colunas[1].get_text()) + " - " + strNormalize(colunas[2].get_text())
                
            elif( numero == strNormalize( colunas[0].get_text() )[0] ): 
                horario  += strNormalize(colunas[1].get_text()) + " - " + strNormalize(colunas[2].get_text())
            else:
                return None
            
            return horario
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

#endregion