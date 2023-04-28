from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from app import myapp_obj, db
from app.models import User, Message

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

@myapp_obj.route("/register")
def register():
    return render_template('register.html')

@myapp_obj.route("/chat")
def chat():
    form = ChatForm()
    sent_messages = Message.query.all()
    return render_template('chat.html', sent_messages=sent_messages, form=form)

@myapp_obj.route("/chat/send_message", methods=["GET", "POST"])
def send_message():
    if request.method == "POST":
        message_content = request.form["message"]
        # Placeholder user id
        user_id = 1
        new_message = Message(content=message_content, user_id=user_id)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("chat"))

    return redirect(url_for("chat"))

class ChatForm(FlaskForm):
     pass

@myapp_obj.route('/delete_messages', methods=['POST'])
def delete_messages():
    Message.query.delete()
    db.session.commit()
    return redirect(url_for('chat'))
