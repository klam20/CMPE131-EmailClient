from flask import *
from flask_sqlalchemy import SQLAlchemy
from app import myapp_obj
from app import db
from app.models import *

@myapp_obj.route("/")

@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@myapp_obj.route("/email", methods=['GET','POST'])
def email():
    db.create_all()
    todo_list = task.query.all()

    return render_template('email.html', todo_list=todo_list)

@myapp_obj.route('/add', methods=['POST'])
def addToDo():
    name = request.form.get("name")
    date = request.form.get("date")
    test = task(name = name, date = date, done = False)
    db.session.add(test)
    db.session.commit()

    return redirect(url_for("email"))

@myapp_obj.route('/update/<int:todo_id>')
def update(todo_id):
    todo = task.query.get(todo_id)
    todo.done=not todo.done
    db.session.commit()
    return redirect(url_for("email"))
    

@myapp_obj.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = task.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("email"))

@myapp_obj.route("/login")
def login():
    return render_template('login.html')

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

