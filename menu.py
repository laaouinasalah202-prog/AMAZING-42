from maze_gen import prims_algo, backtrack_algo, shortest_path
from display_maze import print_maze, display_path, colors, wall_colors

class MENU:
    first_gen = True
    def __init__(self, path: bool, wall_color: str, color: str, algo_name: str):
        self.path: bool = path
        self.wall_color: str = wall_color
        self.color: str = color
        self.algo_name: str = algo_name

    def change_wall_color(self, new_color):
        if new_color.lower() in wall_colors.keys():
            self.wall_color = wall_colors[new_color]
    
    def change_color(self, new_color):
        if new_color.lower() in colors.keys():
            self.color = colors[new_color]

    def generate_maze(self, maze):
        if self.algo_name == "prims":
            prims_algo(maze, self.color, self.wall_color, True)
        elif self.algo_name == "backtrack":
            backtrack_algo(maze, self.color, self.wall_color, True)
        print_maze(maze, self.color, self.wall_color)

def maze_menu(maze, menu):
    print("== A-MAZE-ING ==")
    print("1. Re-generate a new maze")
    print("2. show/Hide path from entry to exit")
    print("3. change maze colors")
    print("4. change algorithms")
    print("5. save maze to file")
    print("6. Quit")
    print("Choice? (1-6):")
    choice = input()
    if  choice == '1':
        print("\33c" , end="")
        maze.maze = maze.creat_maze()
        menu.generate_maze(maze)
        shortest_path(maze)
    elif choice == "2":
        if menu.path == True:
            menu.path = False
            print("\33c" , end="")
            print_maze(maze, menu.color,menu.wall_color)
        else:
            menu.path = True
            print("\33c" , end="")
            if MENU.first_gen == True:
                display_path(maze, menu)
            else:
                print_maze(maze, menu.color,menu.wall_color, True)
            MENU.first_gen = False
    elif choice == "3":
        print("Enter cell color from : red green yellow blue magenta cyan white")
        color = input()
        print("Enter wall color from : yellow blue pink red green")
        wall_color = input()
        menu.change_color(color)
        menu.change_wall_color(wall_color)
        print("\33c" , end="")
        print_maze(maze, menu.color, menu.wall_color)
    elif choice == "4":
        print("available algorithms:")
        print("1. backtracking algorithm")
        print("2. prims algorithm")
        algo_name = input("choose algo name (1/2): ")
        print("\33c" , end="")
        print_maze(maze, menu.color,menu.wall_color)
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
        print("\33c" , end="")
        print_maze(maze, menu.color,menu.wall_color)
        print(f"Maze saved to {maze._out_file}\n")
        maze.maze_to_hex()
    elif choice == "6":
        exit(0)
    else:
        print("\33c" , end="")
        print_maze(maze, menu.color,menu.wall_color)