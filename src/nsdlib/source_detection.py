"""Centrality measures for networks."""

from nsdlib.common.models import SourceDetectionConfig


class SourceDetector:
    def __init__(self, config: SourceDetectionConfig):
        self.config = config

    def estimate_sources(self):
        pass
