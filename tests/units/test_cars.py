from unittest import TestCase, main
from hoo import cars, roads


class TestCarBasicFunctionality(TestCase):
    def test_car_even_exists(self):
        self.assertIsInstance(cars.Car(), cars.Car)

    def test_car_parameters_even_exist_too(self):
        car = cars.Car()
        self.assertIsNotNone(car.x_loc)
        self.assertIsNotNone(car.y_loc)
        self.assertIsNotNone(car.speed)
        self.assertIsNotNone(car.direction)


class Test_Car_exists_in_space_time_continuum(TestCase):
    def test_drive_changes_cars_location(self):
        tesla = cars.Car()
        initial_x, initial_y = tesla.x_loc, tesla.y_loc
        tesla.drive()
        self.assertNotEqual((initial_x, initial_y),
                            (tesla.x_loc, tesla.y_loc))

    def test_drive_changes_location_as_fn_input(self):
        car1 = cars.Car()
        car2 = cars.Car()
        self.assertEqual((car1.x_loc, car1.y_loc),
                         (car2.x_loc, car2.y_loc))
        car1.drive(1)
        car2.drive(10)
        self.assertNotEqual((car1.x_loc, car1.y_loc),
                            (car2.x_loc, car2.y_loc))

    def test_drive_distance_is_steps_times_size(self):
        fiat = cars.Car()
        mercedes = cars.Car()
        fiat.drive(speed=9)
        mercedes.drive(speed=5)
        self.assertEqual(fiat.x_loc, 9)
        self.assertLess(mercedes.x_loc, fiat.x_loc)

    def test_drive_distance_and_angle_from_solved_problem(self):
        car = cars.Car()
        car.direction = 39
        car.drive(speed=30)
        self.assertEqual(car.y_loc, 18.88)

    def test_drive_direction_affects_x_and_y_magnitues(self):
        accord = cars.Car()
        accord.direction = 30
        accord.drive(speed=109.8)
        self.assertEqual(round(accord.x_loc), 95)
        self.assertEqual(round(accord.y_loc), 55)


class Test_check_location(TestCase):
    def test_instantiating_two_cars_in_same_location_fails(self):
        road = roads.Road()
        car1 = cars.Car(road=road)
        car2 = cars.Car(road=road)
        self.assertEqual(car1.loc, (0, 0))
        self.assertNotEqual(car2.loc, (0, 0))


class Test_car_too_close(TestCase):
    def test_car_wont_drive_into_parked_car(self):
        road = roads.Road()
        moving_car = cars.Car(road=road)
        parked_car = cars.Car(road=road)
        moving_car.set_location(0, 0)
        parked_car.set_location(2, 2)

class Test_detect_nearby(TestCase):
    def test_cars_cant_exist_at_the_same_point(self):
        road = roads.Road()
        car1 = cars.Car(road)
        car2 = cars.Car(road)
        self.assertNotEqual(car1.loc, car2.loc)

    def test_one_car_will_not_drive_into_a_parked_car(self):
        self.assertTrue(False)

    def test_cars_avoid_head_on_collision(self):
        self.assertTrue(False)



if __name__ == "__main__":
    main()
