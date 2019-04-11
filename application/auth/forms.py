from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired("Please enter your username.")])
    password = PasswordField("password", validators=[InputRequired("Please enter your password.")])

    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("name", validators=[InputRequired("Please enter your name.")])
    username = StringField("username", validators=[InputRequired("Please enter your username.")])
    email = EmailField("email", validators=[InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField("password", validators=[InputRequired("Please enter your password.")])
    role = StringField("role", validators=[InputRequired("Please enter a role")])

    class Meta:
        csrf = False