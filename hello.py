# https://diyprojects.io/flask-bootstrap-html-interface-effortless-python-projects/#.YZbRdtDMJPZ

from os import name
from flask import (
    Flask, 
    url_for, 
    render_template, 
    redirect, 
    request
)
from flask.templating import render_template_string
from wtforms.fields import form

from wtforms.validators import Email

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator
import os

distance = 0.1

HTML_PAGE = '''

<html>\
    <body>\
        <strong>TEST</strong>\
    </body>\
</html>
'''


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/test')
def test():
    return render_template_string(HTML_PAGE)

@app.route('/home')
def home():
    return render_template('test_subfolder/page.html')

@app.route('/jinja')
def jinja():
    return render_template('test_subfolder/page2.html', status = True, temperature = 24)


@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

@app.route('/article/<article_name>')
def article(article_name):
  return '''
  <a href="/">Return to home page</a>
  '''

@app.route('/threed')
def threed():
    global distance
    return render_template('test_subfolder/page3.html', distance=distance)

@app.route('/setdistance', methods=["POST"])
def setdistance():
    global distance
    distance=float(request.form["distance"])
    print ("set distance to", distance)
    return redirect (request.referrer)


 
if __name__ == '__main__':
    app.run(debug=True)

