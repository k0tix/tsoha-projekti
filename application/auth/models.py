from application import db, flask_bcrypt

from sqlalchemy.sql import text

# Model 

class User(db.Model):
    
    __tablename__= "account"

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                                onupdate=db.func.current_timestamp())
    
    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    email = db.Column(db.String(144), nullable=False)
    pwd_hash = db.Column(db.String(144), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    banned = db.Column(db.Boolean, nullable=False)
    role = db.Column(db.String(144), nullable=False)

    items = db.relationship("Item", backref="account", lazy=True)

    def __init__(self, name, username, email, pwd, role):
        self.name = name
        self.username = username
        self.email = email
        self.pwd_hash = flask_bcrypt.generate_password_hash(pwd).decode("utf-8")
        self.balance = 10000000
        self.banned = False
        self.role = role
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role

    @staticmethod
    def find_users_purchases(user_id):
        stmt = text("SELECT Item.name, Item.price, Purchase.date_created FROM Item"
                    " JOIN Purchase ON Purchase.item_id = Item.id"
                    " WHERE Purchase.account_id = :acc_id").params(acc_id=user_id)

        res = db.engine.execute(stmt)

        response = [{"name":row[0], "price":row[1], "date":row[2]} for row in res]

        return response

    @staticmethod
    def get_total_money_used(user_id):
        stmt = text("SELECT SUM(Item.price) FROM Item"
                    " JOIN Purchase ON Purchase.item_id = Item.id"
                    " WHERE Purchase.account_id = :acc_id").params(acc_id=user_id)

        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

    @staticmethod
    def get_average_quality_purchased(user_id):
        stmt = text("SELECT AVG(Item.quality) FROM Item"
                    " JOIN Purchase ON Purchase.item_id = Item.id"
                    " WHERE Purchase.account_id = :acc_id").params(acc_id=user_id)

        res = db.engine.execute(stmt)

        for row in res:
            return row[0]

