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


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)
        
    with app.app_context():

        db.create_all()

        print("Tabelas criadas")

        c1= Cena ( obstaculos= "300,1,30,170|420,1,30,100|540,1,30,200|660,1,30,120|300,400,30,200|420,300,30,350|540,400,30,250|660,300,30,400")
        db.session.add(c1)
        db.session.commit()

        print(c1)