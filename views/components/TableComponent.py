from typing import List
from .Component import Component


class TableComponent(Component):
    metric_headers = [
        'Metric',
        'Description',
    ]

    def __init__(self, headers: List = None, values: List = None, **kwargs):
        super().__init__(**kwargs)
        self.headers = headers
        self.values = values

    def render(self):
        text = '| ' + ' | '.join(self.headers) + " |\n" \
               + '| ' + ' | '.join(['---' for _ in range(len(self.headers))]) + " |\n"

        for value in self.values:
            text += '| ' + ' | '.join(value) + " |\n"

        self.render_component.markdown(text)
