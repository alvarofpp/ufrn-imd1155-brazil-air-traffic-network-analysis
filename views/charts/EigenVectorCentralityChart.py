import networkx as nx
from typing import Dict
from .CentralityChart import CentralityChart


class EigenVectorCentralityChart(CentralityChart):
    _title = 'Eigen Vector Centrality'
    _attribute = 'eigen_vector_centrality'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('eigen vector centrality', '@' + self._attribute)
            ],
            'palette': 'Viridis256',
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return dict(nx.eigenvector_centrality(graph))
