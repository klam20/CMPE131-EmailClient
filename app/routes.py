from flask import render_template
from flask import flash
from flask import redirect
from .forms import LoginForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

@myapp_obj.route("/")

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@myapp_obj.route("/email")
def email():
    return render_template('email.html')

@myapp_obj.route("/login", methods=['GET','POST'])
def login():    
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/login')
    return render_template('login.html', form=form)

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

