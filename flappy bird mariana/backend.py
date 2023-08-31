# importações
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from config import *
from modelo import *

# rota para retornar os fases
@app.route("/")
def ola():
    return "backend operante"

# curl localhost:5000/listar_fases

@app.route("/listar_fases")
def listar_fases():
    try:
        # obter os dados
        lista = db.session.query(Fases).all()
        # converter pra json
        lista_retorno = [x.json() for x in lista]
        # preparar uma parte da resposta: fases ok
        meujson = {"fases": "ok"}
        meujson.update({"detalhes": lista_retorno})
        # retornar a lista de pessoas json, com fases ok
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"fases": "erro", "detalhes": str(e)})

# iniciar o backend (app.run)
with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)
