import random
import time

maze = [[{"visited": False,"path": False ,"walls": 15} for _ in range(15)] for _ in range(10)]

def print_maze(maze, colors):
    width = len(maze[0])
    hight = len(maze)

    print("╔", end="")
    cx = 0
    while cx < len(maze[0]):
        print("════", end="")
        if cx < len(maze[0]) - 1:
            if maze[0][cx]["walls"] >> 1 & 1 == 1:
                print("╦", end="")
            else:
                print("═", end="")
        cx += 1
    print("╗")

    for y in range(len(maze)):
        x = 0
        print("║", end="")
        while x < width:
            if x < width - 1:
                if maze[y][x]["walls"] == 15:
                    print(colors + " \U0001F606 " + "\033[0m" + "║", end="")
                elif maze[y][x]["walls"] >> 1 & 1 == 1:
                    if maze[y][x].get("path", False):
                        print("  • ║", end="")
                    else:
                        print("    ║", end="")
                else:
                    if maze[y][x].get("path", False):
                        print("  •  ", end="")
                    else:
                        print("     ", end="")
            x += 1

        if maze[y][width - 1]["walls"] == 15:
            print(colors + " \U0001F92B " + "\033[0m" + "║")
        else:
            if maze[y][width - 1].get("path", False):
                print("  • ║")
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

                    if maze[y][x]["walls"] >> 2 & 1 == 1 and maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze[y][x]["walls"] >> 1 & 1 == 1 and maze[y + 1][x]["walls"] >> 1 & 1 == 0:
                            print("╩", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print("═", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print("╦", end="")

                    if maze[y][x + 1]["walls"] >> 2 & 1 == 0:
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                        )):
                            print(" ", end="")
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 0,
                        )):
                            print("╗", end="")
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                        )):
                            print("╣", end="")
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                        )):
                            print("║", end="")
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 0,
                        )):
                            print(" ", end="")
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 0,
                        )):
                            print(" ", end="")
                        if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                        )):
                            print("╝", end="")

                    if maze[y][x]["walls"] >> 2 & 1 == 0 and maze[y][x + 1]["walls"] >> 2 & 1 == 1:
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print("╔", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 1:
                            print("╚", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 0 and maze[y][x]["walls"] >> 1 & 1 == 0:
                            print(" ", end="")
                        if maze[y + 1][x]["walls"] >> 1 & 1 == 1 and maze[y][x]["walls"] >> 1 & 1 == 1:
                            print("╠", end="")
            x += 1

        if y < hight - 1:
            if maze[y][x]["walls"] >> 2 & 1 == 1:
                print("════╣")
            else:
                print("    ║")

    print("╚", end="")
    cx = 0
    while cx < len(maze[hight - 1]):
        print("════", end="")
        if cx < len(maze[hight - 1]) - 1:
            if maze[hight - 1][cx]["walls"] >> 1 & 1 == 1:
                print("╩", end="")
            else:
                print("═", end="")
        cx += 1
    print("╝")


def get_neighbors(maze, coordinates):
    neighbors = []
    r, c = coordinates

    #upper neighbor
    if r > 0:
        neighbors.append((r-1,c))

    #down neighbor
    if r < len(maze) - 1:
        neighbors.append((r + 1,c))

    #left neighbor
    if c > 0:
        neighbors.append((r,c - 1))

    #right neighbor
    if c < len(maze[0]) - 1:
        neighbors.append((r,c + 1))

    return neighbors

def remove_wall_between(cell1, cell2, maze):
    r1 , c1 = cell1
    r2 , c2 = cell2

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

def prims_algo(maze):
    current = (0,0)
    visited = {current}
    frontiers = []
    frontiers.extend(get_neighbors(maze, current))

    while frontiers:
        current = random.choice(frontiers)
        visited.add(current)
        frontiers.remove(current)

        visited_neighbors = []
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited and neighbor not in frontiers:
                frontiers.append(neighbor)
            if neighbor in visited and neighbor not in frontiers:
                visited_neighbors.append(neighbor)

        if visited_neighbors:
            neighbor = random.choice(visited_neighbors)
            remove_wall_between(current, neighbor, maze)
    
        print_maze(maze, "\033[42m")
        if frontiers:
           print("\33c" , end="")
        time.sleep(0.05)
    
    return maze

if __name__ == "__main__":
    prims_algo(maze)
