#!/usr/bin/env python3
"""Routes for the Farmers-Market application."""


from flask import render_template, url_for, flash, redirect
from mkt_app import app, db, bcrypt
from mkt_app.forms import RegistrationForm, LoginForm, PostForm
from mkt_app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def index():
    """Return the index page."""
    posts = Post.query.all()
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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)  # hashing the password
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        # If the form is valid, the validate_on_submit() method returns True
        # and the user is redirected to the home page, 'success' is a
        # bootstrap class
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login a user."""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password',
                  'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    """Create a new post."""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, price=form.price.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('create_post.html', title='New Post', form=form)


@app.route('/logout')
def logout():
    """Logout a user."""
    logout_user()  # !Dont forget to change the logout button in templates
    return redirect(url_for('index'))
