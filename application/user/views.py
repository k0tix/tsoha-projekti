
from flask import redirect, render_template, request, url_for, flash
from flask_login import current_user

from application import app, db, login_required
from application.auth.models import User

@app.route("/user/<user_username>", methods=["GET"])
def user_index(user_username):
    user = User.query.filter_by(username=user_username).first()

    if not user:
        flash("No user was found")
        return redirect(url_for("items_index"))

    if current_user.is_anonymous == True:
        return render_template("user/preview.html", user=user)
    elif current_user.username == user_username:
        purchases = User.find_users_purchases(current_user.id)
        total = User.get_total_money_used(current_user.id)
        if total is None:
            total = 0
        average_quality = User.get_average_quality_purchased(current_user.id)
        return render_template("user/user.html", user=current_user, purchases=purchases, total_money=total, average_quality=average_quality)
    else:
        return render_template("user/preview.html", user=user)

@app.route("/user/ban/<user_id>", methods=["POST"])
@login_required(role="ADMIN")
def user_ban(user_id):
    user = User.query.get(user_id)
    user.banned = True
    db.session.commit()

    return redirect(url_for("user_index", user_username=user.username))
