from functools import lru_cache
from typing import Dict, Set, List, Union

from netcenlib.common import nx_cached
from netcenlib.common.nx_cached import MAX_SIZE
from networkx import Graph

from nsdlib.algorithms import node_evaluation, outbreaks_detection
from nsdlib.common.models import SourceDetectionEvaluation, NODE_TYPE
from nsdlib.taxonomies import (
    NodeEvaluationAlgorithm,
    OutbreaksDetectionAlgorithm,
)


def identify_outbreaks(
    network: Graph, outbreaks_alg: OutbreaksDetectionAlgorithm, *args, **kwargs
) -> Dict[int, list]:
    """Identify outbreaks in a given network."""
    function_name = f"{outbreaks_alg.value.lower()}"
    result = getattr(outbreaks_detection, function_name)(network, *args,
                                                         **kwargs)
    return {index: community for index, community in
            enumerate(result.communities)}


def evaluate_nodes(
    network: Graph, evaluation_alg: NodeEvaluationAlgorithm, *args, **kwargs
):
    """Evaluate nodes in a given network."""
    function_name = f"{evaluation_alg.value.lower()}"
    return getattr(node_evaluation, function_name)(network, *args, **kwargs)


@lru_cache(maxsize=MAX_SIZE)
def identify_outbreaks_cached(
    network: Graph, outbreaks_alg: OutbreaksDetectionAlgorithm, *args, **kwargs
) -> Dict[int, list]:
    """Identify outbreaks in a given network."""
    return identify_outbreaks(network, outbreaks_alg, *args, **kwargs)


@lru_cache(maxsize=MAX_SIZE)
def evaluate_nodes_cached(
    network: Graph, evaluation_alg: NodeEvaluationAlgorithm, *args, **kwargs
):
    """Evaluate nodes in a given network."""
    return evaluate_nodes(network, evaluation_alg, *args, **kwargs)


def compute_error_distances(
    G: Graph, not_detected_sources: Set[int],
    invalid_detected_sources: Set[int]
) -> Dict[NODE_TYPE, float]:
    if not_detected_sources and invalid_detected_sources:
        return {source:
            min(
                [
                    nx_cached.shortest_path_length(G, source=source,
                                                   target=invalid_source)
                    for invalid_source in invalid_detected_sources
                ]
            )
            for source in not_detected_sources
        }

    else:
        return {}


def compute_source_detection_evaluation(
    G: Graph,
    real_sources: List[NODE_TYPE],
    detected_sources: Union[NODE_TYPE, List[NODE_TYPE]]
) -> SourceDetectionEvaluation:
    detected_sources = (
        detected_sources if isinstance(detected_sources, list) else [
            detected_sources]
    )

    correctly_detected_sources = set(real_sources).intersection(
        detected_sources)
    invalid_detected_sources = set(detected_sources).difference(
        correctly_detected_sources
    )
    not_detected_sources = set(real_sources).difference(
        correctly_detected_sources)

    P = len(real_sources)
    N = len(G.nodes) - P
    FP = len(invalid_detected_sources)
    TP = len(correctly_detected_sources)
    FN = len(real_sources) - TP
    TN = N - FN

    error_distances = compute_error_distances(
        G=G,
        not_detected_sources=not_detected_sources,
        invalid_detected_sources=invalid_detected_sources,
    )

    return SourceDetectionEvaluation(
        real_sources=real_sources,
        detected_sources=detected_sources,
        error_distances=error_distances,
        TP=TP,
        FP=FP,
        TN=TN,
        FN=FN,
        P=P,
        N=N,
    )
