from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    content = StringField('Content')
    subject = StringField('Subject')
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    sendEmail = SubmitField('Send Email')
    logOut = SubmitField('Log-Out')
    logIn = SubmitField('Log-In')
    signUp = SubmitField('Sign-Up')

    