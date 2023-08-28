from backend.geral.config import *
from backend.rotas.listar import *
from backend.rotas.atualizar import *
from backend.rotas.consultar import *

# rota padrão
@app.route("/")
def inicio():
    return 'backend com rotas generalizadas de listagem'

# inserindo a aplicação em um contexto :-/
with app.app_context():

    app.run(debug=True)