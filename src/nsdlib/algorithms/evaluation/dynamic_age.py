"""Dynamic age source detection method."""

import copy
from typing import Dict

import networkx as nx
import numpy as np
from networkx import Graph


def dynamic_age(network: Graph) -> Dict[int, float]:
    """Dynamic age source detection method.

    References
    ----------
    - [1] V. Fioriti i M. Chinnici, „Predicting the sources of an outbreak with a spectral technique”, ArXiv12112333 Math-Ph Physicsphysics, lis. 2012, Dostęp: 6 maj 2021. [Online]. Dostępne na: http://arxiv.org/abs/1211.2333
    """
    A = nx.adjacency_matrix(network).todense().A
    dynamicAges = {node: 0 for node in network.nodes}
    lamda_max = max(np.linalg.eigvals(A)).real

    for node in network.nodes:
        A_new = copy.deepcopy(A)
        A_new = np.delete(A_new, node, axis=0)
        A_new = np.delete(A_new, node, axis=1)
        lamda_new = max(np.linalg.eigvals(A_new)).real
        dynamicAges[node] = (lamda_max - lamda_new) / lamda_max

    return dynamicAges
