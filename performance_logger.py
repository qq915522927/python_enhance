import functools
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

class call_logger(object):
    """
    Decorator class to log calls on functions or class methods,
    e.g..

        @call_logger
        def my_function():

       class MyClass(object):         

            @call_logger
            def my_method(self):
    """
    def __init__(self, func):
        self._func = func
        self._wrapped = None
        self._obj = None

    def __call__(self, *args, **kwags):
        if not self._wrapped:
            if self._obj:
                self._wrapped = self._wrap_method(self._func)
                self._wrapped = functools.partial(self._wrapped, self._obj)
            else:
                self._wrapped = self._wrap_function(self._func)
        return self._wrapped(*args, **kwags)

    def __get__(self, obj, type=None):
        self._obj = obj
        return self

    def _wrap_function(self, function):
        """
        Perform the decorator wrapping for a regular function.
        """
        @functools.wraps(function)
        def inner(*args, **kwags):
            """
            Implementation of the wraped function.
            """
            started = time.time()
            exc_name = None
            result = None
            try:
                result = function(*args, **kwags)
            except Exception as ex:
                exc_name = type(ex).__name__
                raise
            finally:
                _log_it(started, function, result, exc_name)
            return result
        return inner

    def _wrap_method(self, method):
        """
        Perform the decorator wrapping for a class method.
        """
        def inner(self, *args, **kwags):
            """
            Implementation of the wrapped function.
            """
            started = time.time()
            exc_name = None
            result = None
            try:
                result = method(self, *args, **kwags)
            except Exception as ex:
                exc_name = type(ex).__name__
                raise
            finally:
                _log_it(started, method, result, exc_name)
        return inner


def _log_it(started, method, result, exc_name):
    finished = time.time()
    elapsed = (finished - started) * 1000
    modname, methname = _get_caller_info(method)
    logging.debug("%s %s takes %s ms", modname, methname, elapsed)


def _get_caller_info(method):
    modname = method.__module__
    methname = method.__name__
    return modname, methname

@call_logger
def test():
    print 'test function'
    time.sleep(1)
    return True

class MyClass(object):

    @call_logger
    def test_method(self):
        time.sleep(1)
        print "test method"

if __name__ == "__main__":
    test()
    test_obj = MyClass()
    test_obj.test_method()
