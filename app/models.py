from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import myapp_obj

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def deleteUser(self):
        user3 = User.query.filter_by(email="klam23@gmail.com")
        db.session.delete(user3)
        db.session.commit()

    def __repr__(self):
        return f'<user {self.id} {self.email}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))    