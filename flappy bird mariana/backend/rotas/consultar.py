from backend.geral.config import *
from backend.modelo.modelo import *

@app.route("/consultar/<string:classe>/<int:id>")
def consultar(classe, id):
    try:    
      # obter o objeto
      obj = None
      if classe == "Cena":
          obj = db.session.get(Cena, id)

      # achou?        
      if obj:
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": obj.json()})
        return jsonify(meujson)
      else:
        return jsonify({"resultado":"erro", "detalhes":"objeto não encontrado: "+id})
      
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})    


@app.route("/consultar/<string:classe>/<int:id>")
def consultar_jogador(classe, id):
    try:    
      # obter o objeto
      obj = None
      if classe == "Jogador":
          obj = db.session.get(Jogador, id)

      # achou?        
      if obj:
        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": obj.json()})
        return jsonify(meujson)
      else:
        return jsonify({"resultado":"erro", "detalhes":"objeto não encontrado: "+id})
      
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})    


    '''
exemplo de teste:
curl localhost:5000/atualizar/Jogador -d '{"id":1, "x":150}' -H 'Content-Type:application/json' -X POST
{
  "detalhes": "ok",
  "resultado": "ok"
}


'''