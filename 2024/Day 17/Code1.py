
counter = 0
a, b, c = 0, 0, 0
ptr = 0
lst = []

def combo(x):
    if x <= 3: return x
    elif x == 4: return a
    elif x == 5: return b
    elif x == 6: return c

def c0(x):
    global ptr
    ptr += 2
    global a
    a //= (2**combo(x))

def c1(x):
    global ptr
    ptr += 2
    global b
    b ^= x

def c2(x):
    global ptr
    ptr += 2
    global b
    b = (combo(x)%8)

def c3(x):
    global ptr
    global a
    if a != 0:
        if ptr == x:
            ptr += 2
        else:
            ptr = x
    else:
        ptr += 2

def c4(x):
    global ptr
    ptr += 2
    global b
    b ^= c

def c5(x):
    global ptr
    ptr += 2
    lst.append(combo(x)%8)

def c6(x):
    global ptr
    ptr += 2
    global b
    b = (a//(2**combo(x)))

def c7(x):
    global ptr
    ptr += 2
    global c
    c = (a//(2**combo(x)))
        
    
# Open the file in read mode ('r') and automatically close it after reading
with open('input2.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        if counter == 0:
            a = int(line.split(":")[1])
            counter += 1
            continue
        if counter == 1:
            b = int(line.split(":")[1])
            counter += 1
            continue
        if counter == 2:
            c = int(line.split(":")[1])
            counter += 1
            continue
        if line != "\n":
            x = line.split(":")[1]
            x = list(map(int,x.split(",")))

            while ptr < len(x):
                #print(str(ptr) + "HI")
                #print(str(x[ptr]) + "HEY")
                d = x[ptr]
                e = x[ptr+1]
                print(str(ptr) + " " + str(d) + " " + str(e) + " " + str(a) + " " + str(b) + " " + str(c))
                if d == 0:
                    c0(e)
                elif d == 1:
                    c1(e)
                elif d == 2:
                    c2(e)
                elif d == 3:
                    c3(e)
                elif d == 4:
                    c4(e)
                elif d == 5:
                    c5(e)
                elif d == 6:
                    c6(e)
                elif d == 7:
                    c7(e)
print(",".join(list(map(str, lst))))
        
