def count(func):
    count_num = [0]
    def wrap( *args, **kwargs):
        func(*args, **kwargs)
        count_num[0] += 1
        print 'run for %s times' %count_num
    return wrap


@count
def test_add(a,b):
    return a+b


if __name__ == '__main__':
    for i in range(10):
        test_add(1,3)

