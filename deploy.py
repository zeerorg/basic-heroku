from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

from database import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testing')
def testing():
    r = requests.get('https://www.python.org')
    return (r.text)

@app.route('/add/<username>/')
def add_user(username):
    user = User(username, username+"@gmail.com")
    db.session.add(user)
    db.session.commit()
    return "Added " + username

@app.route('/allusers/')
def all_users():
    users = User.query.all()
    all_of_them = ""
    for x in users:
        all_of_them += x.__repr__() + "<br>"
    return all_of_them
