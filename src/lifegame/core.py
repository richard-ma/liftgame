#-*- coding: utf-8 -*-

from .mapprinter import MapPrinter


'''
map format
[(x1, y1), (x2, y2)]
(x1, y1) is coodinates of True point

around is also used this format
'''

class World:
    def __init__(self, alive: list) -> None:
        self._alive = alive
    
    def set_alive(self, alive: list) -> None:
        self._alive = alive

    def get_alive(self) -> list:
        return self._alive

    def step_forward(self) -> None:
        # new alive list
        new_alive = list()
        # claculate x aix and y aix
        zipped_data = list(zip(*self._alive))
        x_min, x_max = min(zipped_data[0]), max(zipped_data[0])
        y_min, y_max = min(zipped_data[1]), max(zipped_data[1])
        width = x_max - x_min + 1
        height = y_max - y_min + 1
        # update alive status to new alive list
        for y in range(y_min, y_max+1):
            for x in range(x_min, x_max+1):
                around_sum = 0
                around_list = [
                    (x-1, y-1),
                    (x-1, y),
                    (x-1, y+1),
                    (x, y-1),
                    #(x, y), this is x, y
                    (x, y+1),
                    (x+1, y-1),
                    (x+1, y),
                    (x+1, y+1),
                ]
                for point in around_list:
                    if point in self._alive:
                        around_sum += 1

                print(x, y, around_sum, around_list)
                # get new status
                if (x, y) not in self._alive and around_sum == 3:
                    new_alive.append((x, y))
                elif (x, y) in self._alive and (around_sum == 2 or around_sum == 3): # x, y is alive and around sum is 2 or 3
                    new_alive.append((x, y))
                else:
                    pass
        
        # update self._alive
        self._alive = new_alive

        
class WorldHistory:
    def __init__(self) -> None:
        self._history = list()

    def append_history(self, world: World) -> None:
        self._history.append(world)

    def _clear(self) -> None:
        self._history = list()

    def clear_history(self) -> None:
        self._clear()


            

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
