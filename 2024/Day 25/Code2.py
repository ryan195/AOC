import networkx as nx

G = nx.Graph()

edges = []
counter = 0
# Open the file in read mode ('r') and automatically close it after reading
with open('input.txt', 'r') as file:
    # Read the contents of the file
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        a,b = line.split("-")
        edges.append((a,b))
        
G.add_edges_from(edges)
all_cliques = list(nx.find_cliques(G))
max_clique = max(all_cliques, key=len)
print("All cliques:", all_cliques)
print("Maximum clique:", max_clique)
print("Size of maximum clique:", len(max_clique))
max_clique.sort()
print(",".join(max_clique))
