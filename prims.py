import random

maze1 = [
    [2, 2, 3], 
    [8, 0, 1],
    [12, 8, 12]
]


def get_neighbors(maze, coordinates):
    neighbors = []
    c, r = coordinates

    #upper neighbor
    if r > 0:
        neighbors.append((r-1,c))

    #down neighbor
    if r < len(maze[0]) - 1:
        neighbors.append((r + 1,c))

    #left neighbor
    if c > 0:
        neighbors.append((r,c - 1))

    #right neighbor
    if c < len(maze) - 1:
        neighbors.append((r,c + 1))

    return neighbors

def break_wall(maze,cell,current):
    c_x , c_y = cell
    r_x , r_y = current

    if c_x < r_x:
        maze[c_y][c_x] -= 2
        maze[r_y][r_x] -= 8
    elif c_x > r_x:
        maze[c_y][r_x] -= 2
        maze[r_y][c_x] -= 8

    if c_y < r_y:
        maze[c_y][c_x] -= 4
        maze[r_y][r_x] -= 1
    elif c_y > r_y:
        maze[c_y][c_x] -= 1
        maze[r_y][r_x] -= 4

def prims_algo(maze):
    current = (0,0)
    visited = []
    frontiers = [current]

    frontiers.extend(get_neighbors(maze, current))
    
    while frontiers:
        current = random.choice(frontiers)
        if current not in visited:
            visited.append(current)
            frontiers.extend(get_neighbors(maze, current))
            frontiers.remove(current)
        else:
            frontiers.remove(current)

    print(visited)
    #current = random.choice(frontiers)
    #print(current)
    #frontiers.append(get_neighbors(maze, current))
    #print(frontiers)

prims_algo(maze1)
