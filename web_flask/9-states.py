#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ def doc """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """ /states and /states/<id> """
    not_found = False
    if id is not None:
        states = storage.all(State, id)
        with_id = True
        if len(states) == 0:
            not_found = True
    else:
        states = storage.all(State)
        with_id = False
        return render_template('9-states.html', states=states,
                                with_id=with_id, not_found=not_found)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session (after each request) """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
