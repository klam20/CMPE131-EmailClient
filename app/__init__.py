from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models
from .models import User


""" myapp_obj.app_context().push()
db.create_all()
user = User(email = 'klam23@gmail.com')
user.set_password('password123')
db.session.add(user)
db.session.commit()
user2 = User(email = 'boris@gmail.com')
user2.set_password('password123')
db.session.add(user2)
db.session.commit() """