adj_list = {}

counter = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        a,b = line.split("-")
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []
        adj_list[a].append(b)
        adj_list[b].append(a)
#print(adj_list)
lst = set()
for k, v in adj_list.items():
    for x in v:
        for y in v:
            if y in adj_list[x]:
                inter_lst = [k,x,y]
                inter_lst.sort()
                lst.add(tuple(inter_lst))
tot = 0

for x in lst:
    start = False
    for j in range(len(x)):
        if x[j][0] == "t":
            start = True
    if start:
        tot += 1
print(tot)
