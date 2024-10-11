"""Source detection algorithm."""

from typing import Dict, List, Tuple

from networkx import Graph

from nsdlib.algorithms.algorithms_utils import (
    compute_source_detection_evaluation,
    evaluate_nodes_cached,
    identify_outbreaks_cached,
    reconstruct_propagation_cached,
)
from nsdlib.common.models import (
    NODE_TYPE,
    EnsembleSourceDetectionConfig,
    EnsembleSourceDetectionResult,
    SourceDetectionConfig,
    SourceDetectionEvaluation,
    SourceDetectionResult,
)
from nsdlib.common.nx_utils import create_subgraphs_based_on_outbreaks
from nsdlib.commons import normalize_dict_values
from nsdlib.taxonomies import EnsembleVotingType


class SourceDetector:
    """Source detection generic algorithm."""

    def __init__(self, config: SourceDetectionConfig):
        self.config = config

    def detect_sources(self, IG: Graph, G: Graph) -> SourceDetectionResult:
        IG = self._reconstruct_propagation(IG, G)
        outbreaks = self._detect_outbreaks(IG)
        scores_in_outbreaks = self._evaluate_outbreaks(outbreaks)
        global_scores = self._get_global_scores(scores_in_outbreaks)
        detected_sources = self._select_sources(IG, scores_in_outbreaks)
        return SourceDetectionResult(
            config=self.config,
            G=G,
            IG=IG,
            global_scores=global_scores,
            scores_in_outbreaks=scores_in_outbreaks,
            detected_sources=detected_sources,
        )

    def detect_sources_and_evaluate(
        self, IG: Graph, G: Graph, real_sources: List[NODE_TYPE]
    ) -> Tuple[SourceDetectionResult, SourceDetectionEvaluation]:
        sd_result = self.detect_sources(IG, G)

        evaluation = compute_source_detection_evaluation(
            G=sd_result.IG,
            real_sources=real_sources,
            detected_sources=sd_result.detected_sources,
        )

        return sd_result, evaluation

    def _reconstruct_propagation(self, IG, G):
        if self.config.propagation_reconstruction_algorithm:
            IG = reconstruct_propagation_cached(
                G=G,
                IG=IG,
                reconstruction_alg=self.config.propagation_reconstruction_algorithm,
            )
        return IG

    def _detect_outbreaks(self, IG):
        outbreaks = [IG]

        if self.config.outbreaks_detection_algorithm:
            outbreaks = identify_outbreaks_cached(
                network=IG,
                outbreaks_alg=self.config.outbreaks_detection_algorithm,
            )
            outbreaks = [
                subgraph
                for subgraph in create_subgraphs_based_on_outbreaks(
                    G=IG, outbreaks=outbreaks
                )
            ]
        return outbreaks

    def _get_global_scores(self, outbreaks_evaluation: List[Dict[NODE_TYPE, float]]):
        global_scores = {}
        for outbreak_evaluation in outbreaks_evaluation:
            for node, evaluation in outbreak_evaluation.items():
                global_scores[node] = evaluation
        return global_scores

    def _evaluate_outbreaks(
        self, outbreaks: List[Graph]
    ) -> List[Dict[NODE_TYPE, float]]:
        scores = []
        for outbreak in outbreaks:
            scores.append(
                evaluate_nodes_cached(
                    network=outbreak,
                    evaluation_alg=self.config.node_evaluation_algorithm,
                )
            )
        return scores

    def _select_sources(
        self, IG: Graph, outbreaks_evaluation: List[Dict[NODE_TYPE, float]]
    ):
        sources = []
        for outbreak_evaluation in outbreaks_evaluation:
            if self.config.selection_algorithm.selection_method:
                max_score = max(outbreak_evaluation.values())
                nodes_with_higher_score = [
                    node
                    for node, score in outbreak_evaluation.items()
                    if score == max_score
                ]
                if len(nodes_with_higher_score) == 1:
                    sources.append(nodes_with_higher_score[0])
                else:
                    outbreak_nodes = list(outbreak_evaluation.keys())
                    subgraph = IG.subgraph(outbreak_nodes)
                    selection_evaluation = evaluate_nodes_cached(
                        network=subgraph,
                        evaluation_alg=self.config.selection_algorithm.selection_method,
                    )
                    filtered_second_evaluation = {
                        node: selection_evaluation[node]
                        for node in nodes_with_higher_score
                    }
                    max_second_score = max(filtered_second_evaluation.values())
                    sources.extend(
                        [
                            node
                            for node, score in filtered_second_evaluation.items()
                            if score == max_second_score
                        ]
                    )

            elif self.config.selection_algorithm.selection_threshold is None:
                sources.append(max(outbreak_evaluation, key=outbreak_evaluation.get))
            else:
                outbreaks_evaluation_normalized = normalize_dict_values(
                    outbreak_evaluation
                )

                sources.extend(
                    [
                        node
                        for node, evaluation in outbreaks_evaluation_normalized.items()
                        if evaluation
                        >= self.config.selection_algorithm.selection_threshold
                    ]
                )

        return sources


