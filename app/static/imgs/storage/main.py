#!/usr/bin/python3

"""This module contains the main class for the storage engine."""

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """This class represents the users table."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(80), nullable=False)

    def __init__(self, username, email, password):
        """Initialize the user."""
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        """Return a string representation of the User."""
        return f"(User: {self.username}, {self.email}))"


class User_role(Base):
    """This class represents the user_roles table."""

    __tablename__ = 'user_roles'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey("roles.id") nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __init__(self, role_id, user_id):
        """Initialize the user role."""
        self.role_id = role_id
        self.user_id = user_id

    def __repr__(self):
        """Return a string representation of the User role."""
        return f"(User role: {self.role_id}, {self.user_id}))"


class Role(Base):
    """This class represents the roles table."""

    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    role = Column(String(30), nullable=False)

    def __init__(self, role):
        """Initialize the role."""
        self.role = role

    def __repr__(self):
        """Return a string representation of the Role."""
        return f"(Role: {self.role}))"


class Product(Base):
    """This class represents the products table."""

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)
    classification = Column(String(30))
    market_id = Column(Integer, ForeignKey("markets.id"), nullable=False)

    def __init__(self, name, description, price, classification, market_id):
        """Initialize the product."""
        self.name = name
        self.description = description
        self.price = price
        self.classification = classification
        self.market_id = market_id

    def __repr__(self):
        """Return a string representation of the Product."""
        return f"(Product: {self.name}, {self.description}, {self.price}, {self.classification}, {self.market_id}))"


class Market(Base):
    """This class represents the markets table."""

    __tablename__ = 'markets'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    location = Column(String(255))
    description = Column(String(255))

    def __init__(self, name, location, description):
        """Initialize the market."""
        self.name = name
        self.location = location
        self.description = description

    def __repr__(self):
        """Return a string representation of the Market."""
        return f"(Market: {self.name}, {self.location}, {self.description}00))"


class Price(Base):
    """This class represents the prices table."""

    __tablename__ = 'prices'

    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    market_id = Column(Integer, ForeignKey("markets.id"), nullable=False)
    date = Column(Date, nullable=False)
    unit = Column(Integer, nullable=False)

    def __init__(self, price, product_id, market_id, date, unit):
        """Initialize the price."""
        self.price = price
        self.product_id = product_id
        self.market_id = market_id
        self.date = date
        self.unit = unit

    def __repr__(self):
        """Return a string representation of the Price."""
        return f"(Price: {self.price}, {self.product_id}, {self.market_id}, {self.date}, {self.unit}))"


engine = create_engine('sqlite:///farmers_market.db')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User('John Doe', 'JD', 'Jd@gmail')
user2 = User('Jane Doe', 'JD', 'Jd@gmail')

product1 = Product('Tomatoes', 'Red', 10.00, 'Vegetable', 1)
product2 = Product('Onions', 'White', 5.00, 'Vegetable', 1)

session.add(user1)
session.add(user2)
session.add(product1)
session.add(product2)
session.commit()

results = session.query(Product).all()
print(results)
