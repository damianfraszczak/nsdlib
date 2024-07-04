"""NetSleuth source detection method."""

from typing import Dict

import networkx as nx
import numpy as np
from networkx import Graph


def net_sleuth(network: Graph) -> Dict[int, float]:
    """Netsleuth source detection method."""

    L = nx.laplacian_matrix(network).toarray()
    eigenvalues, eigenvectors = np.linalg.eig(L)
    largest_eigenvalue = max(eigenvalues)
    largest_eigenvector = eigenvectors[:,
                          list(eigenvalues).index(largest_eigenvalue)]

    scores = {
        v: largest_eigenvector[v]
        for v in network.nodes
    }
    return scores
