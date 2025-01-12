ans = 0

def is_good(lst):
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
    return good
    

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst = list(map(int, line.split()))
        if is_good(lst):
            ans += 1
        else:
            for i in range(len(lst)):
                new_lst = []
                for j in range(len(lst)):
                    if i != j:
                        new_lst.append(lst[j])
                if is_good(new_lst):
                    ans += 1
                    break

print(ans)
