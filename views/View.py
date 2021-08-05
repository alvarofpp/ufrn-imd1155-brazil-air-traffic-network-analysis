import abc
from utils.mixins import RenderMixin, CheckMethodsMixin


class View(RenderMixin, CheckMethodsMixin, abc.ABC):
    _methods = [
        'render',
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._check_class()
