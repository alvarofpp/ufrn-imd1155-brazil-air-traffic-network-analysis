import networkx as nx
from .View import View
import streamlit as st
from bokeh.layouts import row
from utils.constants import METRICS
from views.components import TableComponent
from views.charts import KCoreChart, KShellChart


class CoreDecompositionView(View):
    def render(self):
        self.render_component.markdown("""
        ## Core Decomposition
        """)

        # First row
        cols = self.render_component.columns([5, 5])
        graph = st.session_state['graph_selected']

        # Remove self-loops
        if len(list(nx.selfloop_edges(graph))) > 0:
            graph = graph.remove_edges_from(nx.selfloop_edges(graph))

        all_cores = nx.core_number(graph)
        cores_options = set([core for node, core in all_cores.items()])
        core_selected = cols[0].selectbox('Select the core number', options=list(cores_options))

        TableComponent(
            render_component=cols[1],
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
