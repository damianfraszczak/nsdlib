import nbformat
nb = nbformat.read(open('../docs/files/nsdlib.ipynb'), as_version=4)
nbformat.write(nb, '../docs/files/nsdlib.ipynb')


import networkx as nx
import nsdlib as ncl

# Create a graph
G = nx.karate_club_graph()

# Compute degree centrality
degree_centrality = ncl.compute_centrality(G, ncl.Centrality.CENTROID)

# Visualize score
ncl.print_dict(degree_centrality)
