import csv
from csv import writer
import os
from ping import *
def write_csv(trucks):
    titles = ('ID', 'Latitude', 'Longitude')
    with open('locations.csv', 'w') as locations:
        writer_object = writer(locations)
        writer_object.writerow(titles)
        for key in trucks.keys():
            if trucks[key] != (0.0, 0.0):
                writer_object.writerow((key, trucks[key][0], trucks[key][1]))
        locations.close()
    print('test2')
