from unittest import TestCase, main
import random
from hoo import roads

class TestRoadBasics(TestCase):
    def test_road_is_road_object(self):
        self.assertIsInstance(roads.Road(), roads.Road)

    def test_parameters_exist_too(self):
        road = roads.Road()
        self.assertIsNotNone(road.total_distance)
        self.assertIsNotNone(road.total_lanes)
        self.assertIsNotNone(road.speed_limit)
        self.assertIsNotNone(road.paved_zones)

class Test_Instantiate(TestCase):
    def test_only_one_pavement_can_occupy_a_space(self):
        road = roads.Road()
        self.assertEqual(len(road.paved_zones), 0)
        road.lay_pavement(0, 0)
        self.assertEqual(len(road.paved_zones), 1)
        road.lay_pavement(0, 0)

    def test_adding_a_new_pavement_increases_the_count(self):
        road = roads.Road()
        road.lay_pavement(0, 0)
        self.assertEqual(len(road.paved_zones), 1)
        road.lay_pavement(1, 1)
        self.assertEqual(len(road.paved_zones), 2)

    def test_size_param_creates_larger_pavement(self):
        road = roads.Road()
        road.lay_pavement(10, 10, size=2)
        self.assertEqual(len(road.paved_zones), 1)
        road.lay_pavement(11, 11)
        self.assertEqual(len(road.paved_zones), 1)


    # def test_road_is_upside_up(self):
    #     road = roads.Road()
    #     self.assertGreater(road.x_right, road.x_left)
    #     self.assertGreater(road.y_down, road.y_down)

    # def test_road_is_upside_up(self):
    #     road = roads.Road()
    #     self.assertGreater(road.x_right, road.x_left)

if __name__ == "__main__":
    main()
