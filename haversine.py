from math import radians, cos, sin, asin, sqrt
import csv
from csv import writer
from ping import *
RADIUS = 6371
HOME_LAT = 38.000641
HOME_LONG = -121.287399

def haversine(lat1, long1, lat2, long2):
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)

    inner_function = (sin((lat2 - lat1)/2))**2 + cos(lat1)*cos(lat2)*(sin((long2 -long1)/2))**2
    distance = 2 * RADIUS * asin(sqrt(inner_function))

    return distance

def haversine_checker(trucks):
    with open('invite_truckers.csv', 'w') as invite:
        writer_object = writer(invite)
        titles = ('ID', 'Latitude', 'Longitude')
        writer_object.writerow(titles)
        for key in trucks:
            if haversine(HOME_LAT, HOME_LONG, trucks[key][0], trucks[key][1]) <= 200:
                writer_object.writerow((key, trucks[key][0], trucks[key][1]))
