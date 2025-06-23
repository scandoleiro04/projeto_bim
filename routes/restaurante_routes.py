from flask import Blueprint, request, jsonify
from models.restaurante import Restaurante
from services.database import restaurantes

restaurante_bp = Blueprint('restaurante_bp', __name__)

@restaurante_bp.route('/restaurantes', methods=['POST'])
def cadastrar_restaurante():
    data = request.json
    if not data.get('nome') or not data.get('cnpj') or not data.get('endereco'):
        return jsonify({"erro": "INVALID_RESTAURANT_DATA", "mensagem": "Dados inválidos fornecidos."}), 400
    for r in restaurantes:
        if r.cnpj == data['cnpj']:
            return jsonify({"erro": "RESTAURANT_EXISTS", "mensagem": "Restaurante já cadastrado."}), 409
    restaurante = Restaurante(len(restaurantes)+1, data['nome'], data['cnpj'], data['endereco'])
    restaurantes.append(restaurante)
    return jsonify({"mensagem": "Restaurante cadastrado com sucesso."}), 201

@restaurante_bp.route('/restaurantes', methods=['PUT'])
def atualizar_restaurante():
    data = request.json
    for r in restaurantes:
        if r.id == data.get('id'):
            r.nome = data.get('nome', r.nome)
            r.endereco = data.get('endereco', r.endereco)
            return jsonify({"mensagem": "Restaurante atualizado com sucesso."}), 200
    return jsonify({"erro": "RESTAURANT_NOT_FOUND", "mensagem": "Restaurante não encontrado."}), 404
