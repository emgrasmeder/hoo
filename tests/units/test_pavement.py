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
        self.assertIsNotNone(pavement.paved_zones)

    def test_pavement_specific_attributes(self):
        pavement = roads.Pavement()
        self.assertIsNotNone(pavement.bottom_left)
        self.assertIsNotNone(pavement.top_left)
        self.assertIsNotNone(pavement.top_right)
        self.assertIsNotNone(pavement.bottom_right)


if __name__ == "__main__":
    main()
