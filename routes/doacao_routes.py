from flask import Blueprint, request, jsonify
from models.doacao import Doacao
from services.database import doacoes

doacao_bp = Blueprint('doacao_bp', __name__)

@doacao_bp.route('/doacoes', methods=['POST'])
def registrar_doacao():
    data = request.json
    if not data.get('restauranteId') or not data.get('alimento') or not data.get('quantidade'):
        return jsonify({"erro": "INVALID_DONATION_DATA", "mensagem": "Dados de doação incompletos ou inválidos."}), 400
    doacao = Doacao(len(doacoes)+1, data['restauranteId'], data['alimento'], data['quantidade'], data.get('perecivel', False))
    doacoes.append(doacao)
    return jsonify({"mensagem": "Doação registrada com sucesso."}), 201

@doacao_bp.route('/doacoes', methods=['GET'])
def listar_doacoes():
    if not doacoes:
        return jsonify({"erro": "DONATION_LIST_NOT_FOUND", "mensagem": "Nenhuma doação encontrada."}), 404
    return jsonify([{
        "id": d.id,
        "alimento": d.alimento,
        "quantidade": d.quantidade
    } for d in doacoes]), 200

@doacao_bp.route('/doacoes/solicitar', methods=['PUT'])
def solicitar_doacao():
    data = request.json
    for d in doacoes:
        if d.id == data.get('doacaoId'):
            d.ongId = data.get('ongId')
            return jsonify({"mensagem": "Doação associada à ONG com sucesso."}), 200
    return jsonify({"erro": "DONATION_NOT_FOUND", "mensagem": "Doação não encontrada para solicitação."}), 404
