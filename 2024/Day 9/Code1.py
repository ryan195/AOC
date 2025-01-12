lst = []
is_file = True
idx = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        for char in line:
            if char != "\n":
                if is_file:
                    lst.extend([str(idx)]*int(char))
                    idx += 1
                else:
                    lst.extend(['.']*int(char))
                is_file = not is_file

left, right = 0, len(lst) - 1

while left < right:
    if lst[left] != '.':
        left += 1
        continue
    if lst[right] == '.':
        right -= 1
        continue
    lst[left], lst[right] = lst[right], lst[left]
    left += 1
    right -= 1

ans = 0
for i in range(len(lst)):
    if lst[i] == '.':
        break
    ans += int(lst[i])*i

print(ans)
    
