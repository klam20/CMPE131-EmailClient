from flask_wtf import FlaskForm
from app import *
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# empty class, passes form
class ChatForm(FlaskForm):
    pass

class AddRecipientForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Add Recipient")
