class Road:
    def __init__(self):
        self.total_distance = 0
        self.total_lanes = 0
        self.speed_limit = 0
        self.paved_zones = []

    def lay_pavement(self, x_offset, y_offset, size=1):
        if (x_offset, y_offset) not in self.paved_zones:
            self.paved_zones.append((x_offset, y_offset))

class Pavement(Road):
    def __init__(self,
                 bottom_left=[0, 0],
                 top_left=[0, 1],
                 top_right=[1, 1],
                 bottom_right=[1, 0]):
        Road.__init__(self)
        self.bottom_left = bottom_left
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_right = bottom_right

    def contains(self, x_offset, y_offset, size=1):
        return True


