# Quick Start Guide for NSDLib

NSDlib (Network source detection library) is a comprehensive library designed for detecting sources of propagation in networks. This library offers a variety of algorithms that help researchers and developers analyze and identify the origins of information (epidemic etc.) spread within networks.

## Installation

Install NSDLib using pip:

```bash
pip install nsdlib
```

## Basic Usage
NSDLib offers two approaches for computing centrality measures: direct function calls and using the compute_centrality method with centrality enums.

### 'SourceDetector' class
by utilizing 'SourceDetector' class and configuring it with 'SourceDetectionConfig' object. This approach allows for seamless source detection and result evaluation.

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
### direct method calls
by importing and using specific method, each method has appropriate prefix to understand what is the purpose of it:

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

### Enum usage
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


If you would like to test ``NSDLib`` functionalities without installing it on your machine consider using the preconfigured [Jupyter notebook](nsdlib.ipynb).
