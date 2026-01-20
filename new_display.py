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


for y in range(len(maze)):
    x = 0
    print("║", end="")
    while x < width:
        if x < width - 1:
            if maze[y][x]["walls"] >> 1 & 1 == 1:
                print("    ║", end = "")
        x+=1
    print("    ║")
    x = 0
    while x < width:
        if y < hight - 1:
            if x < width - 1:
                if maze[y][x]["walls"] >> 1 & 1 == 1:
                    print(" ════", end="")
        x+=1
    if y < hight - 1:
        print(" ════")




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