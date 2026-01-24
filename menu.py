from maze import MazeGenerator
from display_maze import print_maze , display_path, colors, wall_colors

def maze_menu(width, height, maze, path):
    print("== A-MAZE-ING ==")
    print("1. Re-generate a new maze")
    print("2. show/Hide path from entry to exit")
    print("3. Rotate maze colors")
    print("4. change algorithms")
    print("5. Quit")
    print("Choice? (1-5):")
    choice = input()
    if  choice == '1':
        maze.maze_build("\033[41m", "\033[92m",True)
        print_maze(maze, "\033[41m","\033[92m")
    elif choice == "2":
        print("show path from entry to exit")
        display_path(maze, path, True)
    elif choice == "3":
        print("Enter cell color from : red green yellow blue magenta cyan white")
        color =input()
        print("Enter wall color from : yellow blue pink red green")
        wall_color = input()
        for i in colors:
            if i == color:
                c = colors[i]
        for j in wall_colors:
            if j == wall_color:
                maze.maze_build(c, wall_colors[j], True)
                print_maze(maze, c, wall_colors[j])
                #maze_tohex(maze)
                break
    elif choice == "4":
        exit()
