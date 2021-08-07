import networkx as nx
from typing import Dict
from .CentralityChart import CentralityChart


class DegreeCentralityChart(CentralityChart):
    _title = 'Degree Centrality'
    _attribute = 'degree_centrality'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('degree centrality', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return dict(nx.degree_centrality(graph))
