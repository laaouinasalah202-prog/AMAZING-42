from maze_gen import MazeGenerator, shortest_path
from parssing import parssing
import sys
from menu import MENU, maze_menu
from display_maze import print_maze

if __name__ == "__main__":
    """
    Main script to generate and interact with a maze.

    Usage:
        python3 a_maze_ing.py config.txt

    Reads maze configuration from a file, creates the maze
    ,optionally seeds randomness,generates the maze using a selected algorithm,
    computes the shortest path, and launches an interactive menu for the user.
    """
    print("\033[2J")
    print("\033[3J")


    if len(sys.argv) == 1:
        print("Usage: python3 a_maze_ing.py config.txt")
        exit(0)
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
        seed = None
        if "seed" in [c.lower() for c in n_config]:
            seed = n_config["SEED"]
        maze = MazeGenerator(width, height, entry, exit_p, out_file, perfect, seed)
    except Exception as e:
        print(f"Error: {e}")
        exit(0)
    try:
        menu = MENU(False, "\033[94m", "\033[47m", "prims")
        maze = MazeGenerator(width, height, entry, exit_p, out_file, perfect, seed)
        menu.generate_maze(maze)
        print("\33c", end="")
        print_maze(maze, menu.color, menu.wall_color)
        shortest_path(maze)
    except KeyboardInterrupt:
        print("\33c", end="") 
        exit(0)
    while True:
       try:
           maze_menu(maze, menu)
       except KeyboardInterrupt:
            print("\33c", end="")
            exit(0)
