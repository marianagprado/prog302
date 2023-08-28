from backend.geral.config import *
from backend.modelo.modelo import *

@app.route("/atualizar/<string:classe>", methods=['post'])
def atualizar(classe):
    try:    
      # obter os dados
      dados = request.get_json()
      # pegar o id
      id = dados['id']

      # obter o objeto
      obj = None
      if classe == "Cena":
          obj = db.session.get(Cena, id)

      # achou?        
      if obj:
        # para cada campo enviado, atualiza o objeto
        for campo in dados:
          if campo != 'id': # só não atualiza o id :-)
              # atualiza o campo
              # esse comando setattr é maneiro :-)
              setattr(obj, campo, dados[campo])
        
        # persiste as alterações
        db.session.commit()

        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": "ok"})
        return jsonify(meujson)
      else:
        return jsonify({"resultado":"erro", "detalhes":"objeto não encontrado: "+classe})
      
    except Exception as e:
        return jsonify({"resultado": "erro", "detalhes": str(e)})    


@app.route("/atualizar/<string:classe>", methods=['post'])
def atualizar_jogador(classe):
    try:    
      # obter os dados
      dados = request.get_json()
      # pegar o id
      id = dados['id']

      # obter o objeto
      obj = None
      if classe == "Jogador":
          obj = db.session.get(Jogador, id)

      # achou?        
      if obj:
        # para cada campo enviado, atualiza o objeto
        for campo in dados:
          if campo != 'id': # só não atualiza o id :-)
              # atualiza o campo
              # esse comando setattr é maneiro :-)
              setattr(obj, campo, dados[campo])
        
        # persiste as alterações
        db.session.commit()

        meujson = {"resultado": "ok"}
        meujson.update({"detalhes": "ok"})
        return jsonify(meujson)
      else:
        return jsonify({"resultado":"erro", "detalhes":"objeto não encontrado: "+classe})
      
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