import threading
import itertools
import time
import sys

expressions = ['0.0','0..0','0...0','0..0','0.0']
expressions2 = ['乁( ◔ ౪◔)「','乁( ◕ ౪◕)「']
expressions3 = ['＿|￣|○  ', '＿|＼○＿ ', '＿/＼○＿ ', '＿__＿○＿']
reverse3 =  expressions3[::-1]
expressions4 = ['<（ ‵□′）>     ε（￣▽￣）3', '<（ ‵□′）>     ε（￣▽￣）3', '<（ ‵□′）>C    ε（￣▽￣）3', '<（ ‵□′）>-C   ε（￣▽￣）3', '<（ ‵□′）>--C  ε（￣▽￣）3',


        '<（ ‵□′）>───Ｃε（￣▽￣）3','<（ ‵□′）>───Ｃε（┬﹏┬）3','<（ ‵□′）>───Ｃε（┬_┬）3','<（ ‵□′）>───Ｃε（┬﹏┬）3','<（ ‵□′）>───Ｃε（┬_┬）3'
        
        ]
class Signal:
    go = True



write, flush = sys.stdout.write, sys.stdout.flush

def show_exp():
    n = 0
    for exp in itertools.cycle(expressions4):
        #write(exp)
        #flush()
        #write('\x08' * len(exp))
        #flush()
        #time.sleep(.5)
        #write(' ' * len(exp))
        #flush()
        #write('\x08' * len(exp))
        print('\r'+exp, end='')
        
        time.sleep(.5)

        print('\r'+'  '*30, end='')


def spin(msg, signal):
    for char in itertools.cycle('|/-\\'):
        status = char + '  ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write('  ' * len(status) + '\x08' * len(status))

def slow_function():
    time.sleep(3)
    return 42

def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('Thinking!', signal))
    print('Spinner object:', spinner)
    spinner.start()
    print('...')
    print('...')
    result = slow_function()
    signal.go = False
    spinner.join()
    return result

def main():
    result = supervisor()
    print('Answer:', result)

if __name__ == '__main__':
     main()
#    show_exp()
