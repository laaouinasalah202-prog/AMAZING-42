from mazegen import shortest_path, MazeGenerator, generate_maze
from display_maze import print_maze, display_path, colors, wall_colors


class MENU:
    """
    Represents the user interface for maze generation and visualization.

    Attributes:
        path (bool): Whether to display the solution path.
        wall_color (str): Color code for maze walls.
        color (str): Color code for maze cells.
        algo_name (str): Name of the maze generation algorithm
        ("prims" or "backtrack").
    """
    first_gen = True

    def __init__(
            self, path: bool,
            wall_color: str,
            color: str,
            algo_name: str
            ):
        """
        Initialize the MENU instance with colors and algorithm choice.
        """
        self.path: bool = path
        self.wall_color: str = wall_color
        self.color: str = color
        self.algo_name: str = algo_name

    def change_wall_color(self, new_color: str) -> None:
        """
        Change the wall color if the new color exists in `wall_colors`.
        """
        if new_color.lower() in wall_colors.keys():
            self.wall_color = wall_colors[new_color]

    def change_color(self, new_color: str) -> None:
        """
        Change the cell color if the new color exists in `colors`.
        """
        if new_color.lower() in colors.keys():
            self.color = colors[new_color]


def maze_menu(maze: MazeGenerator, menu: MENU) -> None:
    """
    Display an interactive console menu for the maze.

    Allows the user to:
        1. Regenerate the maze
        2. Show/hide the solution path
        3. Change cell and wall colors
        4. Switch maze generation algorithms
        5. Save the maze to a file
        6. Quit the program
    """
    print("== A-MAZE-ING ==")
    print("1. Re-generate a new maze")
    print("2. show/Hide path from entry to exit")
    print("3. change maze colors")
    print("4. change algorithms")
    print("5. save maze to file")
    print("6. Quit")
    print("Choice? (1-6):")
    choice = input()
    if choice == '1':
        print("\33c", end="")
        MENU.first_gen = True
        maze.maze = maze.creat_maze()
        generate_maze(
            maze,
            menu.algo_name,
            print_maze,
            color=menu.color,
            wall_color=menu.wall_color
            )
        shortest_path(maze)
        print_maze(maze, menu.color, menu.wall_color)
    elif choice == "2":
        if menu.path:
            menu.path = False
            print("\33c", end="")
            print_maze(maze, menu.color, menu.wall_color)
        else:
            menu.path = True
            print("\33c", end="")
            if MENU.first_gen:
                display_path(maze, menu.color, menu.wall_color)
            else:
                print_maze(maze, menu.color, menu.wall_color, True)
            MENU.first_gen = False
    elif choice == "3":
        print("Enter cell color: red green yellow blue magenta cyan white")
        color = input()
        print("Enter wall color: yellow blue pink red green")
        wall_color = input()
        menu.change_color(color)
        menu.change_wall_color(wall_color)
        print("\33c", end="")
        print_maze(maze, menu.color, menu.wall_color)
    elif choice == "4":
        print("available algorithms:")
        print("1. backtracking algorithm")
        print("2. prims algorithm")
        algo_name = input("choose algo name (1/2): ")
        print("\33c", end="")
        print_maze(maze, menu.color, menu.wall_color)
        if algo_name == "1":
            menu.algo_name = "backtrack"
            print("algorithm updated")
        elif algo_name == "2":
            menu.algo_name = "prims"
            print("algorithm updated")
        else:
            print("Invalid choice !")
        print()
    elif choice == "5":
        print("\33c", end="")
        print_maze(maze, menu.color, menu.wall_color)
        maze.maze_to_hex()
        print(f"Maze saved to {maze._out_file}\n")
    elif choice == "6":
        exit(0)
    else:
        print("\33c", end="")
        print_maze(maze, menu.color, menu.wall_color)
