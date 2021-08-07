import networkx as nx
from typing import Dict
from .CentralityChart import CentralityChart


class KCoreChart(CentralityChart):
    _title = 'K-score'
    _attribute = 'k_core'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('k-core', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return {node: degree for node, degree in nx.core_number(graph).items()}
