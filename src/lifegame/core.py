#-*- coding: utf-8 -*-

'''
map format
[(x1, y1), (x2, y2)]
(x1, y1) is coodinates of True point

around is also used this format
'''

# class Life:
#     def __init__(self, status: bool) -> None:
#         self._is_alive = status

#     def progress(self, around: list) -> bool:
#         s = len(around)
#         if self._is_alive == False and s == 3:
#             self._is_alive = True 
#         else: # self._is_alive = True
#             if s < 2 or s > 3:
#                 self._is_alive = False
#             else: # around sum is 2 or 3
#                 self._is_alive = True


class World:
    def __init__(self, alive: list) -> None:
        self._alive = alive
    
    def set_alive(self, alive: list) -> None:
        self._alive = alive

    def get_alive(self) -> list:
        return self._alive

        
class WorldHistory:
    def __init__(self) -> None:
        self._history = list()

    def append_history(self, world: World) -> None:
        self._history.append(world)

    def _clear(self) -> None:
        self._history = list()

    def clear_history(self) -> None:
        self._clear()


class MapPrinter:
    def __init__(self) -> None:
        self.x_min = 0
        self.x_max = -1
        self.y_min = 0
        self.y_max = -1

    def get_width(self) -> int:
        return self.x_max - self.x_min + 1

    def get_height(self) -> int:
        return self.y_max - self.y_min + 1

    def print(self, map_data: list) -> None:
        if map_data and (self.get_width() == 0 or self.get_height() == 0):
            # self not initialized
            zipped_data = list(zip(*map_data))
            self.x_min, self.x_max = min(zipped_data[0]), max(zipped_data[0])
            self.y_min, self.y_max = min(zipped_data[1]), max(zipped_data[1])
        
        for row in range(self.y_min, self.y_max+1):
            for col in range(self.x_min, self.x_max+1):
                if (row, col) in map_data:
                    print('1', end='')
                else:
                    print('0', end='')
            print()
            

class LifeGame:
    def __init__(self, world: World) -> None:
        self._current_world = world
        self._history = WorldHistory()
        self._printer = MapPrinter()

    def progress(self) -> int:
        pass
    

if __name__ == "__main__":
    map_data = [(0, 0), (1, 0), (0, 1), (1, 1), (-3, 2), (-3, -3)]
    mp = MapPrinter()
    mp.print(map_data)
    print(mp.x_min, mp.x_max)
    print(mp.y_min, mp.y_max)
    print(mp.get_width(), mp.get_height())


'''
if __name__ == "__main__":
    width, height = 9, 9
    world_map = [[0 for i in range(width)] for j in range(height)]

    # init world
    world_map[0][0] = 1
    world_map[0][1] = 1
    world_map[1][0] = 1
    world_map[1][1] = 1
    world_map[1][2] = 1

    
    new_world_map = [[0 for i in range(width)] for j in range(height)]
    # update world
    for i in range(height):
        for j in range(width):
            sum_array = list()
            if i == 0 and j == 0:
                sum_array.append(world_map[i+1][j]) 
                sum_array.append(world_map[i][j+1])
                sum_array.append(world_map[i+1][j+1])
            elif i == 0 and j == width - 1:
                sum_array.append(world_map[i+1][j]) 
                sum_array.append(world_map[i][j-1])
                sum_array.append(world_map[i+1][j-1])
            elif i == 0:
                sum_array.append(world_map[i+1][j]) 
                sum_array.append(world_map[i][j+1])
                sum_array.append(world_map[i+1][j+1])
                sum_array.append(world_map[i][j-1])
                sum_array.append(world_map[i+1][j-1])
            elif i == height - 1 and j == 0:
                sum_array.append(world_map[i-1][j])
                sum_array.append(world_map[i][j+1])
                sum_array.append(world_map[i-1][j+1])
            elif i == height - 1 and j == width - 1:
                sum_array.append(world_map[i-1][j])
                sum_array.append(world_map[i][j-1])
                sum_array.append(world_map[i-1][j-1])
            elif i == height - 1:
                sum_array.append(world_map[i-1][j])
                sum_array.append(world_map[i][j+1])
                sum_array.append(world_map[i-1][j+1])
                sum_array.append(world_map[i][j-1])
                sum_array.append(world_map[i-1][j-1])
            elif j == 0:
                sum_array.append(world_map[i-1][j])
                sum_array.append(world_map[i-1][j+1])
                sum_array.append(world_map[i][j+1])
                sum_array.append(world_map[i+1][j+1])
                sum_array.append(world_map[i+1][j]) 
            elif j == width - 1:
                sum_array.append(world_map[i-1][j-1])
                sum_array.append(world_map[i-1][j])
                sum_array.append(world_map[i+1][j]) 
                sum_array.append(world_map[i+1][j-1])
                sum_array.append(world_map[i][j-1])
            else:
                sum_array.append(world_map[i-1][j-1])
                sum_array.append(world_map[i-1][j])
                sum_array.append(world_map[i-1][j+1])
                sum_array.append(world_map[i][j+1])
                sum_array.append(world_map[i+1][j+1])
                sum_array.append(world_map[i+1][j]) 
                sum_array.append(world_map[i+1][j-1])
                sum_array.append(world_map[i][j-1])
            s = sum(sum_array)
            is_alive = world_map[i][j]
            if is_alive == 0 and s == 3:
                new_is_alive = 1
            else: # self._is_alive = 1
                if s < 2 or s > 3:
                    new_is_alive = 0
                else: # around sum is 2 or 3
                    new_is_alive = 1
            new_world_map[i][j] = new_is_alive
                    

    # print world map
    for i in range(height):
        for j in range(width):
            print(world_map[i][j], end='')
        print()
    # print new world map
    for i in range(height):
        for j in range(width):
            print(new_world_map[i][j], end='')
        print()
'''