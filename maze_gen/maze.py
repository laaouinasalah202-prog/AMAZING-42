import random
import os
import time
#from ..display_maze import print_maze, colors, wall_colors
#from menu import maze_menu


class MazeGenerator():
    def __init__(self, width, height, entry, ex):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = ex
        self.maze = self.creat_maze()

    def creat_maze(self):
        maze = [[{"visited": False, "protected": False, "path": False ,"walls": 15} 
        for _ in range(self.width)] for _ in range(self.height)]
        return maze

    def set_42(self):
        center_x = self.width // 2
        center_y = self.height // 2
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
                self.maze[x][y]["protected"] = True
        return coordinate
        

# def maze_to_hex(maze):
#     f = open("output_maze.txt", 'w')

#     for i in maze:
#         for j in i:
#             f.write(str(hex(j["walls"]))[2:])
#         f.write("\n")


# if __name__ == "__main__":
#     maze = MazeGenerator(13,13, (0,0), (4,4))

#     color = colors["green"]
#     wall_color = wall_colors["red"]
#     maze.maze_build(color, wall_color, True)
#     print_maze(maze, color, wall_color)

#     #maze_tohex(maze)
#     while(1):
#         maze = MazeGenerator(13,13, (0,0), (4,4))
#         path = path_finding(maze, (0,0), (12, 12))
#         maze_menu(maze.width, maze.height, maze, path)
