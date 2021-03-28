from ping import ping_api,format
from locations import write_csv
from graph import graph
import sched
import time

while True:
    data = ping_api()
    trucks = format(data)
    write_csv(trucks)
    graph()
    time.sleep(10.0)
print("Truck Location data in truck locations.png")
