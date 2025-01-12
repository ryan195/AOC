lst = []
orig_lst = []
stan = ["#","."]
tot = 0

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append([])
        orig_lst.append([])
        for i in range(len(line)):
            if line[i] != "\n":
                lst[-1].append(line[i])
                orig_lst[-1].append(line[i])
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

def loop(pos, dire):
    counter = 0
    while (0 <= pos[0] < len(lst)) and (0 <= pos[1] < len(lst[0])):
        counter += 1
        if counter > (len(lst)*len(lst[0])):
            #for i in lst:
            #    print("".join(i))
            #print("\n")
            return 1
        lst[pos[0]][pos[1]] = "X"
        x = nextdir(pos, dire)
        if len(x) == 2:
            break
        pos = x[0:2]
        dire = x[2]
    return 0

guarddir = 0
for i in range(len(lst)):
    for j in range(len(lst[0])):
        kept = "."
        #print(str(i) + " " + str(j))
        if lst[i][j] != "#":
            kept = lst[i][j]
            lst[i][j] = "#"
            tot += loop(guardpos, guarddir)
            lst[i][j] = kept
        lst = orig_lst

            
print(tot)
        
