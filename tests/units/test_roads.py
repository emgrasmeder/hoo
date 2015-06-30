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
        self.assertIsNotNone(road.paved_zone)

class Test_Instantiate(TestCase):
    def test_road_is_upside_up(self):
        road = roads.Road()
        self.assertGreater(road.x_right, road.x_left)
        self.assertGreater(road.y_down, road.y_down)

    def test_road_is_upside_up(self):
        road = roads.Road()
        self.assertGreater(road.x_right, road.x_left)

if __name__ == "__main__":
    main()
