#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """display hbnb_filters from static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities
    )


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session (after each request) """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
