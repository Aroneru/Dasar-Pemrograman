# Muhamamad Yermi Rachman
# J0403231034

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Flask!</p>"
