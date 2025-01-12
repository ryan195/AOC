ans = 0

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst = list(map(int, line.split()))
        decreasing = False
        if (lst[0] > lst[1]):
            decreasing = True
        good = True
        for i in range(len(lst) - 1):
            if decreasing:
                if not (1 <= (lst[i] - lst[i + 1]) <= 3):
                    good = False
                    break
            else:
                if not (1 <= (lst[i + 1] - lst[i]) <= 3):
                    good = False
                    break  
        if good:
            ans += 1

print(ans)
