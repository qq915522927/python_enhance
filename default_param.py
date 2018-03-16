
class Bus(object):

    def __init__(self, passager=None):
        if passager is None:
            self.passager = []
        else:
            self.passager = list(passager)

    def pick(self, one):
        self.passager.append(one)

    def drop(self, one):
        self.passager.remove(one)
    


if __name__ == '__main__':
    
    team = [1,2,3,4]
    bus = Bus(team)
    bus.drop(2)
    print(team)
    print(bus.passager)
