import networkx as nx
import netcenlib as ncl
from nsdlib.common.models import SourceDetectionConfig
from nsdlib.source_detection import SourceDetector
from nsdlib.taxonomies import OutbreaksDetectionAlgorithm

# Create a graph
G = nx.karate_club_graph()

config = SourceDetectionConfig(
    selection_threshold=None,
    outbreaks_detection_algorithm=OutbreaksDetectionAlgorithm.LEIDEN,
)

source_detector = SourceDetector(config)

result, evaluation = source_detector.detect_sources_and_evaluate(G=G,
                                        IG=G, real_sources=[0,33])
print(result.global_scores)
print(ncl.degree_centrality(G))

print(evaluation)
