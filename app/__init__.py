import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    UPLOAD_FOLDER = UPLOAD_FOLDER
)

db = SQLAlchemy(myapp_obj)

migrate = Migrate(myapp_obj, db)

login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models
from .models import User
