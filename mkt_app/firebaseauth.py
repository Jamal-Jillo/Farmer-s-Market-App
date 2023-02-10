#!/usr/bin/env python3
import pyrebase
from getpass import getpass

firebaseConfig = {
  'apiKey': "AIzaSyBchLje-msUalYp8wkXOUJWdsdrV7asRl4",
  'authDomain': "mkt-app-d1972.firebaseapp.com",
  'projectId': "mkt-app-d1972",
  'storageBucket': "mkt-app-d1972.appspot.com",
  'messagingSenderId': "134565436102",
  'appId': "1:134565436102:web:f554ea2432834f15d5d5c7"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

email = input("Enter your email: ")
password = getpass("Enter your password: ")

user = auth.create_user_with_email_and_password(email, password)

print("User created successfully!")
