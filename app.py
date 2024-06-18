from flask import Flask
from key_finder import get_key
app = Flask(__name__)

@app.route('/')
def hello_world():
    user_key = get_key()
    return 'Hello, World!'


