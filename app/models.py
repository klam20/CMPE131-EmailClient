from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)

class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id= db.Column(db.Integer, db.ForeignKey('recipient.id'), nullable=False)
#    date_sent = db.Column(db.String(32), nullable=False)
#    parent_message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=True)

    def __repr__(self):
         return f"<Message {self.content}>"

class Recipient(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(64), nullable=False)
   recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   message_id = db.Column(db.Integer, db.ForeignKey('chat_message.id'), nullable=True)
