#-*- coding: utf-8 -*-

from .mapprinter import MapPrinter



        


            

class LifeGame:
    def __init__(self, world: World) -> None:
        self._current_world = world
        self._history = WorldHistory()
        self._printer = MapPrinter()

    def progress(self) -> int:
        pass
    

if __name__ == "__main__":
    alives = [(0, 0), (1, 0), (0, 1), (1, 1), (-2, 3), (-2, 4), (-3, 4), (-3, 3)]
    mp = MapPrinter()
    world = World(alives)
    print(world.get_alive())
    mp.print(world.get_alive())

    world.step_forward()
    print('-' * 30)
    print(world.get_alive())
    mp.print(world.get_alive())

    world.step_forward()
    print('-' * 30)
    print(world.get_alive())
    mp.print(world.get_alive())
