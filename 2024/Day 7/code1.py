def recurs(target, sumi, idx, lst):
    if idx == len(lst):
        return sumi == target
    else:
        return recurs(target, sumi*lst[idx], idx+1, lst) or recurs(target, sumi+lst[idx], idx+1, lst)

tot = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst = line.split(":")
        target = int(lst[0])
        subjects = list(map(int, lst[1][1:].split(" ")))
        if recurs(target, subjects[0], 1, subjects):
            tot += target
print(tot)
