from flask import Flask
from key_finder import get_key
app = Flask(__name__)
user_key = get_key()
@app.route('/')
def hello_world():
    print(user_key)
    return 'Hello, World!'


