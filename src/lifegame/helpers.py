#!/usr/bin/env python3


class MapPrinter:
    def __init__(self) -> None:
        self.x_min = None
        self.x_max = None 
        self.y_min = None
        self.y_max = None

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

    def print(self, map_data: list) -> None:
        if map_data and (self.get_width() == 0 or self.get_height() == 0):
            # self not initialized
            zipped_data = list(zip(*map_data))
            self.x_min, self.x_max = min(zipped_data[0]), max(zipped_data[0])
            self.y_min, self.y_max = min(zipped_data[1]), max(zipped_data[1])
        
        for y in range(self.y_min, self.y_max+1):
            for x in range(self.x_min, self.x_max+1):
                if (x, y) in map_data:
                    print('1', end='')
                else:
                    print('0', end='')
            print()