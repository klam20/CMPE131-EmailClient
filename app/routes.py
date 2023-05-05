from flask import render_template, request, redirect, url_for
from flask_wtf import FlaskForm, CSRFProtect
from app import myapp_obj, db
from app.models import  User, ChatMessage, Recipient
from app.forms import ChatForm, AddRecipientForm

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
    sent_messages = ChatMessage.query.all()
    recipients = Recipient.query.all()
    return render_template('chat.html', sent_messages=sent_messages, recipients=recipients, form=form, selected_recipient_id=None)

@myapp_obj.route("/chat/send_message/<int:recipient_id>", methods=["GET", "POST"])
def send_message(recipient_id):
    if request.method == "POST":
        message_content = request.form["message"]
        # Placeholder user id
        user_id = 1
        new_message = ChatMessage(content=message_content, user_id=user_id, recipient_id=recipient_id)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))

    return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))

@myapp_obj.route("/chat/<int:recipient_id>", methods=['GET', 'POST'])
def chat_with_recipient(recipient_id):
     form = ChatForm()
     recipients = Recipient.query.all()
     messages = ChatMessage.query.filter_by(recipient_id=recipient_id).all()
     user = User.query.get(1)
     if form.validate_on_submit():
        message_content = form.message.data
        user_id = 1
        new_message = ChatMessage(content=message_content, user_id=user_id, recipient_id=recipient_id)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))
     return render_template('chat.html', recipients=recipients, messages=messages, form=form, selected_recipient_id=recipient_id, user=user)

@myapp_obj.route("/add_recipient", methods=["GET", "POST"])
def add_recipient():
    form = AddRecipientForm()
    if form.validate_on_submit():
        recipient_name = form.name.data
        new_user = User(email=f"{recipient_name}@example.com", password="123")
        db.session.add(new_user)
        db.session.flush()

        recipient_id = new_user.id
        new_recipient = Recipient(name=recipient_name, recipient_id=recipient_id)
        db.session.add(new_recipient)
        db.session.commit()
        return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))

    return render_template("add_recipient.html", form=form)

@myapp_obj.route('/delete_messages', methods=['POST'])
def delete_messages():
    ChatMessage.query.delete()
    db.session.commit()
    return redirect(url_for('chat'))

@myapp_obj.route('/remove_recipient/<int:recipient_id>', methods=['POST'])
def remove_recipient(recipient_id):
    recipient = Recipient.query.get(recipient_id)
    if recipient:
        db.session.delete(recipient)
        db.session.commit()
    return redirect(url_for('chat'))
