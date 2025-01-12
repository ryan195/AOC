
d = {}

def recurs(x, iters):
    if iters == 75:
        return 1
    else:
        if (x, iters) in d:
            return d[(x, iters)]
        a = str(x)
        if x == 0:
            d[(x, iters)] = recurs(1, iters + 1)
            return d[(x, iters)]
        elif len(a) % 2:
            d[(x, iters)] = recurs(x*2024, iters + 1)
            return d[(x, iters)]
        else:
            d[(x, iters)] = recurs(int(a[0:int(len(a)/2)]), iters + 1) + recurs(int(a[int(len(a)/2):]), iters + 1)
            return d[(x, iters)]

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst = list(map(int, line.split()))
print(lst)
val = 0
for x in lst:
    print(x)
    val += recurs(x, 0)

print(val)
