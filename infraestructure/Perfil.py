from requests import Session
from bs4 import BeautifulSoup as bs
import re
import io
import helper as hel
import entities as entity

def getDadosAcademicos(cookie, matricula):
    """
    Descrição:

    Obtem dados academicos.
    Em caso de sucesso retorna um objeto do tipo entities.Academico().
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)

        siteHorarios = requestSession.get(hel.URLs.HORARIOS + matricula)
        sitePerfil = requestSession.get(hel.URLs.PERFIL)
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        #academico = entity.Academico()
        #academico.matricula     = pegaPropriedadePerfil(siteHorarios.content, '.Matrícula:')
        #academico.periodoAtual  = pegaPropriedadePerfil(siteHorarios.content, '.Período Atual:')
        #academico.nome          = pegaPropriedadePerfil(sitePerfil.content, '.Nome')
        
        #CampusCurso             = trataCampusCurso(pegaPropriedadePerfil(siteHorarios.content, '.Curso:'))
        #academico.codCampus     = CampusCurso[0]
        #academico.curso         = CampusCurso[1]
        #academico.campus        = hel.object.getNomeCampus(academico.codCampus)
        
        #if (academico.matricula == None):
        #    raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)
        
        #TODO: remover dados mokados

        academico = entity.Academico()
        academico.matricula     = 12345
        academico.periodoAtual  = 6
        academico.nome          = 'DANIEL VEIGA DA SILVA ANTUNES'
        academico.codCampus     = 'PET'
        academico.curso         = 'ENGENHARIA DE COMPUTACAO'
        academico.campus        = 'PETROPOLIS'

        return academico
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

def getDadosPessoais (cookie, matricula):
    """
    Descrição:

    Obtem dados pessoais.
    Em caso de sucesso retorna um objeto do tipo entities.Pessoal().
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)

        sitePerfil = requestSession.get(hel.URLs.PERFIL)
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    
    try:
        pessoal = entity.Pessoal()
        pessoal.nome            = pegaPropriedadePerfil(sitePerfil.content, '.Nome')
        pessoal.nomeMae         = pegaPropriedadePerfil(sitePerfil.content, '.Nome da Mãe')
        pessoal.nomePai         = pegaPropriedadePerfil(sitePerfil.content, '.Nome da Pai')
        pessoal.nascimento      = pegaPropriedadePerfil(sitePerfil.content, '.Nascimento')
        pessoal.sexo            = pegaPropriedadePerfil(sitePerfil.content, '.Sexo')
        pessoal.etnia           = pegaPropriedadePerfil(sitePerfil.content, '.Etnia')
        pessoal.deficiencia     = pegaPropriedadePerfil(sitePerfil.content, '.Deficiência')
        pessoal.tipoSanguineo   = pegaPropriedadePerfil(sitePerfil.content, '.Tipo Sanguíneo')
        pessoal.fatorRH         = pegaPropriedadePerfil(sitePerfil.content, '.Fator RH')
        pessoal.estadoCivil     = pegaPropriedadePerfil(sitePerfil.content, '.Estado Civil')
        pessoal.paginaPessoal   = pegaPropriedadePerfil(sitePerfil.content, '.Página Pessoal')
        pessoal.nacionalidade   = pegaPropriedadePerfil(sitePerfil.content, '.Nacionalidade')
        #TODO: consertar bug, Estado obtem Estado Civil
        pessoal.estado          = pegaPropriedadePerfil(sitePerfil.content, '.Estado')
        pessoal.naturalidade    = pegaPropriedadePerfil(sitePerfil.content, '.Naturalidade')

        if (pessoal.nome == None):
            raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

        return pessoal
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

def getDadosEndereco (cookie, matricula):
    """
    Descrição:
    Obtem dados de endereco.
    Em caso de sucesso retorna um objeto do tipo entities.Endereco().
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        sitePerfil = requestSession.get(hel.URLs.PERFIL)
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)

    try:
        endereco = entity.Endereco()
        endereco.tipoEndereco   = pegaPropriedadePerfil(sitePerfil.content, '.Tipo de endereço')
        endereco.tipoLogradouro = pegaPropriedadePerfil(sitePerfil.content, '.Tipo de logradouro')
        endereco.logradouro     = pegaPropriedadePerfil(sitePerfil.content, '.Logradouro')
        #TODO: consertar bug, Numero não é encontrado
        endereco.numero         = pegaPropriedadePerfil(sitePerfil.content, '.Número')
        endereco.complemento    = pegaPropriedadePerfil(sitePerfil.content, '.Complemento')
        endereco.bairro         = pegaPropriedadePerfil(sitePerfil.content, '.Bairro')
        endereco.pais           = pegaPropriedadePerfil(sitePerfil.content, '.País')
        #TODO: consertar bug, Estado obtem Estado Civil
        endereco.estado         = pegaPropriedadePerfil(sitePerfil.content, '.Estado')
        endereco.cidade         = pegaPropriedadePerfil(sitePerfil.content, '.Cidade')
        endereco.distrito       = pegaPropriedadePerfil(sitePerfil.content, '.Distrito')
        endereco.cep            = pegaPropriedadePerfil(sitePerfil.content, '.CEP')
        endereco.caixaPostal    = pegaPropriedadePerfil(sitePerfil.content, '.Caixa Postal')
        endereco.email          = pegaPropriedadePerfil(sitePerfil.content, '.E-mail')
        endereco.telResidencial = pegaPropriedadePerfil(sitePerfil.content, '.Tel. Residencial')
        endereco.telCelular     = pegaPropriedadePerfil(sitePerfil.content, '.Tel. Celular')
        endereco.telComercial   = pegaPropriedadePerfil(sitePerfil.content, '.Tel. Comercial')
        endereco.fax            = pegaPropriedadePerfil(sitePerfil.content, '.Fax')

        if (endereco.cidade == None):
            raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)
        
        return endereco
    except:
        raise ValueError("Cookie ou Matrícula Inválidos", hel.HttpCodes.NOT_ACCEPTABLE)

def getFileFoto(cookie):
    """
    Descrição:
    Obtem foto de perfil.
    Em caso de sucesso retorna um objeto do tipo File.
    """
    try:
        requestSession = Session()
        requestSession.cookies.set("JSESSIONID", cookie)
        img_data = requestSession.get(hel.URLs.PERFIL_FOTO).content        
    except:
        raise ValueError("Falha ao acessar portal do aluno", hel.HttpCodes.REQUEST_TIMEOUT)
    try:
        img = io.BytesIO()
        img.write(img_data)
        img.seek(0)
        return img
    except:
        raise ValueError("Falha ao baixar Imagem", hel.HttpCodes.NOT_ACCEPTABLE)
    
#region FUNCOES AUX 
def pegaPropriedadePerfil(conteudoHTML, propriedade):
    try:
        sitePerfilBS = bs(conteudoHTML, "html.parser")
        bloco = sitePerfilBS.find('span', text = re.compile(propriedade)).find_parent('td')
        objetoIgnorado = bloco.find('span')
        objetoIgnorado.extract()
        return hel.string.strNormalize(bloco.get_text())
    except:
        return None

def trataCampusCurso(CampusCurso):
    CampusCurso = str(CampusCurso).split('-')
    CampusCurso[0] = hel.string.strNormalize(CampusCurso[0])
    CampusCurso[1] = hel.string.strNormalize(str(CampusCurso[1]).replace("CURSO DE", ""))
    return CampusCurso
#endregion