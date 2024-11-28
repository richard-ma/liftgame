#-*- coding: utf-8 -*-

class Life:
    def __init__(self, status: bool) -> None:
        self._is_alive = 1 if status else 0

    def progress(self, around: list) -> bool:
        s = sum(around)
        if self._is_alive == 0 and s == 3:
            self._is_alive = 1
        else: # self._is_alive = 1
            if s < 2 or s > 3:
                self._is_alive = 0
            else: # around sum is 2 or 3
                self._is_alive = 1


class World:
    def __init__(self, width: int, height: int) -> None:
        self._map = [0] * (width * height)
    
    def set_map(self, map: list) -> None:
        pass

    def get_map(self) -> list:
        pass

    
if __name__ == "__main__":
    width, height = 9, 9
    world_map = [[0 for i in range(width)] for j in range(height)]

    new_world_map = [[0 for i in range(width)] for j in range(height)]

    for i in range(height):
        for j in range(width):
            print(world_map[i][j], end='')
        print()