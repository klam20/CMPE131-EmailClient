from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import login
from app import myapp_obj

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(60))
    recipient = db.Column(db.String(60), nullable=False)
    subject = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.String)

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

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id= db.Column(db.Integer, db.ForeignKey('recipient.id'), nullable=False)

    def __repr__(self):
         return f"<Message {self.content}>"

class Recipient(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   message_id = db.Column(db.Integer, db.ForeignKey('chat_message.id'), nullable=True)
   sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   #messages_sent = db.relationship('Message', backref='user', lazy=True)
    
class task(db.Model, UserMixin):
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date = db.Column(db.String(32))
    done = db.Column(db.Boolean)
    edit = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)

    def set_name(self,taskDisc):
        self.name = taskDisc

    def set_date(self, dueDate):
        self.date = dueDate

@login.user_loader
def load_user(id):
    return User.query.get(int(id))    

