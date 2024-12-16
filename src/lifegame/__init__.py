#-*- coding: utf-8 -*-

from .world import World
from .worldhistory import WorldHistory


class Lifegame:
    def __init__(self, alive: list):
        self._world = World(alive)
        self._world_history = WorldHistory()
        self._world_history.append_history(self._world)

    def step(self)-> bool:
        self._world.step_forward()
        self._world_history.append(self._world)


all = [
    World, 
    WorldHistory,
    Lifegame,
    ]