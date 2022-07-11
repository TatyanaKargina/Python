from itertools import cycle, count

n_start = int(input('Стартовое число: '))
n_stop = n_start * 10

for i in count(n_start):
    if i < n_stop:
        print(i)
    else:
        break
