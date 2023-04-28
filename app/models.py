from app import db
from flask_login import UserMixin

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notificationsEnabled = db.Column(db.Boolean, nullable=False, default = True)

    def enabled(self):
        self.notificationsEnabled = True

    def disabled(self):
        self.notificationsEnabled = False

    def __repr__(self):
        return f'<user {self.id} {self.notificationsEnabled}>'

