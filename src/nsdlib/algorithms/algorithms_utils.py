from functools import lru_cache

from networkx import Graph

from nsdlib.algorithms import node_evaluation, outbreaks_detection
from nsdlib.common.nx_cached import MAX_SIZE
from nsdlib.taxonomies import (
    NodeEvaluationAlgorithm,
    OutbreaksDetectionAlgorithm,
)


def identify_outbreaks(
    network: Graph, outbreaks_alg: OutbreaksDetectionAlgorithm, *args, **kwargs
):
    """Identify outbreaks in a given network."""
    function_name = f"{outbreaks_alg.value.lower()}"
    return getattr(outbreaks_detection, function_name)(network, *args, **kwargs)


def evaluate_nodes(
    network: Graph, evaluation_alg: NodeEvaluationAlgorithm, *args, **kwargs
):
    """Evaluate nodes in a given network."""
    function_name = f"{evaluation_alg.value.lower()}_evaluation"
    return getattr(node_evaluation, function_name)(network, *args, **kwargs)


@lru_cache(maxsize=MAX_SIZE)
def identify_outbreaks_cached(
    network: Graph, outbreaks_alg: OutbreaksDetectionAlgorithm, *args, **kwargs
):
    """Identify outbreaks in a given network."""
    return identify_outbreaks(network, outbreaks_alg, *args, **kwargs)


@lru_cache(maxsize=MAX_SIZE)
def evaluate_nodes_cached(
    network: Graph, evaluation_alg: NodeEvaluationAlgorithm, *args, **kwargs
):
    """Evaluate nodes in a given network."""
    return evaluate_nodes(network, evaluation_alg, *args, **kwargs)
