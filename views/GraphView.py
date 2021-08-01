import networkx as nx
import streamlit as st
from .View import View


class GraphView(View):
    def render(self, graph=None):
        st.markdown("""
        Information about the graph:
        - **Nodes**: {}
        - **Edges**: {}
        - **Connected**: {}
        """.format(
            graph.number_of_nodes(),
            graph.number_of_edges(),
            nx.is_connected(graph)
        ))
        if nx.is_connected(graph):
            st.markdown("""
            Some information is only displayed if the graph if connected:
            - **Diameter**: {}
            - **Radius**: {}
            """.format(
                nx.diameter(graph),
                nx.radius(graph)
            ))
            # TODO Whom are in the diameter
