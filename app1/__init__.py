# -*- coding: utf-8 -*-
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import TestConfig
db=SQLAlchemy()
from app1.models import *
# print(__name__)
def create_app1():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    db.init_app(app)
    return app


# if __name__ == '__main__':
#     app=create_app1()
#     with app.app_context():
#         db.create_all()