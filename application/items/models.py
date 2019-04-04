from application import db

### MODEL ###

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    item_float = db.Column(db.Float, nullable=False) #Describes how good the item is from 0-1. 1 is perfect quality and 0 is worst quality
    item_type = db.Column(db.String(144), nullable=False)
    sold = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, price, item_float, item_type):
        self.name = name
        self.price = price
        self.item_float = item_float
        self.item_type = item_type
        self.sold = False