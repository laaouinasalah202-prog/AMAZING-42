class MazeGenerator:
    def __init__(self, width, height, entry, ex, out_file, perfect):
        self._width = self.width_setter(width)
        self._height = self.height_setter(height)
        self._entry = self.entry_setter(entry)
        self._exit_p = self.exit_setter(ex)
        self._out_file = out_file
        self._perfect = perfect
        self.maze = self.creat_maze()
        self.path = []

    def set_42(self, maze):
        center_x = self._width // 2
        center_y = self._height // 2
        coordinate = [ [(center_y, center_x - k) for k in range(1, 4) if center_x - k >= 0],
                        [(center_y - k, center_x - 3) for k in range(1, 3) if center_y - k >= 0],
                        [(center_y + k, center_x - 1) for k in range(1, 3) if center_y - k >= 0],
                        [(center_y, center_x + k) for k in range(1, 4) if center_x - k >= 0],
                        [(center_y + k, center_x + 1) for k in range(1, 3) if center_y - k >= 0],
                        [(center_y + 2, center_x + k) for k in range(1, 4) if center_x - k >= 0],
                        [(center_y - k, center_x + 3) for k in range(1, 2) if center_x - k >= 0],
                        [(center_y - 2, center_x + k) for k in range(1, 4) if center_x - k >= 0]
                        ]
        for n in coordinate:
            for x, y in n:
                maze[x][y]["protected"] = True
        return coordinate

    def creat_maze(self):
        maze = [[{"visited": False, "protected": False, "path": False ,"walls": 15} 
        for _ in range(self._width)] for _ in range(self._height)]
        self.set_42(maze)
        return maze

    def width_setter(self, width):
        if width < 10:
            raise ValueError(f"Error: Width {width} is below minimum 10")
        elif width > 30:
            raise ValueError(f"Error: width {width} exceeds maximum 30")
        else:
            return width

    def height_setter(self, height):
        if height < 8:
            raise ValueError(f"Error: Height {height} is below minimum 10")
        elif height > 25:
            raise ValueError(f"Error: Height {height} exceeds maximum 25")
        else:
            return height
    
    def entry_setter(self, entry):
        x, y = entry
        if x < 0 or x > self._width - 1:
            raise ValueError(f"set ({entry}) out of range")
        elif y < 0 or y > self._height - 1:
            raise ValueError(f"set ({entry}) out of range")
        else:
            return entry
    
    def exit_setter(self, exit_p):
        x,y = exit_p
        if exit_p == self._entry:
            raise ValueError(f"Error: Starting cell and ending cell overlap")
        if x < 0 or x > self._width - 1:
            raise ValueError(f"set ({exit_p}) out of range")
        elif y < 0 or y > self._height - 1:
            raise ValueError(f"set ({exit_p}) out of range")
        else:
            return exit_p

    def maze_to_hex(self):
        with open(self._out_file, 'w') as f:
            for i in self.maze:
                for j in i:
                    f.write(str(hex(j["walls"]))[2:])
                f.write("\n")
            print("\n")