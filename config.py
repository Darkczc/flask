# -*- coding: utf-8 -*-
from flask_session import Session
from redis import  Redis
class Config(object):
    DEBUG=True
    TESTING=True
    SECRET_KEY='123456.com'
    SESSION_TYPE='redis'
    SESSION_REDIS=Redis(host='192.168.95.26',port=6379,password="l1zll0twUzyF")
    SESSION_COOKIE_NAME='test'
    SESSION_KEY_PREFIX='czcweb_'
    SQLALCHEMY_TRACK_MODIFICATIONS=False



class TestConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://test:123.com@192.168.95.26:3306/t1?charset=utf8'