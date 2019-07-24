#-*- coding: utf-8 -*-
from . import create_app1,db
app=create_app1()
with app.app_context():
    db.create_all()