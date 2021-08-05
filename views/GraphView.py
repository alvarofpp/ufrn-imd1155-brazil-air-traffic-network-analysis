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

        text = 'You can view the data about the{} graph{} below:'
        if len(graphs) > 1:
            text = text.format('s', 's')
        text = text.format('', '')

        cols = self.render_component.beta_columns(2)
        cols[0].markdown(text)
        cols[0].dataframe(dataframe)
        cols[1].markdown("""
        | Metric | Description |
        | --- | --- |
        | `Diameter` |[Diameter](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=5yquhZpJ1DaF&line=2&uniqifier=1) it is the **shortest** distance between the two most distant nodes in the network|
        """)
