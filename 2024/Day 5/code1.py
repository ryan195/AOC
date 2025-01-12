con = True
tot = 0
adjList = {}


# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        if line == "\n":
            con = False
            continue
        if con:
            #Build toposort
            a, b = map(int, line.split("|"))
            if a not in adjList:
                adjList[a] = []
            adjList[a].append(b)
        else:
            wrong = False
            #See if order works
            currlst = list(map(int, line.split(",")))
            d = {}
            for x in currlst:
                if x in adjList:
                    for j in adjList[x]:
                        if j in d:
                            wrong = True
                            break
                if wrong:
                    break
                d[x] = 1
            if not wrong:
                tot += currlst[len(currlst)//2]
print(tot)
