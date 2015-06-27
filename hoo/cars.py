class Car:
    def __init__(self):
        self.x_loc = 0
        self.y_loc = 0
        self.speed = 0
        self.direction = 0


    def dist_premultiplier(self, degrees, distance):
        from math import sin, cos, radians
        hypotenuse = distance
        degrees = degrees % 360
        y_dist = round(hypotenuse * sin(radians(degrees)), 2)
        x_dist = round(hypotenuse * cos(radians(degrees)), 2)
        print("a2 + b2 = {}".format(round((x_dist**2) + (y_dist**2))))
        print("d2 = {}".format(distance**2))
        assert round((x_dist**2) + (y_dist**2)) == round(distance**2)
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
        print("x_dist: {}".format(x_dist))
        print("y_dist: {}".format(y_dist))
        return x_dist, y_dist


    def drive(self, steps=1, speed=1):
        """
        """

        x_dist, y_dist = self.dist_premultiplier(self.direction,
                                                 distance=speed)
        self.x_loc += steps * x_dist
        self.y_loc += steps * y_dist
