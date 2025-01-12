x, y = 101, 103
hx, hy = (x-1)//2, (y-1)//2
q1, q2, q3, q4 = 0, 0, 0, 0

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        l = line.split("=")
        pX, pY = map(int, l[1][:-1].split(","))
        vX, vY = map(int, l[2].split(","))
        nX, nY = pX+(100*vX), pY+(100*vY)
        nX, nY = nX%x, nY%y
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
print(q1*q2*q3*q4)
