mapp = {}
arr1 = []

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        x, y = map(int, line.split())
        arr1.append(x)
        if y not in mapp:
            mapp[y] = 1
        else:
            mapp[y] += 1

# Print the content to verify
sim = 0
for i in range(len(arr1)):
    if arr1[i] in mapp:
        sim += arr1[i]*(mapp[arr1[i]])
print(sim)
