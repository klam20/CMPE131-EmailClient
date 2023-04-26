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

    #Assume register page entered this into a database already
    db.create_all()
    user = User(email = 'klam23@gmail.com')
    user.set_password('password123')
    db.session.add(user)
    db.session.commit()
    
    if form.validate_on_submit():
        # Check if email account exists first
        emailExists = bool(User.query.filter_by(email = form.email.data).first())
        if (emailExists):
            #Query the database for the user
            user = User.query.filter_by(email = form.email.data).first()
            #Check the password entered hashes and matches with database
            if (user.check_password(form.password.data)):
                flash(f'Successful login')
                login_user(user)
                #return redirect('/email')
            else:
                flash(f'Invalid password')
        else:
            flash(f'Account does not exist')

    return render_template('login.html', form=form)
    

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

