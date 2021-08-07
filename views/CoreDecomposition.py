import networkx as nx
from .View import View
from utils.constants import METRICS
from views.components import TableComponent, PanelTabsBokehComponent
from views.charts import KCoreChart, KShellChart
import copy


class CoreDecomposition(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Core Decomposition
        """)
        cols = self.render_component.beta_columns(self._columns_width)

        # Column 1
        graph_selected = cols[1].selectbox('Select the graph', options=list(graphs.keys()), key='core_decomposition')
        graph = copy.deepcopy(graphs[graph_selected])

        # Remove self-loops
        if len(list(nx.selfloop_edges(graph))) > 0:
            graph = graph.remove_edges_from(nx.selfloop_edges(graph))

        all_cores = nx.core_number(graph)
        cores_options = set([core for node, core in all_cores.items()])
        core_selected = cols[1].selectbox('Select the core number', options=list(cores_options))

        TableComponent(
            render_component=cols[1],
            headers=TableComponent.metric_headers,
            values=[
                METRICS['k_core'],
                METRICS['k_shell'],
            ]
        ).render()

        # Column 0
        graph_core = nx.k_core(copy.deepcopy(graph), core_selected, all_cores)
        graph_shell = nx.k_shell(copy.deepcopy(graph), core_selected, all_cores)
        PanelTabsBokehComponent(render_component=cols[0]) \
            .add_tab('K-core ({})'.format(core_selected), KCoreChart().get(graph_core)) \
            .add_tab('K-shell ({})'.format(core_selected), KShellChart().get(graph_shell)) \
            .render()
