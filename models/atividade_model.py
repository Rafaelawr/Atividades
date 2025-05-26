from database import db

class Atividade(db.Model):
    __tablename__ = 'atividade'
    
    id = db.Column(db.Integer, primary_key=True)
    id_professor = db.Column(db.Integer, nullable=False)
    nome_atividade = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=True)
    data_entrega = db.Column(db.DateTime, nullable=False)
    
