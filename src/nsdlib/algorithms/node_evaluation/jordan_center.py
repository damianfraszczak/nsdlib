"""Jordan center source detection method."""

from typing import Dict

import netcenlib as ncl
from networkx import Graph


def jordan_center(IG: Graph) -> Dict[int, float]:
    """Jordan center source detection method."""
    scores = ncl.eccentricity_centrality(IG)
    return {v: 1 / scores.get(v) for v in IG.nodes}
