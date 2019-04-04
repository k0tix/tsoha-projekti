from application import db

### MODEL ###

class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey('item.id'),
                            nullable=False)

    def __init__(self, account_id, item_id):
        self.account_id = account_id
        self.item_id = item_id