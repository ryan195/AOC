graph = []
visited = []
neighbours = [(-1,0),(1,0),(0,-1),(0,1)]

# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        graph.append([])
        visited.append([])
        for char in line:
            if char != "\n":
                graph[-1].append(char)
                visited[-1].append(0)

tot = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if not visited[i][j]:
            queue = [(i, j)]
            counter1 = 0
            counter2 = 0
            fx, fy, lx, ly = i, j, i, j
            visited[i][j] = 1
            while queue:
                counter1 += 1
                currx, curry = queue[0]
                reg = graph[currx][curry]
                queue.pop(0)
                currcount = 4
                for coords in neighbours:
                    if (0 <= currx+coords[0] < len(graph)) and (0 <= curry+coords[1] < len(graph[0])) and (reg == graph[currx+coords[0]][curry+coords[1]]):
                        currcount -= 1
                        if not visited[currx+coords[0]][curry+coords[1]]:
                            visited[currx+coords[0]][curry+coords[1]] = 1
                            queue.append((currx+coords[0], curry+coords[1]))
                counter2 += currcount
            tot += (counter1 * counter2)
print(tot)
            

    


    
