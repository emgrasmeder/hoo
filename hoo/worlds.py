from datetime import datetime, timedelta


class World:

    beginning = datetime.now()
    end = None

    def __init__(self):
        self.max_x = 100
        self.min_x = -100

        self.max_y = 100
        self.min_y = -100

        self.step_speed = timedelta(seconds=.3)
        self.last_step = World.beginning

    def step(self, steps=-1):
        while True:
            if not World.end and steps:
                if (datetime.now() - self.last_step) > self.step_speed:
                    # do next step stuff
                    print("hello world!\n steps = {}".format(steps))
                    self.last_step = datetime.now()
                    steps -= 1
            else:
                break



