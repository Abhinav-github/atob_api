import csv
from ping import *
titles = ('Latitude', 'Longitude')
with open('locations.csv', 'w') as locations:
    locations.write("%s,%s\n"%(titles))
    for key in trucks.keys():
        if trucks[key] != (0.0, 0.0):
            locations.write("%s,%s\n"%(trucks[key]))
