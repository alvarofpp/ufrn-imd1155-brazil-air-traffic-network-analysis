import pandas as pd
import networkx as nx
from typing import Dict
from .View import View
from views.components import TableComponent
from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool, PanTool, ZoomInTool, ZoomOutTool)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx


class NodeRanking(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Node Ranking 
        """)
        cols = self.render_component.beta_columns([7, 3])
        #
        # # Column 1
        graph_selected = cols[1].selectbox('Select the graph', options=list(graphs.keys()), key='node_ranking')
        graph = graphs[graph_selected]

        # Column 0

        # Prepare Data
        G = graph

        SAME_CLUB_COLOR, DIFFERENT_CLUB_COLOR = "black", "red"
        edge_attrs = {}

        for start_node, end_node, _ in G.edges(data=True):
            edge_color = SAME_CLUB_COLOR if G.nodes[start_node]["country"] == G.nodes[end_node][
                "country"] else DIFFERENT_CLUB_COLOR
            edge_attrs[(start_node, end_node)] = edge_color

        nx.set_edge_attributes(G, edge_attrs, "edge_color")

        # Show with Bokeh
        plot = Plot(plot_width=400, plot_height=400,
                    x_range=Range1d(-1.1, 1.1), y_range=Range1d(-1.1, 1.1))
        plot.title.text = "Graph Interaction Demonstration"

        node_hover_tool = HoverTool(tooltips=[("index", "@index"), ("country", "@country")])
        plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool(), PanTool(), ZoomInTool(), ZoomOutTool())

        graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

        graph_renderer.node_renderer.glyph = Circle(size=15, fill_color=Spectral4[0])
        graph_renderer.edge_renderer.glyph = MultiLine(line_color="edge_color", line_alpha=0.8, line_width=1)
        plot.renderers.append(graph_renderer)

        cols[0].bokeh_chart(plot)
    # TODO Degree Centrality
    # TODO Closeness Centrality
    # TODO Betweenness Centrality
    # TODO EigenVector Centrality
    # TODO All together
