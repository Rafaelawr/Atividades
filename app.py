from flask import Flask
from database import create_app, db
from controllers.route_atividade import bp_atividade

app = create_app()

app.register_blueprint(bp_atividade)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

