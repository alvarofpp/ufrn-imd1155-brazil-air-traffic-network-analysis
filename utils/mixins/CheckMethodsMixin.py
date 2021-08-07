class CheckMethodsMixin:
    _methods = []

    def _check_class(self):
        methods = [method for method in dir(self) if method in self._methods]
        if len(methods) != len(self._methods):
            diff_methods = set(self._methods).difference(methods)
            raise NotImplementedError('You must implement the methods: {}.'.format(', '.join(diff_methods)))
