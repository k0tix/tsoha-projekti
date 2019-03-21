# Importing Flask
from flask import Flask
app = Flask(__name__)

# Importing SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Uses marketplace.db SQLite database. 
# File is located in application folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marketplace.db"
# Log all SQL queries
app.config["SQLALCHEMY_ECHO"] = True

# Create db object for database handling
db = SQLAlchemy(app)

# Read views from application folder
from application import views

from application.items import views
from application.items import models

# Create all database tables
db.create_all()