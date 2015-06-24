class Car:
    def __init__(self):
        self.x_loc = 0
        self.y_loc = 0
        self.speed = 0
        self.direction = 0

    def dist_premultiplier(self, degrees, distance):
        from sympy import solve, symbols
        from math import tan, radians
        a, b = symbols("a b")
        j, k = solve([(a/b)-(tan(radians(degrees))),
                      (a**2+b**2)-distance**2],
                     [a, b])
        x = round(abs(k[1]))
        y = round(abs(j[0]))
        print("x:{}".format(x))
        print("y:{}".format(y))
        return x, y



    def drive(self, steps=1, speed=1):
        """
        Here's the mapping I want:
        0 -> 100% y, 0% x
        45 -> 50% y, 50% x
        90 -> 0% y, 100% x
        135 -> -50% y, 50% x
        """
        x_dist, y_dist = self.dist_premultiplier(self.direction, distance=speed)
        self.x_loc += steps * x_dist
        self.y_loc += steps * y_dist
