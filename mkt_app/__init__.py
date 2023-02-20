#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '5367eac0ee1931204394865b0ad6be06'
# This is a random string of characters that is used to encrypt the form data
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# The database URI is the location of the database file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

app.app_context().push()  # Flask-SQLAlchemy requires an application context

from mkt_app import routes

if __name__ == '__main__':
    db.create_all(app=app)
