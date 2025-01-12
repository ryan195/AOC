lst1, lst2 = [], []
lst = []

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        for char in line:
            if char != "\n":
                if len(lst1) == len(lst2):
                    lst.append(len(lst1))
                    lst1.append(int(char))
                else:
                    lst2.append(int(char))
                    lst.append('.')

for i in range(len(lst1)-1, 0, -1):
    for j in range(0, i):
        if lst2[j] < lst1[i]:
            continue
        else:
            can = False
            lst2[j] -= lst1[i]
            counter = 0
            if i <= len(lst2):
                for k in range(len(lst)):
                    if lst[k] == i:
                        lst.insert(k, ".")
                        break
            lst.remove(i)
            for k in range(len(lst)):
                if (counter == j) and (lst[k] == "."):
                    lst.insert(k, i)
                    can = True
                    if i > len(lst2):
                        lst2.append(lst1[i])
                        lst.append(".")
                    else:
                        lst2.insert(i, lst1[i])
                        
                    break
                elif (lst[k] == "."):
                    counter += 1
            if can:
                break
            
tot = 0
counter = 0
l2c = 0
for i in range(len(lst)):
    if lst[i] == ".":
        counter += lst2[l2c]
        l2c += 1
    else:
        for j in range(lst1[lst[i]]):
            tot += (lst[i] * counter)
            counter += 1

print(tot)
            
        
