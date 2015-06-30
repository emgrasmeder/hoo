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
    def __init__(self):
        self.bottom_left = (0, 0)
        self.top_left = (0, 1)
        self.top_right = (1, 1)
        self.bottom_right = (1, 0)

    def contains(self, x_offset, y_offset, size=1):
        pass


