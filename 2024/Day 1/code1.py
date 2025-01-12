arr1, arr2 = [], []

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        x, y = map(int, line.split())
        arr1.append(x)
        arr2.append(y)

# Print the content to verify
arr1.sort()
arr2.sort()
diff = 0
for i in range(len(arr1)):
    diff += abs(arr1[i] - arr2[i])
print(diff)
