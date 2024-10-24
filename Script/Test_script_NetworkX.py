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


import matplotlib.pyplot as plt

# Read the graph from a GraphML file
G = nx.read_graphml("Data/reactome-77-reaction_R-HSA-5218826.graphml")

# Draw the graph
plt.figure(figsize=(10, 10))  # Adjust the figure size as needed
nx.draw(
    G,
    with_labels=True,
    node_color="lightblue",
    edge_color="gray",
    node_size=500,
    font_size=8,
)

# Show the plot
plt.show()


pos = nx.circular_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightgreen",
    edge_color="gray",
    node_size=700,
    font_size=10,
)
plt.show()

pos = nx.spring_layout(G)  # Compute layout positions
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    edge_color="black",
    node_size=600,
    font_size=9,
)
plt.show()


pos = nx.spring_layout(G)
node_labels = nx.get_node_attributes(
    G, "label"
)  # Replace 'label' with the actual attribute name if available
nx.draw(G, pos, with_labels=False, node_color="lightblue", edge_color="gray")
nx.draw_networkx_labels(G, pos, labels=node_labels)
plt.show()
