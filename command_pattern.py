import os

verbose = True

class RenameFile:
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print('[renaming {} to {}]'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print('[renaming {} to {}]'.format(self.dest, self.src))
        os.rename(self.dest, self.src)

def delete_file(path):
    if verbose:
        print('deleting file {}'.format(path))
    os.remove(path)

class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self):
        if verbose:
            print('create file {}'.format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)
        
class ReadFile:
    def __init__(self, src_path):
        self.src_path = src_path

    def execute(self):
        with open(self.src_path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')

def main():
    orig_name, new_name = 'file1', 'file2'

    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n]')

    if answer not in 'yY':
        print('the result is {}'.format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass

if __name__ == '__main__':
    main()
