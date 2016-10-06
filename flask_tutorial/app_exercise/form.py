from flask import Flask
from flask_wtf import Form
from wtforms import TextField, SubmitField, PasswordField

class SignUpForm(Form):
    name = TextField("Name")
    surname = TextField("Surname")
    email = TextField("Email")
    password = PasswordField("Password")
    submit = SubmitField("Send")
