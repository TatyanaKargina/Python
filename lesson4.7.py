from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
n = 0
for i in gen:
    if n < 15:
        print(i)
        n += 1
    else:
        break