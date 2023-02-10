#!/usr/bin/env python3
from datetime import datetime
from mkt_app import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """Load user."""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """
    This class represents a User object in the system.

    It contains attributes such as id, username, email, image_file
    and password, which are all stored in the database.
    The class also has a one-to-many relationship with the Post object
    through the 'posts' attribute. The repr method returns a
    string representation of the User object.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        """Return a string representation of the User object."""
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    """This class represents a Post object in the system.

    It contains attributes such as id, title, date_posted, content,
    and price, which are all stored in the database.
    The class also has a one-to-many relationship with the User object
    through the 'user_id' attribute. The repr method returns a
    string representation of the Post object.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Return a string representation of the Post object."""
        return f"Post('{self.title}', '{self.date_posted}')"
