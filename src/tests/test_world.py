import unittest
from lifegame import *


class TestWorld(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_world_equal(self):
        alive = [(1, 1), (2, 2)]
        world_a = World(alive)
        world_b = World(alive)

        self.assertEqual(world_a, world_b)