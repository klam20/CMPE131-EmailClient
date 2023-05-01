from app import myapp_obj, db, mail
from app.forms import sendEmailForm
from flask import render_template, flash, redirect, url_for
from flask_mail import Message as MailMessage
from flask_login import login_required, current_user
from app.models import Message, User

@myapp_obj.route("/")
@myapp_obj.route("/home")
def home():
    return render_template('home.html')

@login_required
@myapp_obj.route('/email', methods=['GET', 'POST'])
def email():
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
    return render_template('email.html', title='Send Email', form=form)

@myapp_obj.route("/login")
def login():
    return render_template('login.html')

@myapp_obj.route("/register")
def register():
    return render_template('register.html')
