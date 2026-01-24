from maze import MazeGenerator

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
        neighbors = get_neighbors(maze.maze, current)
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
    return path


# maze = MazeGenerator(13,13, (0,0), (12,12))
# prims_algo(maze)
# path = shortest_path(maze, maze.entry, maze.exit)
# display_path(maze, path, True)