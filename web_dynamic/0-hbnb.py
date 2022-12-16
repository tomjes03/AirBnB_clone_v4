#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from flask import Flask, render_template
import uuid;

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
port = 5000
host = '0.0.0.0'

# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


# Flask page rendering
@app.teardown_appcontext
def close_db(error):
    """ AFter each request, this method removes the current SQLAlchemy Session """
    storage.close()


@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """ HBNB is alive! """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    return render_template('0-hbnb.html',
                           cache_id=uuid.uuid4(),
                           states=st_ct,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    """ Main Function """
    app.run(host=host, port=port)
