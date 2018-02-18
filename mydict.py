import collections

class StrKeyDict(collections.UserDict):
    """
    A customized class inherted fron UserDict,
    get value by converting int type of key to str.
    E.g..

        mydict = StrKeyDict({'1':'one'})
        mydict[1]
    output: 'one'
    """
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data
    
    def __setitem__(self, key, item):
        self.data[str(key)] = item


if __name__ == '__main__':
    mydict = StrKeyDict((('1','one'),('2','two')))
    print(mydict[1])
    print(1 in mydict)
    mydict[3] = 'three'
    print(mydict)
