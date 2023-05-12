from flask_wtf import FlaskForm
from app import db
from app import myapp_obj
from app.forms import sendEmailForm
from flask_mail import Message as MailMessage
from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for
from flask import session
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from app.models import User
from app.models import task
from app.models import Message
from app.models import ChatMessage
from app.models import Recipient
from .forms import RegistrationForm
from .forms import LoginForm
from .forms import ChatForm
from .forms import AddRecipientForm
from sqlalchemy import or_
from app import api
from datetime import datetime
from app import ALLOWED_EXTENSIONS
from werkzeug.utils import secure_filename
import os
from flask import send_from_directory

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@myapp_obj.route("/")

@myapp_obj.route("/home", methods=['GET','POST'])
def home():
    #api.randomImageAPI()
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


@myapp_obj.route("/email/attachments/<name>")
def download(name):
    return send_from_directory('attachments/', name)

@myapp_obj.route("/email", methods=['GET','POST'])
@login_required
def email():
    currentUserEmail = User.query.get(current_user.id).email
    form = sendEmailForm()
    todo_list = task.query.all()
    sentEmails = Message.query.filter_by(user_id=current_user.id).order_by(Message.id.desc())
    receivedEmails = Message.query.filter_by(recipient=currentUserEmail).order_by(Message.id.desc())
    messageCount = sentEmails.count() + receivedEmails.count()
    search_query = request.args.get('search_query', None)

    # Search bar 
    if search_query:
        receivedEmails = receivedEmails.filter(
            or_(
                Message.recipient.ilike(f"%{search_query}%"),
                Message.subject.ilike(f"%{search_query}%"),
                Message.content.ilike(f"%{search_query}%"),
                Message.timestamp.ilike(f"%{search_query}"),
                Message.sender.ilike(f"%{search_query}")
            )
        ).all()

        sentEmails = sentEmails.filter(
            or_(
                Message.recipient.ilike(f"%{search_query}%"),
                Message.subject.ilike(f"%{search_query}%"),
                Message.content.ilike(f"%{search_query}%"),
                Message.timestamp.ilike(f"%{search_query}"),
                Message.sender.ilike(f"%{search_query}")
            )
        ).all()

        if not receivedEmails and not sentEmails:
            flash('No emails found. Please try again')
            
    if form.validate_on_submit():
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], filename))

        sourceDate = datetime.now()

        message = Message(
            sender = currentUserEmail,
            subject=form.subject.data,
            recipient=form.recipient.data,
            content=form.content.data,
	        user_id=current_user.id,
            timestamp = sourceDate.strftime("%x"),
            attachment = secure_filename(file.filename)
        )
        db.session.add(message)
        db.session.commit()

        flash('Email is sent')
        return redirect('/email')
    
    if request.method == 'POST':
            if request.form.get('delAcc') == 'Delete Account':
                db.session.delete(current_user)
                db.session.commit()    
                logout_user()
                return redirect('/home')

            if request.form.get('Received') == 'Received':
                    return render_template('email.html', todo_list=todo_list, title='Inbox', form=form, sentEmails=sentEmails, messageCount=messageCount, currentUserEmail=currentUserEmail, receivedEmails=receivedEmails)


            if request.form.get('Sent') == 'Sent':
                    return render_template('emailSent.html', todo_list=todo_list, title='Sent', form=form, sentEmails=sentEmails, messageCount=messageCount, currentUserEmail=currentUserEmail, receivedEmails=receivedEmails)

    return render_template('email.html', todo_list=todo_list, title='Inbox', form=form, sender = currentUserEmail, sentEmails=sentEmails, messageCount=messageCount, currentUserEmail=currentUserEmail, receivedEmails=receivedEmails)

@myapp_obj.route('/email/<int:emailId>', methods=['GET','POST'])
def viewEmail(emailId):
    currentUserEmail = User.query.get(current_user.id).email
    form = sendEmailForm()
    todo_list = task.query.all()
    sentEmails = Message.query.filter_by(user_id=current_user.id)
    receivedEmails = Message.query.filter_by(recipient=currentUserEmail)
    messageCount = sentEmails.count() + receivedEmails.count()

    if form.validate_on_submit():
        message = Message(
            sender = currentUserEmail,
            subject=form.subject.data,
            recipient=form.recipient.data,
            content=form.content.data,
	        user_id=current_user.id,
            timestamp = sourceDate.strftime("%x")
        )
        db.session.add(message)
        db.session.commit()

        flash('Email is sent')
        return redirect('/email')
    
    if request.method == 'POST':
            if request.form.get('delAcc') == 'Delete Account':
                db.session.delete(current_user)
                db.session.commit()    
                logout_user()
                return redirect('/home')

            if request.form.get('delEmail') == 'Delete Email':
                deleteEmail = Message.query.get(emailId)
                db.session.delete(deleteEmail)
                db.session.commit()
                return redirect('/email')

            if request.form.get('return') == 'return':
                return redirect('/email')
                
    email = Message.query.get(emailId)
    attachment_name = email.attachment
    return render_template('viewEmail.html', todo_list=todo_list, title='View Email', form=form, currentUserEmail=currentUserEmail, email=email, attachment_name = attachment_name)


