import re

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    
x = re.findall("(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))", content)
print(x)
val = 0
do = True
for i in range(len(x)):
    if x[i][2]:
        do = False
    elif x[i][1]:
        do = True
    if do and x[i][0]:
        a = x[i][0][4:-1]
        b, c = map(int, a.split(","))
        val += (b*c)
print(val)
