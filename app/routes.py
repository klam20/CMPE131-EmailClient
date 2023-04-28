from flask import render_template, flash, redirect, url_for
from app import myapp_obj, db
from app.models import Register
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

    if form.validate_on_submit():
        new_user = Register(email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)

