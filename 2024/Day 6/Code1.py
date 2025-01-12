lst = []
stan = ["#","."]
tot = 0

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append([])
        for i in range(len(line[:-1])):
            lst[-1].append(line[i])
            if line[i] not in stan:
                guardpos = (len(lst) - 1, i)

def nextdir(curr, dire):
    while True:
        if dire == 0:
            if (curr[0] - 1) >= 0:
                if lst[curr[0]-1][curr[1]] == "#":
                    dire = 1
                else:
                    return (curr[0]-1, curr[1], dire)
            else:
                return (-1,-1)
        elif dire == 1:
            if (curr[1] + 1) < len(lst[0]):
                if lst[curr[0]][curr[1] + 1] == "#":
                    dire = 2
                else:
                    return (curr[0], curr[1]+1, dire)
            else:
                return (-1,-1)
        elif dire == 2:
            if (curr[0] + 1) < len(lst):
                if lst[curr[0]+1][curr[1]] == "#":
                    dire = 3
                else:
                    return (curr[0]+1, curr[1], dire)
            else:
                return (-1, -1)
        elif dire == 3:
            if (curr[1] - 1) >= 0:
                if lst[curr[0]][curr[1]-1] == "#":
                    dire = 0
                else:
                    return (curr[0], curr[1]-1, dire)
            else:
                return (-1,-1)
                

guarddir = 0
currguard = guardpos
while (0 <= currguard[0] < len(lst)) and (0 <= currguard[1] < len(lst[0])):
    if lst[currguard[0]][currguard[1]] != "X":
        tot += 1
    lst[currguard[0]][currguard[1]] = "X"
    if currguard[0] + currguard[1] == -2:
        break
    x = nextdir(currguard, guarddir)
    if len(x) == 2:
        break
    currguard = x[0:2]
    guarddir = x[2]
            
print(tot)
        
