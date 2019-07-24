# -*- coding: utf-8 -*-
from app1 import db
class User(db.Model):
    __tablename__='stu'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,default='loser')
    password= db.Column(db.String(24))
    email = db.Column(db.String(120), unique=True,default='loser@email.com')
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
