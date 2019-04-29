# Importing Flask
from flask import Flask
app = Flask(__name__)

# Importing Bcrypt
from flask_bcrypt import Bcrypt
flask_bcrypt = Bcrypt(app)

# Importing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Uses marketplace.db SQLite database. 
# File is located in application folder

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marketplace.db"
    # Log all SQL queries
    app.config["SQLALCHEMY_ECHO"] = True

# Create db object for database handling
db = SQLAlchemy(app)

# Login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

# Roles in login_required
from functools import wraps

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
            
            if current_user.is_authenticated is False:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ADMIN":
                unauthorized = True
                
                for user_role in current_user.roles():
                    if user_role == role:
                        unauthorized = False
                        break

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

# Read views from application folder
from application import views

from application.items import views
from application.items import models

from application.auth import views
from application.auth import models

from application.user import views

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create all database tables
try:
    db.create_all()
except:
    pass