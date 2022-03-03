from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app=Flask(__name__)
UPLOAD_FOLDER="app/static/uploads"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['SECRET_KEY']='mysecretkey'


db=SQLAlchemy(app)
migrate=Migrate(app,db)



from app.models import*
from main.routes import*
from admin.routes import*

