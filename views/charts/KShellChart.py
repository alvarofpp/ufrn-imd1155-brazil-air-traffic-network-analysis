import networkx as nx
from typing import Dict
from .CentralityChart import CentralityChart


class KShellChart(CentralityChart):
    _title = 'K-shell'
    _attribute = 'k_shell'

    def __init__(self, **kwargs):
        kwargs.update({
            'tooltips': [
                ('k-shell', '@' + self._attribute)
            ],
        })
        super().__init__(**kwargs)

    def manipulate_data(self, graph) -> Dict:
        return {node: degree for node, degree in nx.core_number(graph).items()}
