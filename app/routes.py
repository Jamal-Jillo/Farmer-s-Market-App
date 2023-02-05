#!/usr/bin/python3
"""Routes for the application."""

from flask import render_template, request, redirect, url_for
import app
from app.storage import Product
from app.storage import Market


@app.route('/products')
def show_products():
    """Display all products."""
    products = Product.query.all()
    return render_template('products.html', products=products)


@app.route('/market')
def show_market():
    """Display all markets."""
    markets = Market.query.all()
    return render_template('market.html', markets=markets)

