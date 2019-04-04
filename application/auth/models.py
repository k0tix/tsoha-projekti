from application import db, flask_bcrypt

### Model ###

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

    items = db.relationship("Item", backref="account", lazy=True)

    def __init__(self, name, username, email, pwd):
        self.name = name
        self.username = username
        self.email = email
        self.pwd_hash = flask_bcrypt.generate_password_hash(pwd).decode("utf-8")
        self.balance = 10000000
    
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True