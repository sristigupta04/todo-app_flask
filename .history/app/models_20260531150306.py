from app import db

from flask_login import UserMixin


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key =True)
    username =db.Column(db.String(100),primary_key =True, unique=True)
    password = db.Column(db.String(255),nullable =False)




class Task(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    title= db.Column(db.String(100) ,nullable =False)
    status = db.Column(db.String(20),default="pending")
    


