import graph_classes as gc

# Make the undirected Graph given to us
g_graph = gc.Graph(file_loc = 'a_test.txt', directed=False)

# Make a DFS tree
dfs_graph = g_graph.dfs(3)
print(dfs_graph.bi_connected_component_stack)
for c_node in dfs_graph.node:
    if dfs_graph.node[c_node].articulation is True:
        print(c_node)

a = 5

