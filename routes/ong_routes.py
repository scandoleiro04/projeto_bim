from flask import Blueprint, request, jsonify
from services import ong_service

ong_bp = Blueprint('ong_bp', __name__)

@ong_bp.route('/ongs', methods=['POST'])
def cadastrar_ong():
    data = request.json
    resposta, status = ong_service.cadastrar_ong(data)
    return jsonify(resposta), status

@ong_bp.route('/ongs', methods=['GET'])
def listar_ongs():
    resposta, status = ong_service.listar_ongs()
    return jsonify(resposta), status

@ong_bp.route('/ongs/<int:id>', methods=['GET'])
def obter_ong_por_id(id):
    resposta, status = ong_service.obter_ong_por_id(id)
    return jsonify(resposta), status

@ong_bp.route('/ongs/<int:id>', methods=['PUT'])
def atualizar_ong(id):
    data = request.json
    resposta, status = ong_service.atualizar_ong(id, data)
    return jsonify(resposta), status

@ong_bp.route('/ongs/<int:id>', methods=['DELETE'])
def deletar_ong(id):
    resposta, status = ong_service.deletar_ong(id)
    return jsonify(resposta), status
