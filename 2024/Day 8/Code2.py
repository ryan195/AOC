counter = 0
d = {}
lst = []
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        lst.append([])
        for char in line:
            if char != "\n":
                lst[counter].append(char)
                if char != ".":
                    if char not in d:
                        d[char] = []
                    d[char].append((counter, len(lst[counter]) - 1))
        counter += 1

tot = 0
for k, v in d.items():
    if len(v) > 1:
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                diffx = abs(v[i][0] - v[j][0])
                diffy = abs(v[i][1] - v[j][1])
                a, b = (-1,-1), (-1,-1)
                if (v[i][0] > v[j][0]):
                    if (v[i][1] > v[j][1]):
                        a = (v[i][0] + diffx, v[i][1] + diffy)
                        b = (v[j][0] - diffx, v[j][1] - diffy)
                        while (0 <= a[0] < len(lst)) and (0 <= a[1] < len(lst[0])):
                            if (lst[a[0]][a[1]] != "#"):
                                tot += 1
                                lst[a[0]][a[1]] = "#"
                            a = (a[0] + diffx, a[1] + diffy)
                        while (0 <= b[0] < len(lst)) and (0 <= b[1] < len(lst[0])):
                            if (lst[b[0]][b[1]] != "#"):
                                tot += 1
                                lst[b[0]][b[1]] = "#"
                            b = (b[0] - diffx, b[1] - diffy)
                    else:
                        a = (v[i][0] + diffx, v[i][1] - diffy)
                        b = (v[j][0] - diffx, v[j][1] + diffy)
                        while (0 <= a[0] < len(lst)) and (0 <= a[1] < len(lst[0])):
                            if (lst[a[0]][a[1]] != "#"):
                                tot += 1
                                lst[a[0]][a[1]] = "#"
                            a = (a[0] + diffx, a[1] - diffy)
                        while (0 <= b[0] < len(lst)) and (0 <= b[1] < len(lst[0])):
                            if (lst[b[0]][b[1]] != "#"):
                                tot += 1
                                lst[b[0]][b[1]] = "#"
                            b = (b[0] - diffx, b[1] + diffy)
                else:
                    if (v[i][1] > v[j][1]):
                        a = (v[i][0] - diffx, v[i][1] + diffy)
                        b = (v[j][0] + diffx, v[j][1] - diffy)
                        while (0 <= a[0] < len(lst)) and (0 <= a[1] < len(lst[0])):
                            if (lst[a[0]][a[1]] != "#"):
                                tot += 1
                                lst[a[0]][a[1]] = "#"
                            a = (a[0] - diffx, a[1] + diffy)
                        while (0 <= b[0] < len(lst)) and (0 <= b[1] < len(lst[0])):
                            if (lst[b[0]][b[1]] != "#"):
                                tot += 1
                                lst[b[0]][b[1]] = "#"
                            b = (b[0] + diffx, b[1] - diffy)
                    else:
                        a = (v[i][0] - diffx, v[i][1] - diffy)
                        b = (v[j][0] + diffx, v[j][1] + diffy)
                        while (0 <= a[0] < len(lst)) and (0 <= a[1] < len(lst[0])):
                            if (lst[a[0]][a[1]] != "#"):
                                tot += 1
                                lst[a[0]][a[1]] = "#"
                            a = (a[0] - diffx, a[1] - diffy)
                        while (0 <= b[0] < len(lst)) and (0 <= b[1] < len(lst[0])):
                            if (lst[b[0]][b[1]] != "#"):
                                tot += 1
                                lst[b[0]][b[1]] = "#"
                            b = (b[0] + diffx, b[1] + diffy)
for k, v in d.items():
    for coord in v:
        if lst[coord[0]][coord[1]] != "#":
            tot += 1

print(tot)
