"""Jordan center source detection method."""

from typing import Dict

import netcenlib as ncl
from networkx import Graph


def jordan_center(network: Graph) -> Dict[int, float]:
    """Jordan center node evaluation method.

    References
    ----------
    -  [1] L. Ying and K. Zhu,
        "On the Universality of Jordan Centers for Estimating Infection Sources
         in Tree Networks" IEEE Transactions of Information Theory, 2014
    - [2] L. Ying and K. Zhu,
        "Diffusion Source Localization in Large Networks"
        Synthesis Lectures on Communication Networks, 2018
    """
    scores = ncl.eccentricity_centrality(network)
    return {v: 1 / scores.get(v) for v in network.nodes}
