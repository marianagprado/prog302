
# importações
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS

# configurações
app = Flask(__name__) # vínculo com o Flask
CORS(app)
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(path, 'jogo.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app) # vínculo com o SQLAlchemy


# comando mágico necessário a partir do python 10
app.app_context().push()
