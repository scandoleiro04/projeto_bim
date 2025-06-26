from models.ong import ONG
from services.database import ongs

def cadastrar_ong(data):
    if not data.get('nome') or not data.get('cnpj') or not data.get('localizacao'):
        return {"erro": "INVALID_ONG_DATA", "mensagem": "Dados inválidos fornecidos."}, 400

    for o in ongs:
        if o.cnpj == data['cnpj']:
            return {"erro": "ONG_EXISTS", "mensagem": "ONG já cadastrada."}, 409

    nova_ong = ONG(len(ongs) + 1, data['nome'], data['cnpj'], data['localizacao'])
    ongs.append(nova_ong)

    return {"mensagem": "ONG cadastrada com sucesso."}, 201

def listar_ongs():
    if not ongs:
        return {"erro": "ONG_LIST_NOT_FOUND", "mensagem": "Nenhuma ONG cadastrada."}, 404

    lista = [{
        "id": o.id,
        "nome": o.nome,
        "cnpj": o.cnpj,
        "localizacao": o.localizacao
    } for o in ongs]

    return lista, 200

def obter_ong_por_id(id):
    for o in ongs:
        if o.id == id:
            ong_data = {
                "id": o.id,
                "nome": o.nome,
                "cnpj": o.cnpj,
                "localizacao": o.localizacao
            }
            return ong_data, 200
    return {"erro": "ONG_NOT_FOUND", "mensagem": "ONG não encontrada."}, 404

def atualizar_ong(id, data):
    for o in ongs:
        if o.id == id:
            o.nome = data.get('nome', o.nome)
            o.cnpj = data.get('cnpj', o.cnpj)
            o.localizacao = data.get('localizacao', o.localizacao)
            return {"mensagem": "ONG atualizada com sucesso."}, 200
    return {"erro": "ONG_NOT_FOUND", "mensagem": "ONG não encontrada para atualização."}, 404

def deletar_ong(id):
    for o in ongs:
        if o.id == id:
            ongs.remove(o)
            return {"mensagem": "ONG excluída com sucesso."}, 200
    return {"erro": "ONG_NOT_FOUND", "mensagem": "ONG não encontrada."}, 404
