import networkx as nx
import folium
from utils.colors import *
from .MapFoliumComponent import MapFoliumComponent


class AirportsMapComponent(MapFoliumComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.palettes = {
            'nodes': palette_blue,
            'periphery': palette_wine,
            'diameter': palette_brown,
        }

    def make_map(self, graph):
        self.draw_edges(graph)
        self.draw_nodes(graph)
        if nx.is_connected(graph):
            self.draw_peripheries(graph)
        folium.LayerControl().add_to(self.map)

    def draw_edges(self, graph):
        feature_group = folium.FeatureGroup(name='edges')
        self.map.add_child(feature_group)

        for edge in graph.edges(data=True):
            node_first = graph.nodes[edge[0]]
            node_second = graph.nodes[edge[1]]
            loc = [
                (node_first['latitude'], node_first['longitude']),
                (node_second['latitude'], node_second['longitude']),
            ]

            folium.PolyLine(loc,
                            color='red',
                            weight=edge[2]['flight_count'] * 0.5,
                            opacity=0.02
                            ).add_to(feature_group)

    def draw_nodes(self, graph):
        feature_group = folium.FeatureGroup(name='nodes')
        self.map.add_child(feature_group)

        for code in graph.nodes():
            self.draw_circule(graph, code, graph.nodes()[code], self.palettes['nodes'][0], feature_group)

    def draw_peripheries(self, graph):
        feature_group = folium.FeatureGroup(name='periphery')
        self.map.add_child(feature_group)

        for code in nx.periphery(graph):
            self.draw_circule(graph, code, graph.nodes()[code], self.palettes['periphery'][0], feature_group)

    def draw_circule(self, graph, code, node, color, group):
        folium.Circle(location=(node['latitude'], node['longitude']),
                      popup='<b>{}</b> - <i>{} ({})</i>'.format(code, node['name'], node['country']),
                      tooltip=code,
                      radius=len([n for n in nx.neighbors(graph, code)]) * 1000,
                      color=color,
                      fill=True,
                      fill_opacity=0.6).add_to(group)
