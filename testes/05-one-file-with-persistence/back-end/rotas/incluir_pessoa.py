from config.configuracoes import *
from modelo.pessoa import *

@app.route("/listar_pessoas")
def listar_pessoas():
    try:
        # obter as pessoas
        lista = db.session.query(Pessoa).all()
        # converter pessoas pra json
        lista_retorno = [x.json() for x in lista]
        # preparar uma parte da resposta: resultado ok
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        # retornar a lista de pessoas json, com resultado ok
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})