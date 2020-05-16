from requests import Session
from bs4 import BeautifulSoup as bs
import re
import io
import helper as hel
import entities as entity

def getLista(cookie, matricula):
    """
    Descrição:

    Obtem lista de relatorios disponíveis para o usuário.
    Em caso de sucesso retorna uma lista do tipo entities.Relatorio().
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        siteRelatorios = requestSession.get(hel.URLs.RELATORIOS + matricula)
        siteRelatoriosBS = bs(siteRelatorios.content, "html.parser")
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        Relatorios = []
        RelatoriosBrutos = siteRelatoriosBS.find_all('a', {'title': 'Relatório em formato PDF'})

        for item in RelatoriosBrutos:
            relatorio = entity.Relatorio()
            relatorio.id = RelatoriosBrutos.index(item)
            relatorio.nome = hel.string.strNormalize(item.previousSibling)
            relatorio.link = item['href'].replace("/aluno/aluno/relatorio/", '')
            Relatorios.append(relatorio)

        return Relatorios
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

def getFilePdf(cookie, link):
    """
    Descrição:
    Obtem arquivo pdf.
    Em caso de sucesso retorna um objeto do tipo File.
    """
    try:
        print(hel.URLs.RELATORIO + link)
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        pdf_data = requestSession.get(hel.URLs.RELATORIO + link).content  
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    try:
        pdf = io.BytesIO()
        pdf.write(pdf_data)
        pdf.seek(0)

        return pdf
    except:
        raise ValueError("Falha ao baixar Pdf", hel.HttpCodes.NOT_ACCEPTABLE)
