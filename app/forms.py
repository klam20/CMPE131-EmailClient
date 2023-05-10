from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, MultipleFileField
from wtforms.validators import DataRequired, Email, EqualTo

class sendEmailForm(FlaskForm):
    recipient = StringField('Recipient', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    sendEmail = SubmitField('Send Email')
    attachments = MultipleFileField('Attachments')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
