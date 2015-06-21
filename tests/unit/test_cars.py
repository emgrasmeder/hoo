from unittest import TestCase, main
import random
from hoo import cars


class TestCarBasicFunctionality(TestCase):
    def test_car_even_exists(self):
        self.assertIsInstance(cars.Car(), cars.Car)

    def test_car_parameters_even_exist_too(self):
        car = cars.Car()
        self.assertIsNotNone(car.x_loc)
        self.assertIsNotNone(car.y_loc)
        self.assertIsNotNone(car.speed)
        self.assertIsNotNone(car.direction)

class Test_AccelerateChangesCarsLocation(TestCase):
    def test_cars_without_directions_cant_accelerate(self):
        car = cars.Car()
        car.direction=None
        self.assertRaises(AttributeError, car.accelerate(.5))

    def test_that_the_car_can_drive_north(self):
        car = cars.Car()
        car.direction=0
        old_location = tuple((car.x_loc, car.y_loc))
        car.accelerate(random.choice([x*.01 for x in range(1,99)]))
        new_location = tuple((car.x_loc, car.y_loc))
        self.assertNotEqual(old_location, new_location)


if __name__ == "__main__":
    main()
