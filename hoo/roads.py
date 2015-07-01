class Road:
    def __init__(self):
        self.total_distance = 0
        self.total_lanes = 0
        self.speed_limit = 0
        # make road everywhere
        self.paved_area = {"bottom_left" : (-100, -100),
                           "top_left"    : (-100,  100),
                           "top_right"   : ( 100,  100),
                           "bottom_right": ( 100, -100)}


