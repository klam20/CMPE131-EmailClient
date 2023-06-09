import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from werkzeug.utils import secure_filename

myapp_obj = Flask(__name__)

#Settings for Email Attachments
ALLOWED_EXTENSIONS = {'png','jpg','jpeg','gif', 'pdf', 'docx'}
UPLOAD_FOLDER = 'app/attachments/'
myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

basedir = os.path.abspath(os.path.dirname(__file__))
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False,
    UPLOAD_FOLDER = UPLOAD_FOLDER
)

#Initialize the db
db = SQLAlchemy(myapp_obj)

migrate = Migrate(myapp_obj, db)

#Setup Flask-Login
login = LoginManager(myapp_obj)

login.login_view = 'login'

from app import routes, models, forms
from .models import User