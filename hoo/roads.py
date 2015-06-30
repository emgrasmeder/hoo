class Road:
    def __init__(self):
        self.total_distance = 0
        self.total_lanes = 0
        self.speed_limit = 0
        self.paved_zones = []

    def lay_pavement(self, bottom_left, top_right=None, size=None):
        # if not top_right and not size:
        #     top_right = [bottom_left[0] + 1,
        #                  bottom_left[1] + 1]
        # new_pavement_x_bounds = [bottom_left[0], top_right[0]]
        # new_pavement_y_bounds = [bottom_left[1], top_right[1]]

        if (bottom_left, top_right) not in self.paved_zones:
            self.paved_zones.append((bottom_left, top_right))
