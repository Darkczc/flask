from flask import Flask,render_template,request,redirect,url_for,Blueprint
from flask import signals,session
from flask_session import Session


app_login=Blueprint('login',__name__)
from app1.models import User
from app1 import db

# signals.request_started.connect(func1)

@app_login.route('/')
def index():
    print(session)
    print(request.cookies['test'])
    if request.cookies['test'] in session:
        print(session)
        return render_template('index.html')
    else:
        return redirect(url_for('.login'))
    # session['xxx']=123
    # return 'Hello World!'


@app_login.route('/login',methods=['GET','POST'])
def login():

    if request.method=='GET':
        # session['username']='czc'
        # session['password']='12345
        return render_template('login.html')
    if request.method=="POST":


        if session.get('username')==request.form['user'] and session.get('password')==request.form['pwd']:
            return "Login success"
        else:
            if db.session.query(User).filter(User.username==request.form['user'] and User.password==request.form['pwd']).all():
                session['username']=request.form['user']
                session['password']=request.form['password']
                db.session.close()
                return "DB has record,login success"
            else:
                return redirect(url_for('.register'))

            # cache_operate


@app_login.route('/signin',methods=['GET','POST'],endpoint='register')
def signin():
    if request.method=='GET':
        return render_template('signin.html')
    if request.method=='POST':
        if db.session.query(User).filter(User.username==request.form['user']).all():
            return "account exist"
        else:
            db.session.add(User(username=request.form['user'],password=request.form['pwd'],email=request.form['email']))
            db.session.commit()
            db.session.close()
            return "register success"











# app_login.add_url_rule()

