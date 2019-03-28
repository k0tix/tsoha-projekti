# Importing Flask
from flask import Flask
app = Flask(__name__, static_folder='./static/dist', template_folder='./static')

# Importing Bcrypt
from flask_bcrypt import Bcrypt
flask_bcrypt = Bcrypt(app)

# Importing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Uses marketplace.db SQLite database. 
# File is located in application folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marketplace.db"
# Log all SQL queries
app.config["SQLALCHEMY_ECHO"] = True

# Create db object for database handling
db = SQLAlchemy(app)

# Importing Marshmallow
from flask_marshmallow import Marshmallow

ma = Marshmallow(app)

# Read views from application folder
from application import views

from application.items import views
from application.items import models

from application.auth import views
from application.auth import models

# Login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create all database tables
db.create_all()