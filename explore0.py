import keyword
from collections import abc


class FrozenJSON:


    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls, arg)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(arg) for item in arg ]
        else:
            return arg

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
        self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON(self.__data[name])

    # @classmethod
    # def build(cls, obj):
    #     if isinstance(obj, abc.Mapping):
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):
    #         return [cls.build(item) for item in obj]
    #     else:
    #         return obj
