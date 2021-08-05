from .View import View
from views.components import MapMultiLayerComponent, TableComponent


class FoliumView(View):
    def render(self, graphs):
        self.render_component.markdown("""
        ## Graphs visualization 
        """)

        cols = self.render_component.beta_columns(2)
        map_component = MapMultiLayerComponent(peripheries=True,
                                               whom_diameter=True,
                                               minimap=True,
                                               render_component=cols[0])
        map_component.render(graphs)
        TableComponent(render_component=cols[1], headers=TableComponent.metric_headers, values=[
            ['`Periphery`', 'The [Periphery](https://colab.research.google.com/github/ivanovitchm/network_analysis/blob/main/week_06/Hubs.ipynb#scrollTo=aaV5juQB4kCW&line=1&uniqifier=1) of a network is a set of all nodes whose eccentriciy is **equals** the diameter.', ],
        ]).render()
