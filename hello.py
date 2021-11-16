from flask import (
    Flask, 
    url_for, 
    render_template, 
    redirect
)
from werkzeug import datastructures


from .form import contact_form


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
        print(f"Name:{cform.name.data}, E-mail:{cform.email.data})
        message:{cform.message.data}")
    return render_template("contact.html", form=cform)

 
 
if __name__ == '__main__':
    app.run(debug=True)

