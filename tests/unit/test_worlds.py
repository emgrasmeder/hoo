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



if __name__ == "__main__":
    main()
