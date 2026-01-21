import random
import os

def intitial_map(width: int, high: int):
    maze = []
    for r in range(high):
        row = []
        for col in range(width):
            row.append({
                "visited": False,
                "walls": 15
            }
        )
        maze.append(row)
    return maze


def print_maze(maze, colors):
    width = len(maze[0])
    hight = len(maze)
    print("╔", end="")
    cx = 0
    while cx<len(maze[0]):
        print("════", end="")
        if cx < len(maze[0]) - 1:
            if maze[0][cx]["walls"] >> 1 & 1 == 1:
                print("╦", end="")
            else:
                print("═", end="")
        cx+=1
    print("╗")
    for y in range(len(maze)):
        x = 0
        print("║", end="")
        while x < width:
            if x < width - 1:
                if maze[y][x]["walls"] == 15:
                     print(colors + " \U0001F606 " + "\033[0m"+"║", end = "")
                elif maze[y][x]["walls"] >> 1 & 1 == 1:
                    print("    ║", end = "")
                else:
                    print("     ", end="")
            x+=1
        if maze[y][width-1]["walls"] == 15:
            print(colors +" \U0001F92B " + "\033[0m"+"║")
        else:
            print("    ║")

        x = 0
        while x < width - 1:
            if y < hight - 1:
                if x < width - 1:
                    if x == 0:
                        if maze[y][0]["walls"] >> 2 & 1 == 1:
                            print("╠", end="")
                        else:
                            print("║", end="")
                    if maze[y][x]["walls"] >> 2 & 1 == 1:
                        print("════", end="")
                        if all((
                            maze[y][x + 1]["walls"] >> 2 & 1,
                            maze[y + 1][x]["walls"] >> 1 & 1,
                            maze[y][x]["walls"] >> 1 & 1,
                        )):
                            print("╬", end="")
                    else:
                        print("    ", end="")
                    # print(" ", end="")
                    if maze[y][x]["walls"] >> 2 & 1 == 1 and maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze[y][x]["walls"] >> 1 & 1 == 1 and maze[y + 1][x]["walls"] >> 1 & 1 == 0:
                            print("╩", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and  maze[y][x]["walls"] >> 1 & 1 == 0:
                            print("═", end="")
                        if  maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print("╦", end="")
                    if maze[y][x + 1]["walls"] >> 2 & 1 == 0:
                        if all((maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(" ", end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print("╗",end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print("╣", end="")
                        if all(( maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print("║", end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(" ", end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(" ", end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print("╝", end="")
                    if  maze[y][x]["walls"] >> 2 & 1 == 0 and  maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print("╔",end="")             
                        if  maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 1:
                            print("╚",end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(" ", end="")
                        if  maze[y + 1][x]["walls"] >> 1 & 1 == 1 and  maze[y][x]["walls"] >> 1 & 1 == 1:
                            print("╠", end="")     
            x+=1
        if y < hight - 1 :
            if maze[y][x]["walls"] >> 2 & 1 == 1:
                print("════╣")
            else:
                print("    ║")

    print("╚", end="")
    cx = 0
    while cx < len(maze[hight-1]):
        print("════", end="")
        if cx < len(maze[hight-1]) - 1:
            if maze[hight-1][cx]["walls"] >> 1 & 1 == 1:
                print("╩", end="")
            else:
                print("═", end="")
        cx+=1
    print("╝")
    

def maze_build(maze, color):

    visited = [[False for i in maze[0]] for a in maze]

    dirs = [
    (0, -1, 0, 2),
    (1, 0, 1, 3),
    (0, 1, 2, 0),
    (-1, 0, 3, 1)
    ]

    def check_boundry(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])

    def remove_wall_between(cell1, cell2, maze):
        r1 , c1 = cell1
        r2 , c2 = cell2

        r = 2
        l = 8
        up = 1
        dn = 4
        if r1 == r2:
            if c1 < c2:
                maze[r1][c1]["walls"] -= r
                maze[r2][c2]["walls"] -= l
            elif c1 > c2:
                maze[r1][c1]["walls"] -= l
                maze[r2][c2]["walls"] -= r

        elif c1 == c2:
            if r1 < r2:
                maze[r1][c1]["walls"] -= dn
                maze[r2][c2]["walls"] -= up
            elif r1 > r2:
                maze[r1][c1]["walls"] -= up
                maze[r2][c2]["walls"] -= dn

    def backtrack(x, y, color):
        print_maze(maze, color)
        time.sleep(0.05)
        os.system("clear")

        visited[x][y] = True

        for dx, dy, wall, opp_wall  in random.sample(dirs, len(dirs)):
            nx, ny = x + dx, y + dy
            if check_boundry(nx, ny) and not visited[nx][ny]:
                remove_wall_between((x,y), (nx, ny), maze)
                backtrack(nx, ny, color)
    backtrack(0, 0, color)
    return maze

colors ={
    "BG_BLACK"   : "\033[40m",
    "BG_RED"     : "\033[41m",
    "BG_GREEN"   : "\033[42m",
    "BG_YELLOW"  : "\033[43m",
    "BG_BLUE"    : "\033[44m",
    "BG_MAGENTA" : "\033[45m",
    "BG_CYAN"    : "\033[46m",
    'BG_WHITE'   : "\033[47m"
}
import time
maze = intitial_map(15, 15)
maze = maze_build(maze, colors["BG_GREEN"])
print_maze(maze, colors["BG_GREEN"])


