from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create database object globally
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




    db.__init__(app)

    from app.route.auth import auth_bp
    from app.route.auth import tasks_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    return app

