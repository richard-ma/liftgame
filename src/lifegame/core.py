#-*- coding: utf-8 -*-

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
                else: # x, y is alive
                    if around_sum >= 2 or around_sum <= 3: # around sum is 2 or 3
                        new_alive.append((x, y))
        
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
    alives = [(0, 0), (1, 0), (0, 1), (1, 1), (-2, 3), (-2, 4), (-3, 4), (-3, 3)]
    mp = MapPrinter()
    world = World(alives)
    print(world.get_alive())
    mp.print(world.get_alive())
    world.step_forward()
    print('-' * 30)
    print(world.get_alive())
    mp.print(world.get_alive())
    

    # mp = MapPrinter()
    # mp.print(map_data)
    # print(mp.x_min, mp.x_max)
    # print(mp.y_min, mp.y_max)
    # print(mp.get_width(), mp.get_height())


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