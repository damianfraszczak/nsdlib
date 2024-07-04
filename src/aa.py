import networkx as nx

from nsdlib.common.models import SourceDetectionConfig
from nsdlib.source_detection import SourceDetector
from nsdlib.taxonomies import NodeEvaluationAlgorithm

G = nx.karate_club_graph()

config = SourceDetectionConfig(
    node_evaluation_algorithm=NodeEvaluationAlgorithm.NETSLEUTH,
)

source_detector = SourceDetector(config)

result, evaluation = source_detector.detect_sources_and_evaluate(
    G=G, IG=G, real_sources=[0, 33]
)
print(result.global_scores)
