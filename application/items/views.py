from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application.items.models import Item
from application.items.forms import ItemForm
from application.auth.models import User
from application.purchase.models import Purchase

@app.route("/items/", methods=["GET"])
def items_index():
    return render_template("items/list.html", items = Item.query.all())

@app.route("/items/new")
@login_required
def items_form():
    print(current_user.balance)
    return render_template("items/new.html", form = ItemForm())

@app.route("/items", methods=["POST"])
@login_required
def items_create():
    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/new.html", form = form)

    name = form.name.data
    price = form.price.data
    quality = form.quality.data
    item_type = form.item_type.data

    i = Item(name, price, quality, item_type)
    i.account_id = current_user.id
    db.session.add(i)
    db.session.commit()

    return redirect(url_for("items_index"))

@app.route("/items/<item_id>", methods=["POST"])
@login_required
def items_set_price(item_id):
    i = Item.query.get(item_id)
    i.price = request.form["price"]
    db.session().commit()
    return redirect(url_for("items_index"))

@app.route("/items/purchase/<item_id>", methods=["POST"])
@login_required
def items_purchase(item_id):
    i = Item.query.get(item_id)

    if not i:
        flash("Item not found")
        return redirect(url_for("items_index"))

    user = current_user

    if(i.price > user.balance):
        flash("Not enough balance")
        return redirect(url_for("items_index"))

    p = Purchase(current_user.id, i.id)
    db.session.add(p)
    i.sold = True
    user.balance -= i.price
    db.session().commit()
    flash("Purchase successfull")
    return redirect(url_for("items_index"))
    