xA, yA, xB, yB = 0, 0, 0, 0
prizeX, prizeY = 0, 0


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
            lst = line.split("=")
            prizeX, prizeY = int(lst[-2][:-3]) + 10000000000000,int(lst[-1][:-1]) + 10000000000000
            d = {}
            
            # Calculate if prize possible
            b = ((prizeY*xA) - (yA*prizeX))/((yB*xA) - (yA*xB))
            a = (prizeX - b*xB)/xA
            if (int(b) ==  b) and (int(a) == a):
                tot += (3*a + b)
        counter += 1

print(tot)
        
