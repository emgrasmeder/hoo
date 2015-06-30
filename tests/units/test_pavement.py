from unittest import TestCase, main
import random
from hoo import roads

class TestPavement(TestCase):
    def test_pavement_is_pavement_object(self):
        self.assertIsInstance(roads.Pavement(), roads.Pavement)

    def test_parameters_exist_too(self):
        pavement = roads.Pavement()
        self.assertIsNotNone(pavement.total_distance)
        self.assertIsNotNone(pavement.total_lanes)
        self.assertIsNotNone(pavement.speed_limit)
        self.assertIsNotNone(pavement.paved_zone)

class Test_Instantiate(TestCase):
    def test_pavement_is_upside_up(self):
        pavement = roads.pavement()
        self.assertGreater(pavement.x_right, pavement.x_left)
        self.assertGreater(pavement.y_down, pavement.y_down)

    def test_pavement_is_upside_up(self):
        pavement = roads.pavement()
        self.assertGreater(pavement.x_right, pavement.x_left)

if __name__ == "__main__":
    main()
