from config import *

class Cena(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obstaculos = db.Column(db.Text)


    def __str__(self):
        return f'{self.id}, obstaculos da fase: {self.obstaculos}'
    
    def json(self):
        return {
            "id":self.id,
            "obstaculos":self.obstaculos
        }

class Fases(db.Model):
    # atributo auto-gerado
    id = db.Column(db.Integer, primary_key=True)
    nome_jogador = db.Column(db.Text)
    fases = db.Column(db.Integer)

    def __str__(self):
        return f'{self.nome_jogador} passou por {self.fases} fases'
    
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome_jogador,
            "fases": self.fases
        }