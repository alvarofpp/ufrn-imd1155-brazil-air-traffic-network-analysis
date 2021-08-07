import networkx as nx
from typing import Dict
from .CentralityChart import CentralityChart


class BetweennessCentralityChart(CentralityChart):
    _title = 'Betweenness Centrality'
    _attribute = 'betweenness_centrality'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('betweenness centrality', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return dict(nx.betweenness_centrality(graph))
