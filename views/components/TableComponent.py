from typing import List
from .Component import Component


class TableComponent(Component):
    metric_headers = [
        'Metric',
        'Description',
    ]

    def __init__(self, headers: List = None, values: List = None, **kwargs):
        super().__init__(**kwargs)
        self.headers = headers if headers is not None else []
        self.values = values if values is not None else []

    def render(self):
        text = '| ' + ' | '.join(self.headers) + " |\n" \
               + '| ' + ' | '.join(['---' for _ in range(len(self.headers))]) + " |\n"

        for row in self.values:
            text += '| ' + ' | '.join([str(value) for value in row]) + " |\n"

        self.render_component.markdown(text)
