import random
import time
from display_maze import print_maze

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


def backtrack_algo(maze, color, wall_color, display=False):
    dirs = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
    ]
    coordinate = maze.set_42(maze.maze)
    def check_boundry(x, y):
        return 0 <= x < len(maze.maze) and 0 <= y < len(maze.maze[0])
    
    visited = [[False for i in maze.maze[0]] for a in maze.maze]
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
                maze.maze[r1][c1]["walls"] -= r
                maze.maze[r2][c2]["walls"] -= l
            elif c1 > c2:
                maze.maze[r1][c1]["walls"] -= l
                maze.maze[r2][c2]["walls"] -= r

        elif c1 == c2:
            if r1 < r2:
                maze.maze[r1][c1]["walls"] -= dn
                maze.maze[r2][c2]["walls"] -= up
            elif r1 > r2:
                maze.maze[r1][c1]["walls"] -= up
                maze.maze[r2][c2]["walls"] -= dn

    def backtrack(x, y, color, wall_color, display):
        if display:
            print_maze(maze, color, wall_color)
            time.sleep(0.04)
            print("\33c" , end="")
        visited[x][y] = True

        for dx, dy  in random.sample(dirs, len(dirs)):
            nx, ny = x + dx, y + dy
            if check_boundry(nx, ny) and not visited[nx][ny]:
                remove_wall_between((x,y), (nx, ny), maze)
                backtrack(nx, ny, color, wall_color, display)
    backtrack(0, 0, color, wall_color, display)

def prims_algo(maze,color, wall_color, display):
    current = (0,0)
    visited = {current}
    frontiers = []
    frontiers.extend(get_neighbors(maze.maze, current))

    while frontiers:
        current = random.choice(frontiers)
        visited.add(current)
        frontiers.remove(current)

        visited_neighbors = []
        for neighbor in get_neighbors(maze.maze, current):
            if neighbor not in visited and neighbor not in frontiers:
                frontiers.append(neighbor)
            if neighbor in visited and neighbor not in frontiers:
                visited_neighbors.append(neighbor)

        if visited_neighbors:
            neighbor = random.choice(visited_neighbors)
            remove_wall_between(current, neighbor, maze.maze)
        
        print_maze(maze, color, wall_color)
        print("\33c" , end="")
        time.sleep(0.05)
    return maze

def only_open_neighbors(maze, coordinates):
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
    
def shortest_path(maze):
    x,y = maze._entry
    cells = [(x, y)]
    visited = {maze._entry}
    parent = {}
    path = []

    while cells:
        current = cells.pop(0)
        if current == maze._exit_p:
            break
        neighbors = only_open_neighbors(maze.maze, current)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                parent.update({neighbor: current})
                cells.append(neighbor)

    current = maze._exit_p
    while current != maze._entry:
        x,y = current
        path.append(current)
        current = parent[current]
    path.append(maze._entry)
    path.reverse()
    maze.path = path