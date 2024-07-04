"""Jordan center source detection method."""

from typing import Dict

import netcenlib as ncl
from networkx import Graph


def jordan_center(network: Graph) -> Dict[int, float]:
    """Jordan center source detection method."""
    scores = ncl.eccentricity_centrality(network)
    return {v: 1 / scores.get(v) for v in network.nodes}
