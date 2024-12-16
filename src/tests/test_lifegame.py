import unittest
from lifegame import *


class TestLifegame(unittest.TestCase):
    def setUp(self):
        self.alive = [(1, 1), (2, 2)]
        self.lifegame = Lifegame(self.alive)

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

    def test_get_current_world(self):
        self.assertEqual(self.lifegame.get_current_world().get_alive(), self.alive)