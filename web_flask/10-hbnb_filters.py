#!/usr/bin/python3
""" script that starts a Flask web application """

from flask import Flask, render_template


from models import storage
from models.amenity import amenity
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    all_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    all_states.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    for state in all_states:
        state.cities.sort(key=lambda x: x.name)
    ctxt = {
            'states': all_states,
            'amenities': amenities
            }
    return render_template('10-hbnb_filters.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
