# Description: Test script for Networkx
# https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.graphml.read_graphml.html
# read_graphml(path, node_type=<class 'str'>, edge_key_type=<class 'int'>, force_multigraph=False)


import networkx as nx

# Read the graph from a GraphML file
G = nx.read_graphml("graph.graphml")

# Display basic info about the graph
print(nx.info(G))

# Access nodes and edges
print(G.nodes())
print(G.edges())
