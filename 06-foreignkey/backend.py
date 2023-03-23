# IMPORTAÇÕES --------------------------------
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

# VARIÁVEIS E CONFIGURAÇÕES ------------------
app = Flask(__name__)
# configurações específicas para o SQLite
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, 'pessoas.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + arquivobd
db = SQLAlchemy(app)

# CLASSES ------------------------------------

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)
    email = db.Column(db.Text)
    telefone = db.Column(db.Text)

    # expressar a classe em formato texto
    def __str__(self):
        return f'{self.nome}, ' +\
               f'{self.email}, {self.telefone}'

    # expressar a classe em formato json
    def json(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone
        }

class Celular(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.Text)
    marca = db.Column(db.Text)
    # atributo de relacionamento de chave estrangeira
    proprietario_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    # atributo de acesso ao objeto
    proprietario = db.relationship("Pessoa")
    
    def __str__(self):
        return f'''
        {self.modelo}, {self.marca}, {self.proprietario}
        '''

    def json(self):
        return {
            "id":self.id,
            "modelo":self.modelo,
            "marca":self.marca,
            "proprietario":self.proprietario.json()
        }

# ROTAS ---------------------------------------

@app.route("/")
def ola():
    return "backend operante"

# curl localhost:5000/incluir_pessoa -X POST -d '{"nome":"john", "email":"jo@gmail.com", "telefone":"91234567"}' -H "Content-Type:application/json"
@app.route("/incluir_pessoa", methods=['POST'])
def incluir():
    dados = request.get_json()
    try:
        # cria a pessoa
        nova = Pessoa(**dados)
        # realiza a persistência da nova pessoa
        db.session.add(nova)
        db.session.commit()
        # tudo certo :-) resposta de sucesso
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        # informar mensagem de erro
        return jsonify({"resultado": "erro", "detalhes": str(e)})

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
    
# curl localhost:5000/incluir_celular -X POST -d '{"marca":"Xiami", "modelo":"MI2", "proprietario_id":"1"}' -H "Content-Type:application/json"
@app.route("/incluir_celular", methods=['POST'])
def incluir_celular():
    dados = request.get_json()
    try:
        # cria o celular
        nova = Celular(**dados)
        # realiza a persistência
        db.session.add(nova)
        db.session.commit()
        # tudo certo :-) resposta de sucesso
        return jsonify({"resultado": "ok", "detalhes": "ok"})
    except Exception as e:
        # informar mensagem de erro
        return jsonify({"resultado": "erro", "detalhes": str(e)})

@app.route("/listar_celulares")
def listar_celulares():
    try:
        # obter os celulares
        lista = db.session.query(Celular).all()
        # converter pra json
        lista_retorno = [x.json() for x in lista]
        # preparar uma parte da resposta: resultado ok
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": lista_retorno})
        # retornar a lista em json, com resultado ok
        resposta = jsonify(meujson)
        return resposta
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})    

# INICIO DA APLICAÇÃO -----------------------------------

with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)