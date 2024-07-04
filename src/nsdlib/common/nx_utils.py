import math
import random
from typing import Dict, List, Tuple

from networkx import Graph


def create_snapshot_IG(G, delete_ratio=None) -> Tuple[Graph, list]:
    """Create a snapshot of the network by removing a random number of nodes.

    :param G: The network
    :param ratio_to_remove: The ratio of nodes to remove. If None, remove 10%
    of the nodes.
    """
    IG = G.copy()
    if not delete_ratio:
        delete_ratio = 10
    delete_ratio = delete_ratio / 100 if delete_ratio > 1 else delete_ratio
    k = math.ceil(len(G.nodes) * delete_ratio)
    to_remove = list(sorted(random.sample(list(G.nodes), k=k)))
    IG.remove_nodes_from(to_remove)
    return IG, to_remove


def exclude_nodes(G: Graph, nodes: List[any]) -> Graph:
    """Remove nodes from a graph."""
    g_copy = G.copy()
    g_copy.remove_nodes_from(nodes)
    return g_copy


def create_subgraphs_based_on_outbreaks(
    G: Graph, outbreaks: Dict[int, list]
) -> List[Graph]:
    """Create subgraphs based on outbreaks."""
    return [G.subgraph(outbreak) for outbreak in outbreaks.values()]
