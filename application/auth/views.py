from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, flask_bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods=["POST", "GET"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/login.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/login.html", form = form)

    user = User.query.filter_by(username=form.username.data).first()

    if not user:
        return render_template("auth/login.html", form = LoginForm(), error = "Bad username or password")

    login = flask_bcrypt.check_password_hash(user.pwd_hash, form.password.data)

    if not login:
        return render_template("auth/login.html", form = LoginForm(), error = "Bad username or password")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register", methods=["POST", "GET"])
def auth_register():

    if request.method == "GET":
        return render_template("auth/register.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form, error = "Bad input")

    u = User(form.name.data, form.username.data, form.email.data, form.password.data, form.role.data)
    db.session().add(u)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)
    return redirect(url_for("index"))