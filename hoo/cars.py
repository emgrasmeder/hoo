from hoo import roads
import random
from shapely.geometry import Point, LineString
from datetime import datetime
import csv
import os


class Car:
    logging = True
    _id = 0
    logfile = "temp_log.csv"

    def __init__(self, road=None):
        self._id = Car._id
        Car._id += 1
        self.creation_time = datetime.now().strftime("%Y%m%d%H%M%S")
        self.road = road
        self.speed = 0
        self.direction = 0
        self.safe_distance = 1
        self.set_location(0, 0)
        if not self.road:
            self.road = roads.Road()
        self.road.register(self)
        self.set_safe_location()

    def set_location(self, x, y):
        self.loc = (x, y)
        self.x_loc = self.loc[0]
        self.y_loc = self.loc[1]

    def log(self, filename=None):
        if filename is None:
            filename = Car.logfile
        dir = os.path.dirname(__file__)
        path = os.path.join(dir, "../resources/logs/")

        with open(path + filename, "a+") as f:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            record = [timestamp, str(int(timestamp)-int(self.creation_time)),
                      self._id,
                      self.x_loc, self.y_loc,
                      ]
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(record)


    def set_safe_location(self):
        for car in self.detect_nearby():
            if car != self and car.loc == self.loc:
                self.set_location(random.choice(range(-10, 11)),
                                  random.choice(range(-10, 11)))
                self.set_safe_location()

    def detect_nearby(self):
        """
        Return an exhaustive list of all "nearby" cars on the road.
        """
        nearby_cars = self.road.list_cars()
        return nearby_cars

    def car_too_close(self, landing_spot):
        """
        """
        my_danger_path = (LineString([(self.loc),
                                      (landing_spot)])
                          .buffer(self.safe_distance))
        car_too_close = any([Point(other_car.loc)
                             .buffer(1)
                             .intersects(my_danger_path)
                             for other_car in self.detect_nearby()
                             if other_car != self])
        return(car_too_close)


    def dist_premultiplier(self, degrees, distance):
        from math import sin, cos, radians
        hypotenuse = distance
        degrees = degrees % 360
        y_dist = round(hypotenuse * sin(radians(degrees)), 2)
        x_dist = round(hypotenuse * cos(radians(degrees)), 2)
        assert round((x_dist**2) + (y_dist**2)) == round(hypotenuse**2)
        if degrees in [0, 360]:
            x_dist = distance
            y_dist = 0
        if degrees == 90:
            x_dist = 0
            y_dist = distance
        if degrees == 180:
            x_dist = -1 * distance
            y_dist = 0
        if degrees == 270:
            x_dist = 0
            y_dist = -1 * distance
        return x_dist, y_dist

    def drive(self, speed=1, direction=None):
        """
        """

        if isinstance(direction, int):
            self.direction = direction
        x_dist, y_dist = self.dist_premultiplier(self.direction,
                                                 distance=speed)

        x_loc = self.x_loc + x_dist
        y_loc = self.y_loc + y_dist
        if (not self.road.out_of_bounds(proposed_line=[[self.x_loc,
                                                        self.y_loc],
                                                       [x_loc, y_loc]])
        and
        not self.car_too_close(landing_spot=(x_loc, y_loc))
        and
        True):
            # TODO HERE: Write out to CSV.  Also do it at the top of the file
            self.set_location(x_loc, y_loc)
            self.log()

            # print("(x,y) = ({},{})".format(self.x_loc, self.y_loc))
        else:
            self.drive(speed=speed, direction=random.choice(range(-180, 181)))

