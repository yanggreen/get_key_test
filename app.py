from flask import Flask
from key_finder import get_key
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000)

