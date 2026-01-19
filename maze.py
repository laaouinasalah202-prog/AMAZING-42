def intitial_map(width: int, high: int):
    cell = {
        "visited": False,
        "north": 1,
        "west": 1,
        "east": 1,
        "south": 1
    }

    maze = []
    for r in range(high):
        row = []
        for col in range(width):
            row.append(cell)
        maze.append(row)
    return maze


def maze_build(maze, coord):
    
    visited = [[False for i in maze[0]] for a in maze]

    def check_maze(maze):
        for i in maze:
            for j in i:
                if j["visited"] == False:
                    return 0
        return 1

    dirs = [
    (0, -1, 0, 2),  # up
    (1, 0, 1, 3),   # right
    (0, 1, 2, 0),   # down
    (-1, 0, 3, 1)   # left
]
    def backtrack(self, x, y):
        if check_maze(maze):
            return
        pos = maze[x][y]
        choice = []
    


# print(check_maze(intitial_map(3, 2)))

def creat_maze(maze):

    maze = intitial_map(20, 20)
    m = maze[0]
    high = 20
    width = 20
    print("+" + "---+" * (width + 2))
    for h in range(high):
        top_line = "+"
        bottom_line = "+"
        middle_line = ""
        for w in range(width):
            if maze[h][w]["north"]:
                top_line += "---+"

            if maze[h][w]["west"]:
                middle_line += "|   "

            if maze[h][w]["south"]:
                bottom_line += "---+"
        middle_line += "|   #"
        print("    " + top_line)
        print("#   " + middle_line)
    print("    " + bottom_line )
    print("+" + "---+" * (width + 2))

