# -*- coding: utf-8 -*-
from app1 import create_app1
from app1.views.login import app_login
app=create_app1()
app.register_blueprint(app_login)
if __name__=='__main__':
    app.run()

