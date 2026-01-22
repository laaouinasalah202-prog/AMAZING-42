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

def print_maze(maze, colors, wall_color):
    width = len(maze[0])
    hight = len(maze)
    print(wall_color+"╔", end="")
    cx = 0
    while cx<len(maze[0]):
        print(wall_color+"════", end="")
        if cx < len(maze[0]) - 1:
            if maze[0][cx]["walls"] >> 1 & 1 == 1:
                print(wall_color+"╦", end="")
            else:
                print(wall_color+"═", end="")
        cx+=1
    print(wall_color+"╗")
    for y in range(len(maze)):
        x = 0
        print(wall_color+"║", end="")
        while x < width:
            if x < width - 1:
                if maze[y][x]["walls"] == 15:
                     print(colors + " \U0001F606 " + "\033[0m"+wall_color+"║", end = "")
                elif maze[y][x]["walls"] >> 1 & 1 == 1:
                    print(wall_color+"    ║", end = "")
                else:
                    print("     ", end="")
            x+=1
        if maze[y][width-1]["walls"] == 15:
            print(colors +" \U0001F92B " + "\033[0m"+wall_color+"║")
        else:
            print(wall_color+"    ║")

        x = 0
        while x < width - 1:
            if y < hight - 1:
                if x < width - 1:
                    if x == 0:
                        if maze[y][0]["walls"] >> 2 & 1 == 1:
                            print(wall_color+"╠", end="")
                        else:
                            print(wall_color+"║", end="")
                    if maze[y][x]["walls"] >> 2 & 1 == 1:
                        print(wall_color+"════", end="")
                        if all((
                            maze[y][x + 1]["walls"] >> 2 & 1,
                            maze[y + 1][x]["walls"] >> 1 & 1,
                            maze[y][x]["walls"] >> 1 & 1,
                        )):
                            print(wall_color+"╬", end="")
                    else:
                        print("    ", end="")
                    # print(" ", end="")
                    if maze[y][x]["walls"] >> 2 & 1 == 1 and maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze[y][x]["walls"] >> 1 & 1 == 1 and maze[y + 1][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"╩", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and  maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"═", end="")
                        if  maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"╦", end="")
                    if maze[y][x + 1]["walls"] >> 2 & 1 == 0:
                        if all((maze[y][x]["walls"] >> 2 & 1 == 0,
                                maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                                maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(" ", end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 0,)):
                            print(wall_color+"╗",end="")
                        if all((maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(wall_color+"╣", end="")
                        if all(( maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,)):
                            print(wall_color+"║", end="")
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
                            print(wall_color+"╝", end="")
                    if  maze[y][x]["walls"] >> 2 & 1 == 0 and  maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(wall_color+"╔",end="")             
                        if  maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 1:
                            print(wall_color+"╚",end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(" ", end="")
                        if  maze[y + 1][x]["walls"] >> 1 & 1 == 1 and  maze[y][x]["walls"] >> 1 & 1 == 1:
                            print(wall_color+"╠", end="")     
            x+=1
        if y < hight - 1 :
            if maze[y][x]["walls"] >> 2 & 1 == 1:
                print(wall_color+"════╣")
            else:
                print(wall_color+"    ║")

    print(wall_color+"╚", end="")
    cx = 0
    while cx < len(maze[hight-1]):
        print(wall_color+"════", end="")
        if cx < len(maze[hight-1]) - 1:
            if maze[hight-1][cx]["walls"] >> 1 & 1 == 1:
                print(wall_color+"╩", end="")
            else:
                print(wall_color+"═", end="")
        cx+=1
    print(wall_color+"╝"+'\033[0m')
    

def maze_build(maze, color, wall_color):

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

    def backtrack(x, y, color, wall_color):
        print_maze(maze, color, wall_color)
        time.sleep(0.07)
        os.system("clear")

        visited[x][y] = True

        for dx, dy, wall, opp_wall  in random.sample(dirs, len(dirs)):
            nx, ny = x + dx, y + dy
            if check_boundry(nx, ny) and not visited[nx][ny]:
                remove_wall_between((x,y), (nx, ny), maze)
                backtrack(nx, ny, color, wall_color)
    backtrack(0, 0, color, wall_color)
    return maze

colors ={
    "back"   : "\033[40m",
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
wall_color = wall_colors["red"]
color = colors["green"]
import time
widht = 20
hight = 20

maze = intitial_map(widht, hight)
maze_build(maze, color, wall_color)
print_maze(maze, colors["green"], wall_color)

def maze_tohex(maze):
    f = open("output_maze.txt", 'w')

    for i in maze:
        for j in i:
            f.write(str(hex(j["walls"]))[2:])
        f.write("\n")

maze_tohex(maze)
def maze_menu(widht, hight):
    print("== A-MAZE-ING ==")
    print("1. Re-generate a new maze")
    print("2. show/Hide path from entry to exit")
    print("3. Rotate maze colors")
    print("4. Quit")
    print("Choice? (1-4):")
    choice = input()
    if choice == "1":
        maze = intitial_map(widht, hight)
        maze = maze_build(maze, colors["green"], wall_color)
        print_maze(maze, colors["green"], wall_color)
    elif choice == "2":
        print("show path from entry to exit")
    elif choice == "3":
        print("Enter cell color: from : back red green yellow lue magenta cyan white")
        color =input()
        print("Enter wall color: from : yellow blue pink red green")
        wall_color = input()
        for i in colors:
            if i == color:
                c = colors[i]
        for j in wall_colors:
            if j == wall_color:
                maze = intitial_map(widht, hight)
                maze = maze_build(maze, c, wall_colors[j])
                print_maze(maze, c, wall_colors[j])
    elif choice == "4":
        exit()

maze_menu(widht, hight)
