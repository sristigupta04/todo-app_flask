from flask import Flask
from Flask_sqlalchemy import SQLALchemy

db= SQLALchemy()

def create_app():
    app = Flask(__name__)
    app.config




    db.__init__(app)

    from app.route.auth import auth_bp
    from app.route.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app

