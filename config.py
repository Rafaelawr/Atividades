import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db

db = SQLAlchemy()

app= Flask(__name__)

app.config["HOST"] = "0.0.0.0"
app.config["PORT"] = 5002
app.config["DEBUG"] = True


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atividade.db'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)