d = {}
counter = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst = []
        x = int(line)
        lst.append(x%10)
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
            lst.append(x%10)
            if len(lst) >= 5:
                z = lst[-5:]
                lst2 = []
                for k in range(1,5):
                    lst2.append(z[k]-z[k-1])
                z = lst2[0]*1000000+lst2[1]*10000+lst2[2]*100+lst2[3]
                if z not in d:
                    d[z] = {}
                    d[z][counter] = (x%10)
                else:
                    if counter not in d[z]:
                        d[z][counter] = (x%10)
        counter += 1

ans = 0
for k, v in d.items():
    curr = 0
    for k2, v2 in v.items():
        curr += v2
    if curr > ans:
        ans = max(ans, curr)
print(ans)


