from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item
import json

@app.route("/items/", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
def items_form():
    return render_template("items/new.html")

@app.route("/items/<item_id>/", methods=["POST"])
def items_set_price(item_id):

    t = Item.query.get(item_id)
    t.price = request.form.get("price")
    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/", methods=["POST"])
def items_create():
    i = Item(request.form.get("name"), request.form.get("price"), request.form.get("float"))
    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))