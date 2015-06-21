class Car:
    def __init__(self):
        self.x_loc = 0
        self.y_loc = 0
        self.speed = 0
        self.direction = None
    def accelerate(self, acc_percent):
        if self.direction is None:
            raise(AttributeError) #, "Acceleration function requires `direction`")

