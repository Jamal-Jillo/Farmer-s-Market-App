#!/usr/bin/env python3
"""Routes for the Farmers-Market application."""


from flask import render_template, url_for, flash, redirect
from mkt_app import app
from mkt_app.forms import RegistrationForm, LoginForm, PostForm
from mkt_app.models import User, Post



posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2023',
        'price': '10.00'
    },
    {
        'author': 'Jane Doe',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2023',
        'price': '20.00'
    }
]


@app.route('/')
@app.route('/home')
def index():
    """Return the index page."""
    return render_template('index.html', posts=posts)


@app.route('/about')
def about_page():
    """Return the index page."""
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])
# The methods argument is used to specify the HTTP methods that the route
# should accept
def register():
    """Register a new user."""
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        # If the form is valid, the validate_on_submit() method returns True
        # and the user is redirected to the home page, 'success' is a
        # bootstrap class
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    """Login a user."""
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title='New Post', form=form)
