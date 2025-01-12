con = True
tot = 0
adjList = {}
adjList2 = {}

def wron(lst):
    d = {}
    for x in lst:
        if x in adjList:
            for j in adjList[x]:
                if j in d:
                    return True
        d[x] = 1
    return False
    

def fix(lst):
    newlst = []
    return newlst


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
            if b not in adjList2:
                adjList2[b] = []
            adjList[a].append(b)
            adjList2[b].append(a)
        else:
            wrong = False
            #See if order works
            currlst = list(map(int, line.split(",")))
            d = {}
            wrong = wron(currlst)
            if wrong:
                # Need to sort
                newlst = []
                while currlst:
                    #stuff
                    for val in currlst:
                        can = True
                        for val2 in currlst:
                            for val3 in adjList2[val]:
                                if val2 == val3:
                                    can = False
                        if can:
                            newlst.append(val)
                            currlst.remove(val)
                            break
                    
                tot += newlst[len(newlst)//2]
print(tot)
