from models.doacao import Doacao
from services.database import doacoes

def registrar_doacao(data):
    if not data.get('restauranteId') or not data.get('alimento') or not data.get('quantidade'):
        return {"erro": "INVALID_DONATION_DATA", "mensagem": "Dados de doação incompletos ou inválidos."}, 400
    
    nova_doacao = Doacao(
        id=len(doacoes) + 1,
        restauranteId=data['restauranteId'],
        alimento=data['alimento'],
        quantidade=data['quantidade'],
        perecivel=data.get('perecivel', False)
    )
    doacoes.append(nova_doacao)
    return {"mensagem": "Doação registrada com sucesso."}, 201

def listar_doacoes():
    if not doacoes:
        return {"erro": "DONATION_LIST_NOT_FOUND", "mensagem": "Nenhuma doação encontrada."}, 404

    lista = [{
        "id": d.id,
        "restauranteId": d.restauranteId,
        "alimento": d.alimento,
        "quantidade": d.quantidade,
        "perecivel": d.perecivel,
        "ongId": getattr(d, 'ongId', None)  # pode não existir
    } for d in doacoes]

    return lista, 200

def obter_doacao_por_id(id):
    for d in doacoes:
        if d.id == id:
            doacao_data = {
                "id": d.id,
                "restauranteId": d.restauranteId,
                "alimento": d.alimento,
                "quantidade": d.quantidade,
                "perecivel": d.perecivel,
                "ongId": getattr(d, 'ongId', None)
            }
            return doacao_data, 200
    return {"erro": "DONATION_NOT_FOUND", "mensagem": "Doação não encontrada."}, 404

def atualizar_doacao(id, data):
    for d in doacoes:
        if d.id == id:
            
            d.restauranteId = data.get('restauranteId', d.restauranteId)
            d.alimento = data.get('alimento', d.alimento)
            d.quantidade = data.get('quantidade', d.quantidade)
            d.perecivel = data.get('perecivel', d.perecivel)
            
            return {"mensagem": "Doação atualizada com sucesso."}, 200
    return {"erro": "DONATION_NOT_FOUND", "mensagem": "Doação não encontrada para atualização."}, 404

def deletar_doacao(id):
    for i, d in enumerate(doacoes):
        if d.id == id:
            doacoes.pop(i)
            return {"mensagem": "Doação removida com sucesso."}, 200
    return {"erro": "DONATION_NOT_FOUND", "mensagem": "Doação não encontrada para remoção."}, 404

def solicitar_doacao(data):
    for d in doacoes:
        if d.id == data.get('doacaoId'):
            d.ongId = data.get('ongId')
            return {"mensagem": "Doação associada à ONG com sucesso."}, 200
    return {"erro": "DONATION_NOT_FOUND", "mensagem": "Doação não encontrada para solicitação."}, 404
