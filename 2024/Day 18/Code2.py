import time
print(time.perf_counter())
def par(x):
  p[x] = par(p[x]) if p[x] != x else x
  return p[x]

def merge(a, b):
  p[par(a)] = par(b)

val = 212

counter = 0

dv = {}
lstEdge = []
direc = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
currsides = []

dumSouthWest = (-1, 0)
dumNorthEast = (0, -1)

# Open the file in read mode ('r') and automatically close it after reading
with open('Day18challengeM.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        counter += 1
        x, y = map(int, line.split(","))
        if x not in dv:
            dv[x] = {}
        dv[x][y] = counter
        if x == 0:
            lstEdge.append((0,dumSouthWest[0],dumSouthWest[1],0,y))
        if x == val:
            lstEdge.append((0,dumNorthEast[0],dumNorthEast[1],val,y))
        if y == 0:
            lstEdge.append((0,dumNorthEast[0],dumNorthEast[1],x, 0))
        if y == val:
            lstEdge.append((0,dumSouthWest[0],dumSouthWest[1],x, val))
        for c in direc:
            if x+c[0] in dv:
                if y+c[1] in dv[x+c[0]]:
                    lstEdge.append((max(dv[x+c[0]][y+c[1]], counter),x,y,x+c[0],y+c[1]))

dv[-1] = {}
dv[-1][0] = counter + 1
dv[0][-1] = counter + 2

p = [i for i in range(counter + 3)]
spot = -1
lstEdge.sort()
for edge in lstEdge:
    merge(dv[edge[1]][edge[2]],dv[edge[3]][edge[4]])
    if par(counter + 1) == par(counter + 2):
        print(str(edge[1]) + " " + str(edge[2]))
        break
print(time.perf_counter())
    
        
