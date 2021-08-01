from .View import View
import folium
from streamlit_folium import folium_static


class FoliumView(View):
    def __init__(self):
        super().__init__()
        self.quartile_1 = 0.0
        self.quartile_2 = 0.0
        self.quartile_3 = 0.0

    def render(self, graph=None):
        self.define_quartiles(graph)
        self.draw_map(graph)

    def define_quartiles(self, graph):
        # Sort weights
        edges_weight = sorted(graph.edges(data=True), key=lambda edge: edge[2]['flight_count'], reverse=True)

        # Get maximum weight
        max_weight = edges_weight[0][2]['flight_count']

        # Binds
        self.quartile_1 = max_weight * 0.1
        self.quartile_2 = max_weight * 0.2
        self.quartile_3 = max_weight * 0.4

    def weight_line(self, weight):
        if weight < self.quartile_1:
            return 0.1
        if weight < self.quartile_2:
            return 0.1
        if weight < self.quartile_3:
            return 1

        return 3

    def draw_map(self, graph):
        map = folium.Map(
            location=[-5.826592, -35.212558],
            zoom_start=3,
            tiles='OpenStreetMap'
        )

        # Adds nodes
        for code in graph.nodes():
            node = graph.nodes()[code]

            folium.Circle([node['latitude'], node['longitude']],
                          popup='<i>' + node['name'] + '</i>',
                          tooltip=code,
                          radius=10).add_to(map)

        # Adds edges
        for edge in graph.edges(data=True):
            node_first = graph.nodes[edge[0]]
            node_second = graph.nodes[edge[1]]
            loc = [
                (node_first['latitude'], node_first['longitude']),
                (node_second['latitude'], node_second['longitude']),
            ]

            folium.PolyLine(loc,
                            color='red',
                            weight=self.weight_line(edge[2]['flight_count']),
                            opacity=0.6).add_to(map)

        # call to render Folium map in Streamlit
        folium_static(map)
