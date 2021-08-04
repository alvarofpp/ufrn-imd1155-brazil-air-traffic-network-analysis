from .View import View
from views.components import MapMultiLayerComponent


class FoliumView(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Nodes visualization 
        """)

        map_component = MapMultiLayerComponent(peripheries=True, whom_diameter=True, minimap=True)
        map_component.render(graphs)
