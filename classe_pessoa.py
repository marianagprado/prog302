class Pessoa:
    # usando valor padrão nos parâmetros do construtor
    def __init__(self, nome="", email="", telefone=""):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    # usando string formatada, que coisa linda :-)
    def __str__(self):
        return f'{self.nome}, '+\
               f'{self.email}, {self.telefone}'
