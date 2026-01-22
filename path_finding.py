import prims
import time

maze = [[{"visited": False, "path": False, "walls": 15} for _ in range(10)] for _ in range(10)]

def get_neighbors(maze, coordinates):
    neighbors = []
    r, c = coordinates
    #upper neighbor
    if ((maze[r][c]["walls"] >> 0) & 1) == 0 and r > 0:
        neighbors.append((r-1,c))

    #down neighbor
    if ((maze[r][c]["walls"] >> 2) & 1) == 0 and r < len(maze) - 1:
        neighbors.append((r + 1,c))
    
    #left neighbor
    if ((maze[r][c]["walls"] >> 3) & 1) == 0 and c > 0:
        neighbors.append((r,c - 1))
    
    #right neighbor
    if ((maze[r][c]["walls"] >> 1) & 1) == 0 and c < len(maze[0]) - 1:
        neighbors.append((r,c + 1))
        
    return neighbors
    
def shortest_path(maze, start, end):
    x,y = start
    cells = [(x, y)]
    visited = {start}
    parent = {}
    path = []

    while cells:
        current = cells.pop(0)
        if current == end:
            break
        neighbors = get_neighbors(maze, current)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parent.update({neighbor: current})
                cells.append(neighbor)

    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    path.reverse()

    for x, y in path:
        maze[x][y]["path"] = True
        prims.print_maze(maze, "\033[42m")
        print("\33c" , end="")
        time.sleep(0.5)
    return path

maze = prims.prims_algo(maze)
prims.print_maze(maze, "\033[42m")
path = shortest_path(maze, (0,0), (9,9))
prims.print_maze(maze, "\033[42m")
