#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ Display a list of states """
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Displays cities of a state"""
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session (after each request) """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
