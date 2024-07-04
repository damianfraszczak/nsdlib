from networkx import Graph

from nsdlib.algorithms.reconstruction.utils import (
    NODE_INFECTION_PROBABILITY_ATTR,
    compute_neighbors_probability,
    init_extended_network,
    remove_invalid_nodes,
)


def sbrp(
    G: Graph, IG: Graph, reconstruction_threshold=0.5, max_iterations: int = 1
) -> Graph:
    # flake8: noqa
    """SbRP graph reconstruction algorithm.

    @param G: Network
    @param IG: Infected network
    @param reconstruction_threshold: Reconstruction threshold

    @return: Extended network
    References
        ----------
        - [1] W. Zang, P. Zhang, C. Zhou, i L. Guo, „Discovering Multiple
        Diffusion Source Nodes in Social Networks”, Procedia Comput. Sci.,
        t. 29, s. 443–452, 2014, doi: 10.1016/j.procs.2014.05.040.
        - [2] W. Zang, P. Zhang, C. Zhou, i L. Guo, „Locating multiple sources
        in social networks under the SIR model: A divide-and-conquer approach”,
         J. Comput. Sci., t. 10, s. 278–287, wrz. 2015,
         doi: 10.1016/j.jocs.2015.05.002.
    """
    EG = init_extended_network(G=G, IG=IG)
    iter = 1
    nodes = [1]
    while iter < max_iterations and nodes:
        iter += 1
        for node in IG:
            for neighbour in G.neighbors(node):
                if neighbour in IG:
                    continue
                EG.nodes[neighbour][NODE_INFECTION_PROBABILITY_ATTR] = (
                    compute_neighbors_probability(G=EG, node=neighbour)
                )

    remove_invalid_nodes(EG, reconstruction_threshold)
    return EG
