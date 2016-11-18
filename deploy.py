from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testing')
def testing():
    r = requests.get('https://www.python.org')
    return (r.text)