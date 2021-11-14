from flask import Flask
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class contact_form(FlaskForm):
    name = StringField(
        "Name",
        [DataRequired()]

    )

    #email = StringField(
     #   "Email",
      #  [
       # Email(message=("Not a valid email address.")),
       # DataRequired()
       # ]
    #)

    body = TextAreaField(
        "Message",
        [
            DataRequired(),
            Length(min=4,
            message=("Your mesage is too short"))
        ]

    )

    recaptcha = RecaptchaField()
    submit = SubmitField("Submit")

    
