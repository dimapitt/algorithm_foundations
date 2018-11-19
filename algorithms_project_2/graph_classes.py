from collections import defaultdict
import copy


class NodeProps:
    def __init__(self):
        self.connections = set()
        self.visited = False
        self.complete = False
        self.root = False
        self.parents = set()
        self.children = set()


class Graph:
    def __init__(self, file_loc=None, directed=False):
        self.directed = directed
        self.node = defaultdict()

        if file_loc is not None:  # Make graph from file if available
            self.read_file(file_loc)

    def remove_node(self, node_ind):
        cnt_nodes = self.node[node_ind].connections

        for cnt_node in cnt_nodes:
            self.node[cnt_node].connections.remove(node_ind)

        del self.node[node_ind]  # Remove that node input

    def read_file(self, file_loc):
        c_file = open(file_loc, 'r')
        n_nodes = c_file.readline()  #First line is the # of vertices
        n_nodes = int(n_nodes[:-1])
        for k in range(int(n_nodes)):
            str_edges = c_file.readline()
            edges = [int(s) for s in str_edges.split() if s.isdigit()]
            self.add_node(k+1, edges=edges)

    def add_node(self,  node_key, edges=None):
        if node_key not in self.node.keys():
            self.node.update({node_key: NodeProps()})

        if edges is not None:
            edges = set(edges)
            for end_node in edges:
                if end_node not in self.node.keys():
                    self.add_node(end_node)  # Add the edge node if it doesn't already exist
                self.add_edge(node_key, end_node)
        return node_key

    def add_edge(self, node_a, node_b):
        self.node[node_a].connections.add(node_b)
        if not self.directed:
            self.node[node_b].connections.add(node_a)
        else:
            self.node[node_a].children.add(node_b)
            self.node[node_b].parents.add(node_a)

    def dfs(self, start_index, graph=None, dfs_graph = None, parent=-1):
        if dfs_graph is None:
            dfs_graph = Graph(directed = True)
        if graph is None:
            graph = copy.deepcopy(self)

        graph.node[start_index].visited = True
        for c_connection in graph.node[start_index].connections:
            if graph.node[c_connection].visited is not True:
                dfs_graph = self.dfs(c_connection, graph=graph, parent=start_index, dfs_graph = dfs_graph)

        dfs_graph.add_node(start_index)
        dfs_graph.add_node(parent)
        dfs_graph.add_edge(parent, start_index)

        return dfs_graph
