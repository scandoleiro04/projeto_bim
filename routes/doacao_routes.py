from flask import Blueprint, request, jsonify
from services import doacao_service

doacao_bp = Blueprint('doacao_bp', __name__)


@doacao_bp.route('/doacoes', methods=['POST'])
def registrar_doacao():
    data = request.json
    resposta, status = doacao_service.registrar_doacao(data)
    return jsonify(resposta), status


@doacao_bp.route('/doacoes', methods=['GET'])
def listar_doacoes():
    resposta, status = doacao_service.listar_doacoes()
    return jsonify(resposta), status


@doacao_bp.route('/doacoes/<int:id>', methods=['GET'])
def obter_doacao_por_id(id):
    resposta, status = doacao_service.obter_doacao_por_id(id)
    return jsonify(resposta), status


@doacao_bp.route('/doacoes/<int:id>', methods=['PUT'])
def atualizar_doacao(id):
    data = request.json
    resposta, status = doacao_service.atualizar_doacao(id, data)
    return jsonify(resposta), status


@doacao_bp.route('/doacoes/<int:id>', methods=['DELETE'])
def deletar_doacao(id):
    resposta, status = doacao_service.deletar_doacao(id)
    return jsonify(resposta), status


@doacao_bp.route('/doacoes/solicitar', methods=['PUT'])
def solicitar_doacao():
    data = request.json
    resposta, status = doacao_service.solicitar_doacao(data)
    return jsonify(resposta), status
