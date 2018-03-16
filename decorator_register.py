
registry = set()


def register(active=True):
    def decorate(func):
        print()
        if active:
            registry.add(func)
        else:
            registry.discard(func)
    return decorate


@register(active=True)
def test():
    pass

@register(active=False)
def test1():
    pass

@register(active=True)
def test2():
    pass

if __name__=='__main__':
    print(registry)
