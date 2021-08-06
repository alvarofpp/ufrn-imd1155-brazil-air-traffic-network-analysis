import folium
from typing import Dict
from .Component import Component
from folium import folium, plugins
from streamlit_folium import folium_static


class MapFoliumComponent(Component):
    _methods = [
        'render',
        'make_map',
    ]
    _map_config_default = {
        'location': [-5.826592, -35.212558],
        'zoom_start': 3,
        'tiles': 'OpenStreetMap',
    }

    def __init__(self, map_config: Dict = None, minimap: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.map_config = self._map_config_default.copy()
        self.map_config.update(map_config if map_config is not None else {})
        self.map = folium.Map(**self.map_config)
        self.minimap = minimap

    def render(self, graph):
        self.make_map(graph)

        if self.minimap:
            minimap = plugins.MiniMap()
            self.map.add_child(minimap)

        # Call to render Folium map in Streamlit
        with self.render_component:
            folium_static(self.map)
