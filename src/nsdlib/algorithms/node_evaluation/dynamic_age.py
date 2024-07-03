"""Dynamic age source detection method."""

import copy
from typing import Dict

import networkx as nx
import numpy as np
from networkx import Graph


def dynamic_age(IG: Graph) -> Dict[int, float]:
    """Dynamic age source detection method."""
    A = nx.adjacency_matrix(IG).todense().A
    dynamicAges = {node: 0 for node in IG.nodes}
    lamda_max = max(np.linalg.eigvals(A)).real

    for node in IG.nodes:
        A_new = copy.deepcopy(A)
        A_new = np.delete(A_new, node, axis=0)
        A_new = np.delete(A_new, node, axis=1)
        lamda_new = max(np.linalg.eigvals(A_new)).real
        dynamicAges[node] = (lamda_max - lamda_new) / lamda_max

    return dynamicAges
