import random
import time
import os
from maze import MazeGenerator


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

def get_neighbors(maze, coordinates):
    neighbors = []
    r, c = coordinates

    #upper neighbor
    if r > 0 and maze[r - 1][c]["protected"] == False:
        neighbors.append((r-1,c))

    #down neighbor
    if r < len(maze) - 1 and maze[r + 1][c]["protected"] == False:
        neighbors.append((r + 1,c))

    #left neighbor
    if c > 0 and maze[r][c - 1]["protected"] == False:
        neighbors.append((r,c - 1) )

    #right neighbor
    if c < len(maze[0]) - 1 and maze[r][c + 1]["protected"] == False:
        neighbors.append((r,c + 1))

    return neighbors

def remove_wall_between(cell1, cell2, maze):
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


class maze_algo(MazeGenerator):
    def __init__(self,width, height, entry, ex, algo_name):
        super().__init__(width, height, entry, ex)
        self.algo_name = algo_name

    def backtrack_algo(self, color, wall_color, display=False):
        dirs = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
        ]
        coordinate = maze.set_42()
        def check_boundry(x, y):
            return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0])
        
        visited = [[False for i in self.maze[0]] for a in self.maze]
        for a in coordinate:
            for x,y in a:
                visited[x][y] = True

        def remove_wall_between(cell1, cell2, maze):
            r1 , c1 = cell1
            r2 , c2 = cell2

            r = 2
            l = 8
            up = 1
            dn = 4
            if r1 == r2:
                if c1 < c2:
                    self.maze[r1][c1]["walls"] -= r
                    self.maze[r2][c2]["walls"] -= l
                elif c1 > c2:
                    self.maze[r1][c1]["walls"] -= l
                    self.maze[r2][c2]["walls"] -= r

            elif c1 == c2:
                if r1 < r2:
                    self.maze[r1][c1]["walls"] -= dn
                    self.maze[r2][c2]["walls"] -= up
                elif r1 > r2:
                    self.maze[r1][c1]["walls"] -= up
                    self.maze[r2][c2]["walls"] -= dn

        def backtrack(x, y, color, wall_color, display):
            if display:
                print_maze(self, color, wall_color)
                time.sleep(0.04)
                os.system("clear")
            visited[x][y] = True

            for dx, dy  in random.sample(dirs, len(dirs)):
                nx, ny = x + dx, y + dy
                if check_boundry(nx, ny) and not visited[nx][ny]:
                    remove_wall_between((x,y), (nx, ny), maze)
                    backtrack(nx, ny, color, wall_color, display)
        backtrack(0, 0, color, wall_color, display)

    def prims_algo(self, display):
        current = (0,0)
        visited = {current}
        frontiers = []
        frontiers.extend(get_neighbors(self.maze, current))

        self.set_42()

        while frontiers:
            current = random.choice(frontiers)
            visited.add(current)
            frontiers.remove(current)

            visited_neighbors = []
            for neighbor in get_neighbors(self.maze, current):
                if neighbor not in visited and neighbor not in frontiers:
                    frontiers.append(neighbor)
                if neighbor in visited and neighbor not in frontiers:
                    visited_neighbors.append(neighbor)

            if visited_neighbors:
                neighbor = random.choice(visited_neighbors)
                remove_wall_between(current, neighbor, maze.maze)
        return maze


maze = MazeGenerator(13,13, (0,0), (4,4))

algo = maze_algo(13,13, (0,0), (4,4),"backtrack")

if algo.algo_name == "backtrack":
    algo.backtrack_algo("\033[41m", "\033[92m",True)
elif algo.algo_name == "prims":
    algo.prims_algo(True)