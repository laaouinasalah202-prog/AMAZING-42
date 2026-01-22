import random
import time

maze = [[15 for _ in range(10)] for _ in range(10)]

def print_maze1(maze):
    # top border
    maze_width = len(maze[0])
    maze_height = len(maze)
    line = "+"
    for x in range(maze_width):
        line += "---+"
    print(line)

    for y in range(maze_height):
        line1 = "|"
        line2 = "+"
        for x in range(maze_width):
            cell = maze[y][x]
            line1 += "   "
            line1 += "|" if cell & 2 else " "
            line2 += "---+" if cell & 4 else "   +"
        print(line1)
        print(line2)

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
            maze[r1][c1] -= 2
            maze[r2][c2] -= 8
        elif c1 > c2:
            maze[r1][c1] -= 8
            maze[r2][c2] -= 2

    elif c1 == c2:
        if r1 < r2:
            maze[r1][c1] -= 4
            maze[r2][c2] -= 1
        elif r1 > r2:
            maze[r1][c1] -= 1
            maze[r2][c2] -= 4

def prims_algo(maze):
    current = (0,0)
    visited = {current}
    frontiers = []
    frontiers.extend(get_neighbors(maze, current))

    while frontiers:
        current = random.choice(frontiers)
        frontiers.remove(current)
        visited.add(current)

        visited_neighbors = []

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited and neighbor not in frontiers:
                frontiers.append(neighbor)
            if neighbor in visited and neighbor not in frontiers:
                visited_neighbors.append(neighbor)

        if visited_neighbors:
            neighbor = random.choice(visited_neighbors)
            remove_wall_between(current, neighbor, maze)
    
        print_maze1(maze)
        if frontiers:
           print("\33c" , end="")
        time.sleep(0.2)
    
    return maze

prims_algo(maze)

#print_maze1(maze)