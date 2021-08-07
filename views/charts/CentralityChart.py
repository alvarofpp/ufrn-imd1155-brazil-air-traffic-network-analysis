import abc
import copy
from typing import List, Tuple
import networkx as nx
import bokeh.plotting
from bokeh.plotting import from_networkx
from bokeh.transform import linear_cmap
from bokeh.models import Circle, HoverTool, ColorBar, LogColorMapper, MultiLine


class CentralityChart(abc.ABC):
    _methods = [
        'manipulate_data',
    ]

    _tooltips_default = [
        ('airport', '@index'),
        ('name', '@name'),
        ('country', '@country'),
    ]

    def __init__(self,
                 tooltips: List[Tuple[str, str]] = None,
                 palette: str = 'Viridis256',
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if tooltips is None:
            tooltips = []

        self.tooltips = [
            *self._tooltips_default,
            *tooltips,
        ]
        self.palette = palette

    def get(self, graph_original):
        graph = copy.deepcopy(graph_original)

        # Figure
        figure = self._get_figure()

        # Hover
        node_hover_tool = self._get_hover()
        figure.add_tools(node_hover_tool)

        # Attribute
        nodes_attribute = self.manipulate_data(graph)
        nx.set_node_attributes(graph, nodes_attribute, self._attribute)

        # Color bar
        color_list = list(nodes_attribute.values())
        color_mapper = LogColorMapper(palette=self.palette, low=min(color_list), high=max(color_list))
        color_bar = ColorBar(
            color_mapper=color_mapper,
            location=(0, 0),
            label_standoff=6
        )
        figure.add_layout(color_bar, 'right')

        # Graph from networkx
        graph_renderer = from_networkx(graph, nx.spring_layout, scale=2, center=(0, 0))
        graph_renderer.node_renderer.glyph = Circle(size=15,
                                                    fill_color=linear_cmap(
                                                        self._attribute,
                                                        self.palette,
                                                        min(color_list),
                                                        max(color_list)
                                                    ))
        graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.6, line_width=1)
        figure.renderers.append(graph_renderer)

        return figure

    def _get_figure(self):
        title = self._title if self._title is not None else ''
        return bokeh.plotting.figure(title=title,
                                     x_range=(-1.1, 1.1),
                                     y_range=(-1.1, 1.1))

    def _get_hover(self) -> HoverTool:
        return HoverTool(tooltips=self.tooltips)
