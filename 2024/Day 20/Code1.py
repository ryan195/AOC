
lst = []
visited = []
start = (-1,-1)
end = (-1, -1)
target = 1000000000000
direc = [(-1,0),(1,0),(0,-1),(0,1)]
tot = 0

def orig_bfs(start):
    ans = -1
    queue = [(start[0], start[1], 0)]
    visited[start[0]][start[1]] = 1
    while queue:
        curr = queue[0]
        queue.pop(0)
        if (curr[0] == end[0]) and (curr[1] == end[1]):
            ans = curr[2]
            break
        else:
            for coord in direc:
                if (0 <= curr[0]+coord[0] < len(lst)) and (0 <= curr[1]+coord[1] < len(lst[0])) and (lst[curr[0]+coord[0]][curr[1]+coord[1]] != "#") and (visited[curr[0]+coord[0]][curr[1]+coord[1]] == 0):
                    visited[curr[0]+coord[0]][curr[1]+coord[1]] = 1
                    queue.append((curr[0]+coord[0],curr[1]+coord[1],curr[2]+1))
    return ans




# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append([])
        visited.append([])
        for char in line:
            if char != "\n":
                lst[-1].append(char)
                visited[-1].append(0)
                if char == "S":
                    start = (len(lst)-1, len(lst[-1])-1)
                if char == "E":
                    end = (len(lst)-1, len(lst[-1])-1)
                
target = orig_bfs(start) - 100
for i in range(len(visited)):
    for j in range(len(visited[i])):
        visited[i][j] = 0
for i in range(len(visited)):
    for j in range(len(visited[i])):
        if lst[i][j] == "#":
            lst[i][j] = "."
            x = orig_bfs(start)
            if (x != -1) and (x <= target):
                tot += 1
            lst[i][j] = "#"
            for k in range(len(visited)):
                for l in range(len(visited[i])):
                    visited[k][l] = 0

print(tot)
