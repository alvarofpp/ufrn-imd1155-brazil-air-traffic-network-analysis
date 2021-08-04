import abc
from utils.mixins import RenderMixin, CheckMethodsMixin


class Component(RenderMixin, CheckMethodsMixin, abc.ABC):
    _methods = [
        'render',
    ]

    def __init__(self):
        self._check_class()
