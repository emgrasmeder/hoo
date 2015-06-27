from unittest import TestCase, main
import random
from hoo import worlds

class TestWorldExists(TestCase):
    def test_world_is_world_object(self):
        self.assertIsInstance(worlds.World(), worlds.World)

    def test_worlds_ID_is_zero(self):
        world = worlds.World()
        r = random.choice(range(5))
        world.g(r)
        if r > 3:
            self.assertEqual(world.id, r)
        else:
            self.assertEqual(world.id, 3)

class Test_Step(TestCase):
    def test_step_updates_last_step_time(self):
        import time
        earth = worlds.World()
        initial_step = earth.last_step
        time.sleep(1.1)
        self.assertEqual(initial_step, earth.last_step)
        earth.step(11)
        for i in range(10):
            self.assertNotEqual(initial_step, earth.last_step)

    def test_step_can_be_limited_with_a_steps_Arg(self):
        self.assertIsNone(worlds.World().step(1))



if __name__ == "__main__":
    main()
