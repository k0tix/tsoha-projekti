from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.auth.models import User

@app.route("/user/", methods=["GET"])
@login_required
def user_index():
    purchases = User.find_users_purchases(current_user.id)
    total = User.get_total_money_used(current_user.id)
    average_quality = User.get_average_quality_purchased(current_user.id)
    return render_template("user/user.html", user=current_user, purchases=purchases, total_money=total, average_quality=average_quality)
