from flask import Blueprint, request, jsonify
from models.ong import ONG
from services.database import ongs

ong_bp = Blueprint('ong_bp', __name__)

@ong_bp.route('/ongs', methods=['POST'])
def cadastrar_ong():
    data = request.json
    if not data.get('nome') or not data.get('cnpj') or not data.get('localizacao'):
        return jsonify({"erro": "INVALID_ONG_DATA", "mensagem": "Dados inválidos fornecidos."}), 400
    for o in ongs:
        if o.cnpj == data['cnpj']:
            return jsonify({"erro": "ONG_EXISTS", "mensagem": "ONG já cadastrada."}), 409
    ong = ONG(len(ongs)+1, data['nome'], data['cnpj'], data['localizacao'])
    ongs.append(ong)
    return jsonify({"mensagem": "ONG cadastrada com sucesso."}), 201

@ong_bp.route('/ongs/<int:id>', methods=['DELETE'])
def deletar_ong(id):
    for o in ongs:
        if o.id == id:
            ongs.remove(o)
            return jsonify({"mensagem": "ONG excluída com sucesso."}), 200
    return jsonify({"erro": "ONG_NOT_FOUND", "mensagem": "ONG não encontrada."}), 404
