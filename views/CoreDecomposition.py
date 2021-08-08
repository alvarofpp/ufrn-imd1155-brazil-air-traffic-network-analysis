import copy
import networkx as nx
from .View import View
from bokeh.layouts import row
from utils.constants import METRICS
from views.components import TableComponent
from views.charts import KCoreChart, KShellChart


class CoreDecomposition(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Core Decomposition
        """)

        # First row
        cols = self.render_component.columns([3, 3, 3])
        graph_selected = cols[0].selectbox('Select the graph', options=list(graphs.keys()), key='core_decomposition')
        graph = copy.deepcopy(graphs[graph_selected])

        # Remove self-loops
        if len(list(nx.selfloop_edges(graph))) > 0:
            graph = graph.remove_edges_from(nx.selfloop_edges(graph))

        all_cores = nx.core_number(graph)
        cores_options = set([core for node, core in all_cores.items()])
        core_selected = cols[1].selectbox('Select the core number', options=list(cores_options))

        TableComponent(
            render_component=cols[2],
            headers=TableComponent.metric_headers,
            values=[
                METRICS['k_core'],
                METRICS['k_shell'],
            ]
        ).render()

        # Second row
        graph_core = nx.k_core(graph, core_selected, all_cores)
        graph_shell = nx.k_shell(graph, core_selected, all_cores)

        plot = row(KCoreChart().get(graph_core), KShellChart().get(graph_shell))
        self.render_component.bokeh_chart(plot)
