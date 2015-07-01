from unittest import TestCase, main
from hoo import cars

class Test_CarsGoOnRoads(TestCase):
    def test_cars_drive_around_without_leaving_road(self):

        # When we make a car, it comes with its own default road
        car = cars.Car()
        # and that car's road has some x,y coordinates that define it

        self.assertEqual(car.road.paved_area["bottom_left"],
                         (-100, -100))
        self.assertEqual(car.road.paved_area["top_left"],
                         (-100, 100))
        self.assertEqual(car.road.paved_area["top_right"],
                         (100, 100))
        self.assertEqual(car.road.paved_area["bottom_right"],
                         (100, -100))

        # The car begins in the middle of the road
        self.assertEqual((car.x_loc, car.y_loc), (0, 0))

        # but it can drive in any direction it want (degrees as input!)

        car.drive(direction=90)
        self.assertEqual(
            (car.x_loc, car.y_loc),
            (0, 1)
                         )

        # until it comes to a dead end, in which case it
        # picks a new direction and carries on

        for i in range(1000):
            car.drive()
            self.assertLessEqual(car.y_loc, 100)
            self.assertGreaterEqual(car.y_loc, -100)
            self.assertLessEqual(car.x_loc, 100)
            self.assertGreaterEqual(car.x_loc, -100)



if __name__ == "__main__":
    main()
