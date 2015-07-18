from unittest import TestCase, main
import random
from hoo import roads, cars

class TestRoadBasics(TestCase):
    def test_road_is_road_object(self):
        self.assertIsInstance(roads.Road(), roads.Road)

    def test_parameters_exist_too(self):
        road = roads.Road()
        self.assertIsNotNone(road.total_distance)
        self.assertIsNotNone(road.total_lanes)
        self.assertIsNotNone(road.speed_limit)
        self.assertIsNotNone(road.paved_area)


class Test_out_of_bounds(TestCase):
    def test_long_line_is_out_of_bounds(self):
        road = roads.Road()
        proposed_line = [[-1000, -1000], [1000, 1000]]
        self.assertIsNotNone(road.out_of_bounds(proposed_line))

    def test_y_equals_zero_in_triangle(self):
        car = cars.Car()
        car.road.paved_area["upper_left"] = (0, 100)
        car.road.paved_area["upper_left"] = (0, 100)
        car.road.paved_area["bottom_left"] = (-100, -100)
        car.road.paved_area["bottom_right"] = (100, -100)
        for i in range(1000):
            car.drive(direction=0)
            self.assertLess(car.x_loc, 100)

        for i in range(1000):
            car.drive(direction=180)
            self.assertGreater(car.x_loc, -100)

class Test_slope(TestCase):
    def test_slope_of_one(self):
        slope = roads.Road().slope
        self.assertEqual(1, slope((0, 0), (1, 1)))

    def test_slope_of_negative_one(self):
        slope = roads.Road().slope
        self.assertEqual(-1, slope((0, 1), (1, 0)))

    def test_slope_of_zero(self):
        slope = roads.Road().slope
        self.assertEqual(0, slope((1, 1), (1, 1)))

    def test_undefined_slope(self):
        slope = roads.Road().slope
        self.assertEqual("undefined", slope((0, 0), (0, 1)))



# class Test_Instantiate(TestCase):
#     def test_only_one_pavement_can_occupy_a_space(self):
#         road = roads.Road()
#         self.assertEqual(len(road.paved_zones), 0)
#         road.lay_pavement(0, 0)
#         self.assertEqual(len(road.paved_zones), 1)
#         road.lay_pavement(0, 0)

#     def test_adding_a_new_pavement_increases_the_count(self):
#         road = roads.Road()
#         road.lay_pavement(0, 0)
#         self.assertEqual(len(road.paved_zones), 1)
#         road.lay_pavement(1, 1)
#         self.assertEqual(len(road.paved_zones), 2)

#     def test_size_param_creates_larger_pavement(self):
#         road = roads.Road()
#         road.lay_pavement(10, 10, size=2)
#         self.assertEqual(len(road.paved_zones), 1)
#         road.lay_pavement(11, 11)
#         self.assertEqual(len(road.paved_zones), 1)


    # def test_road_is_upside_up(self):
    #     road = roads.Road()
    #     self.assertGreater(road.x_right, road.x_left)
    #     self.assertGreater(road.y_down, road.y_down)

    # def test_road_is_upside_up(self):
    #     road = roads.Road()
    #     self.assertGreater(road.x_right, road.x_left)

if __name__ == "__main__":
    main()
