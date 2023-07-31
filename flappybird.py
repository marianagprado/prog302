from config import *
#Cena(obstaculos: list of (x, y, b, h))

class Cena(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obstaculos = db.Column(db.Text)


    def __str__(self):
        return f'{self.id}, {self.obstaculos}'
    
    def json(self):
        return {
            "id":self.id,
            "obstaculos":self.obstaculos
        }



if os.path.exists(arquivobd):
    os.remove(arquivobd)
    
db.create_all()

print("Tabelas criadas")

c1= Cena ( obstaculo= x=20, y=50, b=30, h=10
)