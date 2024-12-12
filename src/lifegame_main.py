#!/usr/bin/env python3

from lifegame import *


if __name__ == "__main__":
    true_map = [(1, 1)]
    world = World(true_map)

    mp = MapPrinter()
    mp.print(world.get_alive())

    world.step_forward()
    mp.print(world.get_alive())