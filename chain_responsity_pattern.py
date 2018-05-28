class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)

        elif self.parent:
            self.parent.handle(event)

        elif hasattr(self, 'handle_default'):
            self.handle_default(event)

class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: close')

    def handle_default(self, event):
        print('MainWindow default {}'.format(event))
        
class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog paint')

class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText {}'.format(event))

def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        mw.handle(evt)
        sd.handle(evt)
        sd.handle(evt)
        msg.handle(evt)

if __name__ == '__main__':
    main()

