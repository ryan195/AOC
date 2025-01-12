locks = []
keys = []
height = 0
prev_height = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    lst = []
    is_lock = False
    for line in file:
        if line == "\n":
            if not has_calculated:
                curr = []
                for i in range(5):
                    counter = 0
                    for j in range(len(lst)):
                        if lst[j][i] == "#":
                            counter += 1
                    counter -= 1
                    curr.append(counter)
                if is_lock:
                    locks.append(tuple(curr))
                else:
                    keys.append(tuple(curr))
                prev_height = height
            lst = []
        else:
            if lst == []:
                if line[0] == "#":
                    is_lock = True
                else:
                    is_lock = False
                height = 1
                has_calculated = False
            else:
                height += 1
            lst.append(line.strip())
            if height == prev_height:
                has_calculated = True
                curr = []
                for i in range(5):
                    counter = 0
                    for j in range(len(lst)):
                        if lst[j][i] == "#":
                            counter += 1
                    counter -= 1
                    curr.append(counter)
                if is_lock:
                    locks.append(tuple(curr))
                else:
                    keys.append(tuple(curr))                
tot = 0
for x in locks:
    for y in keys:
        pos = True
        for i in range(5):
            if x[i]+y[i]+2 > height:
                pos = False
        if pos:
            tot += 1
print(tot)
