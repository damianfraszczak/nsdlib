import operator
from functools import reduce

import networkx as nx
from networkx import Graph

from nsdlib.common.models import NODE_TYPE

NODE_INFECTION_PROBABILITY_ATTR = "INFECTION_PROBABILITY"


def init_extended_network(G: Graph, IG: Graph) -> Graph:
    """
    Initialize extended network.

    @param G: Network
    @param IG: Infected network

    @return: Extended network
    """
    EG = G.copy()
    nx.set_node_attributes(
        EG,
        {
            node: {NODE_INFECTION_PROBABILITY_ATTR: 1.0 if node in IG else 0.0}
            for node in G
        },
    )
    return EG


def compute_neighbors_probability(node: NODE_TYPE, G: Graph) -> float:
    """
    Compute probability of infection for a given node.

    @param node: Node
    @param G: Graph

    @return: Probability of infection for a given node
    """
    neighbors_probability = [
        G.nodes[node][NODE_INFECTION_PROBABILITY_ATTR] for node in nx.neighbors(G, node)
    ]
    return reduce(
        operator.mul,
        neighbors_probability,
        1,
    )


def remove_invalid_nodes(EG: Graph, threshold: float) -> Graph:
    """
    Remove nodes with infection probability lower than threshold.

    @param EG: Extended network
    @param threshold: Infection probability threshold

    @return: Extended network with removed nodes that have infection probability lower than threshold
    """
    nodes_to_remove = []
    for node in EG.nodes(data=True):
        data = node[1]
        infection_probability = data[NODE_INFECTION_PROBABILITY_ATTR]
        if infection_probability < threshold:
            nodes_to_remove.append(node[0])

    EG.remove_nodes_from(nodes_to_remove)
    EG.remove_nodes_from(list(nx.isolates(EG)))

    return EG
