from flask import Blueprint, request, jsonify
from services import restaurante_service

restaurante_bp = Blueprint('restaurante_bp', __name__)

@restaurante_bp.route('/restaurantes', methods=['POST'])
def cadastrar_restaurante():
    data = request.json
    resposta, status = restaurante_service.cadastrar_restaurante(data)
    return jsonify(resposta), status

@restaurante_bp.route('/restaurantes', methods=['GET'])
def listar_restaurantes():
    resposta, status = restaurante_service.listar_restaurantes()
    return jsonify(resposta), status

@restaurante_bp.route('/restaurantes/<int:id>', methods=['GET'])
def obter_restaurante_por_id(id):
    resposta, status = restaurante_service.obter_restaurante_por_id(id)
    return jsonify(resposta), status

@restaurante_bp.route('/restaurantes/<int:id>', methods=['PUT'])
def atualizar_restaurante(id):
    data = request.json
    resposta, status = restaurante_service.atualizar_restaurante(id, data)
    return jsonify(resposta), status

@restaurante_bp.route('/restaurantes/<int:id>', methods=['DELETE'])
def deletar_restaurante(id):
    resposta, status = restaurante_service.deletar_restaurante(id)
    return jsonify(resposta), status
