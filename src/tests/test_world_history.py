import unittest
from lifegame import *


class TestWorldHistory(unittest.TestCase):
    def setUp(self):
        self.first_history = World([1, 1])
        self.second_history = World([1, 2])
        self.last_history = World([1, 3])
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_append_history(self):
        world_history = WorldHistory()
        world_history.append_history(self.first_history)
        self.assertEqual(1, world_history.len())
        world_history.append_history(self.second_history)
        self.assertEqual(2, world_history.len())
        world_history.append_history(self.last_history)
        self.assertEqual(3, world_history.len())

    def test_save_history(self):
        world_history = WorldHistory()
        world_history.append_history(self.first_history)
        world_history.append_history(self.last_history)

        world_history.save("test")
        world_history.load("test")