@myapp_obj.route('/download_attachment/<int:message_id>/<int:attachment_index>')
@login_required
def download_attachment(message_id, attachment_index):
    message = Message.query.get_or_404(message_id)
    attachments = message.attachments.split(',')
    if attachment_index < len(attachments):
        attachment_path = attachments[attachment_index]
        return send_from_directory(myapp_obj.config['UPLOAD_FOLDER'], attachment_path, as_attachment=True)
    flash('Attachment not found')
    return redirect(url_for('email'))

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
        emailExists = bool(User.query.filter_by(email=form.email.data).first())
        #for field, errors in form.errors.items():
            #for error in errors:
               # flash(f'{field.capitalize()} field: {error}', 'error-message')

        if(emailExists):
            flash(f'Account already exists')
            return redirect("/register")

        else:
            new_user = User(email=form.email.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect("/login")
       
    return render_template('register.html', title='Register', form = form)

@myapp_obj.route("/chat")
@login_required
def chat():
    form = ChatForm()
    current_user_id = current_user.id
    sent_messages = ChatMessage.query.all()
    recipients = Recipient.query.filter_by(user_id=current_user.id, sender_id=current_user.id).all()
    return render_template('chat.html', sent_messages=sent_messages, recipients=recipients, form=form, selected_recipient_id=None)

@myapp_obj.route("/chat/send_message/<int:recipient_id>", methods=["GET", "POST"])
@login_required
def send_message(recipient_id):
    if request.method == "POST":
        message_content = request.form["message"]
        sender_id = current_user.id
        new_message = ChatMessage(content=message_content, sender_id=sender_id, recipient_id=recipient_id, reactMode=False)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))

    return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))

@myapp_obj.route("/chat/<int:recipient_id>", methods=['GET', 'POST'])
@login_required
def chat_with_recipient(recipient_id):
     form = ChatForm()
     recipients = Recipient.query.filter_by(user_id=current_user.id, sender_id=current_user.id).all()
     current_user_id = current_user.id
     messages = ChatMessage.query.filter(
        ((ChatMessage.recipient_id == recipient_id) & (ChatMessage.sender_id == current_user_id)) |
        ((ChatMessage.recipient_id == current_user_id) & (ChatMessage.sender_id == recipient_id))
     ).all()
     user = User.query.get(current_user_id)
     if form.validate_on_submit():
        message_content = form.message.data
        sender_id = current_user_id
        new_message = ChatMessage(content=message_content, sender_id=sender_id, recipient_id=recipient_id)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("chat_with_recipient", recipient_id=recipient_id))
     return render_template('chat.html', recipients=recipients, messages=messages, form=form, selected_recipient_id=recipient_id, user=user)

@myapp_obj.route("/add_recipient", methods=["GET", "POST"])
@login_required
def add_recipient():
    form = AddRecipientForm()
    if form.validate_on_submit():
        recipient_email = form.name.data
        recipient = User.query.filter_by(email=recipient_email).first()
        if recipient:
            user_id = current_user.id
            sender_id = current_user.id
            new_recipient = Recipient(name=recipient_email, user_id=user_id, sender_id=sender_id)
            db.session.add(new_recipient)

            user_as_recipient = Recipient(name=current_user.email, user_id=recipient.id, sender_id=recipient.id)
            db.session.add(user_as_recipient)

            db.session.commit()
            return redirect(url_for("chat"))
        else:
            flash('User email not found')
            return redirect(url_for("chat"))
    return render_template("chat.html", form=form)

@myapp_obj.route('/delete_messages', methods=['POST'])
@login_required
def delete_messages():
    ChatMessage.query.delete()
    db.session.commit()
    return redirect(url_for('chat'))

@myapp_obj.route('/openReactRecieved/<int:id>')
@login_required
def openReactRecieved(id):
    message = ChatMessage.query.get(id)
    message.reactMode = not message.reactMode
    db.session.commit()
    sender_id=message.sender_id
    redirect_URL = "/chat/" + str(sender_id)
    return redirect(redirect_URL)

@myapp_obj.route('/reactHeart/<int:id>')
@login_required
def reactHeart(id):
    message = ChatMessage.query.get(id)
    message.reactMode = not message.reactMode
    message.reaction = "❤️"
    db.session.commit()
    sender_id=message.sender_id
    redirect_URL = "/chat/" + str(sender_id)
    return redirect(redirect_URL)

@myapp_obj.route('/reactAnger/<int:id>')
@login_required
def reactAnger(id):
    message = ChatMessage.query.get(id)
    message.reactMode = not message.reactMode
    message.reaction = "😡"
    db.session.commit()
    sender_id=message.sender_id
    redirect_URL = "/chat/" + str(sender_id)
    return redirect(redirect_URL)

@myapp_obj.route('/reactTear/<int:id>')
@login_required
def reactTear(id):
    message = ChatMessage.query.get(id)
    message.reactMode = not message.reactMode
    message.reaction = "😢"
    db.session.commit()
    sender_id=message.sender_id
    redirect_URL = "/chat/" + str(sender_id)
    return redirect(redirect_URL)

@myapp_obj.route('/reactJoy/<int:id>')
@login_required
def reactJoy(id):
    message = ChatMessage.query.get(id)
    message.reactMode = not message.reactMode
    message.reaction = "😂"
    db.session.commit()
    sender_id=message.sender_id
    redirect_URL = "/chat/" + str(sender_id)
    return redirect(redirect_URL)

@myapp_obj.route('/reactThumbsUp/<int:id>')
@login_required
def reactThumbsUp(id):
    message = ChatMessage.query.get(id)
    message.reactMode = not message.reactMode
    message.reaction = "👍"
    db.session.commit()
    sender_id=message.sender_id
    redirect_URL = "/chat/" + str(sender_id)
    return redirect(redirect_URL)

@myapp_obj.route('/remove_recipient/<int:recipient_id>', methods=['POST'])
@login_required
def remove_recipient(recipient_id):
    recipient = Recipient.query.get(recipient_id)
    if recipient:
        db.session.delete(recipient)
        db.session.commit()
    return redirect(url_for('chat'))

@myapp_obj.route('/addTodo', methods=['POST'])
def addToDo():
    name = request.form.get("name")
    date = request.form.get("date")
    userID = current_user.id
    test = task(name = name, date = date, done = False, edit = False, user_id = userID)
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

