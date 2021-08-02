import networkx as nx
import streamlit as st
from .View import View
from views.components import MapFoliumComponent


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
            diameter = nx.diameter(graph)
            st.markdown("""
            Some information is only displayed if the graph if connected:
            - **Diameter**: {}
            - **Radius**: {}
            """.format(
                diameter,
                nx.radius(graph)
            ))
            st.markdown("""
            ### Periphery
            """)
            map_periphery_component = MapFoliumComponent(peripheries=nx.periphery(graph))
            map_periphery_component.render(graph)

            st.markdown("""
            ### Diameter
            """)
            print(nx.eccentricity(graph).items())
            whom_diameter = [code for code, value in nx.eccentricity(graph).items() if value == diameter]
            map_diameter_component = MapFoliumComponent(whom_diameter=whom_diameter)
            map_diameter_component.render(graph)
