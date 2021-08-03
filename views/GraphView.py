import networkx as nx
from .View import View
import pandas as pd


class GraphView(View):
    def render(self, graphs):
        data = {}

        for year, graph in graphs.items():
            data[year] = {
                'nodes': graph.number_of_nodes(),
                'edges': graph.number_of_edges(),
                'is_connected': True if nx.is_connected(graph) else False,
                'diameter': 0,
                'radius': 0,
            }
            if nx.is_connected(graph):
                data[year]['diameter'] = nx.diameter(graph)
                data[year]['radius'] = nx.radius(graph)

        dataframe = pd.DataFrame.from_dict(data, orient='index')

        text = 'Você pode visualizar os dados sobre o{} grafo{} logo abaixo:'
        if len(graphs) > 1:
            text = text.format('s', 's')
        text = text.format('', '')
        self.render_component.markdown(text)
        self.render_component.dataframe(dataframe)
