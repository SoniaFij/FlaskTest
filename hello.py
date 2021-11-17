from os import name
from flask import (
    Flask, 
    url_for, 
    render_template, 
    redirect
)
#from werkzeug import datastructures
from wtforms.validators import Email

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator
import os

app = Flask(__name__)
#app.secret_key = "any-string-you-want-just-keep-it-secret"

SECRET_KEY = os.urandom(32)
app.secret_key = settings.SECRET_KEY

#SECRET_KEY = os.urandom(32)
#app.config['SECRET_KEY'] = SECRET_KEY
 
class contact_form(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
    submit = SubmitField(label="Log In")




#from .form import contact_form


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/test')
def hello_test():
    return 'test'

@app.route('/home')
def home():
    return '<h1>Hello, World!</h1>'


@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

@app.route('/article/<article_name>')
def article(article_name):
  return '''
  <a href="/">Return back to home page</a>
  '''


@app.route('/contact', methods=["GET", "POST"])
def contact():
    cform=contact_form()
    if cform.validate_on_submit():
        print(f"Name:{cform.name.data}",
              "E-mail:{cform.email.data}",
              "message:{cform.message.data}")
    else:
        print("Invalid Credentials")

    return render_template("contact.html", form=cform)

 
 
if __name__ == '__main__':
    app.run(debug=True)

