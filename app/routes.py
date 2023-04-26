from flask import render_template
from flask import flash
from flask import redirect
from .forms import LoginForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from app import db

@myapp_obj.route("/")

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@myapp_obj.route("/email")
@login_required
def email():
    return render_template('email.html')

@myapp_obj.route("/login", methods=['GET','POST'])
def login():    
    form = LoginForm()
    #Assume already created database
    db.create_all()
    user = User(username = 'bob123')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    
    if form.validate_on_submit():
        # search register database for username
        # user = User.query.filter_by(...)
        test = User.query.filter_by(username = form.username.data).first()
        # check the password
        flash(f'Here are the input {test.username} {test.password} {user.username} and {user.password} {user.check_password("password121")}')
        # if password matches
        # login_user(user)
    return render_template('login.html', form=form)
    

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

