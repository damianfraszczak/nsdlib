"""Centrality measures for networks."""
from typing import Dict, Union, List, Tuple

from networkx import Graph

from nsdlib.algorithms.algorithms_utils import identify_outbreaks_cached, \
    evaluate_nodes_cached, compute_source_detection_evaluation
from nsdlib.common.models import SourceDetectionConfig, NODE_TYPE, \
    SourceDetectionResult, \
    SourceDetectionEvaluation
from nsdlib.common.nx_utils import create_subgraphs_based_on_outbreaks
from nsdlib.commons import normalize_dict_values


class SourceDetector:
    def __init__(self, config: SourceDetectionConfig):
        self.config = config

    def _reconstruct_propagation(self, IG, G):
        if self.config.propagation_reconstruction_algorithm:
            IG = IG
        return IG

    def _detect_outbreaks(self, IG):
        outbreaks = [IG]

        if self.config.outbreaks_detection_algorithm:
            outbreaks = identify_outbreaks_cached(
                network=IG,
                outbreaks_alg=self.config.outbreaks_detection_algorithm,
            )
            outbreaks = [subgraph
                         for subgraph in create_subgraphs_based_on_outbreaks(
                    G=IG, outbreaks=outbreaks
                )
                         ]
        return outbreaks

    def _get_global_scores(self,
                           outbreaks_evaluation: List[Dict[NODE_TYPE, float]]):
        global_scores = {}
        for outbreak_evaluation in outbreaks_evaluation:
            for node, evaluation in outbreak_evaluation.items():
                global_scores[node] = evaluation
        return global_scores

    def _evaluate_outbreaks(self, outbreaks: List[Graph]) -> List[
        Dict[NODE_TYPE, float]]:
        scores = []
        for outbreak in outbreaks:
            scores.append(evaluate_nodes_cached(
                network=outbreak,
                evaluation_alg=self.config.node_evaluation_algorithm,
            ))
        return scores

    def _select_sources(self,
                        outbreaks_evaluation: List[Dict[NODE_TYPE, float]]):
        sources = []
        for outbreak_evaluation in outbreaks_evaluation:
            if self.config.selection_threshold is None:
                sources.append(
                    max(outbreak_evaluation, key=outbreak_evaluation.get))
            else:
                outbreaks_evaluation_normalized = normalize_dict_values(
                    outbreak_evaluation)

                sources.extend(
                    [node for node, evaluation in
                     outbreaks_evaluation_normalized.items()
                     if evaluation >= self.config.selection_threshold]
                )
        return sources

    def detect_sources(self, IG: Graph, G: Graph) -> SourceDetectionResult:
        IG = self._reconstruct_propagation(IG, G)
        outbreaks = self._detect_outbreaks(IG)
        scores_in_outbreaks = self._evaluate_outbreaks(outbreaks)
        global_scores = self._get_global_scores(scores_in_outbreaks)
        detected_sources = self._select_sources(scores_in_outbreaks)
        return SourceDetectionResult(
            config=self.config,
            G=G,
            IG=IG,
            global_scores=global_scores,
            scores_in_outbreaks=scores_in_outbreaks,
            detected_sources=detected_sources,
        )

    def detect_sources_and_evaluate(self, IG: Graph, G: Graph,
                                    real_sources: List[NODE_TYPE]) -> Tuple[
        SourceDetectionResult, SourceDetectionEvaluation]:
        sd_result = self.detect_sources(IG, G)

        evaluation = compute_source_detection_evaluation(
            G=sd_result.IG,
            real_sources=real_sources,
            detected_sources=sd_result.detected_sources,
        )

        return sd_result, evaluation
