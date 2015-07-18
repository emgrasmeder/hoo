from hoo import roads
import random


class Car:
    def __init__(self, road=None):

        self.road = road
        self.x_loc = 0
        self.y_loc = 0
        self.loc = (self.x_loc, self.y_loc)
        self.speed = 0
        self.direction = 0

        if not self.road:
            self.road = roads.Road()
            self.road.register(self)
        self.check_location()

    def check_location(self):
        for loc in self.detect_nearby():
            if loc == self.loc:
                self.x_loc += random.choice(range(-10, 11))
                self.y_loc += random.choice(range(-10, 11))
                self.check_location()

    def detect_nearby(self):
        """
        Return an exhaustive list of all "nearby" cars on the road.
        """
        nearby_cars = self.road.list_cars(radius=3)
        return nearby_cars

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
        if not self.road.out_of_bounds(proposed_line=[[self.x_loc, self.y_loc],
                                                      [x_loc, y_loc]]):
            self.x_loc, self.y_loc = x_loc, y_loc
            # print("(x,y) = ({},{})".format(self.x_loc, self.y_loc))
        else:
            self.drive(speed=speed, direction=random.choice(range(-180, 181)))


