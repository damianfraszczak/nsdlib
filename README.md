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
- [Algebraic](https://www.centiserver.org/centrality/Algebraic_Centrality/)
- [Average Distance](https://www.centiserver.org/centrality/Average_Distance/)
- [Barycenter](https://www.centiserver.org/centrality/Barycenter_Centrality/)
- [Betweenness](https://www.centiserver.org/centrality/Shortest-Paths_Betweenness_Centrality/)
- [BottleNeck]( https://www.centiserver.org/centrality/BottleNeck/)
- [Centroid](https://www.centiserver.org/centrality/Centroid_value/)
- [Closeness](https://www.centiserver.org/centrality/Closeness_Centrality/)
- [ClusterRank](https://www.centiserver.org/centrality/ClusterRank/)
- [Communicability Betweenness](https://www.centiserver.org/centrality/Communicability_Betweenness_Centrality/)
- [Coreness](https://www.centiserver.org/centrality/Coreness_Centrality/)
- [Current Flow Betweenness](https://www.centiserver.org/centrality/Current-Flow_Betweenness_Centrality/)
- [Current Flow Closeness](https://www.centiserver.org/centrality/Current-Flow_Closeness_Centrality/)
- [Decay](https://www.centiserver.org/centrality/Decay_Centrality/)
- [Degree](https://www.centiserver.org/centrality/Degree_Centrality/)
- [Diffusion degree](https://www.centiserver.org/centrality/Diffusion_Degree/)
- [Eigenvector](https://www.centiserver.org/centrality/Eigenvector_Centrality/)
- [Entropy](https://www.centiserver.org/centrality/Entropy_Centrality/)
- [Geodestic k path](https://www.centiserver.org/centrality/Geodesic_K-Path_Centrality/)
- [Group Betweenness Centrality](https://www.centiserver.org/centrality/Group_Betweenness_Centrality/)
- [Group Closeness](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.group_closeness_centrality.html)
- [Group Degree](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.group_degree_centrality.html)
- [Harmonic](https://www.centiserver.org/centrality/Harmonic_Centrality/)
- [Heatmap](https://www.centiserver.org/centrality/Heatmap_Centrality/)
- [Katz](https://www.centiserver.org/centrality/Katz_Centrality/)
- [Hubbell](https://www.centiserver.org/centrality/Hubbell_Centrality/)
- [Laplacian](https://www.centiserver.org/centrality/Laplacian_Centrality/)
- [Leverage](https://www.centiserver.org/centrality/Leverage_Centrality/)
- [Lin](https://www.centiserver.org/centrality/Lin_Centrality/)
- [Load](https://www.centiserver.org/centrality/Load_Centrality/)
- [Mnc](https://www.centiserver.org/centrality/MNC_Maximum_Neighborhood_Component/)
- [Pagerank](https://www.centiserver.org/centrality/PageRank/)
- [Pdi](https://www.centiserver.org/centrality/Pairwise_Disconnectivity_Index/)
- [Percolation](https://www.centiserver.org/centrality/Percolation_Centrality/)
- [Radiality](https://www.centiserver.org/centrality/Radiality_Centrality/)
- [Rumor](https://www.centiserver.org/centrality/Rumor_Centrality/)
- [Second Order](https://www.centiserver.org/centrality/Second_Order_Centrality/)
- [Semi Local](https://www.centiserver.org/centrality/Semi_Local_Centrality/)
- [Subgraph](https://www.centiserver.org/centrality/Subgraph_Centrality/)
- [Topological](https://www.centiserver.org/centrality/Topological_Coefficient/)
- [Trophic Levels](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.centrality.trophic_levels.html)

### Outbreak detection algorithms
- test

### Graph reconstruction algorithms
- SbRP

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

- by importing and using specific method:

```python
from typing import Any
import networkx as nx
from networkx import Graph

from nsdlib.source_detection import compute_centrality
from nsdlib.taxonomies import Centrality

g: Graph = nx.karate_club_graph()
centrality_centroid: dict[Any, float] = compute_centrality(g, Centrality.CENTROID)
```

This method allows you not to directly specify centrality, making it easy to compute different centralises in a loop.

For more examples and details, please refer to the [official documentation](https://nsdlib.readthedocs.io/en/latest/index.html).

## Contributing

For contributing, refer to its [CONTRIBUTING.md](.github/CONTRIBUTING.md) file.
We are a welcoming community... just follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md).

## Maintainers

Project maintainers are:

- Damian Frąszczak
- Edyta Frąszczak
