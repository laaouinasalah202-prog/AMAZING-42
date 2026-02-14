"""Maze visualization and display utilities.

This module provides functions to render mazes in the terminal using
Unicode box-drawing characters with customizable colors. It supports
displaying static mazes and animating solution paths.
"""

import time
from mazegen import MazeGenerator

colors = {
    "red": "\033[41m",
    "green": "\033[42m",
    "yellow": "\033[43m",
    "blue": "\033[44m",
    "magenta": "\033[45m",
    "cyan": "\033[46m",
    'white': "\033[47m"
}
wall_colors = {
    "yellow": '\033[93m',
    "blue": '\033[94m',
    "pink": '\033[95m',
    "red": '\033[91m',
    "green": '\033[92m'}


def print_maze(maze: MazeGenerator,
               colors: str,
               wall_color: str,
               path: bool = False
               ) -> None:
    """Print the maze to the console using Unicode box-drawing characters.

    Displays walls, open spaces, and optionally the solution path with
    customizable colors for walls and cells.

    Args:
        maze: A MazeGenerator instance containing the maze to display.
        colors: ANSI color code for cell backgrounds.
        wall_color: ANSI color code for wall characters.
        path: If True, displays the solution path with bullet markers.
            Defaults to False.
    """
    print("\033[H", end="")
    print("\033[?25l")
    width = len(maze.maze[0])
    height = len(maze.maze)
    print(wall_color+"╔", end="")
    cx = 0
    while cx < len(maze.maze[0]):
        print(wall_color+"════", end="")
        if cx < len(maze.maze[0]) - 1:
            if maze.maze[0][cx]["walls"] >> 1 & 1 == 1:
                print(wall_color+"╦", end="")
            else:
                print(wall_color+"═", end="")
        cx += 1
    print(wall_color+"╗")
    for y in range(len(maze.maze)):
        x = 0
        print(wall_color+"║", end="")
        while x < width:
            if x < width - 1:
                if (y, x) == maze._entry:
                    print("\033[91m  E \033[0m"+wall_color, end="")
                    if maze.maze[y][x]["walls"] >> 1 & 1 == 1:
                        print("║", end="")
                    else:
                        print(" ", end="")
                    x += 1
                    continue
                elif (y, x) == maze._exit_p:
                    print("\033[91m  X \033[0m"+wall_color, end="")
                    if maze.maze[y][x]["walls"] >> 1 & 1 == 1:
                        print("║", end="")
                    else:
                        print(" ", end="")
                    x += 1
                    continue
                if maze.maze[y][x]["walls"] == 15:
                    print(colors + "    " + "\033[0m"+wall_color+"║", end="")
                elif maze.maze[y][x]["walls"] >> 1 & 1 == 1:
                    if maze.maze[y][x]["path"] and path:
                        print("  • ║", end="")
                    else:
                        print(wall_color+"    ║", end="")
                else:
                    if maze.maze[y][x]["path"] and path:
                        print("  •  ", end="")
                    else:
                        print("     ", end="")
            x += 1
        if (y, width-1) == maze._entry:
            print("\033[91m  E \033[0m"+wall_color+"║")
        elif (y, width-1) == maze._exit_p:
            print("\033[91m  X \033[0m"+wall_color+"║")
        elif maze.maze[y][width-1]["walls"] == 15:
            print(colors + "    " + "\033[0m"+wall_color+"║")
        else:
            if maze.maze[y][width - 1].get("path", False) and path:
                print("  • ║")
            else:
                print("    ║")
        x = 0
        while x < width - 1:
            if y < height - 1:
                if x < width - 1:
                    if x == 0:
                        if maze.maze[y][0]["walls"] >> 2 & 1 == 1:
                            print(wall_color+"╠", end="")
                        else:
                            print(wall_color+"║", end="")
                    if maze.maze[y][x]["walls"] >> 2 & 1 == 1:
                        print(wall_color+"════", end="")
                        if all((
                            maze.maze[y][x + 1]["walls"] >> 2 & 1,
                            maze.maze[y + 1][x]["walls"] >> 1 & 1,
                            maze.maze[y][x]["walls"] >> 1 & 1,
                        )):
                            print(wall_color+"╬", end="")
                    else:
                        print("    ", end="")
                    if maze.maze[y][x + 1]["walls"] >> 2 & 1 == 0:
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 0)):
                            print(" ", end="")
                    if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze.maze[y][x + 1]["walls"] >> 2 & 1 == 1)):
                        if all((maze.maze[y][x]["walls"] >> 1 & 1 == 1,
                               maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0)):
                            print(wall_color+"╩", end="")
                        if all((maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                               maze.maze[y][x]["walls"] >> 1 & 1 == 0)):
                            print(wall_color+"═", end="")
                        if all((maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                               maze.maze[y][x]["walls"] >> 1 & 1 == 0)):
                            print(wall_color+"╦", end="")
                    if maze.maze[y][x + 1]["walls"] >> 2 & 1 == 0:
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 1)):
                            print(" ", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(wall_color+"╗", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(wall_color+"╣", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(wall_color+"║", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(" ", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze.maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(" ", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                                maze.maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(wall_color+"╝", end="")
                    if all((maze.maze[y][x]["walls"] >> 2 & 1 == 0,
                           maze.maze[y][x + 1]["walls"] >> 2 & 1 == 1)):
                        if all((maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                               maze.maze[y][x]["walls"] >> 1 & 1 == 0)):
                            print(wall_color+"╔", end="")
                        if all((maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                               maze.maze[y][x]["walls"] >> 1 & 1 == 1)):
                            print(wall_color+"╚", end="")
                        if all((maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                               maze.maze[y][x]["walls"] >> 1 & 1 == 0)):
                            print(" ", end="")
                        if all((maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                               maze.maze[y][x]["walls"] >> 1 & 1 == 1)):
                            print(wall_color+"╠", end="")
            x += 1
        if y < height - 1:
            if maze.maze[y][x]["walls"] >> 2 & 1 == 1:
                print(wall_color+"════╣")
            else:
                print(wall_color+"    ║")

    print(wall_color+"╚", end="")
    cx = 0
    while cx < len(maze.maze[height-1]):
        print(wall_color+"════", end="")
        if cx < len(maze.maze[height-1]) - 1:
            if maze.maze[height-1][cx]["walls"] >> 1 & 1 == 1:
                print(wall_color+"╩", end="")
            else:
                print(wall_color+"═", end="")
        cx += 1
    print(wall_color+"╝"+"\033[0m")


def display_path(maze: MazeGenerator, color: str, wall_color: str) -> None:
    """Animate the maze solution path step by step in the console.

    Marks each cell in the solution path and updates the display,
    creating an animation effect showing the path from entry to exit.

    Args:
        maze: A MazeGenerator instance containing the maze and solution path.
        color: ANSI color code for cell backgrounds.
        wall_color: ANSI color code for wall characters.
    """
    for x, y in maze.path:
        print("\33c", end="")
        maze.maze[x][y]['path'] = True
        print_maze(maze, color, wall_color, True)
        time.sleep(0.05)
