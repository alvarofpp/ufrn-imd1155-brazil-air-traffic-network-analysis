from typing import List
from .Component import Component
from utils.constants import MODE_RENDER, MODE_MARKDOWN


class TableComponent(Component):
    metric_headers = [
        'Metric',
        'Description',
    ]

    def __init__(self, headers: List = None, values: List = None, **kwargs):
        super().__init__(**kwargs)
        self.headers = headers if headers is not None else []
        self.values = values if values is not None else []

    def render(self, mode: int = MODE_RENDER):
        text = '| ' + ' | '.join(self.headers) + " |\n" \
               + '| ' + ' | '.join(['---' for _ in range(len(self.headers))]) + " |\n"

        for row in self.values:
            text += '| ' + ' | '.join([str(value) for value in row]) + " |\n"

        if mode not in [MODE_RENDER, MODE_MARKDOWN]:
            raise ValueError(
                'Invalid mode. Expect [{}], given {}'.format(', '.join([str(MODE_RENDER), str(MODE_MARKDOWN)]), str(mode))
            )

        if mode == MODE_MARKDOWN:
            return text

        self.render_component.markdown(text)

    def get_markdown(self) -> str:
        return self.render(MODE_MARKDOWN)
