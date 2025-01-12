lst = []
visited = []
val = 70
for i in range(val+1):
    lst.append([])
    visited.append([])
    for j in range(val+1):
        lst[-1].append(".")
        visited[-1].append(0)

counter = 0

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        counter += 1
        x, y = map(int, line.split(","))
        if counter <= 1024:
            lst[y][x] = "#"

q = [(0,0,0)]
visited[0][0] = 1
direc = [(-1,0),(1,0),(0,-1),(0,1)]
while q:
    curr = q[0]
    if (curr[0] == val) and (curr[1] == val):
        print(curr[2])
        break
    q.pop(0)
    for coord in direc:
        if (0 <= curr[0]+coord[0] <= val) and (0 <= curr[1]+coord[1] <= val) and (visited[curr[0]+coord[0]][curr[1]+coord[1]] == 0):
            if (lst[curr[0]+coord[0]][curr[1]+coord[1]] == "."):
                visited[curr[0]+coord[0]][curr[1]+coord[1]] = 1
                q.append((curr[0]+coord[0], curr[1]+coord[1], curr[2]+1))
