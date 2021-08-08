import networkx as nx
from typing import Dict
from .BokehChart import BokehChart


class EigenvectorCentralityChart(BokehChart):
    _title = 'Eigenvector Centrality'
    _attribute = 'eigenvector_centrality'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('eigenvector centrality', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return dict(nx.eigenvector_centrality(graph))
