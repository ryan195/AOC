adj_list = {}
lst = []
action = False

ans = 0
counter = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        counter += 1
        if line == "\n":
            action = True
        elif not action:
            gate, val = line.split(":")
            val = int(val)
            adj_list[gate] = val
        else:
            x = line.split("->")
            target = x[1].strip()
            if x[0][4] == "O":
                a, b = x[0][0:3], x[0][7:10]
                lst.append(((a,b),"OR",target))
            else:
                a, b, act = x[0][0:3],x[0][8:11],x[0][4:7]
                lst.append(((a,b),act,target))

for _ in range(counter + 5):
    for x in lst:
        if (x[0][0] in adj_list) and (x[0][1] in adj_list):
            if x[1] == "AND":
                adj_list[x[2]] = adj_list[x[0][0]]&adj_list[x[0][1]]
            elif x[1] == "OR":
                adj_list[x[2]] = adj_list[x[0][0]]|adj_list[x[0][1]]
            elif x[1] == "XOR":
                adj_list[x[2]] = adj_list[x[0][0]]^adj_list[x[0][1]]

new_lst = [-1 for i in range(50)]
for k, v in adj_list.items():
    if k[0] == "z":
        new_lst[(int(k[1:]))] = v
print(new_lst)
