from app import *

class task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date = db.Column(db.String(32))
    done = db.Column(db.Boolean)

    def set_name(self,taskDisc):
        self.name = taskDisc

    def set_date(self, dueDate):
        self.date = dueDate
