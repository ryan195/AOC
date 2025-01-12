lst = []
visited = []
start = (-1,-1)
end = (-1, -1)
target = 100
direc = [(-1,0),(1,0),(0,-1),(0,1)]
tot = 0

def check(curr):
    if (0 <= curr[0] < len(lst)) and (0 <= curr[1] < len(lst[0])) and (lst[curr[0]][curr[1]] != "#"):
        return True
    return False

def orig_bfs(start):
    ans = -1
    queue = [(start[0], start[1], 0)]
    visited[start[0]][start[1]] = 1
    while queue:
        curr = queue[0]
        lst[curr[0]][curr[1]] = curr[2]
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


    
def new_dfs(start):
    global tot
    new_lst = [start]
    while new_lst:
        curr = new_lst[0]
        new_lst.pop(0)
        if curr == end:
            return
        for i in range(21):
            for j in range(21):
                if (1 < (i+j) <= 20):
                    if i == 0:
                        for x in [(i,j),(i,-j)]:
                            if (check((curr[0]+x[0],curr[1]+x[1]))) and (lst[curr[0]+x[0]][curr[1]+x[1]] != "#") and (lst[curr[0]][curr[1]] +target+i+j <= lst[curr[0]+x[0]][curr[1]+x[1]]):
                                tot += 1
                    elif j == 0:
                        for x in [(i,j),(-i,j)]:
                            if (check((curr[0]+x[0],curr[1]+x[1]))) and (lst[curr[0]+x[0]][curr[1]+x[1]] != "#") and (lst[curr[0]][curr[1]] +target+i+j <= lst[curr[0]+x[0]][curr[1]+x[1]]):
                                tot += 1
                    else:
                        for x in [(i,j),(-i,j),(i,-j),(-i,-j)]:
                            if (check((curr[0]+x[0],curr[1]+x[1]))) and (lst[curr[0]+x[0]][curr[1]+x[1]] != "#") and (lst[curr[0]][curr[1]] +target+i+j <= lst[curr[0]+x[0]][curr[1]+x[1]]):
                                tot += 1
        for coord in direc:
            if (lst[curr[0]+coord[0]][curr[1]+coord[1]] != "#") and (lst[curr[0]][curr[1]] + 1 == lst[curr[0]+coord[0]][curr[1]+coord[1]]):
                new_lst.append((curr[0]+coord[0],curr[1]+coord[1]))
    return



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
orig_bfs(start)  
new_dfs(start)
print(tot)

