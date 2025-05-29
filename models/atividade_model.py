import requests
from database import db


class Atividade(db.Model):
    __tablename__ = 'atividade'
    
    id = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, nullable=False)
    nome_atividade = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    observacoes = db.Column(db.Text)
    
        
    professor = db.relationship('Professor', backref='atividades', lazy=True)

    def __init__(self, id_professor, nome_atividade, descricao=None, observacoes=None):
        self.id_professor = id_professor
        self.nome_atividade = nome_atividade
        self.descricao = descricao
        self.observacoes = observacoes
        
    def to_dict(self):
        return {
            'id': self.id,
            'id_professor': self.id_professor,
            'nome_atividade': self.nome_atividade,
            'descricao': self.descricao,
            'observacoes': self.observacoes
        }        
class AtividadeNaoEncontrada(Exception):
    pass        
def buscar_atividade_por_id(atividade_id):
    atividade = Atividade.query.get(atividade_id)
    if not atividade:
        raise AtividadeNaoEncontrada(f'Atividade com ID {atividade_id} não encontrada.')
    return atividade.to_dict()        

def listar_atividades():
    atividades = Atividade.query.all()
    return [atividade.to_dict() for atividade in atividades]

def adicionar_atividade(atividade_data):
    nova_atividade = Atividade(
        id_professor=atividade_data['id_professor'],
        nome_atividade=atividade_data['nome_atividade'],
        descricao=atividade_data.get('descricao'),
        observacoes=atividade_data.get('observacoes')
    )
        
    db.session.add(nova_atividade)
    db.session.commit()
    return nova_atividade.to_dict()