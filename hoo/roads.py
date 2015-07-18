from shapely.geometry import LineString
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


    def out_of_bounds(self, proposed_line):
        """
        """
        return any([LineString(proposed_line).intersects(LineString(bound))
                    for bound in self.relevant_bounds()])

    def slope(self, point1, point2):
        """
        Turns points (x1,y1), (x2, y2) into equation of a line:
        y = mx + b
        """
        x, y = 0, 1
        rise = point2[y] - point1[y]
        run = point2[x] - point1[x]
        if rise == 0:
            return 0
        else:
            try:
                m = rise / run
            except ZeroDivisionError:
                return "undefined"
        return m

    def relevant_bounds(self):
        """
        """

        left_bound =   [self.paved_area["bottom_left"],
                        self.paved_area["top_left"]]

        top_bound =    [self.paved_area["top_left"],
                        self.paved_area["top_right"]]

        right_bound =  [self.paved_area["bottom_right"],
                        self.paved_area["top_right"]]

        bottom_bound = [self.paved_area["bottom_right"],
                        self.paved_area["bottom_left"]]
        return(left_bound, top_bound, right_bound, bottom_bound)
