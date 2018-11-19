import graph_classes as gc

# Make the undirected Graph given to us
g_graph = gc.Graph(file_loc = '/Users/kalikd1/Documents/classes/algorithms/algorithm_foundations/ArticulationData.txt', directed=False)

# Make a DFS tree
dfs_graph = g_graph.dfs(71)
a = 5

