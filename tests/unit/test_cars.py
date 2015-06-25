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


class Test_Car_exists_in_space_time_continuum(TestCase):
    def test_drive_changes_cars_location(self):
        tesla = cars.Car()
        initial_x, initial_y = tesla.x_loc, tesla.y_loc
        tesla.drive(steps=10)
        self.assertNotEqual((initial_x, initial_y),
                            (tesla.x_loc, tesla.y_loc))

    def test_drive_changes_location_as_fn_input(self):
        car1 = cars.Car()
        car2 = cars.Car()
        self.assertEqual((car1.x_loc, car1.y_loc),
                         (car2.x_loc, car2.y_loc))
        car1.drive(steps=1)
        car2.drive(steps=10)
        self.assertNotEqual((car1.x_loc, car1.y_loc),
                            (car2.x_loc, car2.y_loc))


    def test_drive_distance_is_steps_times_size(self):
        fiat = cars.Car()
        mercedes = cars.Car()
        fiat.drive(steps=10, speed=100)
        mercedes.drive(steps=10, speed=10)
        self.assertLess(mercedes.y_loc, fiat.y_loc)

    def test_drive_direction_affects_x_and_y_magnitues(self):
        accord = cars.Car()
        accord.direction=30
        accord.drive(speed=109.8)
        self.assertEqual(accord.x_loc, 95)
        self.assertEqual(accord.y_loc, 55)

    def test_premultiplier_does_its_math_right(self):
        car = cars.Car()
        x, y = car.dist_premultiplier(degrees=30, distance=109.8)
        self.assertEqual(x, 95)
        self.assertEqual(y, 55)



if __name__ == "__main__":
    main()
