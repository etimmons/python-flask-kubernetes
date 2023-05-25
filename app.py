from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Hello, Test!</p>"
