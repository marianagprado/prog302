# importacao das configurações comuns ao sistema
from config.configuracoes import *

# importar os modelos
from modelo.pessoa import *

# importação das rotas
# exercício: converter a importação abaixo para funcionar "de uma só vez"
# algo assim: from rotas import *
# o que é preciso fazer?
from rotas import incluir_pessoa
from rotas import listar_pessoas


# INICIO DA APLICAÇÃO
#

with app.app_context():

    # criar o banco de dados, caso não esteja criado
    db.create_all()

    # provendo o CORS ao sistema
    CORS(app)

    # iniciar o servidor
    app.run(debug=True)