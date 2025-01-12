import heapq

direc = ((0,1),(1,0),(0,-1),(-1,0))
lst = []
start = (-1,-1,(0,1))
d = {}
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append([])
        for char in line:
            lst[-1].append(char)
            if char == "S":
                start = (len(lst)-1,len(lst[-1])-1,(0,1))

d[start] = 1
q = [(0, start)]
heapq.heapify(q)

while True:
    curr = heapq.heappop(q)
    currP, currord = curr[0], curr[1]
    if lst[currord[0]+currord[2][0]][currord[1]+currord[2][1]] == "E":
        print(currP + 1)
        break
    if lst[currord[0]+currord[2][0]][currord[1]+currord[2][1]] != "#":
        if (currord[0]+currord[2][0],currord[1]+currord[2][1],currord[2]) not in d:
            d[(currord[0]+currord[2][0],currord[1]+currord[2][1],currord[2])] = 1
            heapq.heappush(q,(currP+1,(currord[0]+currord[2][0],currord[1]+currord[2][1],currord[2])))
    for x in direc:
        if currord[2][0] == 0:
            if x[0] != 0:
                if (currord[0],currord[1],x) not in d:
                    d[(currord[0],currord[1],x)] = 1
                    heapq.heappush(q, (currP+1000,(currord[0],currord[1],x)))
        else:
            if x[1] != 0:
                if (currord[0],currord[1],x) not in d:
                    d[(currord[0],currord[1],x)] = 1
                    heapq.heappush(q, (currP+1000,(currord[0],currord[1],x)))
