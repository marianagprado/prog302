''' 
configurações:
* importação de bibliotecas
* vínculo da aplicação flask
* configurações de persistência
'''

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# temporário: persistência em memória
# criar uma lista de pessoas
# essa lista fica acessível para todas as rotas
lista = []
