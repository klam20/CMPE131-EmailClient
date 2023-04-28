from app import db

class Register(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(20), nullable=False)
   email = db.Column(db.String(50), nullable=False, unique=True)

   def __init__(self):
      return f"Register('{self.name}', '{self.email}')"
