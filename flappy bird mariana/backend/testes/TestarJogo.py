from backend.geral.config import *
from backend.modelo.modelo import *

def run():
    print("TESTE DE CENA")
    
    c1= Cena ( obstaculos= "300,1,30,170|420,1,30,100|540,1,30,200|660,1,30,120|300,400,30,200|420,300,30,350|540,400,30,250|660,300,30,400")
    c2= Cena ( obstaculos= "300,1,30,230|420,1,30,70|540,1,30,280|660,1,30,100|300,400,30,280|420,300,30,400|540,400,30,180|660,300,30,300")
    c3= Cena ( obstaculos= "300,1,30,100|420,1,30,150|540,1,30,320|660,1,30,150|300,400,30,240|420,300,30,300|540,400,30,220|660,300,30,450")

    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.commit()

    print(c1)
    print(c2)
    print(c3.json())