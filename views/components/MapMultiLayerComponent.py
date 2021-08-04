import folium
from folium import plugins
import networkx as nx
from .MapFoliumComponent import MapFoliumComponent


class MapMultiLayerComponent(MapFoliumComponent):
    def __init__(self,
                 peripheries=False,
                 whom_diameter=False
                 ):
        super().__init__()
        self.peripheries = peripheries
        self.whom_diameter = whom_diameter

    def make_map(self, graphs):
        self.draw_nodes(graphs)

        if self.peripheries:
            self.draw_peripheries(graphs)
        if self.whom_diameter:
            self.draw_whom_diameter(graphs)

        folium.LayerControl(collapsed=False).add_to(self.map)

    def draw_nodes(self, graphs):
        color = '#2980b9'
        label_group = 'nodes'

        feature_group = folium.FeatureGroup(name=label_group)
        self.map.add_child(feature_group)

        for label, graph in graphs.items():
            subgroup = plugins.FeatureGroupSubGroup(feature_group, label_group + '-' + label)
            self.map.add_child(subgroup)

            for code in graph.nodes():
                node = graph.nodes()[code]

                folium.Circle((node['latitude'], node['longitude']),
                              popup='<b>{}</b> - <i>{} ({})</i>'.format(code, node['name'], node['country']),
                              tooltip=code,
                              radius=10,
                              color=color).add_to(subgroup)

    def draw_peripheries(self, graphs):
        color = '#e74c3c'
        label_group = 'periphery'
        graphs_filtered = {year: graph for year, graph in graphs.items() if nx.is_connected(graph)}

        if len(graphs_filtered) == 0:
            return

        feature_group = folium.FeatureGroup(name=label_group)
        self.map.add_child(feature_group)

        for label, graph in graphs_filtered.items():
            subgroup = plugins.FeatureGroupSubGroup(feature_group, label_group + '-' + label)
            self.map.add_child(subgroup)

            for code in nx.periphery(graph):
                node = graph.nodes()[code]

                folium.Circle((node['latitude'], node['longitude']),
                              popup='<b>{}</b> - <i>{} ({})</i>'.format(code, node['name'], node['country']),
                              tooltip=code,
                              radius=10,
                              color=color).add_to(subgroup)

    def draw_whom_diameter(self, graphs):
        color = '#e74c3c'
        label_group = 'whom_diameter'
        graphs_filtered = {year: graph for year, graph in graphs.items() if nx.is_connected(graph)}

        if len(graphs_filtered) == 0:
            return

        feature_group = folium.FeatureGroup(name=label_group)
        self.map.add_child(feature_group)

        for label, graph in graphs_filtered.items():
            subgroup = plugins.FeatureGroupSubGroup(feature_group, label_group + '-' + label)
            self.map.add_child(subgroup)

            diameter = nx.diameter(graph)
            whom_diameter = [code for code, value in nx.eccentricity(graph).items() if value == diameter]

            for code in whom_diameter:
                node = graph.nodes()[code]

                folium.Circle((node['latitude'], node['longitude']),
                              popup='<b>{}</b> - <i>{} ({})</i>'.format(code, node['name'], node['country']),
                              tooltip=code,
                              radius=10,
                              color=color).add_to(subgroup)
