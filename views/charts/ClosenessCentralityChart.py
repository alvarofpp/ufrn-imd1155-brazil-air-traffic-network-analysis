import networkx as nx
from typing import Dict
from .CentralityChart import CentralityChart


class ClosenessCentralityChart(CentralityChart):
    _title = 'Closeness Centrality'
    _attribute = 'closeness_centrality'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('closeness centrality', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return dict(nx.closeness_centrality(graph))
