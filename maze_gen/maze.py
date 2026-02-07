import random

class MazeGenerator:
    def __init__(self, width, height, entry, ex, out_file, perfect, seed):
        self._width = self.width_setter(width)
        self._height = self.height_setter(height)
        self._entry = self.entry_setter(entry)
        self._exit_p = self.exit_setter(ex)
        self._out_file = out_file
        self._perfect = perfect
        self.seed = seed
        self.maze = self.creat_maze()
        self.path = []

    def set_42(self, maze):
        """
        Mark a specific 42 pattern of cells near the maze center as protected.

        Returns the list of coordinates that were marked.
        """
        center_x = self._width // 2
        center_y = self._height // 2
        coordinate = [
                    [(center_y, center_x - k) for k in range(1, 4)
                        if center_x - k >= 0],
                    [(center_y - k, center_x - 3) for k in range(1, 3)
                        if center_y - k >= 0],
                    [(center_y + k, center_x - 1) for k in range(1, 3)
                        if center_y - k >= 0],
                    [(center_y, center_x + k) for k in range(1, 4)
                        if center_x - k >= 0],
                    [(center_y + k, center_x + 1) for k in range(1, 3)
                        if center_y - k >= 0],
                    [(center_y + 2, center_x + k) for k in range(1, 4)
                        if center_x - k >= 0],
                    [(center_y - k, center_x + 3) for k in range(1, 2)
                        if center_x - k >= 0],
                    [(center_y - 2, center_x + k) for k in range(1, 4)
                        if center_x - k >= 0]
            ]
        for n in coordinate:
            for x, y in n:
                maze[x][y]["protected"] = True
        return coordinate

    def creat_maze(self):
        """
        Create a new maze grid with all cells initialized.
        Returns the maze as a 2D list of cell dictionaries.
        """
        maze = [[
            {"visited": False, "protected": False, "path": False, "walls": 15}
            for _ in range(self._width)]
            for _ in range(self._height)
            ]
        self.set_42(maze)
        e_r, e_c = self._entry
        x_r, x_c = self._exit_p
        if maze[e_r][e_c]["protected"]:
            raise ValueError("Entry should be out of 42 pattern")
        elif maze[x_r][x_c]["protected"]:
            raise ValueError("Exit should be out of 42 pattern")
        return maze

    def width_setter(self, width):
        """
        Validate and set the maze width.

        Raises a ValueError if the width is not between 10 and 30.
        Returns the width if valid.
        """
        try:
            if width < 10:
                raise ValueError(f"Error: Width {width} is below minimum 10")
            else:
                return width
        except ValueError as e:
            print(f"{e}")
            exit(0)

    def height_setter(self, height):
        """
        Validate and set the maze height.

        Raises a ValueError if the height is not between 8 and 25.
        Returns the height if valid.
        """
        if height < 8:
            raise ValueError(f"Error: Height {height} is below minimum 10")
        else:
            return height

    def entry_setter(self, entry):
        """
        Validate and set the maze entry point.

        Raises a ValueError if the entry coordinates are out of maze bounds.
        Returns the entry coordinates if valid.
        """
        x, _ = entry
        if x < 0 or x > self._width - 1:
            raise ValueError(f"set {entry} out of range")
        else:
            return entry

    def exit_setter(self, exit_p):
        """
        Validate and set the maze exit point.

        Raises a ValueError if the exit coordinates are out of maze bounds
        or overlap with the entry point. Returns the exit coordinates if valid.
        """
        x, y = exit_p
        if exit_p == self._entry:
            raise ValueError("Error: Starting cell and ending cell overlap")
        if x < 0 or x > self._width - 1:
            raise ValueError(f"set {exit_p} out of range")
        elif y < 0 or y > self._height - 1:
            raise ValueError(f"set {exit_p} out of range")
        else:
            return exit_p

    def maze_to_hex(self):
        """
        Save the maze walls as hexadecimal values to a file.
        Writes each row of the maze as a line
        of hex strings to `self._out_file`.
        """
        path = ""
        i = 0
        while i < len(self.path) - 1:
            r , c = self.path[i]
            r_n , c_n = self.path[i + 1]

            if c < c_n:
                path += "E"
            elif c > c_n:
                path += "W"
            elif r < r_n:
                path += "S"
            elif r > r_n:
                path += "N"
            i += 1

        with open(self._out_file, 'w') as f:
            for i in self.maze:
                for j in i:
                    f.write(str(hex(j["walls"]))[2:])
                f.write("\n")
            f.write("\n")
            entry = str(self._entry).strip('()')
            f.write(entry.replace(" ", ""))
            f.write("\n")
            exit_p = str(self._exit_p).strip('()')
            f.write(exit_p.replace(" ", ""))
            f.write("\n")
            f.write(path)
            f.write("\n")