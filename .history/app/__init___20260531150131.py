from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# create database object globally
from flask_login import LoginManager


db = SQLAlchemy()
Login_Manager = LoginManager()



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app)
    

    # existing config 
    Login_Manager.init_app(app)
    Login_Manager.login_view = "auth.login"

       


    from app.routes.auth import auth_bp
    from app.routes.task import tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    
    return app


@Login_Manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))
