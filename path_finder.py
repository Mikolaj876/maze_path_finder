class OutOfRange(BaseException):
    def __init__(self, indx, maxs):
        self.indx = indx
        self.maxs = maxs
        self.message = f"{self.indx} are to big. The maximum size is {self.maxs}"
        print(self.message)
class Path():

    def __init__(self, start=(0,0), end=(7,7)):
        self.grid = [[0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 0, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0],
    ]
                    
                
        self.moves = [(0,1), (1,0), (-1,0), (0, -1)]
        self.in_bounds_list = self.in_bounds(self.grid)
        self.path_ = []
        self.visited = []
        self.start = start
        self.end = end

    def shortest_path(self):
        func = self.rec_search(self.start)
        if func[0] == "END":
            return self.polish_path(func[1])

        return func

    def ret_value_at(self, grid, x, y):
        if (y <= len(grid) - 1) and (x < len(grid[y])):
            return grid[y][x]

        else:
            raise OutOfRange((f"{x} or {y}"), len(grid) - 1)

    def in_bounds(self, grid):
        in_bounds = []
        for y in range(0,len(grid)):
            for x in range(0,len(grid)):
                in_bounds.append((x,y))

        return in_bounds

    def neighbours(self, x, y):
        open_neighbours = []
        for mov in self.moves:
            mot_x = int(x)
            mot_y = int(y)
            mot_x += mov[0]
            mot_y += mov[1]

            if (mot_x, mot_y) in self.in_bounds_list and self.ret_value_at(self.grid, mot_x, mot_y) != 1:
                open_neighbours.append((mot_x, mot_y))

        return open_neighbours

    def rec_search(self, cords):
        x = cords[0]
        y = cords[1]
        self.path_.append((x,y))
        self.visited.append((x,y))
        
        if (x,y) == self.end:
            return ["END", self.path_]

        for neighbour in self.neighbours(x, y):
            if neighbour not in self.visited:
                self.path_.append((x,y))
                self.visited.append((x,y))
                return self.rec_search(neighbour)

        self.visited.remove((x, y))
        self.path_.pop()
        return ["No path.", False]

    def polish_path(self, path_):
        polished = []
        for element in path_:
            if element not in polished:
                polished.append(element)

        return polished