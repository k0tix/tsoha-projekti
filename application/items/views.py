from application import app, db
from flask import redirect, render_template, request, url_for, jsonify
from application.items.models import Item, item_schema, items_schema

@app.route("/api/items/", methods=["GET"])
def items_index():
    items = items_schema.dump(Item.query.all()).data
    return jsonify(items)
    #return render_template("items/list.html", items = Item.query.all())

@app.route("/api/items/", methods=["POST"])
def items_form():
    json = request.get_json()
    i = Item(json["name"], json["price"], json["item_float"])
    db.session().add(i)
    db.session.commit()
    return jsonify(item_schema.dump(i).data)

@app.route("/api/items/<item_id>/", methods=["PUT"])
def items_set_price(item_id):
    json = request.get_json()
    t = Item.query.get(item_id)
    t.price = request.get_json()['price']
    db.session().commit()
    return jsonify(item_schema.dump(t).data)