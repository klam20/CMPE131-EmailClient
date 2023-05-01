from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class sendEmailForm(FlaskForm):
    recipient = StringField('Recipient', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    sendEmail = SubmitField('Send Email')

