from .Component import Component


class SelectComponent(Component):
    def __init__(self, values=None, **kwargs):
        super().__init__(**kwargs)
        self.values = values

    def format(self, option: int):
        return self.values[option]

    def render(self, label: str):
        return self.render_component.selectbox(label, options=list(self.values.keys()), format_func=self.format)
