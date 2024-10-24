# Description: Test script for Networkx
# https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.graphml.read_graphml.html
# read_graphml(path, node_type=<class 'str'>, edge_key_type=<class 'int'>, force_multigraph=False)
import networkx as nx

# Read the graph from a GraphML file
G = nx.read_graphml("Data/reactome-77-reaction_R-HSA-5218826.graphml")

# Display basic info about the graph (number of nodes, edges, graph type)
print(f"Graph type: {type(G)}")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# Access nodes and edges
print("Nodes:", G.nodes(data=True))  # 'data=True' shows node attributes
print("Edges:", G.edges(data=True))  # 'data=True' shows edge attributes
