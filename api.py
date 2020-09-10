from flask import Flask, jsonify, request, send_file
import unicodedata
import os
import io
import re
import aplication as apli
import entities as ent
import helper as hel

app = Flask(__name__)
#alterado
#AUTENTICACAO------------------------------------
@app.route('/autenticacao', methods=['POST'])
def autenticacao():
    result = ent.Resultado()
    try:
        usuario = request.get_json().get('usuario')
        senha = request.get_json().get('senha')
        result = apli.Autenticacao.getSessao(usuario, senha)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))
#------------------------------------------------

#PERFIL------------------------------------------
@app.route('/perfil', methods=['GET'])
def perfil():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Perfil.getAll(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))

@app.route('/perfil/academico', methods=['GET'])
def perfilAcademico():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Perfil.getAcademico(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))

@app.route('/perfil/pessoal', methods=['GET'])
def perfilPessoal():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Perfil.getPessoal(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))

@app.route('/perfil/endereco', methods=['GET'])
def perfilEndereco():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Perfil.getEndereco(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))

@app.route('/perfil/foto', methods=['GET'])
def perfilFoto():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        result = apli.Perfil.getImagem(cookie)
        if (result.code == hel.HttpCodes.OK):
            return send_file(
                result.data,
                as_attachment=True,
                attachment_filename='imagemPerfil.jpeg',
                mimetype='image/jpeg')
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))
#------------------------------------------------

#RELATORIOS--------------------------------------
@app.route('/relatorios', methods=['GET'])
def relatorios():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Relatorio.getLista(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))

@app.route('/relatorios/pdf', methods=['GET'])
def relatoriosPdf():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        link = request.args.get('link')
        result = apli.Relatorio.getPdf(cookie, link)
        if (result.code == hel.HttpCodes.OK):
            return send_file(
                result.data,
                as_attachment=True,
                attachment_filename='relatorio.pdf',
                mimetype='application/pdf')
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))
#------------------------------------------------

#CAMPUS------------------------------------------
@app.route('/campus/<codeCampus>/foto', methods=['GET'])
def campusFoto(codeCampus):
    result = ent.Resultado()
    try:
        result = apli.Campus.getImagem(codeCampus)
        if (result.code == hel.HttpCodes.OK):
            return send_file(
                result.data,
                mimetype='image/jpeg')
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR

    return jsonify(hel.object.toJson(result))
#------------------------------------------------

#PERIODOS----------------------------------------
@app.route('/periodos', methods=['GET'])
def getPeriodo():
    result = ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Periodo.getPeriodo(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR
    
    return jsonify(hel.object.toJson(result))

@app.route('/periodos/disciplinas', methods=['GET'])
def getAllDisciplinas():
    result= ent.Resultado()
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Periodo.getAllDisciplinas(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR
    
    return jsonify(hel.object.toJson(result))

@app.route('/periodos/<codPeriodo>/disciplinas', methods=['GET'])
def getDiscByPeriodo(codPeriodo):
    result= ent.Resultado()   
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Periodo.getDiscByPeriodo(cookie, matricula,codPeriodo)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR
    
    return jsonify(hel.object.toJson(result))
#-------------------------------------------------

#TURMAS-------------------------------------------
@app.route('/turmas/<codTurma>', methods=['GET'])
def getDiscByCod(codTurma):
    result= ent.Resultado()   
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        #result = apli.Periodo.getDiscByCod(cookie, matricula, codPeriodo, codDisciplina)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR
    
    return jsonify(hel.object.toJson(result))
#-------------------------------------------------
#HORÁRIOS-----------------------------------------
@app.route('/horarios', methods=['GET'])
def getHorarios():
    result= ent.Resultado()   
    try:
        cookie = request.args.get('cookie')
        matricula = request.args.get('matricula')
        result = apli.Horarios.getHorarios(cookie, matricula)
    except:
        result.data = "Erro: Falha interna no servidor"
        result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR
    
    return jsonify(hel.object.toJson(result))
#-------------------------------------------------

#ERROR HANDLER------------------------------------
@app.errorhandler(hel.HttpCodes.NOT_FOUND)
def respond404(error):
    result = ent.Resultado()
    result.code = hel.HttpCodes.NOT_FOUND
    result.data = "NotFound"
    return jsonify(hel.object.toJson(result))

@app.errorhandler(hel.HttpCodes.BAD_REQUEST)
def respond400(error):
    result = ent.Resultado()
    result.code = hel.HttpCodes.BAD_REQUEST
    result.data = "BadRequest"
    return jsonify(hel.object.toJson(result))

@app.errorhandler(hel.HttpCodes.INTERNAL_SERVER_ERROR)
def respond500(error):
    result = ent.Resultado()
    result.code = hel.HttpCodes.INTERNAL_SERVER_ERROR
    result.data = "InternalServerError"
    return jsonify(hel.object.toJson(result))
#-----------------------------------------------


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)  # para prod, ative aqui! Para commitar
    #app.run(debug=True, host='127.0.0.1', port=port)  # para dev, ative aqui! Para testar em local host
