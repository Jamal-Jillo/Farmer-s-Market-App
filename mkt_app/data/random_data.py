from faker import Faker
from mkt_app.models import db, User, Post
import random
from datetime import datetime, timedelta
import json

fake = Faker()

# create 10 random users
for i in range(10):
    username = fake.user_name()
    email = fake.email()
    image_file = 'default.jpg'
    password = fake.password()
    user = User(username=username, email=email, image_file=image_file,
                password=password)
    db.session.add(user)
    db.session.commit()

# get all users from the database
users = User.query.all()

# create 50 random posts
for i in range(50):
    title = fake.sentence()
    date_posted = datetime.utcnow() - timedelta(days=random.randint(0, 10))
    content = fake.text()
    price = round(random.uniform(1, 10), 2)
    user_id = random.choice(users).id
    post = Post(title=title, date_posted=date_posted, content=content,
                price=price, user_id=user_id)
    db.session.add(post)
    db.session.commit()

serialized_users = []
for user in users:
    serialized_user = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'image_file': user.image_file,
        'password': user.password,
        'posts': [post.id for post in user.posts]
    }
    serialized_users.append(serialized_user)

# serialize posts
posts = Post.query.all()
serialized_posts = []
for post in posts:
    serialized_post = {
        'id': post.id,
        'title': post.title,
        'date_posted': post.date_posted.isoformat(),
        'content': post.content,
        'price': post.price,
        'user_id': post.user_id
    }
    serialized_posts.append(serialized_post)

# combine serialized users and posts
serialized_data = {
    'users': serialized_users,
    'posts': serialized_posts
}

# write to a file
with open('data.json', 'w') as f:
    json.dump(serialized_data, f)
