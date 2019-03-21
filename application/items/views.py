from application import app, db
from flask import redirect, render_template, request, url_for
from application.items.models import Item

@app.route("/items/", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new/")
def items_form():
    return render_template("items/new.html")

@app.route("/items/", methods=["POST"])
def items_create():
    i = Item(request.form.get("name"), request.form.get("price"), request.form.get("float"))
    db.session().add(i)
    db.session().commit()

    return redirect(url_for("items_index"))