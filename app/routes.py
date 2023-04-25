from flask import render_template
from .forms import LoginForm
from app import myapp_obj

@myapp_obj.route("/")

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@myapp_obj.route("/email")
def email():
    return render_template('email.html')

@myapp_obj.route("/login")
def login():
    current_form = LoginForm()
    return render_template('login.html', form=current_form)

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

