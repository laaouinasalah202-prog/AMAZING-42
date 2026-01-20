import random


def intitial_map(width: int, high: int):
    cell = {

    }

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
        visited[x][y] = True
        maze[x][y]["visited"] = True

        random.shuffle(dirs)        
        
        for dx, dy, wall, opp_wall  in dirs:
            nx, ny = x + dx, y + dy
            if check_boundry(nx, ny) and not visited[nx][ny]:
                maze[x][y]["Walls"][wall] = False
                maze[nx][ny]["Walls"][opp_wall] = False
                backtrack(nx, ny)
    backtrack(0, 0)
    return maze

def display_maze(maze):

    m = maze[0]
    high = len(maze)
    width = len(maze[0])
    print("+" + "---+" * (width + 2))
    for h in range(high):
        top_line = "+"
        bottom_line = "+"
        middle_line = ""
        for w in range(width):
            if maze[h][w]["Walls"][0]:
                top_line += "---+"
            else:
                top_line += "   +"
            if maze[h][w]["Walls"][1]:
                middle_line += "|   "
            else:
                middle_line += "    "
            if maze[h][w]["Walls"][2]:
                bottom_line += "---+"
            else:
                bottom_line += "   +"
        middle_line += "|   #"
        print("    " + top_line)
        print("#   " + middle_line)
    print("    " + bottom_line )
    print("+" + "---+" * (width + 2))


maze = intitial_map(10, 10)
# maze = maze_build(maze) 
display_maze(maze)