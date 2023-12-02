# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(autoload_with=engine)
# Save references to each table
measurement = base.classes.measurement
station = base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello, World!"
if __name__ == '__main__':
    app.run(debug=True)
    python app.py

#################################################
# Flask Routes
#################################################
from flask import Flask

app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to the Climate App!"
@app.route('/api/v1.0/precipitation')
def precipitation():
    # Logic to query precipitation data
    precipitation_data = {}  # Replace with actual data retrieval logic
    return jsonify(precipitation_data)
@app.route('/api/v1.0/stations')
def stations():
    # Logic to get station data
    stations_list = []  # Replace with actual data retrieval logic
    return jsonify(stations_list)
@app.route('/api/v1.0/tobs')
def tobs():
    # Logic to get temperature observations
    tobs_data = []  # Replace with actual data retrieval logic
    return jsonify(tobs_data)
@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def temp_stats(start, end=None):
    # Logic to calculate temperature statistics
    temp_stats_data = {}  # Replace with actual data retrieval and calculation logic
    return jsonify(temp_stats_data)
if __name__ == '__main__':
    app.run(debug=True)
