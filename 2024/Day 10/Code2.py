lst = []
starts = []
dirc = [(-1,0),(0,-1),(0,1),(1,0)]

def dfs(curr, coord):
    if (curr == 9):
        return 1
    else:
        v = 0
        for co in dirc:
            if (0 <= (coord[0] + co[0]) < len(lst)) and (0 <= (coord[1] + co[1]) < len(lst[0])):
                if lst[coord[0] + co[0]][coord[1] + co[1]] == (curr + 1):
                    v += dfs(curr + 1, (coord[0] + co[0],coord[1] + co[1]))
        return v

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append([])
        c = 0
        for char in line:
            if char != "\n":
                lst[-1].append(int(char))
                if int(char) == 0:
                    starts.append((len(lst) - 1, c))
            c += 1

ans = 0
for coords in starts:
    curr = 0
    ans += dfs(curr, coords)


print(ans)
    
        