class EnsembleSourceDetector:
    """Ensemble source detection algorithm."""

    def __init__(self, config: EnsembleSourceDetectionConfig):
        self.config = config

    def detect_sources(self, IG: Graph, G: Graph) -> List[SourceDetectionResult]:
        return [
            SourceDetector(config).detect_sources(IG, G)
            for config in self.config.detection_configs
        ]

    def detect_sources_and_evaluate(
        self, IG: Graph, G: Graph, real_sources: List[NODE_TYPE]
    ) -> Tuple[EnsembleSourceDetectionResult, SourceDetectionEvaluation]:
        sd_results = self.detect_sources(IG, G)
        ensemble_result = self._combine_results(sd_results)

        evaluation = compute_source_detection_evaluation(
            G=ensemble_result.IG,
            real_sources=real_sources,
            detected_sources=ensemble_result.detected_sources,
        )

        return ensemble_result, evaluation

    def _combine_results(
        self, results: List[SourceDetectionResult]
    ) -> EnsembleSourceDetectionResult:
        if self.config.voting_type == EnsembleVotingType.SOFT:
            return self._soft_voting(results)
        else:
            return self._hard_voting(results)

    def _soft_voting(
        self, results: List[SourceDetectionResult]
    ) -> EnsembleSourceDetectionResult:
        combined_scores = {}
        for result in results:
            for node, score in result.global_scores.items():
                if node not in combined_scores:
                    combined_scores[node] = 0
                combined_scores[node] += score * (
                    self.config.classifier_weights[results.index(result)]
                    if self.config.classifier_weights
                    else 1
                )

        total_weight = (
            sum(self.config.classifier_weights)
            if self.config.classifier_weights
            else len(results)
        )
        for node in combined_scores:
            combined_scores[node] /= total_weight

        detected_sources = [
            k
            for k, v in sorted(
                combined_scores.items(), key=lambda item: item[1], reverse=True
            )
        ]

        return EnsembleSourceDetectionResult(
            config=self.config,
            G=results[0].G,
            IG=results[0].IG,
            global_scores=combined_scores,
            ensemble_scores=results,
            detected_sources=detected_sources,
        )

    def _hard_voting(
        self, results: List[SourceDetectionResult]
    ) -> EnsembleSourceDetectionResult:
        vote_counts = {}
        for result in results:
            for node in result.detected_sources:
                if node not in vote_counts:
                    vote_counts[node] = 0
                vote_counts[node] += 1 * (
                    self.config.classifier_weights[results.index(result)]
                    if self.config.classifier_weights
                    else 1
                )

        detected_sources = [
            k
            for k, v in sorted(
                vote_counts.items(), key=lambda item: item[1], reverse=True
            )
        ]

        return EnsembleSourceDetectionResult(
            config=self.config,
            G=results[0].G,
            IG=results[0].IG,
            global_scores=vote_counts,
            ensemble_scores=results,
            detected_sources=detected_sources,
        )
