#!/usr/bin/env python3
"""Routes for the Farmers-Market application."""


from flask import render_template, url_for, flash, redirect, request, abort, jsonify
from sqlalchemy import or_
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


@app.route('/landing')
def landing_page():
    """Return the landing page."""
    return render_template('landingpage.html')

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
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@app.route('/logout')
def logout():
    """Logout a user."""
    logout_user()  # !Dont forget to change the logout button in templates
    return redirect(url_for('index'))


@app.route("/post/<int:post_id>")
def post(post_id):
    """Display specific post."""
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.price = form.price.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.price.data = post.price
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('index'))


@app.route('/search')
def search():
    query = request.args.get('query')
    results = []

    if query:
        # search for posts and users that match the query
        posts = Post.query.filter(Post.title.ilike(f'%{query}%')).all()
        users = User.query.filter(User.username.ilike(f'%{query}%')).all()

        # check if any results were found
        if not posts and not users:
            flash(f"No results found for '{query}'", 'danger')
            return redirect(url_for('search'))

        # combine the results into a single list
        results = posts + users

    return render_template('search_results.html', results=results, query=query)


# used this piece of code to push random data to the database
@app.route('/push_data', methods=['POST'])
def push_data():
    data = request.get_json()
    users = data['users']
    posts = data['posts']

    # Add users to the database
    for user_data in users:
        user = User(username=user_data['username'], email=user_data['email'], image_file=user_data['image_file'], password=user_data['password'])
        db.session.add(user)
        db.session.commit()
        
    # Add posts to the database
    for post_data in posts:
        post = Post(title=post_data['title'], date_posted=post_data['date_posted'], content=post_data['content'], price=post_data['price'], user_id=post_data['user_id'])
        db.session.add(post)
        db.session.commit()
    
    return jsonify({'message': 'Data added successfully'})
# end of the code


@app.route('/insights', methods=['GET', 'POST'])
def insights():
    """Show insights."""
    return render_template('insights.html')
