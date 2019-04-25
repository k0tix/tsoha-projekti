from application import db

from sqlalchemy.sql import text

### MODEL ###

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quality = db.Column(db.Float, nullable=False) #Describes how good the item is from 0-1. 1 is perfect quality and 0 is worst quality
    item_type = db.Column(db.String(144), nullable=False)
    sold = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name, price, quality, item_type):
        self.name = name
        self.price = price
        self.quality = quality
        self.item_type = item_type
        self.sold = False

    @staticmethod
    def find_items_with_username():
        stmt = text("SELECT Item.id, Item.name, Item.price, Item.quality, Item.item_type, Item.sold, Account.username FROM Item"
                    " JOIN Account ON Account.id = Item.account_id"
                    " WHERE Item.sold = FALSE")

        res = db.engine.execute(stmt)

        response = [{"id": row[0], "name": row[1], "price": row[2], "quality": row[3], "item_type": row[4], "sold": row[5], "seller_username": row[6]} for row in res]

        return response