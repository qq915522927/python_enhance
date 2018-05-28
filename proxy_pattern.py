
# lazy property

class LazyProperty:
    sef __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value
