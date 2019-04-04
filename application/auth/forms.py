from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("name")
    username = StringField("username")
    email = StringField("email")
    password = PasswordField("password")

    class Meta:
        csrf = False