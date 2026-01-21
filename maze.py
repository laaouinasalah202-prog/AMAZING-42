import random
import os

def print_maze(maze):
    line = "+"
    for x in range(15):
        line += "---+"
    print(line)

    for y in range(15):
        line1 = "|"
        line2 = "+"
        for x in range(15):
            cell = maze[x][y]["Walls"]
            if sum(cell) == 4: 
                line1 += "\033[41m   \033[0m"
            else:
                line1 += "   "
            line1 += "|" if cell[1] else " "
            line2 += "---+" if cell[2] else "   +"
        print(line1)
        print(line2)


def show_maze(maze):
    

def intitial_map(width: int, high: int):
    maze = []
    for r in range(high):
        row = []
        for col in range(width):
            row.append({
                "visited": False,
                "Walls": [1, 1, 1, 1]
            }
        )
        maze.append(row)
    return maze


def maze_build(maze):

    visited = [[False for i in maze[0]] for a in maze]

    dirs = [
    (0, -1, 0, 2),  # up
    (1, 0, 1, 3),   # right
    (0, 1, 2, 0),   # down
    (-1, 0, 3, 1)   # left
    ]

    def check_boundry(x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0])

    def backtrack(x, y):
        print_maze(maze)
        # time.sleep(0.05)
        os.system("clear")
        # random.shuffle(dirs)

        visited[x][y] = True

        for dx, dy, wall, opp_wall  in random.sample(dirs, len(dirs)):
            nx, ny = x + dx, y + dy
            if check_boundry(nx, ny) and not visited[nx][ny]:
                maze[x][y]["Walls"][wall] = 0
                maze[nx][ny]["Walls"][opp_wall] = 0
                backtrack(nx, ny)
    backtrack(0, 0)
    return maze


import time
maze = intitial_map(15, 15)
maze = maze_build(maze) 
print_maze(maze)

for row in maze:
    for col in row:
        col = [str(c) for c in col["Walls"]]
        a = ''.join(col)
        print(f"{hex(int(a, 2))[2:]}  ", end='')
    print()
