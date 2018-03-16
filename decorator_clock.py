import time
import functools


def clock(func):
    total_time = 0
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        nonlocal total_time
        total_time += elapsed
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args )
        print('[%0.8fs] %s(%s) -> %s'%(elapsed, name, arg_str, result))
        print('Total time -> %s', total_time)
        return result
    return clocked


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@clock
def factorial(num):
    return 1 if num < 2 else num*factorial(num-1)

if __name__ == '__main__':
    #factorial(10)
    #print(factorial.__name__)
    print(fibonacci(6))


