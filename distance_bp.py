from flask import Blueprint, render_template, request
from geopy.geocoders import Nominatim
from geopy import distance
import pandas as pd
from shapely.geometry import Polygon
from shapely.geometry import Point
import logging

# Constants
MKAD_LOCATION = (55.8277252, 37.6387268)

# Nominatim geolocation service
geolocator = Nominatim(user_agent="myapp.py")

# Creating the Blueprint
distance_bp = Blueprint('distance_bp', __name__)

# Configure the logging
logging.basicConfig(filename = 'result.log', level=logging.DEBUG)


# Functions
def create_polygon():
    """Return a polygon created with the set of coordinates that delimit the
    MKAD area.
    """
    df = pd.read_csv(r'mkad_coordinates.csv')
    df = df.rename(columns = {'37.842762': 'lat', "55.774558" : 'long'})
    polygon_matrix = [[df['long'][ind], df['lat'][ind]] for ind in df.index]
    return Polygon(polygon_matrix)

def get_distance(lat, long):
    """If the point related to lat and long coordinates is inside MKAD
    area, distance is not calculated else, it assigns the geodesic distance.
    """
    if(create_polygon().contains(Point(lat, long))):
        dist = "Address is inside of MKAD"
        logging.debug("distance: {}".format(dist))
    else:
        # Use geopy to get the geodesic distance
        dist = distance.distance(MKAD_LOCATION, (lat, long))
        logging.debug("distance: {}".format(dist))
    return dist

def get_location_parameters(loc):
    """If the address is found with geopy, it obtains the lat, long, address and
    distance. Otherwise it assigns null values to the previous
    mentioned variables.
    """
    location = geolocator.geocode(loc)
    if(location is not None): # If the address exists in database
        latitude = location.latitude
        longitude = location.longitude
        formatted_address = location.address
        dist = get_distance(latitude, longitude)
    else:
        latitude, longitude, formatted_address, dist = null_address()

    return latitude, longitude, formatted_address, dist

def no_input():
    """Fills variables for null address."""
    return "Null input", "Null input", "Null input","Null input"

def null_address():
    """Fills variables for an unknown address."""
    return "Null address", "Null address", "Null address", "Null address"


@distance_bp.route('/result',methods = ['POST', 'GET'])
def result():
    """The blueprint finds the distance from Moscow Ring Road to an addressed
    passed to the application in an HTTP request. If the address is located
    inside the MKAD, the distance is stated this way; if the geolocator is
    unable to find the address the results are stated as null address; and if
    the input address is null, the results are stated as null input.
    """
    if request.method == 'POST':
        location = request.form["location"]
        if(location.strip()): # If location is not null
            (latitude,
             longitude,
             formatted_address,
             dist) = get_location_parameters(location)
        else:
            (latitude,
            longitude,
            formatted_address,
            dist) = no_input()

    # Write address and distance into .log file
    logging.debug("{} distance to Moscow Ring Road: {}".format(formatted_address,
                                                        dist))

    return render_template("result.html",
                          result = formatted_address,
                          Latitude=latitude,
                          longitude=longitude,
                          distance=dist)
