from flask_wtf import FlaskForm
from app import *
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChatForm(FlaskForm):
    name = StringField('Recipient Name', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')

class AddRecipientForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Add Recipient")
