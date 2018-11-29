import graph_classes as gc

# Make the undirected Graph given to us
print("")
print('Bi-Connected Components:')
g_graph = gc.Graph(file_loc = 'a_test.txt', directed=False)
# Compute bi-connected components and articulation points
dfs_graph = g_graph.dfs_and_biconnected(1)
print("")

for i in dfs_graph.node:
    print("Index "+str(i)+"|  "+ "disc: "+ str(dfs_graph.node[i].disc) + ", low: "+ str(dfs_graph.node[i].low))

# Print articulation points
for c_node in dfs_graph.node:
    if dfs_graph.node[c_node].articulation is True:
        print("\narticulation:"+ str(c_node))


