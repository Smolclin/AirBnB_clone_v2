#!/usr/bin/python3
""" script that starts a Flask web application """

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    all_state = list(storage.all(State).values())
    all_state.sort(key=lambda y: y.name)
    for state in all_state:
        state.city.sort(key=lambda y: y.name)
    ctxt = {
            'states': all_state
            }
    return render_template('8-cities_by_states.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    storage.close()
