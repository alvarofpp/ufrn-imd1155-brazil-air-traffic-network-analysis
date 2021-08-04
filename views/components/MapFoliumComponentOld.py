from .Component import Component
import folium
from folium import folium, plugins
from streamlit_folium import folium_static


class MapFoliumComponentOld(Component):
    def __init__(self,
                 draw_edges=False,
                 peripheries=None,
                 whom_diameter=None
                 ):
        super().__init__()
        self.quartile_1 = 0.0
        self.quartile_2 = 0.0
        self.quartile_3 = 0.0
        self.draw_edges = draw_edges
        self.peripheries = peripheries
        self.whom_diameter = whom_diameter

        if peripheries is not None:
            self.peripheries = {periphery: {} for periphery in peripheries}
        if whom_diameter is not None:
            self.whom_diameter = {who: {} for who in whom_diameter}

    def render(self, graph):
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
            return 0.25
        if weight < self.quartile_3:
            return 1

        return 3

    def draw(self, graphs):
        map = folium.Map(
            location=[-5.826592, -35.212558],
            zoom_start=3,
            tiles='OpenStreetMap'
        )

        fg = folium.FeatureGroup(name="groups")
        m.add_child(fg)

        g1 = plugins.FeatureGroupSubGroup(fg, "group1")
        m.add_child(g1)

        g2 = plugins.FeatureGroupSubGroup(fg, "group2")
        m.add_child(g2)

        folium.Marker([-1, -1]).add_to(g1)
        folium.Marker([1, 1]).add_to(g1)

        folium.Marker([-1, 1]).add_to(g2)
        folium.Marker([1, -1]).add_to(g2)

        folium.LayerControl(collapsed=False).add_to(m)

        m

    def draw_map(self, graph):
        # TODO find center among periphery or diameter
        map = folium.Map(
            location=[-5.826592, -35.212558],
            zoom_start=3,
            tiles='OpenStreetMap'
        )

        # Adds nodes
        for code in graph.nodes():
            node = graph.nodes()[code]
            color = '#2980b9'

            if self.peripheries is not None and code in self.peripheries:
                color = '#e74c3c'
                self.peripheries[code] = node
            if self.whom_diameter is not None and code in self.whom_diameter:
                color = '#f1c40f'
                self.whom_diameter[code] = node

            folium.Circle((node['latitude'], node['longitude']),
                          popup='<b>{}</b> - <i>{} ({})</i>'.format(code, node['name'], node['country']),
                          tooltip=code,
                          radius=10,
                          color=color).add_to(map)

        # Adds edges
        if self.draw_edges:
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
                                opacity=0.6
                                ).add_to(map)

        # Render periphery nodes
        if self.peripheries is not None:
            text = "\n".join(
                ["- {} - {} ({})".format(code, periphery['name'], periphery['country'])
                 for code, periphery in self.peripheries.items()]
            )
            self.render_component.markdown(text)

        # Render diameter nodes
        if self.whom_diameter is not None:
            text = "\n".join(
                ["- {} - {} ({})".format(code, who['name'], who['country'])
                 for code, who in self.whom_diameter.items()]
            )
            self.render_component.markdown(text)

        # Call to render Folium map in Streamlit
        folium_static(map)
