from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator
#import os



app = Flask(__name__)
#app.secret_key = "any-string-you-want-just-keep-it-secret"

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
 
class contact_form(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
    submit = SubmitField(label="Log In")



    

    
