#-*- coding: utf-8 -*-

from .world import World
from .worldhistory import WorldHistory


class Lifegame:
    def __init__(self):
        self._world_history = WorldHistory()


all = [
    World, 
    WorldHistory,
    Lifegame,
    ]