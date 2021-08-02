import networkx as nx
from .View import View
from views.components import MapFoliumComponent


class FoliumView(View):
    def __init__(self, width: float = 100):
        super().__init__()
        self.width = width

    def render(self, graph):
        if nx.is_connected(graph):
            self.render_component.markdown("""
                        ### Periphery
                        """)
            map_periphery_component = MapFoliumComponent(peripheries=nx.periphery(graph), width=self.width)
            map_periphery_component.render(graph)

            self.render_component.markdown("""
                        ### Diameter
                        """)
            # print(nx.eccentricity(graph).items())
            diameter = nx.diameter(graph)
            whom_diameter = [code for code, value in nx.eccentricity(graph).items() if value == diameter]
            map_diameter_component = MapFoliumComponent(whom_diameter=whom_diameter, width=self.width)
            map_diameter_component.render(graph)

        map_component = MapFoliumComponent(draw_edges=True, width=self.width)
        map_component.render(graph)
