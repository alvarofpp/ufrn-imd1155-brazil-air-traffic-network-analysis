import abc
from utils.mixins import RenderMixin, CheckMethodsMixin


class View(RenderMixin, CheckMethodsMixin, abc.ABC):
    _methods = [
        'render',
    ]
    _columns_width = [6, 3]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._check_class()
