from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from app import login
from app import myapp_obj

# Table for the many-to-many relationship between users and recipients
user_recipients = db.Table('user_recipients',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('recipient_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(60))
    recipient = db.Column(db.String(60), nullable=False)
    subject = db.Column(db.String(60), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.String)
    attachment = db.Column(db.String)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    recipients = db.relationship(
        "User", secondary=user_recipients,
        primaryjoin=(user_recipients.c.user_id == id),
        secondaryjoin=(user_recipients.c.recipient_id == id),
        backref=db.backref('recipients_of', lazy='dynamic'), lazy='dynamic')

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
    recipient_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reactMode = db.Column(db.Boolean)
    reaction = db.Column(db.String(10))
    
    def __repr__(self):
         return f"<Message {self.content}>"

class Recipient(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   message_id = db.Column(db.Integer, db.ForeignKey('chat_message.id'), nullable=True)
   sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
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

