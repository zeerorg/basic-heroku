from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/testing')
def testing():
    r = requests.get('https://www.python.org')
    return (r.text)