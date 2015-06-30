class Road:
    def __init__(self):
        self.total_distance = 0
        self.total_lanes = 0
        self.speed_limit = 0
        self.paved_zones = []

    def lay_pavement(self, bottom_left, top_right):
        self.paved_zones = [1]
