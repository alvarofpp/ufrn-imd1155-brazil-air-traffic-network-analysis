import pandas as pd
import networkx as nx
from typing import Dict
from .View import View
from views.components import TableComponent


class GraphView(View):
    def render(self, graphs):
        data = {}

        for year, graph in graphs.items():
            data[year] = self.collect_data_from_graph(graph)

            if nx.number_connected_components(graph) > 1:
                count_component = 1
                for component in nx.connected_components(graph):
                    subgraph = nx.subgraph(graph, component)
                    data['{} ({})'.format(year, count_component)] = self.collect_data_from_graph(subgraph)
                    count_component += 1

        dataframe = pd.DataFrame.from_dict(data, orient='index')

        text = 'You can view the data about the{} graph{} below:'
        if len(graphs) > 1:
            text = text.format('s', 's')
        text = text.format('', '')

        cols = self.render_component.beta_columns(2)
        cols[0].markdown(text)
        cols[0].dataframe(dataframe)
        TableComponent(render_component=cols[1], headers=TableComponent.metric_headers, values=[
            ['`Diameter`', '[Diameter](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=5yquhZpJ1DaF&line=2&uniqifier=1) it is the **shortest** distance between the two most distant nodes in the network.', ],
        ]).render()

    def collect_data_from_graph(self, graph) -> Dict:
        data = {
                'nodes': graph.number_of_nodes(),
                'edges': graph.number_of_edges(),
                'is_connected': True if nx.is_connected(graph) else False,
                'diameter': 0,
                'radius': 0,
                'number_connected_components': nx.number_connected_components(graph),
            }
        if nx.is_connected(graph):
            data.update({
                'diameter': nx.diameter(graph),
                'radius': nx.radius(graph),
            })

        return data
