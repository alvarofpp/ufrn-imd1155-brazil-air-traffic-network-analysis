import networkx as nx
import folium
from folium import plugins
from utils.colors import *
from .MapFoliumComponent import MapFoliumComponent


class MapMultiLayerComponent(MapFoliumComponent):
    def __init__(self,
                 peripheries=False,
                 whom_diameter=False,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        self.peripheries = peripheries
        self.whom_diameter = whom_diameter
        self.palettes = {
            'nodes': palette_blue,
            'periphery': palette_wine,
            'diameter': palette_brown,
        }

    def make_map(self, graphs):
        self.draw_nodes(graphs)

        if self.peripheries:
            self.draw_peripheries(graphs)
        if self.whom_diameter:
            self.draw_whom_diameter(graphs)

        folium.LayerControl().add_to(self.map)

    def draw_nodes(self, graphs):
        label_group = 'nodes'
        feature_group = folium.FeatureGroup(name='all ' + label_group)
        self.map.add_child(feature_group)

        count_color = 0
        for label, graph in graphs.items():
            subgroup = plugins.FeatureGroupSubGroup(feature_group, label_group + ' - ' + label)
            self.map.add_child(subgroup)

            for code in graph.nodes():
                self.draw_circule(graph, code, graph.nodes()[code], self.palettes['nodes'][count_color], subgroup)
            count_color += 1

    def draw_peripheries(self, graphs):
        graphs_filtered = {year: graph for year, graph in graphs.items() if nx.is_connected(graph)}

        if len(graphs_filtered) == 0:
            return

        label_group = 'periphery'
        feature_group = folium.FeatureGroup(name='all ' + label_group)
        self.map.add_child(feature_group)

        count_color = 0
        for label, graph in graphs_filtered.items():
            subgroup = plugins.FeatureGroupSubGroup(feature_group, label_group + '-' + label)
            self.map.add_child(subgroup)

            for code in nx.periphery(graph):
                self.draw_circule(graph, code, graph.nodes()[code], self.palettes['periphery'][count_color], subgroup)
            count_color += 1

    def draw_whom_diameter(self, graphs):
        graphs_filtered = {year: graph for year, graph in graphs.items() if nx.is_connected(graph)}

        if len(graphs_filtered) == 0:
            return

        label_group = 'whom_diameter'
        feature_group = folium.FeatureGroup(name='all ' + label_group)
        self.map.add_child(feature_group)

        count_color = 0
        for label, graph in graphs_filtered.items():
            subgroup = plugins.FeatureGroupSubGroup(feature_group, label_group + '-' + label)
            self.map.add_child(subgroup)

            diameter = nx.diameter(graph)
            whom_diameter = [code for code, value in nx.eccentricity(graph).items() if value == diameter]

            for code in whom_diameter:
                self.draw_circule(graph, code, graph.nodes()[code], self.palettes['diameter'][count_color], subgroup)
            count_color += 1

    def draw_circule(self, graph, code, node, color, subgroup):
        folium.Circle(location=(node['latitude'], node['longitude']),
                      popup='<b>{}</b> - <i>{} ({})</i>'.format(code, node['name'], node['country']),
                      tooltip=code,
                      radius=len([n for n in nx.neighbors(graph, code)])*1000,
                      color=color,
                      fill=True,
                      fill_opacity=0.6).add_to(subgroup)
