from application import db, ma

### MODEL ###

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    item_float = db.Column(db.Float, nullable=False)

    def __init__(self, name, price, item_float):
        self.name = name
        self.price = price
        self.item_float = item_float

### SCHEMA ###

class ItemSchema(ma.ModelSchema):
    class Meta:
        model = Item

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)