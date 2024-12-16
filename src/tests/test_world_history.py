import unittest
from lifegame import *


class TestWorldHistory(unittest.TestCase):
    def setUp(self):
        self.first_history = World([1, 1])
        self.second_history = World([1, 2])
        self.last_history = World([1, 3])

        self.world_history = WorldHistory()
        self.world_history.append_history(self.first_history)
        self.world_history.append_history(self.second_history)
        self.world_history.append_history(self.last_history)
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
    
    def test_append_history(self):
        self.assertEqual(3, self.world_history.len())

    def test_get_history(self):
        self.assertEqual(self.world_history.get(0), self.first_history)
        self.assertEqual(self.world_history.get(-1), self.last_history)

    def test_save_history(self):
        self.world_history.save("history_test.json")
        self.world_history.load("history_test.json")