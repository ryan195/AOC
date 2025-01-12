lst = []

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append(line)

counter = 0
print(lst)

print(len(lst))
print(len(lst[0]))
for i in range(len(lst)):
    for j in range(len(lst[0])-1):
        #print(str(i) + "   " + str(j))
        if lst[i][j] == 'A':
            if (i > 0) and (i < len(lst) - 1) and (j > 0) and (j < len(lst[0]) - 1):
                if ((lst[i-1][j-1] == "M") and (lst[i+1][j+1] == "S")) or ((lst[i-1][j-1] == "S") and (lst[i+1][j+1] == "M")):
                    if ((lst[i-1][j+1] == "M") and (lst[i+1][j-1] == "S")) or ((lst[i-1][j+1] == "S") and (lst[i+1][j-1] == "M")):
                        counter += 1#print(str(i) + "  " + str(j))

print(counter)
            
