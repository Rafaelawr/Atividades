from flask import Blueprint, request, jsonify
from  models import atividade_model 
from database import db



bp_atividade = Blueprint('bp_atividade', __name__)

#Criar nova rota
@bp_atividade.route('/atividade', methods=['POST'])
def criar_atividade():
    dados = request.json
    try:
        nova_atividade = atividade_model.adicionar_atividade(dados)
        return jsonify(nova_atividade), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


#Listar todas as atividades
@bp_atividade.route('/atividade', methods=['GET'])
def listar_atividade():
    try:
        atividades = atividade_model.listar_atividades()
        return jsonify(atividades),200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Buscar atividade por ID

@bp_atividade.route('/atividade/<int:id_atividade>', methods=['GET'])
def buscar_atividade(id_atividade):
    try:
        atividade = atividade_model.buscar_atividade_por_id(id_atividade)
        return jsonify(atividade)
    except atividade_model.AtividadeNaoEncontrada:
        return jsonify({'error': 'Atividade não encontrada'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
