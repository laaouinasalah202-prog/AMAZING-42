from maze_gen import MazeGenerator, shortest_path
from parssing import parssing
import sys
import random
from menu import MENU, maze_menu


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

    menu = MENU(False, "\033[95m", "\033[44m", "prims")
    maze = MazeGenerator(width, height, entry, exit_p, out_file, perfect)
    menu.generate_maze(maze)
    shortest_path(maze)

    while True:
        try:
            maze_menu(maze, menu)
        except KeyboardInterrupt:
            exit(0)
