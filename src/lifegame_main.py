#!/usr/bin/env python3

from lifegame import *


if __name__ == "__main__":
    alive = [(0, 0), (1, 0), (0, 1), (1, 1), ]
    lg = Lifegame(alive)

    for _ in range(1000):
        lg.step()
    
    lg.get_world_history().save("history_1000.json")