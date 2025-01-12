tot = 0

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        x = int(line)
        for _ in range(2000):
            y = x*64
            x ^= y
            x %= 16777216
            y = x//32
            x ^= y
            x %= 16777216
            y = x*2048
            x ^= y
            x %= 16777216
        tot += x
print(tot)
