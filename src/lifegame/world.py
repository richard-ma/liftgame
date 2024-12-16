#!/usr/bin/env python3


'''
map format
[(x1, y1), (x2, y2)]
(x1, y1) is coodinates of True point

around is also used this format
'''

class World:
    def __init__(self, alive: list) -> None:
        self._alive = alive

        self.x_min = None
        self.x_max = None 
        self.y_min = None
        self.y_max = None

    def __eq__(self, other) -> bool:
        if isinstance(other, World):
            return self._alive == other._alive
        else:
            raise TypeError(other, " is not the instance of Wrold.")
    
    def set_alive(self, alive: list) -> None:
        self._alive = alive

    def get_alive(self) -> list:
        return self._alive

    def get_width(self) -> int:
        if self.x_max and self.x_min:
            return self.x_max - self.x_min + 1
        else:
            return 0

    def get_height(self) -> int:
        if self.y_max and self.y_min:
            return self.y_max - self.y_min + 1
        else:
            return 0

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

    def __str__(self) -> None:
        map_data = self._alive
        if map_data and (self.get_width() == 0 or self.get_height() == 0):
            # self not initialized
            zipped_data = list(zip(*map_data))
            self.x_min, self.x_max = min(zipped_data[0]), max(zipped_data[0])
            self.y_min, self.y_max = min(zipped_data[1]), max(zipped_data[1])
        
        ret = ""
        for y in range(self.y_min, self.y_max+1):
            for x in range(self.x_min, self.x_max+1):
                if (x, y) in map_data:
                    ret += '1'
                else:
                    ret += '0'
            ret += '\n'

        return ret