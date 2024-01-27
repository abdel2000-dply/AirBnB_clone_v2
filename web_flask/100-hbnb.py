#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State
from models.place import Place

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display hbnb"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    places = storage.all(Place).values()
    return render_template(
        '100-hbnb.html', states=states, amenities=amenities, places=places
    )


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session (after each request) """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
