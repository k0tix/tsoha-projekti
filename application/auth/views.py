from flask import request, redirect, jsonify
from flask_login import login_user, logout_user

from application import app, db, flask_bcrypt
from application.auth.models import User

@app.route("/api/auth/login", methods=["POST"])
def auth_login():
    json = request.get_json()
    user = User.query.filter_by(username=json["username"]).first()

    login = flask_bcrypt.check_password_hash(user.pwd_hash, json["password"])
    if not login:
        return jsonify({"error": "login failed"})

    login_user(user)
    return jsonify({"message": "logged in succesfully"})

@app.route("/api/auth/logout")
def auth_logout():
    logout_user()
    return jsonify({"message": "logged out"})

@app.route("/api/auth/register", methods=["POST"])
def auth_register():
    json = request.get_json()
    u = User(json["name"], json["username"], json["password"])
    db.session().add(u)
    db.session().commit()
    return jsonify({"message": "new account created"})