from flask import Blueprint, request, jsonify
from  atividade_model import Atividade
import requests

bp_atividade = Blueprint('atividade', __name__)

@bp_atividade.route('/reservas', methods=['GET'])

