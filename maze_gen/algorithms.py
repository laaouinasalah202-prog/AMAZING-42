import random
import time

def get_neighbors(maze, coordinates):
    """
    Return all valid neighboring cells of a given position in the maze.
    A neighbor is considered valid if it lies within the maze boundaries
    and its "protected" flag is set to False.
    """
    neighbors = []
    r, c = coordinates

    # upper neighbor
    if r > 0 and not maze[r - 1][c]["protected"]:
        neighbors.append((r - 1, c))

    # down neighbor
    if r < len(maze) - 1 and not maze[r + 1][c]["protected"]:
        neighbors.append((r + 1, c))

    # left neighbor
    if c > 0 and not maze[r][c - 1]["protected"]:
        neighbors.append((r, c - 1))

    # right neighbor
    if c < len(maze[0]) - 1 and not maze[r][c + 1]["protected"]:
        neighbors.append((r, c + 1))

    return neighbors


def remove_wall_between(cell1, cell2, maze):
    """
    remove the wall according to its position
    """
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


def backtrack_algo(maze, color, wall_color, print_maze):
    """
    Generate a maze using the recursive backtracking (DFS) algorithm.

    Optionally displays the maze generation process step by step.
    """
    dirs = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]
    coordinate = maze.set_42(maze.maze)
    
    if maze.seed != None:
        random.seed(maze.seed)
    def check_boundry(x, y):
        return 0 <= x < len(maze.maze) and 0 <= y < len(maze.maze[0])

    visited = [[False for i in maze.maze[0]] for a in maze.maze]
    for a in coordinate:
        for x, y in a:
            visited[x][y] = True

    def remove_wall_between(cell1, cell2, maze):
        r1, c1 = cell1
        r2, c2 = cell2

        r = 2
        le = 8
        up = 1
        dn = 4
        if r1 == r2:
            if c1 < c2:
                maze.maze[r1][c1]["walls"] -= r
                maze.maze[r2][c2]["walls"] -= le
            elif c1 > c2:
                maze.maze[r1][c1]["walls"] -= le
                maze.maze[r2][c2]["walls"] -= r

        elif c1 == c2:
            if r1 < r2:
                maze.maze[r1][c1]["walls"] -= dn
                maze.maze[r2][c2]["walls"] -= up
            elif r1 > r2:
                maze.maze[r1][c1]["walls"] -= up
                maze.maze[r2][c2]["walls"] -= dn

    def backtrack(x, y, color, wall_color):
        print_maze(maze, color, wall_color)
        time.sleep(0.01)
        visited[x][y] = True

        for dx, dy in random.sample(dirs, len(dirs)):
            nx, ny = x + dx, y + dy
            if check_boundry(nx, ny) and not visited[nx][ny]:
                remove_wall_between((x, y), (nx, ny), maze)
                backtrack(nx, ny, color, wall_color)
    backtrack(0, 0, color, wall_color)


def prims_algo(maze, color, wall_color, print_maze):
    """
    Generate a maze using Prim's algorithm.

    Expands the maze by randomly connecting frontier cells to
    already visited cells, optionally displaying each step.
    """
    current = (0, 0)
    visited = {current}
    frontiers = []
    frontiers.extend(get_neighbors(maze.maze, current))

    if maze.seed != None:
        random.seed(maze.seed)
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
        time.sleep(0.01)
    return maze


def only_open_neighbors(maze, coordinates):
    """
    Return neighboring cells that are reachable (no wall in between).

    Checks the wall bitmask of the current cell to determine open paths.
    """
    neighbors = []
    r, c = coordinates
    # upper neighbor
    if ((maze[r][c]["walls"] >> 0) & 1) == 0 and r > 0:
        neighbors.append((r-1, c))

    # down neighbor
    if ((maze[r][c]["walls"] >> 2) & 1) == 0 and r < len(maze) - 1:
        neighbors.append((r + 1, c))

    # left neighbor
    if ((maze[r][c]["walls"] >> 3) & 1) == 0 and c > 0:
        neighbors.append((r, c - 1))

    # right neighbor
    if ((maze[r][c]["walls"] >> 1) & 1) == 0 and c < len(maze[0]) - 1:
        neighbors.append((r, c + 1))

    return neighbors


def shortest_path(maze):
    """
    Compute the shortest path from entry to exit in the maze using BFS.

    Stores the resulting path in `maze.path`.
    """
    x, y = maze._entry
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
        x, y = current
        path.append(current)
        current = parent[current]
    path.append(maze._entry)
    path.reverse()
    maze.path = path

def count_walls(n):
    i = 0
    c = 0
    while i < 4:
        if (n >> i & 1):
            c += 1
        i += 1
    return c

def only_close_neighbors(maze, coordinates):
    """
    Return neighboring cells that are reachable (no wall in between).

    Checks the wall bitmask of the current cell to determine open paths.
    """
    neighbors = []
    r, c = coordinates
    # upper neighbor
    if ((maze[r][c]["walls"] >> 0) & 1) == 1 and r > 0:
        if maze[r - 1][c]["protected"] == False and count_walls(maze[r - 1][c]["walls"]) > 2:
            neighbors.append((r-1, c))

    # down neighbor
    if ((maze[r][c]["walls"] >> 2) & 1) == 1 and r < len(maze) - 1:
        if maze[r + 1][c]["protected"] == False and count_walls(maze[r + 1][c]["walls"]) > 2:
            neighbors.append((r + 1, c))

    # left neighbor
    if ((maze[r][c]["walls"] >> 3) & 1) == 1 and c > 0:
        if maze[r][c - 1]["protected"] == False and count_walls(maze[r][c - 1]["walls"]) > 2:
            neighbors.append((r, c - 1))

    # right neighbor
    if ((maze[r][c]["walls"] >> 1) & 1) == 1 and c < len(maze[0]) - 1:
        if maze[r][c + 1]["protected"] == False and count_walls(maze[r][c + 1]["walls"]) > 2:
            neighbors.append((r, c + 1))

    return neighbors

def break_cell(maze, cell, coordinates):
    if count_walls(cell["walls"] < 3) or cell["protected"]:
        return

    neighbors = only_close_neighbors(maze.maze, coordinates)
    if neighbors:
        remove_wall_between(coordinates, random.choice(neighbors), maze.maze)

def imperfect_maze(maze):
    r = 0
    for row in maze.maze:
        c = 0
        for cell in row:
            if random.random() > 0.6:
                break_cell(maze, cell, (r, c))
            c += 1
        r += 1