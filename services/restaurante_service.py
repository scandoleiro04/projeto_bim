from models.restaurante import Restaurante
from services.database import restaurante

def cadastrar_restaurante(data):
    if not data.get('nome') or not data.get('cnpj') or not data.get('localizacao'):
        return {"erro": "INVALID_RESTAURANT_DATA", "mensagem": "Dados inválidos fornecidos."}, 400
    
    for r in restaurante:
        if r.cnpj == data['cnpj']:
            return {"erro": "RESTAURANT_EXISTS", "mensagem": "Restaurante já cadastrado."}, 409
    
    novo_restaurante = Restaurante(
        id=len(restaurante) + 1,
        nome=data['nome'],
        cnpj=data['cnpj'],
        localizacao=data['localizacao']
    )
    restaurante.append(novo_restaurante)
    return {"mensagem": "Restaurante cadastrado com sucesso."}, 201

def listar_restaurantes():
    if not restaurante:
        return {"erro": "RESTAURANT_LIST_NOT_FOUND", "mensagem": "Nenhum restaurante cadastrado."}, 404

    lista = [{
        "id": r.id,
        "nome": r.nome,
        "cnpj": r.cnpj,
        "localizacao": r.localizacao
    } for r in restaurante]

    return lista, 200

def obter_restaurante_por_id(id):
    for r in restaurante:
        if r.id == id:
            restaurante_data = {
                "id": r.id,
                "nome": r.nome,
                "cnpj": r.cnpj,
                "localizacao": r.localizacao
            }
            return restaurante_data, 200
    return {"erro": "RESTAURANT_NOT_FOUND", "mensagem": "Restaurante não encontrado."}, 404

def atualizar_restaurante(id, data):
    for r in restaurante:
        if r.id == id:
            r.nome = data.get('nome', r.nome)
            r.cnpj = data.get('cnpj', r.cnpj)
            r.localizacao = data.get('localizacao', r.localizacao)
            return {"mensagem": "Restaurante atualizado com sucesso."}, 200
    return {"erro": "RESTAURANT_NOT_FOUND", "mensagem": "Restaurante não encontrado para atualização."}, 404

def deletar_restaurante(id):
    for r in restaurante:
        if r.id == id:
            restaurante.remove(r)
            return {"mensagem": "Restaurante excluído com sucesso."}, 200
    return {"erro": "RESTAURANT_NOT_FOUND", "mensagem": "Restaurante não encontrado."}, 404
