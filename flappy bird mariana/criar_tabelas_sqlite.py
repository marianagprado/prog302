from config import *
from modelo import *

# inserindo a aplicação em um contexto :-/
with app.app_context():

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    print("Banco de dados e tabelas criadas")