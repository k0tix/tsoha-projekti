from application import db

class Bookmark(db.Model):
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)

    item_id = db.Column(db.Integer, db.ForeignKey("item.id"), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    __table_args__ = (
        db.PrimaryKeyConstraint('item_id', 'account_id'),
        {},
    )

    def __init__(self, name, item_id, account_id):
        self.name = name
        self.item_id = item_id
        self.account_id = account_id