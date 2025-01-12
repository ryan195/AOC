xA, yA, xB, yB = 0, 0, 0, 0
prizeX, prizeY = 0, 0
d = {}

def uknap(currX, currY, push):
    if (currX + xA <= prizeX) and (currY + yA <= prizeY):
        if (currX + xA, currY + yA) in d:
            if push + 3 < d[(currX + xA, currY + yA)]:
                d[(currX + xA, currY + yA)] = push + 3
                uknap(currX + xA, currY + yA, push + 3)
        else:
            d[(currX + xA, currY + yA)] = push + 3
            uknap(currX + xA, currY + yA, push + 3)
    if (currX + xB <= prizeX) and (currY + yB <= prizeY):
        if (currX + xB, currY + yB) in d:
            if push + 1 < d[(currX + xB, currY + yB)]:
                d[(currX + xB, currY + yB)] = push + 1
                uknap(currX + xB, currY + yB, push + 1)
        else:
            d[(currX + xB, currY + yB)] = push + 1
            uknap(currX + xB, currY + yB, push + 1)    

tot = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    counter = 0
    for line in file:
        if counter % 4 == 0:
            # Button A
            lst = line.split("+")
            xA, yA = int(lst[-2][:-3]), int(lst[-1][:-1])
        elif counter % 4 == 1:
            # Button B
            lst = line.split("+")
            xB, yB = int(lst[-2][:-3]), int(lst[-1][:-1])
        elif counter % 4 == 2:
            # Prize
            print("hi")
            lst = line.split("=")
            prizeX, prizeY = int(lst[-2][:-3]) + 10000000000000,int(lst[-1][:-1]) + 10000000000000
            d = {}
            
            # Calculate if prize possible
            uknap(0,0,0)
            if (prizeX, prizeY) in d:
                tot += d[(prizeX, prizeY)]
                if d[(prizeX, prizeY)] > 400:
                    print(str(prizeX) + " " + str(prizeY) + " " + str(d[(prizeX, prizeY)]))
        counter += 1

print(tot)
