import collections

class Text(collections.UserString):

    def __repr__(self):
        return 'Test({!r}'.format(self.data)

    def reverse(self):
        return self[::-1]
