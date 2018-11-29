import graph_classes as gc

# Make the undirected Graph given to us
print('Bi-Connected Components:')
g_graph = gc.Graph(file_loc = 'ArticulationData.txt', directed=False)

# Compute bi-connected components and articulation points
dfs_graph = g_graph.dfs(20)

# Print articulation Points
print("articulation points:")
for c_node in dfs_graph.node:
    if dfs_graph.node[c_node].articulation is True:
        print("\n"+str(c_node))





