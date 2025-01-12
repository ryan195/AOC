lstP = []
lstV = []
x, y = 101, 103
hx, hy = (x-1)//2, (y-1)//2

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        l = line.split("=")
        pX, pY = map(int, l[1][:-1].split(","))
        vX, vY = map(int, l[2].split(","))
        lstP.append((pX, pY))
        lstV.append((vX, vY))

counter = 1
mini = 218619324
while True:
    display = []
    for i in range(103):
        display.append([])
        for j in range(101):
            display[-1].append(".")
    q1, q2, q3, q4 = 0, 0, 0, 0
    for i in range(len(lstP)):
        nX, nY = (lstP[i][0]+(lstV[i][0]*counter))%101, (lstP[i][1]+(lstV[i][1]*counter))%103
        display[nY][nX] = 'X'
        if nX < hx:
            if nY < hy:
                q1 += 1
            elif nY > hy:
                q2 += 1
        elif nX > hx:
            if nY > hy:
                q4 += 1
            elif nY < hy:
                q3 += 1
    mini = min(q1*q2*q3*q4, mini)
    if (counter > 100) and (mini == (q1*q2*q3*q4)):
        for i in range(103):
            print("".join(display[i]))
        print(counter)
    counter += 1
