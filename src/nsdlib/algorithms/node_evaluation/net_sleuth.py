"""NetSleuth source detection method."""

from typing import Dict

import networkx as nx
import numpy as np
from networkx import Graph


def net_sleuth(network: Graph) -> Dict[int, float]:
    # flake8: noqa
    """NetSleuth source evaluation method.

    References
    ----------
    - [1] B. A. Prakash, J. Vreeken, C. Faloutsos,
        "Efficiently spotting the starting points of an epidemic in a large
        graph" Knowledge and Information Systems, 2013
        https://link.springer.com/article/10.1007/s10115-013-0671-5
    - [2] L. Ying and K. Zhu,
        "Diffusion Source Localization in Large Networks"
        Synthesis Lectures on Communication Networks, 2018
    """
    L = nx.laplacian_matrix(network).toarray()
    eigenvalues, eigenvectors = np.linalg.eig(L)
    largest_eigenvalue = max(eigenvalues)
    largest_eigenvector = eigenvectors[:, list(eigenvalues).index(largest_eigenvalue)]

    scores = {v: largest_eigenvector[v] for v in network.nodes}
    return scores
