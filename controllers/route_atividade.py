from flask import Blueprint, request, jsonify
from  models import atividade_model 
from database import db
import requests


bp_atividade = Blueprint('bp_atividade', __name__)

@bp_atividade.route('/atividade', methodos=['POST'])
def criar_atividade():
    dados = request.json
    try:
        nova_atividade = atividade_model.criar_atividade(dados)
        return jsonify(nova_atividade), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400
@bp_atividade.route('/atividade', methods=['POST']) 



@bp_atividade.route('/atividade', methods=['GET'])
def listar_atividade():
    atividades = atividade_model.listar_atividade()
    return jsonify(atividades)


@bp_atividade.route('/atividade/<int:id_atividade>', methods=['GET'])
def buscar_atividade(id_atividade):
    try:
        atividade = atividade_model.buscar_atividade(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNotFound:
        return jsonify({'error': 'Atividade não encontrada'}), 404

