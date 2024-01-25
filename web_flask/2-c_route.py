#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display 'HBNB'"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text"""
    return 'C {}'.format(escape(text.replace('_', ' ')))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
