from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from networkx import Graph

from nsdlib.taxonomies import (
    EnsembleVotingType,
    NodeEvaluationAlgorithm,
    OutbreaksDetectionAlgorithm,
    PropagationReconstructionAlgorithm,
)

NODE_TYPE = Union[int, str]


@dataclass
class SelectionAlgorithm:
    selection_method: Optional[NodeEvaluationAlgorithm] = None
    selection_threshold: Optional[float] = None

    def __post_init__(self):
        if self.selection_threshold is not None and not (
            0 <= self.selection_threshold <= 1
        ):
            raise ValueError("selection_threshold must be None or between 0 and 1.")
        if self.selection_method and self.selection_threshold:
            raise ValueError(
                "selection_method and selection_threshold cannot be used together."
            )


@dataclass
class SourceDetectionConfig:
    """Source detection configuration."""

    node_evaluation_algorithm: NodeEvaluationAlgorithm = (
        NodeEvaluationAlgorithm.CENTRALITY_DEGREE
    )
    selection_algorithm: Optional[SelectionAlgorithm] = None
    outbreaks_detection_algorithm: Optional[OutbreaksDetectionAlgorithm] = None
    propagation_reconstruction_algorithm: Optional[
        PropagationReconstructionAlgorithm
    ] = None

    def __post_init__(self):
        if not self.selection_algorithm:
            self.selection_algorithm = SelectionAlgorithm()


@dataclass
class EnsembleSourceDetectionConfig:
    """Ensemble source detection configuration."""

    detection_configs: List[SourceDetectionConfig] = field(default_factory=list)
    voting_type: EnsembleVotingType = EnsembleVotingType.HARD
    classifier_weights: List[float] = field(default_factory=list)


CLASSIFICATION_REPORT_FIELDS = (
    "P",
    "N",
    "TP",
    "TN",
    "FP",
    "FN",
    "ACC",
    "F1",
    "TPR",
    "TNR",
    "PPV",
    "NPV",
    "FNR",
    "FPR",
    "FDR",
    "FOR",
    "TS",
)


@dataclass
class ClassificationMetrics:
    """Confusion matrix representation.

    It is based on https://en.wikipedia.org/wiki/Confusion_matrix.

    """

    TP: int  # true positive
    TN: int  # true negative (TN)
    FP: int  # false positive (FP)
    FN: int  # false negative (FN)
    P: int  # condition positive (P) - the number of real positive cases in
    # the data
    N: int  # condition negative (N) - the number of real negative cases in

    # the data
    @property
    def confusion_matrix(self) -> List[List[float]]:
        """Confusion matrix."""
        return [[self.TP, self.FP], [self.FN, self.TN]]

    @property
    def TPR(self):
        """Sensitivity, recall, hit rate, or true positive rate (TPR)."""
        return self.TP / self.P

    @property
    def TNR(self):
        """Specificity, selectivity or true negative rate (TNR)."""
        return self.TN / self.N

    @property
    def PPV(self):
        """Precision or positive predictive value (PPV)."""
        return self.TP / (self.TP + self.FP)

    @property
    def NPV(self):
        """Negative predictive value (NPV)."""
        return self.TN / (self.TN + self.FN)

    @property
    def FNR(self):
        """
        Miss rate or false negative rate (FNR).
        """
        return self.TN / (self.TN + self.FN)

    @property
    def FPR(self):
        """Fall-out or false positive rate (FPR)."""
        return self.FP / (self.FP + self.TN)

    @property
    def FDR(self):
        """False discovery rate (FDR)."""  # noqa
        return self.FP / (self.FP + self.TP)

    @property
    def FOR(self):
        """False omission rate (FOR)."""  # noqa
        return self.FN / (self.FN + self.TN)

    @property
    def TS(self):
        """False omission rate (FOR)."""  # noqa
        return self.TP / (self.TP + self.FN + self.FP)

    @property
    def ACC(self):
        """
        Accuracy (ACC).
        """
        return (self.TP + self.TN) / (self.P + self.N)

    @property
    def F1(self):
        """F1 score."""
        return (
            0
            if self.PPV + self.TPR == 0
            else 2 * self.PPV * self.TPR / (self.PPV + self.TPR)
        )

    def get_classification_report(self) -> Dict[str, float]:
        """Classification report as string."""
        return {attr: getattr(self, attr) for attr in CLASSIFICATION_REPORT_FIELDS}


@dataclass
class SourceDetectionEvaluation(ClassificationMetrics):
    real_sources: List[NODE_TYPE]
    detected_sources: List[NODE_TYPE]
    # shortest path length from the detected invalid source to the closest
    # real source
    error_distances: Dict[NODE_TYPE, float]

    @property
    def avg_error_distance(self) -> float:
        """Average error distance."""
        return sum(self.error_distances.values()) / len(self.error_distances)


@dataclass
class SourceDetectionResult:
    config: SourceDetectionConfig
    G: Graph
    IG: Graph
    global_scores: Dict[NODE_TYPE, float]
    scores_in_outbreaks: List[Dict[NODE_TYPE, float]]
    detected_sources: List[NODE_TYPE]


@dataclass
class EnsembleSourceDetectionResult:
    config: EnsembleSourceDetectionConfig
    G: Graph
    IG: Graph
    global_scores: Dict[NODE_TYPE, float]
    ensemble_scores: List[SourceDetectionResult]
    detected_sources: List[NODE_TYPE]
