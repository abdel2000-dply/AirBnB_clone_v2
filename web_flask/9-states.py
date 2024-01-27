#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def display_state(id):
    """Displays a HTML page with a list of City objects linked to the State"""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    else:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session (after each request) """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
