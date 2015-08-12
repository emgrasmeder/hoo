from hoo import roads, cars
from datetime import datetime


def simulate(**kwargs):
    road = roads.Road()
    cars.Car.logging = kwargs["no_logging"]
    #if
    cars.Car.logfile = datetime.now().strftime("%Y%m%d%H%M%S") + ".csv"
    agents = [cars.Car(road) for car in range(kwargs["agents"])]
    for step in range(kwargs["steps"]):
        [car.drive() for car in agents]

