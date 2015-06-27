from unittest import TestCase
from hoo import cars


class PresetAngles(TestCase):
    def setUp(self):
        self.car = cars.Car()
        self.sqrt2ovr2 = round(((2**.5)/2), 2)
        self.sqrt3ovr2 = round(((3**.5)/2), 2)
        self.sqrt3 = round(3**.5)
        self.sqrt2 = round(2**.5)




class Test_UnitCircle_QuadrantOne(PresetAngles):
    def test_pi_over_six(self):
        car = cars.Car()
        car.direction = 30
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (self.sqrt3ovr2, .5)
                         )

    def test_pi_over_four(self):
        car = cars.Car()
        car.direction = 45
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (self.sqrt2ovr2,
                          self.sqrt2ovr2))

    def test_pi_over_three(self):
        car = cars.Car()
        car.direction = 60
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (.5, self.sqrt3ovr2))


class Test_UnitCircle_QuadrantTwo(PresetAngles):
    def test_two_pi_over_three(self):
        car = cars.Car()
        car.direction = 120
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (-.5, self.sqrt3ovr2))

    def test_three_pi_over_four(self):
        car = cars.Car()
        car.direction = 135
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (-1*self.sqrt2ovr2, self.sqrt2ovr2))

    def test_five_pi_over_six(self):
        car = cars.Car()
        car.direction = 150
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (-1 * self.sqrt3ovr2, .5))


class Test_UnitCircle_QuadrantThree(PresetAngles):
    def test_seven_pi_over_six(self):
        car = cars.Car()
        car.direction = 210
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (-1 * self.sqrt3ovr2, -1 * .5))

    def test_five_pi_over_four(self):
        car = cars.Car()
        car.direction = 225
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (-1 * self.sqrt2ovr2, -1 * self.sqrt2ovr2))

    def test_four_pi_over_three(self):
        car = cars.Car()
        car.direction = 240
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (-1 * .5, -1 * self.sqrt3ovr2))


class Test_UnitCircle_QuadrantFour(PresetAngles):

    def test_five_pi_over_three(self):
        car = cars.Car()
        car.direction = 300
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (.5,
                          -1 * self.sqrt3ovr2))



    def test_seven_pi_over_four(self):
        car = cars.Car()
        car.direction = 315
        car.drive(speed=1)
        self.assertEqual(
                         (car.x_loc,
                          car.y_loc),
                         (self.sqrt2ovr2,
                          -1 * self.sqrt2ovr2))

    def test_eleven_pi_over_six(self):
        car = cars.Car()
        car.direction = 330
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (self.sqrt3ovr2,
                         -1 * .5)
                        )


class Test_UnitCircle_Axes(TestCase):
    def test_zero_and_two_pi(self):
        car = cars.Car()
        car2 = cars.Car()
        car.direction = 0
        car2.direction = 0
        car.drive(speed=1)
        car2.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (1, 0)
                        )
        self.assertEqual(
                        (car2.x_loc, car2.y_loc),
                        (1, 0)
                        )

    def test_pi_over_two(self):
        car = cars.Car()
        car.direction = 90
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (0, 1)
                        )

    def test_pi(self):
        car = cars.Car()
        car.direction = 180
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (-1, 0)
                        )

    def test_three_pi_over_two(self):
        car = cars.Car()
        car.direction = 270
        car.drive(speed=1)
        self.assertEqual(
                        (car.x_loc, car.y_loc),
                        (0, -1)
                        )


if __name__ == "__main__":
  from unittest import main
  main()
