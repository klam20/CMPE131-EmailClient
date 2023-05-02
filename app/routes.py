from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from .forms import LoginForm, sendEmailForm, registerForm
from app import myapp_obj
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import *
from app import db

@myapp_obj.route("/")

@myapp_obj.route("/home", methods=['GET','POST'])
def home():
    db.create_all()
    if current_user.is_authenticated:
        if request.method == 'POST':
            if request.form.get('logOut') == 'Log-Out': 
                logout_user()
                return redirect('/home')
        return render_template('home_logged_in.html')
    else:
        if request.method == 'POST':
            if request.form.get('logIn') == 'Log-In': 
                return redirect('/login')
            elif request.form.get('signUp') == 'Sign-Up':
                return redirect('/register')
        return render_template('home_logged_out.html')

@myapp_obj.route("/email", methods=['GET','POST'])
@login_required
def email():
    form = LoginForm()
    form2 = sendEmailForm()
    todo_list = task.query.all()
    currentUser = current_user
    if request.method == 'POST':
            if request.form.get('delAcc') == 'del-Acc':
                db.session.delete(currentUser)
                db.session.commit()    
                logout_user()
                return redirect('/home')
            else:
                composeEmail = Message(recipient=form2.recipient.data, subject=form2.subject.data, content=form2.content.data)
                db.session.add(composeEmail)
                db.session.commit()
                flash(f'Email is sent')
                return redirect('/email')
                
    return render_template('email.html', todo_list=todo_list, form=form, form2=form2)

@myapp_obj.route("/login", methods=['GET','POST'])
def login():    
    form = LoginForm()
    #Assume register page entered this into a database already
    
    if form.validate_on_submit():
        # Check if email account exists first
        emailExists = bool(User.query.filter_by(email = form.email.data).first())
        if (emailExists):
            #Query the database for the user
            user = User.query.filter_by(email = form.email.data).first()
            #Check the password entered hashes and matches with database
            if (user.check_password(form.password.data)):
                login_user(user)
                return redirect('/email')
            else:
                flash(f'Invalid password')
        else:
            flash(f'Account does not exist')

    return render_template('login.html', form=form)
    

@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        new_user = User(email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/home')

    return render_template('register.html', title='Register', registerForm=form)

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