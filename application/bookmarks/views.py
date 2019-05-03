from application import app, db
from flask import redirect, flash, url_for, render_template, request
from flask_login import login_required, current_user

from application.items.models import Item
from application.auth.models import User
from application.bookmarks.models import Bookmark

@app.route("/bookmarks/<item_id>", methods=["POST"])
@login_required
def add_bookmark(item_id):
    i = Item.query.get(item_id)

    if not i:
        flash("Item was not found")
        return redirect(url_for("items_index"))
    
    if current_user.is_anonymous is True:
        flash("You need to log in to add a bookmard")
        return redirect(url_for("items_index"))

    b = Bookmark.query.filter_by(item_id=item_id, account_id=current_user.id).first()

    if b:
        flash("You have already bookmarked that item")
        return redirect(url_for("items_index"))

    name = request.form.get("name")

    bm = Bookmark(name, item_id, current_user.id)
    db.session.add(bm)
    db.session.commit()

    return redirect(url_for("items_index"))
    
@app.route("/bookmarks", methods=["GET"])
@login_required
def list_bookmarks():
    bookmarks = Bookmark.query.join(Item, Bookmark.item_id==Item.id).add_columns(Item.name).filter(Bookmark.account_id == current_user.id).all()

    return render_template("bookmarks/list.html", bookmarks=bookmarks)

@app.route("/bookmarks/delete/<item_id>", methods=["POST"])
@login_required
def bookmarks_delete(item_id):
    bk = Bookmark.query.get((item_id, current_user.id))

    if not bk:
        flash("Bookmark was not found")
    else:
        db.session.delete(bk)
        db.session.commit()
        flash("Bookmark deleted")

    return redirect(url_for("list_bookmarks"))

@app.route("/bookmarks/update/<item_id>", methods=["POST"])
@login_required
def update_bookmark(item_id):
    i = Item.query.get(item_id)

    if not i:
        flash("Item was not found")
        return redirect(url_for("items_index"))
    
    if current_user.is_anonymous is True:
        flash("You need to log in to add a bookmard")
        return redirect(url_for("items_index"))

    b = Bookmark.query.filter_by(item_id=item_id, account_id=current_user.id).first()

    b.name = request.form.get("name")
    db.session.commit()

    return redirect(url_for("list_bookmarks"))