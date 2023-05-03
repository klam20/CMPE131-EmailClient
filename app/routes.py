from app import mail
from app import db
from app.forms import sendEmailForm
from flask_mail import Message as MailMessage
from app.models import Message
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from .forms import LoginForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from app.models import db
from app.models import Register
from .forms import RegistrationForm

@myapp_obj.route("/")

@myapp_obj.route("/home", methods=['GET','POST'])
def home():
    db.create_all()
    form = LoginForm()
    if current_user.is_authenticated:
        if request.method == 'POST':
            if request.form.get('logOut') == 'Log-Out': 
                logout_user()
                return redirect('/home')
        return render_template('home_logged_in.html', form = form)
    else:
        if request.method == 'POST':
            if request.form.get('logIn') == 'Log-In': 
                return redirect('/login')
            elif request.form.get('signUp') == 'Sign-Up':
                return redirect('/register')
        return render_template('home_logged_out.html', form = form)
    
@myapp_obj.route("/email", methods=['GET','POST'])
@login_required
def email():
    currentUser = current_user
    form = sendEmailForm()
    if form.validate_on_submit():
        recipient_user = User.query.filter_by(id=form.recipient.data).first()
        recipient_email = None
        if recipient_user:
            recipient_email = recipient_user.email

        msg = MailMessage(
            subject=form.subject.data,
            recipients=[recipient_email],
            body=form.content.data
        )
        mail.send(msg)

        message = Message(
            subject=form.subject.data,
            recipient=form.recipient.data,
            content=form.content.data,
	    user_id=current_user.id
        )
        db.session.add(message)
        db.session.commit()
        
        flash('Email is sent')
        return redirect(url_for('email'))
    
    if request.method == 'POST':
            if request.form.get('delAcc') == 'del-Acc':
                db.session.delete(currentUser)
                db.session.commit()    
                logout_user()
                return redirect('/home')
            
    return render_template('email.html', title='Send Email', form=form)

@myapp_obj.route("/login", methods=['GET','POST'])
def login():    
    form = LoginForm()
    #Assume register page entered this into a database already
    if form.validate_on_submit():
        # Check if email account exists first
        emailExists = bool(Register.query.filter_by(email=form.email.data).first())
        if (emailExists):
            #Query the database for the user
            user = Register.query.filter_by(email = form.email.data).first()
            #Check the password entered hashes and matches with database
            if (user.check_password(form.password.data)):
                flash(f'Successful login')
                login_user(user)
                return redirect('/email')
            else:
                flash(f'Invalid password')
        else:
            flash(f'Account does not exist')
    return render_template('login.html', form=form)
    

@myapp_obj.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = Register(email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', registerForm = form)

@myapp_obj.route("/search_email", methods=['GET'])
@login_required
def search_email():
    search_query = request.args.get('search_query', '')
    search_results = Message.query.filter(
        Message.user_id == current_user.id,
        Message.subject.ilike(f"%{search_query}%")
    ).all()
    return render_template('search_results.html', search_results=search_results)