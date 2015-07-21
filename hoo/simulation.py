from hoo import roads, cars

def simulate(**kwargs):
    print("\n\nArguments we've been given:{}".format(kwargs))
    road = roads.Road()
    agents = [cars.Car(road) for car in range(kwargs["agents"])]
    for step in range(kwargs["steps"]):
        [car.drive() for car in agents]

