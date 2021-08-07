import bokeh
import bokeh.layouts
import bokeh.models
from .Component import Component


class PanelTabsBokehComponent(Component):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tabs = []

    def render(self):
        tabs = bokeh.models.Tabs(
            tabs=self.tabs
        )
        self.render_component.bokeh_chart(tabs)

    def add_tab(self, title: str, *args):
        column = bokeh.layouts.Column(
            children=[*args], sizing_mode='stretch_width'
        )
        self.tabs.append(bokeh.models.Panel(child=column, title=title))

        return self
