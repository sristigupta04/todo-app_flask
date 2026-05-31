from app import db

from flask_login import UserMixin

class Task(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key =True)
    title= db.Column(db.String(100) ,nullable =False)
    status = db.Column(db.String(20),default="pending")
    


class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key =True)
    username =db.Column(db. String(100),primary_key =True)
    password = db.Column(db.String(255),nullable =False)


