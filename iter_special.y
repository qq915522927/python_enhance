from random import randint

def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)

for item in enumerate(d6_iter):
    print('%s => %s'% item)


with open('vector.py', 'r') as fp:
    for line in iter(fp.readline, '\n'):
        print line
