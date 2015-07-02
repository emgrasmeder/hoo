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
        Usage example:

        L1 = line([0,1], [2,3])
        L2 = line([2,3], [0,4])

        R = intersection(L1, L2)
        if R:
            print "Intersection detected:", R
        else:
            print "No single intersection point detected"
        """
        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0]*p2[1] - p2[0]*p1[1])
            return A, B, -C

        def intersection(L1, L2):
            D  = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x,y
            else:
                return False
        left_bound =[self.paved_area["bottom_left"],
                     self.paved_area["top_left"]]
        top_bound = [self.paved_area["top_left"],
                     self.paved_area["top_right"]]
        right_bound = [self.paved_area["bottom_right"],
                       self.paved_area["top_right"]]
        bottom_bound = [self.paved_area["bottom_right"],
                        self.paved_area["bottom_left"]]
        for xy in [left_bound, top_bound, right_bound, bottom_bound]:
            L1 = line(xy[0], xy[1])
            L2 = line(proposed_line[0], proposed_line[1])
            R = intersection(L1, L2)
            if R:
                break
        return R
