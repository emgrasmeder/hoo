from unittest import TestCase, main
from hoo import worlds

class TestWorldExists(TestCase):
    def test_world_is_world_object(self):
        self.assertIsInstance(worlds.World(), worlds.World)

if __name__ == "__main__":
    main()
