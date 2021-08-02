import abc


class Component(abc.ABC):
    def __init__(self):
        self._methods = [
            'render',
        ]
        self._check_class()

    def _check_class(self):
        methods = [method for method in dir(self) if method in self._methods]
        if len(methods) != len(self._methods):
            diff_methods = set(self._methods).difference(methods)
            raise NotImplemented('you must implement the methods: {}.'.format(', '.join(diff_methods)))
