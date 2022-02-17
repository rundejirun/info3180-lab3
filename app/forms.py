from email.message import Message
from multiprocessing.spawn import import_main_path
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name= StringField ('Name', validators=[DataRequired()])
    email= StringField ('E-mail', validators=[DataRequired(), Email()])
    subject= StringField('Subject', validators=[DataRequired()])
    message= TextAreaField('Message', validators=[DataRequired()])