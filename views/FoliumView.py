from .View import View
from views.components import MapFoliumComponent


class FoliumView(View):

    def render(self, graph=None):
        map_component = MapFoliumComponent(draw_edges=True)
        map_component.render(graph)
