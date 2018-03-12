class Command(object):
    
    def __init__(self, receiver):
        self.receiver = receiver

    def excute(self):
        raise NotImplementedError
    

class Light(object):

    def __init__(self):
        self.status = False

    def turn_on(self):
        print 'The light is ON'

    def turn_off(self):
        print 'The light is off'

    def switch(self):
        self.status = not self.status
        if self.status:
            self.turn_on()
        else:
            self.turn_off()


class LightCommand(Command):
    
    def excute(self):
        self.receiver.switch()

    def __unicode__(self):
        return "Light on/off"

    def __str__(self):
        return "Light on/off"

class RemoteControl(object):

    def __init__(self, *command):
        self.command = list(command)
        self.button_map = {}
        self.map()

    def map(self):
        for i,c in enumerate(self.command):
            self.button_map[i] = c

    def press_button(self, button_no):
        self.button_map[button_no].excute()

    def __unicode__(self):
        return self.button_map
    def __str__(self):
        result = ''
        for k, v in self.button_map.items():
            result += 'button {} => {} \n'.format(k, v)

        return result


if __name__ == '__main__':
    light = Light()
    light_command = LightCommand(light)
    control = RemoteControl(light_command)
    while True:
        print '{}'.format(control)
        button_no = raw_input('Press the button with your desired number!i\n')
        control.press_button(int(button_no))

