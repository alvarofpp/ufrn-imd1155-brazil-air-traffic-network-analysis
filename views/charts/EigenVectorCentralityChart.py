import networkx as nx
from typing import Dict
from .BokehChart import BokehChart


class EigenVectorCentralityChart(BokehChart):
    _title = 'Eigen Vector Centrality'
    _attribute = 'eigen_vector_centrality'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('eigen vector centrality', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return dict(nx.eigenvector_centrality(graph))
