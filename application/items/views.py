from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user

from application.items.models import Item
from application.items.forms import ItemForm
from application.auth.models import User
from application.purchase.models import Purchase

@app.route("/items/", methods=["GET"])
def items_index():
    i = Item.find_items_with_username()
    return render_template("items/list.html", items = i)

@app.route("/items/new")
@login_required
def items_form():
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

@app.route("/items/<item_id>", methods=["GET"])
def items_view(item_id):
    i = Item.query.join(User, Item.account_id==User.id).add_columns(User.username, User.banned).filter(Item.id == item_id).first()

    username = i[1]
    banned = i[2]
    i = i[0]

    if not i:
        flash("item was not found")
        redirect(url_for("items_index"))

    if current_user.is_anonymous is True or i.account_id != current_user.id:
        return render_template("items/view.html", item=i, username=username, banned=banned)
    else:
        form = ItemForm()
        form.name.data = i.name
        form.price.data = i.price
        form.item_type.data = i.item_type
        form.quality.data = i.quality
        return render_template("items/user_view.html", form = form, item=i)
    
@app.route("/items/<item_id>", methods=["POST"])
@login_required
def items_update(item_id):
    i = Item.query.get(item_id)

    if i.account_id != current_user.id:
        flash("You cannot edit other accounts items")
        return redirect(url_for("items_index"))

    form = ItemForm(request.form)

    if not form.validate():
        return render_template("items/user_view.html", form = form)

    i.name = form.name.data
    i.price = form.price.data
    i.item_type = form.item_type.data
    i.quality = form.quality.data

    db.session().commit()

    return redirect(url_for("items_index"))

@app.route("/items/delete/<item_id>", methods=["POST"])
@login_required
def items_delete(item_id):
    i = Item.query.get(item_id)

    if not i:
        flash("Item not found")
    elif i.sold:
        flash("Item has already been sold")
    elif i.account_id == current_user.id or current_user.role == "ADMIN":
        db.session.delete(i)
        db.session.commit()
        flash("Item deleted successfully")
    else:
        flash("Something went wrong")

    return redirect(url_for("items_index"))

@app.route("/items/purchase/<item_id>", methods=["POST"])
@login_required
def items_purchase(item_id):
    i = Item.query.get(item_id)

    if not i:
        flash("Item not found")
        return redirect(url_for("items_index"))

    user = current_user
    seller = User.query.get(i.account_id)

    if user.id == seller.id:
        flash("You cannot buy your own item")
        return redirect(url_for("items_index"))

    if i.price > user.balance:
        flash("Not enough balance")
        return redirect(url_for("items_index"))

    p = Purchase(current_user.id, i.id)
    db.session.add(p)
    i.sold = True
    
    user.balance -= i.price
    seller.balance += i.price

    db.session().commit()
    flash("Purchase successfull")
    return redirect(url_for("items_index"))
    