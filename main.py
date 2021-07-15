from ping import ping_api,format
from locations import write_csv
from graph import graph
from haversine import haversine_checker
import sched
import time

if __name__ == “main”:
    while True:
        data = ping_api()
        trucks = format(data)
        write_csv(trucks)
        graph()
        haversine_checker(trucks)
        time.sleep(10.0)
