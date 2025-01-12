lst = []

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append(line)

counter = 0
    
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] == 'X':
            if (i > 2) and (j > 2):
                if (lst[i-1][j-1] == 'M') and (lst[i-2][j-2] == 'A') and (lst[i-3][j-3] == 'S'):
                    counter += 1
            if (i > 2):
                if (lst[i-1][j] == 'M') and (lst[i-2][j] == 'A') and (lst[i-3][j] == 'S'):
                    counter += 1
            if (i > 2) and (j < (len(lst[0]) - 3)):
                if (lst[i-1][j+1] == 'M') and (lst[i-2][j+2] == 'A') and (lst[i-3][j+3] == 'S'):
                    counter += 1
            if (j > 2):
                if (lst[i][j-1] == 'M') and (lst[i][j-2] == 'A') and (lst[i][j-3] == 'S'):
                    counter += 1
            if (j < (len(lst[0]) - 3)):
                if (lst[i][j+1] == 'M') and (lst[i][j+2] == 'A') and (lst[i][j+3] == 'S'):
                    counter += 1
            if (i < (len(lst) - 3)) and (j > 2):
                if (lst[i+1][j-1] == 'M') and (lst[i+2][j-2] == 'A') and (lst[i+3][j-3] == 'S'):
                    counter += 1
            if (i < (len(lst) - 3)):
                if (lst[i+1][j] == 'M') and (lst[i+2][j] == 'A') and (lst[i+3][j] == 'S'):
                    counter += 1
            if (i < (len(lst) - 3)) and (j < (len(lst[0]) - 3)):
                if (lst[i+1][j+1] == 'M') and (lst[i+2][j+2] == 'A') and (lst[i+3][j+3] == 'S'):
                    counter += 1


print(counter)
            
