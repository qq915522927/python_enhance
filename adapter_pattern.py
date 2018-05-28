class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 's {}'.format(self.name)

    def play(self):
        return 'play song'

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'h {}'.format(self.name)

    def speak(self):
        return 'hello'
# ---------------------------------------
# internal------------------------------

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'c {}'.format(self.name)

    def execute(self):
        return 'execute'




class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

def main():
    objects = [Computer('personal computer')]
    synth = Synthesizer('music')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Tommy')
    objects.append(Adapter(human, dict(execute=human.speak)))
    for i in objects:
        print('{} {}'.format(str(i), i.execute()))
