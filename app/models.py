from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Register(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(20), nullable = True)
   password = db.Column(db.String(50), nullable = True, unique=True)

   def set_password(self,password):
        self.password = generate_password_hash(password)

