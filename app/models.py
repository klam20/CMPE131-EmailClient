from app import db
from app import login
from app import myapp_obj
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id} {self.email}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))    