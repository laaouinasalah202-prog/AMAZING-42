from maze_gen import MazeGenerator, shortest_path
from parssing import parssing
import sys
import random
from menu import MENU, maze_menu
from display_maze import print_maze


def only_close_neighbors(maze, coordinates):
    """
    Return neighboring cells that are reachable (no wall in between).

    Checks the wall bitmask of the current cell to determine open paths.
    """
    neighbors = []
    r, c = coordinates
    # upper neighbor
    if ((maze[r][c]["walls"] >> 0) & 1) == 1 and r > 0:
        if maze[r - 1][c]["protected"] == False:
            neighbors.append((r-1, c))

    # down neighbor
    if ((maze[r][c]["walls"] >> 2) & 1) == 1 and r < len(maze) - 1:
        if maze[r + 1][c]["protected"] == False:
            neighbors.append((r + 1, c))

    # left neighbor
    if ((maze[r][c]["walls"] >> 3) & 1) == 1 and c > 0:
        if maze[r][c - 1]["protected"] == False:
            neighbors.append((r, c - 1))

    # right neighbor
    if ((maze[r][c]["walls"] >> 1) & 1) == 1 and c < len(maze[0]) - 1:
        if maze[r][c + 1]["protected"] == False:
            neighbors.append((r, c + 1))

    return neighbors

def remove_wall_between(cell1, cell2, maze):
    """
    remove the wall according to its position
    """
    r1, c1 = cell1
    r2, c2 = cell2

    if r1 == r2:
        if c1 < c2:
            maze[r1][c1]["walls"] -= 2
            maze[r2][c2]["walls"] -= 8
        elif c1 > c2:
            maze[r1][c1]["walls"] -= 8
            maze[r2][c2]["walls"] -= 2

    elif c1 == c2:
        if r1 < r2:
            maze[r1][c1]["walls"] -= 4
            maze[r2][c2]["walls"] -= 1
        elif r1 > r2:
            maze[r1][c1]["walls"] -= 1
            maze[r2][c2]["walls"] -= 4


def count_walls(n):
    i = 0
    c = 0
    while i < 4:
        if (n >> i & 1):
            c += 1
        i += 1
    return c

def break_cell(maze, cell, coordinates):
    if count_walls(cell["walls"] < 3) or cell["protected"]:
        return

    neighbors = only_close_neighbors(maze.maze, coordinates)
    if neighbors:
        remove_wall_between(coordinates, random.choice(neighbors), maze.maze)


def imperfect_maze(maze):
    r = 0
    for row in maze.maze:
        c = 0
        for cell in row:
            if random.random() > 0.5:
                break_cell(maze, cell, (r, c))
            c += 1
        r += 1

if __name__ == "__main__":
    """
    Main script to generate and interact with a maze.

    Usage:
        python3 a_maze_ing.py config.txt

    Reads maze configuration from a file, creates the maze
    ,optionally seeds randomness,generates the maze using a selected algorithm,
    computes the shortest path, and launches an interactive menu for the user.
    """

    if len(sys.argv) == 1:
        print("Usage: python3 a_maze_ing.py config.txt")
        exit(1)
    else:
        file_path = sys.argv[1]
    n_config = parssing(file_path)
    try:
        width = n_config["WIDTH"]
        height = n_config["HEIGHT"]
        entry = n_config["ENTRY"]
        exit_p = n_config["EXIT"]
        out_file = n_config["OUTPUT_FILE"]
        perfect = n_config["PERFECT"]
        maze = MazeGenerator(width, height, entry, exit_p, out_file, perfect)
        if "seed" in [c.lower() for c in n_config]:
            random.seed(n_config["SEED"])
    except Exception as e:
        print(f"Error: {e}")
    try:
        menu = MENU(False, "\033[95m", "\033[44m", "prims")
        maze = MazeGenerator(width, height, entry, exit_p, out_file, perfect)
        menu.generate_maze(maze)
        print("\33c", end="")
        imperfect_maze(maze)
        print_maze(maze, menu.color, menu.wall_color)
        shortest_path(maze)
    except KeyboardInterrupt:
        exit(0)
    #while True:
    #    try:
    #    maze_menu(maze, menu)
    #    except KeyboardInterrupt:
    #        exit(0)
