# ═  ║  ╔  ╗  ╚  ╝
# ╠  ╣  ╦  ╩  ╬
 
# ║

# ╩
# ╦ 

# ╬

# ╠

# ╣ 
# ╔═══╦═══╦════╦════╦════╦═════════════╗ 
# ║   ║ 


# ╚═════════════════════════════════════╝
hight = 20
width = 20
maze = []

for i in range(hight):
    row = []
    for j in range(width):
        row.append({
        "visited" : False,
        "walls": 15 })
    maze.append(row)

swd
    print("╔", end="")
    cx = 0
    while cx<len(maze[0]):
        print("════", end="")
        if cx < len(maze[0]) - 1:
            if maze[0][cx]["walls"] >> 1 & 1 == 1:
                print("╦", end="")
            else:
                print("═", end="")
        cx+=1
    print("╗")


    def in_boundary(maze, x, y):
        if 0 <= x < len(maze[0]) and 0 <= y < len(maze):
            return 1
        else:
            return 0

    for y in range(len(maze)):
        x = 0
        print("║", end="")
        while x < width:
            if x < width - 1:
                if maze[y][x]["walls"] >> 1 & 1 == 1:
                    print("    ║", end = "")
                else:
                    print("     ", end="")
            x+=1
        print("    ║")

        x = 0
        while x < width - 1:
            if y < hight - 1:
                if x < width - 1:
                    if x == 0:
                        if maze[y][0]["walls"] >> 2 & 1 == 1: ## print the first corner
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
                    if all((
                            maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                    )):
                    print("╠",end="")
                    if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y][x + 1]["walls"] >> 2 & 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                    )):
                        print("╩", end="")
                    if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                    )):
                        print("╣", end="")
                    if all((
                            maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 1,
                            maze[y][x]["walls"] >> 1 & 1 == 1,
                    )):
                        print("║", end="")
                    if all((
                            maze[y][x]["walls"] >> 2 & 1 == 1,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 1,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 0,
                    )):
                        print("═", end="")
                    if all((
                            maze[y][x]["walls"] >> 2 & 1 == 0,
                            maze[y][x + 1]["walls"] >> 2 & 1 == 0,
                            maze[y + 1][x]["walls"] >> 1 & 1 == 0,
                            maze[y][x]["walls"] >> 1 & 1 == 0,
                    )):
                        print(" ", end="")
            x+=1

        if y < hight - 1 :  # must not be the last because the last is alwayws closed
            if maze[y][x]["walls"] >> 2 & 1 == 1:
                print("════╣") # the last corner with the last botttm cell 
            else:
                print("    ║")
            
        

    print("╚", end="")
    cx = 0
    while cx < len(maze[hight-1]):
        print("════", end="")
        if cx < len(maze[hight-1]) - 1:
            if maze[0][cx]["walls"] >> 1 & 1 == 1:
                print("╩", end="")
            else:
                print("═", end="")
        cx+=1
    print("╝")