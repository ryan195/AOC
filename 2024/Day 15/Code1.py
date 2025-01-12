action = False
lst = []
currPos = (-1,-1)

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        if line == "\n":
            action = True
            continue
        if not action:
            lst.append([])
            for char in line:
                lst[-1].append(char)
                if char == "@":
                    currPos = (len(lst[-1])-1, len(lst)-1)
        else:
            # Move
            for char in line:
                if char == "^":
                    can = False
                    for i in range(currPos[0], 0, -1):
                        if lst[i][currPos[1]] == ".":
                            can = True
                            break
                        elif lst[i][currPos[1]] == "#":
                            break
                    if can:
                        lst[currPos[0]][currPos[1]] = "."
                        prev = "@"
                        for i in range(currPos[0] - 1, 0, -1):
                            lst[i][currPos[1]], prev = prev, lst[i][currPos[1]]
                            if prev == ".":
                                break
                        currPos = (currPos[0]-1, currPos[1])
                elif char == ">":
                    can = False
                    for i in range(currPos[1], len(lst)):
                        if lst[currPos[0]][i] == ".":
                            can = True
                            break
                        elif lst[currPos[0]][i] == "#":
                            break
                    if can:
                        lst[currPos[0]][currPos[1]] = "."
                        prev = "@"
                        for i in range(currPos[1] + 1, len(lst)):
                            lst[currPos[0]][i], prev = prev, lst[currPos[0]][i]
                            if prev == ".":
                                break
                        currPos = (currPos[0], currPos[1]+1)
                elif char == "v":
                    can = False
                    for i in range(currPos[0], len(lst[0])):
                        if lst[i][currPos[1]] == ".":
                            can = True
                            break
                        elif lst[i][currPos[1]] == "#":
                            break
                    if can:
                        lst[currPos[0]][currPos[1]] = "."
                        prev = "@"
                        for i in range(currPos[0] + 1, len(lst[0])):
                            lst[i][currPos[1]], prev = prev, lst[i][currPos[1]]
                            if prev == ".":
                                break
                        currPos = (currPos[0]+1, currPos[1])
                elif char == "<":
                    can = False
                    for i in range(currPos[1], 0, -1):
                        if lst[currPos[0]][i] == ".":
                            can = True
                            break
                        elif lst[currPos[0]][i] == "#":
                            break
                    if can:
                        lst[currPos[0]][currPos[1]] = "."
                        prev = "@"
                        for i in range(currPos[1] - 1, 0, -1):
                            lst[currPos[0]][i], prev = prev, lst[currPos[0]][i]
                            if prev == ".":
                                break
                        currPos = (currPos[0], currPos[1]-1)
for x in lst:
    print("".join(x))
tot = 0
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] == "O":
            tot += (100*i + j)
print(tot)
