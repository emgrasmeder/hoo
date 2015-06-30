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

    def test_pavement_cant_instantiate_with_nonsense_args(self):
        bad_pavement1 = roads.Pavement(bottom_left=[0, 0],
                                       top_left=[1, 1])
        bad_pavement2 = roads.Pavement(bottom_left=[10, 0],
                                       bottom_right=[-10, 0])
        self.assertEqual(bad_pavement1.bottom_left[0],
                         bad_pavement1.top_left[0])
        self.assertEqual(bad_pavement2.bottom_left[0], -10)
        self.assertEqual(bad_pavement2.bottom_right[0], 10)

class Test_contains(TestCase):
    def test_pavement_returns_false_for_uncontained_pavement(self):
        pavement = roads.Pavement(top_left=[0, 10],
                                  top_right=[10, 10],
                                  bottom_right=[10, 0])




if __name__ == "__main__":
    main()
