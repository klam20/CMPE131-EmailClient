from app import db
from app import myapp_obj
from app.forms import sendEmailForm
from flask_mail import Message as MailMessage
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from app.models import task
from app.models import Message
from .forms import RegistrationForm
from .forms import LoginForm

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
    todo_list = task.query.all()
    inboxMessages = Message.query.filter_by(user_id=current_user.id)
    messageCount = inboxMessages.count()


    if form.validate_on_submit():

        message = Message(
            subject=form.subject.data,
            recipient=form.recipient.data,
            content=form.content.data,
	    user_id=current_user.id
        )
        db.session.add(message)
        db.session.commit()

        flash('Email is sent')
        return redirect('/email')
    
    if request.method == 'POST':
            if request.form.get('delAcc') == 'del-Acc':
                db.session.delete(currentUser)
                db.session.commit()    
                logout_user()
                return redirect('/home')
            
    return render_template('email.html', todo_list=todo_list, title='Send Email', form=form, inboxMessages=inboxMessages, messageCount=messageCount)
@myapp_obj.route("/login", methods=['GET','POST'])
def login():    
    form = LoginForm()
    #Assume register page entered this into a database already
    if form.validate_on_submit():
        # Check if email account exists first
        emailExists = bool(User.query.filter_by(email=form.email.data).first())
        if (emailExists):
            #Query the database for the user
            user = User.query.filter_by(email = form.email.data).first()
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
        new_user = User(email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', registerForm = form)

@myapp_obj.route('/addTodo', methods=['POST'])
def addToDo():
    name = request.form.get("name")
    date = request.form.get("date")
    test = task(name = name, date = date, done = False, edit = False)
    db.session.add(test)
    db.session.commit()

    return redirect("/email")

@myapp_obj.route('/updateTodo/<int:todo_id>')
def updateTask(todo_id):
    todo = task.query.get(todo_id)
    todo.done=not todo.done
    db.session.commit()
    return redirect("/email")
    

@myapp_obj.route('/deleteTodo/<int:todo_id>')
def deleteTask(todo_id):
    todo = task.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/email")

@myapp_obj.route('/submitEdit/<int:todo_id>', methods=['POST'])
def submitEdit(todo_id):
    todo = task.query.get(todo_id)
    todo.name = request.form.get("editInputText")
    todo.date = request.form.get("editInputDate")
    todo.edit = not todo.edit
    db.session.commit()
    return redirect("/email")

@myapp_obj.route('/startEdit/<int:todo_id>')
def startEdit(todo_id):
    todo = task.query.get(todo_id)
    todo.edit = not todo.edit
    db.session.commit()
    return redirect("/email")

