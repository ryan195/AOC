import copy

action = False
lst = []
currPos = (-1,-1)

def check(char):
    if char == "<":
        for i in range(currPos[1], 0, -1):
            if lst[currPos[0]][i] == ".":
                return True
            elif lst[currPos[0]][i] == "#":
                return False
    elif char == ">":
        for i in range(currPos[1], len(lst[0])):
            if lst[currPos[0]][i] == ".":
                return True
            elif lst[currPos[0]][i] == "#":
                return False
    elif char == "^":
        posList = [currPos[1]]
        currRow = currPos[0]-1
        while posList:
            newList = []
            for pos in posList:
                if lst[currRow][pos] == "#":
                    return False
                elif lst[currRow][pos] != ".":
                    newList.append(pos)
                    if lst[currRow][pos] == "[":
                        newList.append(pos+1)
                    if lst[currRow][pos] == "]":
                        newList.append(pos-1)
            currRow -= 1
            posList = newList
        return True
    elif char == "v":
        posList = [currPos[1]]
        currRow = currPos[0]+1
        while posList:
            newList = []
            for pos in posList:
                if lst[currRow][pos] == "#":
                    return False
                elif lst[currRow][pos] != ".":
                    newList.append(pos)
                    if lst[currRow][pos] == "[":
                        newList.append(pos+1)
                    if lst[currRow][pos] == "]":
                        newList.append(pos-1)
            currRow += 1
            posList = newList
        return True

def change(char):
    global lst
    updatelist = copy.deepcopy(lst)
    global currPos
    if char == "<":
        prev = "@"
        lst[currPos[0]][currPos[1]] = "."
        currCol = currPos[1] - 1
        currPos = (currPos[0], currCol)
        while prev != ".":
            prev, lst[currPos[0]][currCol] = lst[currPos[0]][currCol], prev
            currCol -= 1
        
    elif char == ">":
        prev = "@"
        lst[currPos[0]][currPos[1]] = "."
        currCol = currPos[1] + 1
        currPos = (currPos[0], currCol)
        while prev != ".":
            prev, lst[currPos[0]][currCol] = lst[currPos[0]][currCol], prev
            currCol += 1

    elif char == "^":
        posList = [currPos[1]]
        currRow = currPos[0]-1
        updatelist[currPos[0]][currPos[1]] = "."
        currPos = (currPos[0]-1, currPos[1])
        while posList:
            newList = []
            for pos in posList:
                updatelist[currRow][pos] = lst[currRow+1][pos]
                if lst[currRow][pos] != ".":
                    newList.append(pos)
                    if lst[currRow][pos] == "[":
                        if (pos+1) not in newList:
                            newList.append(pos+1)
                            updatelist[currRow][pos+1] = "."
                    if lst[currRow][pos] == "]":
                        if (pos-1) not in newList:
                            newList.append(pos-1)
                            updatelist[currRow][pos-1] = "."
            currRow -= 1
            posList = newList
        lst = updatelist
    elif char == "v":
        posList = [currPos[1]]
        currRow = currPos[0]+1
        updatelist[currPos[0]][currPos[1]] = "."
        currPos = (currPos[0]+1, currPos[1])
        while posList:
            newList = []
            for pos in posList:
                updatelist[currRow][pos] = lst[currRow-1][pos]
                if lst[currRow][pos] != ".":
                    newList.append(pos)
                    if lst[currRow][pos] == "[":
                        if (pos+1) not in newList:
                            newList.append(pos+1)
                            updatelist[currRow][pos+1] = "."
                    if lst[currRow][pos] == "]":
                        if (pos-1) not in newList:
                            newList.append(pos-1)
                            updatelist[currRow][pos-1] = "."
            currRow += 1
            posList = newList
        lst = updatelist
    
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
                if char == "#":
                    lst[-1].append("#")
                    lst[-1].append("#")
                elif char == "O":
                    lst[-1].append("[")
                    lst[-1].append("]")
                elif char == ".":
                    lst[-1].append(".")
                    lst[-1].append(".")
                elif char == "@":
                    lst[-1].append("@")
                    lst[-1].append(".")
                    currPos = (len(lst)-1, len(lst[-1])-2)
        else:
            for char in line:
                if check(char):
                    change(char)
            

tot = 0
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] == "[":
            tot += (100*i + j)
print(tot)
