from enum import Enum


class NodeEvaluationAlgorithm(Enum):
    """A list of node evaluation algorithms."""

    # NetCenLib algorithms
    CENTRALITY_ALGEBRAIC = "algebraic_centrality"
    CENTRALITY_AVERAGE_DISTANCE = "average_distance_centrality"
    CENTRALITY_BARYCENTER = "barycenter_centrality"
    CENTRALITY_BETWEENNESS = "betweenness_centrality"
    CENTRALITY_BOTTLE_NECK = "bottle_neck_centrality"
    CENTRALITY_CENTROID = "centroid_centrality"
    CENTRALITY_CLOSENESS = "closeness_centrality"
    CENTRALITY_CLUSTER_RANK = "cluster_rank_centrality"
    CENTRALITY_COMMUNICABILITY_BETWEENNESS = "communicability_betweenness_centrality"
    CENTRALITY_CORENESS = "coreness_centrality"
    CENTRALITY_CURRENT_FLOW_BETWEENNESS = "current_flow_betweenness_centrality"
    CENTRALITY_CURRENT_FLOW_CLOSENESS = "current_flow_closeness_centrality"
    CENTRALITY_DECAY = "decay_centrality"
    CENTRALITY_DEGREE = "degree_centrality"
    CENTRALITY_DIFFUSION_DEGREE = "diffusion_degree_centrality"
    CENTRALITY_EIGENVECTOR = "eigenvector_centrality"
    CENTRALITY_ENTROPY = "entropy_centrality"
    CENTRALITY_GEODESTIC_K_PATH = "geodestic_k_path_centrality"
    CENTRALITY_GROUP_BETWEENNESS = "group_betweenness_centrality"
    CENTRALITY_GROUP_CLOSENESS = "group_closeness_centrality"
    CENTRALITY_GROUP_DEGREE = "group_degree_centrality"
    CENTRALITY_HARMONIC = "harmonic_centrality"
    CENTRALITY_HEATMAP = "heatmap_centrality"
    CENTRALITY_HUBBELL = "hubbell_centrality"
    CENTRALITY_KATZ = "katz_centrality"
    CENTRALITY_LAPLACIAN = "laplacian_centrality"
    CENTRALITY_LEVERAGE = "leverage_centrality"
    CENTRALITY_LIN = "lin_centrality"
    CENTRALITY_LOAD = "load_centrality"
    CENTRALITY_MNC = "mnc_centrality"
    CENTRALITY_PAGERANK = "pagerank_centrality"
    CENTRALITY_PDI = "pdi_centrality"
    CENTRALITY_PERCOLATION = "percolation_centrality"
    CENTRALITY_RADIALITY = "radiality_centrality"
    CENTRALITY_RUMOR = "rumor_centrality"
    CENTRALITY_SECOND_ORDER = "second_order_centrality"
    CENTRALITY_SEMI_LOCAL = "semi_local_centrality"
    CENTRALITY_SUBGRAPH = "subgraph_centrality"
    CENTRALITY_TOPOLOGICAL = "topological_centrality"
    CENTRALITY_TROPHIC_LEVELS = "trophic_levels_centrality"

    # NSDLib algorithms
    DYNAMIC_AGE = "dynamic_age"
    JORDAN_CENTER = "jordan_center"
    NETSLEUTH = "net_sleuth"


class PropagationReconstructionAlgorithm(Enum):
    SBRP = "sbrp"


class OutbreaksDetectionAlgorithm(Enum):
    CPM_BIPARTITE = "CPM_Bipartite"
    AGDL = "agdl"
    ANGEL = "angel"
    ASLPAW = "aslpaw"
    ASYNC_FLUID = "async_fluid"
    ATTRIBUTE_CLUSTERING = "attribute_clustering"
    BAYAN = "bayan"
    BELIEF = "belief"
    BIMLPA = "bimlpa"
    BIPARTITE_CLUSTERING = "bipartite_clustering"
    COACH = "coach"
    CONDOR = "condor"
    CONGA = "conga"
    CONGO = "congo"
    CORE_EXPANSION = "core_expansion"
    CPM = "cpm"
    CRISP_PARTITION = "crisp_partition"
    DCS = "dcs"
    DEMON = "demon"
    DER = "der"
    DPCLUS = "dpclus"
    EBGC = "ebgc"
    EDGE_CLUSTERING = "edge_clustering"
    EGO_NETWORKS = "ego_networks"
    EIGENVECTOR = "eigenvector"
    EM = "em"
    ENDNTM = "endntm"
    EVA = "eva"
    FRC_FGSN = "frc_fgsn"
    GA = "ga"
    GDMP2 = "gdmp2"
    GIRVAN_NEWMAN = "girvan_newman"
    GRAPH_ENTROPY = "graph_entropy"
    GREEDY_MODULARITY = "greedy_modularity"
    HEAD_TAIL = "head_tail"
    HIERARCHICAL_LINK_COMMUNITY = "hierarchical_link_community"
    ILOUVAIN = "ilouvain"
    INFOMAP = "infomap"
    INFOMAP_BIPARTITE = "infomap_bipartite"
    INTERNAL = "internal"
    INTERNAL_DCD = "internal_dcd"
    IPCA = "ipca"
    KCLIQUE = "kclique"
    KCUT = "kcut"
    LABEL_PROPAGATION = "label_propagation"
    LAIS2 = "lais2"
    LEIDEN = "leiden"
    LEMON = "lemon"
    LFM = "lfm"
    LOUVAIN = "louvain"
    LPAM = "lpam"
    LPANNI = "lpanni"
    LSWL = "lswl"
    LSWL_PLUS = "lswl_plus"
    MARKOV_CLUSTERING = "markov_clustering"
    MCODE = "mcode"
    MOD_M = "mod_m"
    MOD_R = "mod_r"
    MULTICOM = "multicom"
    NODE_PERCEPTION = "node_perception"
    OVERLAPPING_PARTITION = "overlapping_partition"
    OVERLAPPING_SEED_SET_EXPANSION = "overlapping_seed_set_expansion"
    PARIS = "paris"
    PERCOMVC = "percomvc"
    PRINCIPLED_CLUSTERING = "principled_clustering"
    PYCOMBO = "pycombo"
    R_SPECTRAL_CLUSTERING = "r_spectral_clustering"
    RB_POTS = "rb_pots"
    RBER_POTS = "rber_pots"
    RICCI_COMMUNITY = "ricci_community"
    SBM_DL = "sbm_dl"
    SBM_DL_NESTED = "sbm_dl_nested"
    SCAN = "scan"
    SIBLINARITY_ANTICHAIN = "siblinarity_antichain"
    SIGNIFICANCE_COMMUNITIES = "significance_communities"
    SLPA = "slpa"
    SPECTRAL = "spectral"
    SPINGLASS = "spinglass"
    SURPRISE_COMMUNITIES = "surprise_communities"
    TEMPORAL_PARTITION = "temporal_partition"
    THRESHOLD_CLUSTERING = "threshold_clustering"
    TILES = "tiles"
    UMSTMO = "umstmo"
    WCOMMUNITY = "wCommunity"
    WALKSCAN = "walkscan"
    WALKTRAP = "walktrap"
