import networkx as nx
from .View import View
from views.components import MapMultiLayerComponent


class PeripheryView(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Periphery
        """)

        graphs_filtered = {year:graph for year, graph in graphs.items() if nx.is_connected(graph)}
        map_periphery_component = MapMultiLayerComponent()
        map_periphery_component.render(graphs_filtered)
