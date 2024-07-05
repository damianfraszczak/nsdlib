import networkx as nx

import nsdlib as nsd
from nsdlib import NodeEvaluationAlgorithm, PropagationReconstructionAlgorithm

G = nx.karate_club_graph()
IG = G.copy()
IG.remove_nodes_from([10, 15, 20, 33])
real_sources = [0, 8]

EIG = nsd.reconstruct_propagation(G, IG, PropagationReconstructionAlgorithm.SBRP)

outbreaks = nsd.identify_outbreaks(EIG, nsd.OutbreaksDetectionAlgorithm.LEIDEN)
outbreaks_G = nsd.create_subgraphs_based_on_outbreaks(EIG, outbreaks)
detected_sources = []
for outbreak in outbreaks_G:
    nodes_evaluation = nsd.evaluate_nodes(
        outbreak, NodeEvaluationAlgorithm.CENTRALITY_AVERAGE_DISTANCE
    )
    outbreak_detected_source = max(nodes_evaluation, key=nodes_evaluation.get)
    print(f"Outbreak: {outbreak}, Detected Source: {outbreak_detected_source}")
    detected_sources.append(outbreak_detected_source)

evaluation = nsd.compute_source_detection_evaluation(
    G=EIG,
    real_sources=real_sources,
    detected_sources=detected_sources,
)
print(evaluation)
