import time

colors ={
    "red"     : "\033[41m",
    "green"   : "\033[42m",
    "yellow"  : "\033[43m",
    "blue"    : "\033[44m",
    "magenta" : "\033[45m",
    "cyan"    : "\033[46m",
    'white'   : "\033[47m"
}
wall_colors = {
    "yellow" : '\033[93m',
    "blue" : '\033[94m',
    "pink" : '\033[95m',
    "red" : '\033[91m',
    "green" : '\033[92m'}

def print_maze(maze, colors, wall_color):
    width = len(maze.maze[0])
    height = len(maze.maze)
    print(wall_color+"╔", end="")
    cx = 0
    while cx<len(maze.maze[0]):
        print(wall_color+"════", end="")
        if cx < len(maze.maze[0]) - 1:
            if maze.maze[0][cx]["walls"] >> 1 & 1 == 1:
                print(wall_color+"╦", end="")
            else:
                print(wall_color+"═", end="")
        cx+=1
    print(wall_color+"╗")
    for y in range(len(maze.maze)):
        x = 0
        print(wall_color+"║", end="")
        while x < width:
            if x < width - 1:
                if maze.maze[y][x]["walls"] == 15:
                     print(colors + "    " + "\033[0m"+wall_color+"║", end = "")
                elif maze.maze[y][x]["walls"] >> 1 & 1 == 1:
                    if maze.maze[y][x]["path"] == True:
                        print("  • ║", end="")
                    else:
                        print(wall_color+"    ║", end = "")
                else:
                    if maze.maze[y][x]["path"] == True:
                        print("  •  ", end="")
                    else:
                        print("     ", end="")
            x+=1
        if maze.maze[y][width-1]["walls"] == 15:
            print(colors +"    " + "\033[0m"+wall_color+"║")
        else:
            if maze.maze[y][width - 1].get("path", False):
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
                    # print(" ", end="")
                    if maze.maze[y][x]["walls"] >> 2 & 1 == 1 and maze.maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze.maze[y][x]["walls"] >> 1 & 1 == 1 and maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"╩", end="")
                        if maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0 and  maze.maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"═", end="")
                        if  maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze.maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"╦", end="")
                    if maze.maze[y][x + 1]["walls"] >> 2 & 1 == 0:
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze.maze[y][x]["walls"] >> 1 & 1 == 1)):
                            print(" ", end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze.maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(wall_color+"╗",end="")
                        if all((maze.maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze.maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(wall_color+"╣", end="")
                        if all(( maze.maze[y][x]["walls"] >> 2 & 1 == 0,
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
                    if  maze.maze[y][x]["walls"] >> 2 & 1 == 0 and  maze.maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze.maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"╔",end="")             
                        if  maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze.maze[y][x]["walls"] >> 1 & 1 == 1:
                            print(wall_color+"╚",end="")
                        if maze.maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze.maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(" ", end="")
                        if  maze.maze[y + 1][x]["walls"] >> 1 & 1 == 1 and  maze.maze[y][x]["walls"] >> 1 & 1 == 1:
                            print(wall_color+"╠", end="")     
            x+=1
        if y < height - 1 :
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
        cx+=1
    print(wall_color+"╝"+"\033[0m")

def display_path(maze, path):
    
    for x, y in path:
        maze.maze[x][y]["path"] = True
        print_maze(maze, "\033[41m","\033[92m")
        print("\33c" , end="")
        time.sleep(0.5)