from flask import render_template
from flask import flash
from app import myapp_obj
from app import db
from app.models import Notification

@myapp_obj.route("/")

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@myapp_obj.route("/email")
def email():
    db.create_all()
    notifyTest = Notification()
    notifyTest.disabled()
    db.session.add(notifyTest)
    db.session.commit()
    first_query = Notification.query.filter_by(notificationsEnabled = False).first()
    flash(f'{first_query.id} {first_query.notificationsEnabled}')
    return render_template('email.html')

@myapp_obj.route("/login")
def login():
    return render_template('login.html')

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

