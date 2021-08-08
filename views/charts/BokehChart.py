import abc
import copy
import uuid
from typing import List, Tuple
import networkx as nx
import bokeh.plotting
import bokeh.palettes
from bokeh.plotting import from_networkx
from bokeh.transform import linear_cmap
from bokeh.models import Circle, HoverTool, ColorBar, LogColorMapper, MultiLine


class BokehChart(abc.ABC):
    _methods = [
        'manipulate_data',
    ]

    _tooltips_default = [
        ('airport', '@index'),
        ('name', '@name'),
        ('country', '@country'),
    ]

    _palette_default = bokeh.palettes.Viridis256

    def __init__(self,
                 tooltips: List[Tuple[str, str]] = None,
                 palette: str = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)
        if tooltips is None:
            tooltips = []
        if palette is None:
            palette = self._palette_default

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
        min_color = min(color_list)
        max_color = max(color_list)
        if min_color < max_color:
            color_mapper = LogColorMapper(palette=self.palette, low=min_color, high=max_color)
            color_bar = ColorBar(
                color_mapper=color_mapper,
                location=(0, 0),
                label_standoff=6
            )
            figure.add_layout(color_bar, 'right')
            fill_color = linear_cmap(
                self._attribute,
                self.palette,
                min(color_list),
                max(color_list)
            )
        else:
            fill_color = self.palette[0]

        # Graph from networkx
        graph_renderer = from_networkx(graph, nx.spring_layout, scale=2, center=(0, 0))
        graph_renderer.node_renderer.glyph = Circle(size=15,
                                                    fill_color=fill_color)
        graph_renderer.edge_renderer.glyph = MultiLine(line_alpha=0.6, line_width=1)
        figure.renderers.append(graph_renderer)

        return figure

    def _get_figure(self):
        title = self._title if self._title is not None else ''
        return bokeh.plotting.figure(title=title,
                                     x_range=(-1.1, 1.1),
                                     y_range=(-1.1, 1.1),
                                     id=str(uuid.uuid4())
                                     )

    def _get_hover(self) -> HoverTool:
        return HoverTool(tooltips=self.tooltips)
