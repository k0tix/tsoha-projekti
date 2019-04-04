from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.auth.models import User

@app.route("/user/", methods=["GET"])
@login_required
def user_index():
    return render_template("user/user.html", user=current_user)
