"""NetSleuth source detection method."""

from typing import Dict

import networkx as nx
import numpy as np
from networkx import Graph


def netsleuth(IG: Graph) -> Dict[int, float]:
    """Netsleuth source detection method."""
    nodes = np.array(IG.nodes())
    L = nx.laplacian_matrix(IG).todense().A
    w, v = np.linalg.eig(L)
    v1 = v[np.where(w == np.min(w))][0]
    max_val = np.max(v1)
    sources = nodes[np.where(v1 == np.max(v1))]
    return {source: max_val for source in sources}
