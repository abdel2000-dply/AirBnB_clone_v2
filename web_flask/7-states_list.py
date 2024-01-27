#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a list of states """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session (after each request) """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
