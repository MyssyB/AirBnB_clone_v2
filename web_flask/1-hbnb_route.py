#!/usr/bin/python3
"""Flask script to start a web app"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Say something on start
    listening: 0.0.0.0
    port: 5000
    """

    return "Hello HBNH!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB output"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0' port=5000)
