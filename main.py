#export FLASK_APP=main.py
from flask import Flask

app = Flask(__name__)   #name of this file

@app.route('/')
def hello():
    return 'Hello world'
