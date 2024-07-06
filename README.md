# NSDlib

NSDlib (Network source detection library) is a comprehensive library designed for detecting sources of propagation in networks. This library offers a variety of algorithms that help researchers and developers analyze and identify the origins of information (epidemic etc.) spread within networks.

## Overview

NSDLib is a complex library designed for easy integration into existing projects. It aims to be a comprehensive repository
of source detection methods, outbreak detection techniques, and propagation graph reconstruction tools. Researchers worldwide are encouraged to contribute and utilize this library,
facilitating the development of new techniques to combat misinformation and improve propagation analysis.
Each  year, new techniques are introduced through scientific papers, often with only pseudo-code descriptions, making it
difficult for researchers to evaluate and compare them with existing methods. NSDlib tries to bridge this gap and enhance researchers to put their implementations here.

## Code structure

All custom implementations are provided under `nsdlib/algorithms` package. Each method is implemented in a separate file, named after the method itself and in appropriate package according to its intended purpose e.g. reconstruction algorithm should be placed in `reconstruction` package. . Correspondingly, each file contains a function, named identically to the file, which does appropriate logic.  Ultimately, every custom implementation is made available through the `nsdlib/algorithms` package.
## Implemented features:

### Node evaluation algorithms
- [algebraic_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.algebraic_centrality.html)
- [average_distance_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.average_distance_centrality.html)
- [barycenter_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.barycenter_centrality.html)
- [betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.betweenness_centrality.html)
- [bottle_neck_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.bottle_neck_centrality.html)
- [centroid_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.centroid_centrality.html)
- [closeness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.closeness_centrality.html)
- [cluster_rank_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.cluster_rank_centrality.html)
- [communicability_betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.communicability_betweenness_centrality.html)
- [coreness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.coreness_centrality.html)
- [current_flow_betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.current_flow_betweenness_centrality.html)
- [current_flow_closeness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.current_flow_closeness_centrality.html)
- [decay_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.decay_centrality.html)
- [degree_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.degree_centrality.html)
- [diffusion_degree_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.diffusion_degree_centrality.html)
- [dynamic_age](https://nsdlib.readthedocs.io/en/latest/source/nsdlib.algorithms.evaluation.dynamic_age.html#nsdlib.algorithms.evaluation.dynamic_age.dynamic_age)
- [eccentricity_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.eccentricity_centrality.html)
- [eigenvector_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.eigenvector_centrality.html)
- [entropy_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.entropy_centrality.html)
- [geodestic_k_path_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.geodestic_k_path_centrality.html)
- [group_betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.group_betweenness_centrality.html)
- [group_closeness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.group_closeness_centrality.html)
- [group_degree_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.group_degree_centrality.html)
- [harmonic_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.harmonic_centrality.html)
- [heatmap_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.heatmap_centrality.html)
- [hubbell_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.hubbell_centrality.html)
- [jordan_center](https://nsdlib.readthedocs.io/en/latest/source/nsdlib.algorithms.evaluation.jordan_center.html)
- [katz_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.katz_centrality.html)
- [laplacian_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.laplacian_centrality.html)
- [leverage_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.leverage_centrality.html)
- [lin_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.lin_centrality.html)
- [load_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.load_centrality.html)
- [mnc_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.mnc_centrality.html)
- [net_sleuth](https://nsdlib.readthedocs.io/en/latest/source/nsdlib.algorithms.evaluation.net_sleuth.html#nsdlib.algorithms.evaluation.net_sleuth.net_sleuth)
- [pagerank_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.pagerank_centrality.html)
- [pdi_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.pdi_centrality.html)
- [percolation_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.percolation_centrality.html)
- [radiality_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.radiality_centrality.html)
- [rumor_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.rumor_centrality.html)
- [second_order_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.second_order_centrality.html)
- [semi_local_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.semi_local_centrality.html)
- [subgraph_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.subgraph_centrality.html)
- [topological_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.topological_centrality.html)
- [trophic_levels_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.trophic_levels_centrality.html)
- [algebraic_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.algebraic_centrality.html)
- [average_distance_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.average_distance_centrality.html)
- [barycenter_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.barycenter_centrality.html)
- [betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.betweenness_centrality.html)
- [bottle_neck_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.bottle_neck_centrality.html)
- [centroid_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.centroid_centrality.html)
- [closeness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.closeness_centrality.html)
- [cluster_rank_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.cluster_rank_centrality.html)
- [communicability_betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.communicability_betweenness_centrality.html)
- [coreness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.coreness_centrality.html)
- [current_flow_betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.current_flow_betweenness_centrality.html)
- [current_flow_closeness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.current_flow_closeness_centrality.html)
- [decay_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.decay_centrality.html)
- [degree_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.degree_centrality.html)
- [diffusion_degree_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.diffusion_degree_centrality.html)
- [eccentricity_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.eccentricity_centrality.html)
- [eigenvector_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.eigenvector_centrality.html)
- [entropy_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.entropy_centrality.html)
- [geodestic_k_path_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.geodestic_k_path_centrality.html)
- [group_betweenness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.group_betweenness_centrality.html)
- [group_closeness_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.group_closeness_centrality.html)
- [group_degree_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.group_degree_centrality.html)
- [harmonic_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.harmonic_centrality.html)
- [heatmap_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.heatmap_centrality.html)
- [hubbell_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.hubbell_centrality.html)
- [katz_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.katz_centrality.html)
- [laplacian_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.laplacian_centrality.html)
- [leverage_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.leverage_centrality.html)
- [lin_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.lin_centrality.html)
- [load_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.load_centrality.html)
- [mnc_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.mnc_centrality.html)
- [pagerank_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.pagerank_centrality.html)
- [pdi_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.pdi_centrality.html)
- [percolation_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.percolation_centrality.html)
- [radiality_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.radiality_centrality.html)
- [rumor_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.rumor_centrality.html)
- [second_order_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.second_order_centrality.html)
- [semi_local_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.semi_local_centrality.html)
- [subgraph_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.subgraph_centrality.html)
- [topological_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.topological_centrality.html)
- [trophic_levels_centrality](https://netcenlib.readthedocs.io/en/latest/source/netcenlib.algorithms.trophic_levels_centrality.html)

### Outbreak detection algorithms
- [CPM_Bipartite](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.CPM_Bipartite.html)
- [agdl](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.agdl.html)
- [angel](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.angel.html)
- [aslpaw](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.aslpaw.html)
- [async_fluid](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.async_fluid.html)
- [bayan](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.bayan.html)
- [belief](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.belief.html)
- [bimlpa](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.bimlpa.html)
- [coach](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.coach.html)
- [condor](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.condor.html)
- [conga](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.conga.html)
- [congo](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.congo.html)
- [core_expansion](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.core_expansion.html)
- [cpm](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.cpm.html)
- [dcs](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.dcs.html)
- [demon](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.demon.html)
- [der](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.der.html)
- [dpclus](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.dpclus.html)
- [ebgc](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.ebgc.html)
- [ego_networks](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.ego_networks.html)
- [eigenvector](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.eigenvector.html)
- [em](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.em.html)
- [endntm](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.endntm.html)
- [eva](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.eva.html)
- [frc_fgsn](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.frc_fgsn.html)
- [ga](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.ga.html)
- [gdmp2](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.gdmp2.html)
- [girvan_newman](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.girvan_newman.html)
- [graph_entropy](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.graph_entropy.html)
- [greedy_modularity](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.greedy_modularity.html)
- [head_tail](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.head_tail.html)
- [hierarchical_link_community](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.hierarchical_link_community.html)
- [ilouvain](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.ilouvain.html)
- [infomap](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.infomap.html)
- [infomap_bipartite](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.infomap_bipartite.html)
- [ipca](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.ipca.html)
- [kclique](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.kclique.html)
- [kcut](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.kcut.html)
- [label_propagation](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.label_propagation.html)
- [lais2](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lais2.html)
- [leiden](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.leiden.html)
- [lemon](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lemon.html)
- [lfm](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lfm.html)
- [louvain](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.louvain.html)
- [lpam](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lpam.html)
- [lpanni](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lpanni.html)
- [lswl](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lswl.html)
- [lswl_plus](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.lswl_plus.html)
- [markov_clustering](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.markov_clustering.html)
- [mcode](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.mcode.html)
- [mod_m](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.mod_m.html)
- [mod_r](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.mod_r.html)
- [multicom](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.multicom.html)
- [node_perception](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.node_perception.html)
- [overlapping_seed_set_expansion](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.overlapping_seed_set_expansion.html)
- [paris](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.paris.html)
- [percomvc](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.percomvc.html)
- [principled_clustering](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.principled_clustering.html)
- [pycombo](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.pycombo.html)
- [r_spectral_clustering](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.r_spectral_clustering.html)
- [rb_pots](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.rb_pots.html)
- [rber_pots](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.rber_pots.html)
- [ricci_community](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.ricci_community.html)
- [sbm_dl](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.sbm_dl.html)
- [sbm_dl_nested](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.sbm_dl_nested.html)
- [scan](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.scan.html)
- [siblinarity_antichain](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.siblinarity_antichain.html)
- [significance_communities](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.significance_communities.html)
- [slpa](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.slpa.html)
- [spectral](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.spectral.html)
- [spinglass](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.spinglass.html)
- [surprise_communities](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.surprise_communities.html)
- [threshold_clustering](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.threshold_clustering.html)
- [tiles](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.tiles.html)
- [umstmo](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.umstmo.html)
- [wCommunity](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.wCommunity.html)
- [walkscan](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.walkscan.html)
- [walktrap](https://cdlib.readthedocs.io/en/latest/reference/generated/cdlib.algorithms.walktrap.html)

### Graph reconstruction algorithms
- [SbRP](https://nsdlib.readthedocs.io/en/latest/source/nsdlib.algorithms.reconstruction.sbrp.html#nsdlib.algorithms.reconstruction.sbrp.sbrp)

### Ensemble methods
This package provides implementation for easily combining multiple source detection methods into one ensemble method. Use 'EnsembleSourceDetector' with config objects as arguments to create an ensemble method.

## How to use
Library can be installed using pip:

```bash
pip install nsdlib
```

## Code usage

Provided algorithms can be executed in the following ways:

- by utilizing 'SourceDetector' class and configuring it with 'SourceDetectionConfig' object. This approach allows for seamless source detection and result evaluation.

```python
import networkx as nx

from nsdlib.common.models import SourceDetectionConfig
from nsdlib.source_detection import SourceDetector
from nsdlib.taxonomies import NodeEvaluationAlgorithm


G = nx.karate_club_graph()

config = SourceDetectionConfig(
    node_evaluation_algorithm=NodeEvaluationAlgorithm.NETSLEUTH,
)

source_detector = SourceDetector(config)

result, evaluation = source_detector.detect_sources_and_evaluate(G=G,
                                        IG=G, real_sources=[0,33])
print(evaluation)


```

For performing ensemble source detection, use 'EnsembleSourceDetector' class and configure it with 'EnsembleSourceDetectionConfig' object. This approach allows for seamless source detection and result evaluation.

```python

import networkx as nx

from nsdlib.common.models import SourceDetectionConfig, \
    EnsembleSourceDetectionConfig
from nsdlib.source_detection import SourceDetector, EnsembleSourceDetector
from nsdlib.taxonomies import NodeEvaluationAlgorithm, EnsembleVotingType

G = nx.karate_club_graph()

config_netsleuth = SourceDetectionConfig(
    node_evaluation_algorithm=NodeEvaluationAlgorithm.NETSLEUTH,
)

config_degree = SourceDetectionConfig(
    node_evaluation_algorithm=NodeEvaluationAlgorithm.CENTRALITY_DEGREE,
)

ensemble_config = EnsembleSourceDetectionConfig(
    detection_configs=[config_netsleuth, config_degree],
    voting_type=EnsembleVotingType.HARD,
    classifier_weights=[0.5, 0.5],
)

source_detector = EnsembleSourceDetector(ensemble_config)

result, evaluation = source_detector.detect_sources_and_evaluate(G=G,
                                        IG=G, real_sources=[0,33])
print(evaluation)


```

- by importing and using specific method, each method has appropriate prefix to understand what is the purpose of it:

```python
import networkx as nx

import nsdlib as nsd

G = nx.karate_club_graph()
IG = G.copy()
IG.remove_nodes_from([10,15,20,33])
real_sources = [0,8]

EIG = nsd.reconstruction_sbrp(G, IG)

outbreaks = nsd.outbreaks_leiden(EIG)

detected_sources = []
for outbreak in outbreaks.communities:
    outbreak_G = G.subgraph(outbreak)
    nodes_evaluation = nsd.evaluation_jordan_center(outbreak_G)
    outbreak_detected_source = max(nodes_evaluation, key=nodes_evaluation.get)
    print(f"Outbreak: {outbreak}, Detected Source: {outbreak_detected_source}")
    detected_sources.append(outbreak_detected_source)

evaluation = nsd.compute_source_detection_evaluation(
    G=EIG,
    real_sources=real_sources,
    detected_sources=detected_sources,
)
print(evaluation)

```

This method allows you to directly specify the process of source detection, making it easy to do any modifications to standardlogic.

- by using appropriate enum and method for computing desired method:
```python

import networkx as nx

import nsdlib as nsd
from nsdlib import PropagationReconstructionAlgorithm, NodeEvaluationAlgorithm, OutbreaksDetectionAlgorithm

G = nx.karate_club_graph()
IG = G.copy()
IG.remove_nodes_from([10,15,20,33])
real_sources = [0,8]

EIG = nsd.reconstruct_propagation(G, IG, PropagationReconstructionAlgorithm.SBRP)

outbreaks = nsd.identify_outbreaks(EIG, OutbreaksDetectionAlgorithm.LEIDEN)
outbreaks_G = nsd.create_subgraphs_based_on_outbreaks(EIG, outbreaks)
detected_sources = []
for outbreak in outbreaks_G:
    nodes_evaluation = nsd.evaluate_nodes(outbreak, NodeEvaluationAlgorithm.CENTRALITY_AVERAGE_DISTANCE)
    outbreak_detected_source = max(nodes_evaluation, key=nodes_evaluation.get)
    print(f"Outbreak: {outbreak}, Detected Source: {outbreak_detected_source}")
    detected_sources.append(outbreak_detected_source)

evaluation = nsd.compute_source_detection_evaluation(
    G=EIG,
    real_sources=real_sources,
    detected_sources=detected_sources,
)
print(evaluation)
```

This approach is more flexible and allows for the computation of multiple techniques at once or when iterating over multiple methods making it easy to perform analysis of selected set of techniques.


For more examples and details, please refer to the [official documentation](https://nsdlib.readthedocs.io/en/latest/index.html).

## Contributing

For contributing, refer to its [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.
We are a welcoming community... just follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak
