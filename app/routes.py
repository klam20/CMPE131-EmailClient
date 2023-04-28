from flask import render_template,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from app import myapp_obj
from app import db
from app.models import *
from .forms import RegistrationForm

@myapp_obj.route("/")

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@myapp_obj.route("/email")
def email():
    return render_template('email.html')

@myapp_obj.route("/login")
def login():
    return render_template('login.html')

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()    
    db.create_all()
    
    new_user = Register(email= "fml@gmail.com")

    new_user.set_password('123')
    db.session.add(new_user)
    db.session.commit()   

    if form.validate_on_submit():
        new_user = User(email=form.email.data)
        new_user.set_password(form.password.data)
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



